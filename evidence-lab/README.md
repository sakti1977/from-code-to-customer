# Evidence relevance: a passing boundary can still accept the wrong source

Run with Python 3.10+ and no dependencies:

```sh
python evidence-lab/evidence_lab.py
python -m unittest discover -s evidence-lab -p 'test_*.py' -v
```

## Observed development results, 7 November 2026

| Approach | Exact expected case mappings | Unsupported selected items | Missing expected items |
|---|---:|---:|---:|
| Original structured-tag baseline | 5/12 | 5 | 6 |
| Cautious header parser | 11/12 | 0 | 2 |

These are 12 deliberately authored development fixtures with author-assigned
answers. They are not a representative sample, a held-out benchmark, an LLM
comparison or clinical validation. The parser was designed with these cases in
view. The results show behaviour in this exercise only. Raw inputs are generated
by `cases()`; every expected mapping and observed output is in `results.json`.

An exact mapping includes correct abstention: two current orders require review,
so neither is selected automatically. Unsupported means a selected requirement/
document pair differs from the reference. Missing means an expected pair was not
returned; selecting the wrong document can count in both categories. Report these
counts separately rather than adding them as independent case failures.

## What broke

A signed billing document is incorrectly tagged as an order. The old baseline
selects it. The general runtime also accepts a verbatim quote from that document
as an order candidate: the quote exists, the document is in scope, and signed=true.
Those checks do not establish that it is an order. A dedicated test records this
limitation rather than treating a passing suite as proof of semantic correctness.

The cautious parser checks a narrow declared document type, service and current
status, rejects unsigned orders and abstains on duplicate current candidates. It
avoids that false selection but returns nothing for the prose-only case. This is
an honest trade-off, not evidence that language models are unnecessary or superior.

The test asserting runtime acceptance documents a known boundary limitation. It
is not a production acceptance criterion. A real deployment needs evidence-
adequacy evaluation and accountable review, as well as mechanical access controls.

## Twelve cases

Routine; missing tags; misleading tag; superseded copy; wrong service; unsigned
order; missing referral; two current orders; injected source text; wrong patient;
prose without headers; unclear status. All documents and requirements are synthetic.
The toy grammar is not a payer policy or a clinical standard.

## Next experiment

Implement a fixed model extraction and an agent using the same sources and
permissions, pre-register held-out cases, and record repeated live runs. Measure
mapping quality, abstention, corrections, latency and usage separately. No live
model experiment was run for these results; a credential was not available.

## Capstone review

Use cases 08, 11 and 12. Explain the ambiguity, decide which questions need a human,
and propose an improvement without weakening tenant, patient or approval controls.
Provide a failing regression case, a change, the resulting trace and a release
recommendation. The expected mappings are available for self-study; they are not
hidden assessment data. A team assessor should supply additional unseen cases.
