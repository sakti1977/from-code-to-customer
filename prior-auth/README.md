# Cedar Imaging prior authorization lab

This original learning project accompanies **From Code to Customer**, revised
healthcare edition. All people, records, plans, requirements and outcomes are
fictional. `SYN-IMG-01` is not a CPT/HCPCS billing code. The two-item policy is a
teaching fixture, not a medical-necessity standard or a real payer policy.

## Start offline

Python 3.10 or later; no extra packages. From this folder:

```bash
python prior_auth_lab.py baseline --out run_baseline
python prior_auth_lab.py baseline --variant varied --out run_varied_baseline
python prior_auth_lab.py replay --variant varied --out run_varied_replay
python prior_auth_lab.py demo --out run_story
python -m unittest -v test_prior_auth.py
```

Use a different empty output folder for each run. Inspect `case.json` for state,
packet, approval and trace; `payer.json` holds the synthetic remote receipt.
The demo restarts from saved state after a timeout and reconciles one existing
request. It then injects an explicit mock payer approval. Receipt alone never
becomes approval. Authorization matching never means payment is guaranteed.

The baseline uses existing structured requirement tags. The replay path feeds
recorded tool proposals into the same execution boundary used by the optional
model. It is deterministic and is **not evidence of LLM quality or economic
benefit**. A stronger deterministic extraction baseline is a valid improvement.

## Optional live model

Use only these bundled synthetic records. Set `OPENAI_API_KEY` locally using
your usual secret-management method. Choose a model available to your account
that supports Responses API structured outputs, then run:

```bash
python prior_auth_lab.py live --model YOUR_MODEL_ID --out run_live
```

This sends synthetic task context and allowed source text to the OpenAI API and
can incur API charges. The API key is not written to the run folder. There are
at most 12 model calls per invocation, 1,200 output tokens per call and a
40-second HTTP timeout; these are not a currency-spend guarantee. `store:false`
does not by itself establish zero retention, a BAA, or suitability for ePHI.
The adapter was checked with a mocked API response; a live model run was not
performed for this edition. Inspect actual model behavior and usage yourself.

API references checked 7 November 2026:
- https://developers.openai.com/api/docs/guides/text
- https://developers.openai.com/api/docs/guides/structured-outputs

## What to inspect

- `execute`: typed tool allowlist, budget and trace boundary.
- `scoped_document`: tenant, patient and case checks before content is returned.
- `propose_packet`: exact source quote, read-before-cite, signature flag and missing items.
- `packet_hash` / `approve`: staff signs off on the version actually reviewed.
- `submit` / `reconcile`: persist intent, simulate remote acceptance, reconcile by original reference.
- `record_payer_decision`: a separate mock payer adapter, never an agent tool.

An exact quote can still be irrelevant. Staff review must judge the evidence
mapping and administrative adequacy. The code does not validate clinical
sufficiency, choose care, infer medical necessity or adjudicate coverage.

## Deliberate limits and extensions

This is a single-process local lab with JSON persistence, not a production
transaction service. The two files are not a distributed atomic transaction.
Real identity, access-control services, concurrent transactions, secret
management, audit retention, policy retrieval, OCR, FHIR conformance, real payer
submission, appeals and operational security are outside this implementation.
The mock payer contains one case and a fixed correlation ID. New invocations
reset the execution budget. Local filesystem write access can change the lab's
records; there is no adversarial storage protection.

Capstone: choose an extension from page 45 of the book: add regression coverage
for same-patient wrong-case reads, a durable escalation for unresolved submissions,
or stronger evidence-relevance checks. Add positive and negative tests, preserve
the original boundaries, and explain what your result does and does not prove.
Use the book's solo review cards if no colleague is available.

Set a publication/reuse licence with the presenting organisation before
redistributing this original code publicly. Referenced projects retain their
own licences. This folder has not been published to a public repository.
