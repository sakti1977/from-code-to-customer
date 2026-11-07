import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from prior_auth_lab import Lab, Blocked, fixture, proposal, replay, baseline, evidence_for, live_action


class PriorAuthTests(unittest.TestCase):
    def ready(self, directory=None):
        lab=Lab(directory=directory)
        replay(lab)
        return lab

    def test_T01_structured_baseline(self):
        self.assertEqual(baseline(Lab())['missing'],[])

    def test_T02_missing_order_stops_at_information(self):
        lab=Lab(fixture('missing')); replay(lab)
        self.assertEqual(lab.data['state'],'NEEDS_INFORMATION')
        with self.assertRaises(Blocked):lab.approve('Maya')

    def test_T03_unindexed_sources_need_inspection(self):
        lab=Lab(fixture('varied'))
        self.assertEqual(len(baseline(lab)['missing']),2)
        replay(lab)
        self.assertEqual(lab.data['state'],'READY_FOR_REVIEW')
        self.assertIsNone(lab.data['approval'])

    def test_T04_fabricated_quote_is_rejected(self):
        lab=Lab();lab.execute(proposal('read_document','D-01'))
        ev=[{'requirement_id':'R-ORDER','document_id':'D-01','quote':'invented clinical fact'}]
        with self.assertRaises(Blocked):lab.execute(proposal('propose_packet',evidence=ev))
        self.assertIsNone(lab.data['packet'])

    def test_T05_other_case_never_reaches_reader(self):
        lab=Lab()
        with self.assertRaises(Blocked):lab.execute(proposal('read_document','D-99'))
        self.assertNotIn('D-99',lab.read_docs)
        self.assertNotIn('This record must',json.dumps(lab.data['trace']))

    def test_T06_wrong_patient_same_tenant_is_blocked(self):
        f=fixture();f['documents']['D-01']['patient']='SYN-P002';lab=Lab(f)
        with self.assertRaises(Blocked):lab.execute(proposal('read_document','D-01'))

    def test_T07_conflicting_policy_stops_preparation(self):
        f=fixture();f['policy']['conflict']=True;lab=Lab(f)
        with self.assertRaises(Blocked):lab.execute(proposal('inspect_case'))
        self.assertEqual(lab.data['state'],'POLICY_REVIEW')

    def test_T08_injected_export_has_no_capability(self):
        lab=Lab(fixture('injection'))
        lab.execute(proposal('read_document','D-02'))
        with self.assertRaises(Blocked):lab.execute(proposal('export_all_records'))
        with self.assertRaises(Blocked):lab.execute(proposal('approve'))
        self.assertIsNone(lab.data['approval'])

    def test_T09_changed_packet_revokes_submission(self):
        lab=self.ready();lab.approve('Maya')
        lab.data['documents']['D-02']['text']+=' Changed after review.'
        with self.assertRaises(Blocked):lab.submit()
        self.assertEqual(lab.receipts,{})

    def test_T10_timeout_restart_reconcile_one_request(self):
        with tempfile.TemporaryDirectory() as directory:
            lab=self.ready(directory);lab.approve('Maya');lab.submit(True)
            self.assertEqual(lab.data['state'],'SUBMISSION_UNKNOWN')
            resumed=Lab.load(directory);resumed.reconcile()
            self.assertEqual(resumed.data['state'],'SUBMITTED_PENDING')
            self.assertEqual(len(resumed.receipts),1)
            self.assertIsNone(resumed.data['payer_decision'])
            with self.assertRaises(Blocked):resumed.submit()

    def test_T11_authorization_date_scope_rechecked(self):
        lab=self.ready();lab.approve('Maya');lab.submit()
        lab.record_payer_decision({'correlation':'HARBOR-7001','status':'APPROVED',
             'service':'SYN-IMG-01','site':'CEDAR-A','valid_from':'2026-11-10','valid_to':'2026-11-20'})
        self.assertTrue(lab.authorization_matches())
        lab.data['service_date']='2026-12-01'
        self.assertFalse(lab.authorization_matches())
        self.assertEqual(lab.data['payer_decision']['status'],'APPROVED')

    def test_T12_budget_stop_is_recorded(self):
        lab=Lab(max_steps=1);lab.execute(proposal('inspect_case'))
        with self.assertRaises(Blocked):lab.execute(proposal('inspect_case'))
        self.assertEqual(lab.data['trace'][-1]['reason'],'execution budget exhausted')

    def test_expired_policy_is_blocked(self):
        lab=Lab(today='2027-01-01')
        with self.assertRaises(Blocked):lab.execute(proposal('inspect_case'))

    def test_model_cannot_override_trusted_tenant(self):
        lab=Lab();p=proposal('inspect_case');p['tenant']='OTHER'
        with self.assertRaises(Blocked):lab.execute(p)
        self.assertEqual(lab.data['tenant'],'CEDAR')

    def test_read_before_citing_and_signature_check(self):
        lab=Lab()
        with self.assertRaises(Blocked):lab.execute(proposal('propose_packet',evidence=evidence_for(lab)))
        lab=Lab(fixture('missing'));lab.execute(proposal('read_document','D-01'))
        bad=[{'requirement_id':'R-ORDER','document_id':'D-01','quote':lab.data['documents']['D-01']['text']}]
        with self.assertRaises(Blocked):lab.execute(proposal('propose_packet',evidence=bad))

    def test_payer_receipt_cannot_be_promoted_to_approval(self):
        lab=self.ready();lab.approve('Maya');lab.submit()
        with self.assertRaises(Blocked):lab.record_payer_decision({'correlation':'HARBOR-7001','status':'RECEIVED'})
        self.assertEqual(lab.data['state'],'SUBMITTED_PENDING')

    def test_live_adapter_reads_message_text_not_reasoning(self):
        class FakeResponse:
            def __enter__(self):return self
            def __exit__(self,*args):pass
            def read(self):
                return json.dumps({'status':'completed','output':[
                    {'type':'reasoning','summary':[]},
                    {'type':'message','content':[{'type':'output_text','text':json.dumps(proposal('inspect_case'))}]}],
                    'usage':{'input_tokens':1,'output_tokens':1}}).encode()
        with patch.dict('os.environ',{'OPENAI_API_KEY':'unit-test-placeholder'}),patch('prior_auth_lab.urlopen',return_value=FakeResponse()) as mock:
            action,_=live_action([{'task':'synthetic'}],'test-model')
            self.assertEqual(action['tool'],'inspect_case')
            sent=json.loads(mock.call_args.args[0].data)
            self.assertFalse(sent['store'])
            self.assertTrue(sent['text']['format']['strict'])


if __name__=='__main__':unittest.main(verbosity=2)
