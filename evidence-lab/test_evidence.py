import unittest
from evidence_lab import cases,cautious_baseline,runtime,run

class EvidenceTests(unittest.TestCase):
    def case(self,name):return next(c['fixture'] for c in cases() if name in c['id'])
    def test_superseded_tag_does_not_outvote_current_source(self):
        result=cautious_baseline(runtime.Lab(self.case('superseded')))
        self.assertEqual(result['R-ORDER'],'D-01')
    def test_ambiguous_current_orders_require_review(self):
        self.assertNotIn('R-ORDER',cautious_baseline(runtime.Lab(self.case('two-current'))))
    def test_wrong_service_is_not_order_evidence(self):
        self.assertNotIn('R-ORDER',cautious_baseline(runtime.Lab(self.case('wrong-service'))))
    def test_unfamiliar_prose_is_a_visible_limitation(self):
        self.assertEqual(cautious_baseline(runtime.Lab(self.case('prose'))),{})
    def test_exact_quote_boundary_does_not_prove_relevance(self):
        lab=runtime.Lab(self.case('misleading-tag'))
        lab.execute(runtime.proposal('read_document','D-09'))
        quote=lab.data['documents']['D-09']['text']
        result=lab.execute(runtime.proposal('propose_packet',evidence=[dict(requirement_id='R-ORDER',document_id='D-09',quote=quote)]))
        # A recorded limitation: the general runtime accepts this exact but irrelevant quote.
        self.assertEqual(result['missing'],['R-REFERRAL'])
        self.assertEqual(lab.data['packet']['evidence'][0]['document_id'],'D-09')
    def test_report_contains_every_named_case(self):
        report=run();self.assertEqual(len(report['cases']),12)
        self.assertTrue(all('expected' in r and 'cautious_score' in r for r in report['cases']))

if __name__=='__main__':unittest.main()
