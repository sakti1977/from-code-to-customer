# From Code to Customer

*Minocha Praxis / Kodiflex Quick Guides · Accelerating AI Adoption Series · Authored by Sakti Prasad Bagchi · First Edition, Bangalore Tech Summit Edition (November 2026)*

**What is new?** See [LATEST.md](LATEST.md) for changes since the book was printed.

A companion for working engineers learning domain discovery, system design,
agentic implementation and customer communication. Start with one workflow:
synthetic US provider-side prior authorization.

**Status:** educational starter, not a production application or completed benchmark.
The healthcare lab is synthetic. No real patient data or real payer integration.

## Choose your gap

| I need help with… | Start here | Produce |
|---|---|---|
| Running my first agent lab (no AI model needed) | [Beginner lab](beginner-lab/README.md) | A run that shows a double payment, then the fix |
| Learning an unfamiliar domain | [Domain fieldwork](domain/README.md) | Reviewed workflow and evidence ledger |
| Designing a dependable system | [System design](system-design/README.md) | Architecture decision and race-condition test |
| Speaking and writing clearly | [Communication](communication/README.md) | Recorded explanation and customer follow-up |
| Building an agent runtime | [Prior-auth lab](prior-auth/README.md) | Candidate packet and restart trace |
| Proving model usefulness | [Evaluation protocol](evaluation/README.md) | Measured comparison, including failures |
| Controlling an AI coding agent | [Harness Engineering](https://github.com/sakti1977/Harness-Engineering) | Outcome checks and a verified handoff |

The existing Harness Engineering repository concerns the environment around a
**coding agent**. The prior-auth lab concerns an assistant **inside an application**.
Some principles transfer, but their permissions, inputs and evaluation targets differ.
This companion links to that project instead of copying it.

## Run offline

Python 3.10 or newer, standard library only. From this directory:

```sh
python -m unittest discover -s prior-auth -p 'test_*.py' -v
python -m unittest discover -s system-design -p 'test_*.py' -v
python -m unittest discover -s beginner-lab -p 'test_*.py' -v
python system-design/review_race.py
python prior-auth/prior_auth_lab.py demo --out /tmp/cedar-demo-new
```

Use a fresh output path for the prior-auth demo. See its README before optional
paid live-model use. Offline replay does not measure model accuracy.

## Learning contract

Read one source, inspect one worked example, make one artifact, challenge it
with a counterexample, and revise it. Passing a file-format check or an AI grading
prompt cannot certify domain competence, English proficiency or safe deployment.

All source links and access notes are in [resources](resources/README.md).
Original exercises are provided here; linked publishers retain their own terms.
Do not copy their books or videos into this repository without permission.

## Next evidence required

1. A richer synthetic document pack with ambiguous and conflicting evidence.
2. A stronger deterministic baseline and a fixed model workflow alongside the agent.
3. Real model runs on held-out cases, reported separately from runtime unit tests.
4. Independent domain and engineering review, with changes recorded.
5. A verified Kodiflex engineering story supplied by the team, not invented for marketing.

See [evaluation protocol](evaluation/README.md). This starter does not claim these
items are already complete. Repository: https://github.com/sakti1977/from-code-to-customer
Original-content reuse terms have not yet been assigned; linked projects retain
their own licences.
