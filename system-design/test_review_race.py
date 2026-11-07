from pathlib import Path
import tempfile
import unittest
from review_race import connect,initialize,approve,edit,record_intent,StaleReview

class ReviewRaceTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.path=Path(self.tmp.name)/'case.db'
        initialize(self.path);self.a=connect(self.path);self.b=connect(self.path)
    def tearDown(self):
        self.a.close();self.b.close();self.tmp.cleanup()
    def test_stale_reader_cannot_submit_after_another_worker_edits(self):
        approve(self.a)
        cached=self.a.execute('SELECT version,approved_version FROM packet').fetchone()
        self.assertEqual(cached,(1,1))
        edit(self.b,'new packet')
        with self.assertRaises(StaleReview):record_intent(self.a)
        self.assertEqual(self.a.execute('SELECT count(*) FROM intent').fetchone()[0],0)
    def test_current_review_records_current_content(self):
        edit(self.b,'new packet');approve(self.a);record_intent(self.a)
        self.assertEqual(self.b.execute('SELECT version,body FROM intent').fetchone(),(2,'new packet'))
    def test_repeat_intent_after_restart_has_one_key(self):
        approve(self.a);key=record_intent(self.a)
        with connect(self.path) as restarted:self.assertEqual(record_intent(restarted),key)
        self.assertEqual(self.b.execute('SELECT count(*) FROM intent').fetchone()[0],1)
    def test_edit_after_intent_requires_amendment(self):
        approve(self.a);record_intent(self.a)
        with self.assertRaises(StaleReview):edit(self.b,'changed')
        self.assertEqual(self.a.execute('SELECT version FROM packet').fetchone()[0],1)

if __name__=='__main__':unittest.main()
