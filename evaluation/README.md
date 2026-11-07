# Evidence needed before stronger claims

The existing 17 tests are runtime checks. They are not a benchmark of a model.
This protocol is a proposed next experiment; it contains no fabricated results.

## Compare three approaches

1. A credible deterministic baseline with indexing and document-version handling.
2. A fixed model workflow: extraction, then the same deterministic validation.
3. A bounded agent choosing allowed inspection actions, with the same validation.

Use identical access boundaries and business acceptance criteria. Do not give the
agent better source information than the alternatives. Separate development cases
from held-out evaluation cases before prompt tuning.

## Initial dataset proposal

Start with 30–50 original synthetic cases for debugging and exploratory evaluation,
not a statistically established production acceptance sample. Include routine
records, missing items, duplicates, conflicting versions, irrelevant quoted text,
wrong-patient results, untrusted instructions and external-response uncertainty.
Ground any real domain rules in cited current sources and domain review; otherwise
keep the policy explicitly fictional. Record expected outputs before model runs.

Repeat model trials and record model identifier, prompt/tool versions, date,
case version, token usage, latency, retries and raw permitted traces. Report the
number of cases and trials separately. Keep model quality separate from enforced
security boundaries and connector reliability.

## Report table

| Approach | Evidence relevance/completeness | Hard-boundary failures | Reviewer corrections/time | Latency/cost | Limits |
|---|---|---|---|---|---|
| Deterministic baseline | Not measured | Not measured | Not measured | Not measured | Pending |
| Fixed model workflow | Not measured | Not measured | Not measured | Not measured | Pending |
| Bounded agent | Not measured | Not measured | Not measured | Not measured | Pending |

Report every failure category, not just a blended score. A fabricated source or
cross-patient read must remain visible even when average quality improves. Human
reviewer time requires an actual reviewer; token duration is not a proxy.

## Engineering story template

- Observed failure and reproduction.
- Initial hypothesis and the evidence against it.
- First fix, why it failed or what it cost.
- Revised boundary and regression case.
- Measured result and remaining limitations.

Label a synthetic experiment as synthetic. A real Kodiflex account requires the
team's evidence and disclosure clearance. Do not convert a proposed design into
a story about a deployed customer system.
