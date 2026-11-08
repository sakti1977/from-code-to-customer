import io
import os
import runpy
import unittest
from contextlib import redirect_stdout

HERE = os.path.dirname(os.path.abspath(__file__))


def run(name):
    buf = io.StringIO()
    with redirect_stdout(buf):
        runpy.run_path(os.path.join(HERE, name), run_name="__main__")
    return buf.getvalue()


class PaymentLab(unittest.TestCase):
    def test_careless_pays_twice_when_reply_is_lost(self):
        out = run("payment_lab.py")
        self.assertIn("careless reply_lost", out)
        self.assertIn("Rs 97,000", out)

    def test_careful_pays_once_in_both_modes(self):
        out = run("payment_lab.py")
        careful = [l for l in out.splitlines() if l.startswith("careful")]
        self.assertEqual(len(careful), 2)
        self.assertEqual(out.count("Rs 97,000"), 1)


class AskModel(unittest.TestCase):
    def test_offline_model_is_held_by_harness(self):
        os.environ.pop("ANTHROPIC_API_KEY", None)
        out = run("ask_model.py")
        self.assertIn("HELD", out)

    def test_harness_refuses_unknown_action(self):
        ns = runpy.run_path(os.path.join(HERE, "ask_model.py"))
        self.assertTrue(ns["harness"]({"action": "export"}).startswith("REFUSED"))
        self.assertTrue(ns["harness"]({"action": "pay", "amount": "lots"}).startswith("HELD"))
        self.assertTrue(ns["harness"]({"action": "pay", "amount": 48500}).startswith("ALLOWED"))


if __name__ == "__main__":
    unittest.main()


def test_notebook_cells_run_in_order():
    """The no-typing notebook must stay runnable top to bottom."""
    import contextlib
    import io
    import json
    import pathlib
    nb = json.loads((pathlib.Path(__file__).parent / "payment_lab.ipynb").read_text())
    scope = {"__name__": "notebook"}
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        for cell in nb["cells"]:
            if cell["cell_type"] == "code":
                exec("".join(cell["source"]), scope)
    text = out.getvalue()
    assert "Rs 97,000" in text and "Rs 48,500" in text
    assert "HELD" in text
