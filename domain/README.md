# Learn a domain by tracing work

You do not need to become a clinician to implement an administrative handoff.
You do need to know which decisions you understand, which evidence supports them,
and which person must resolve the questions beyond your expertise.

## A suggested ten-session learning cycle

This is a practice schedule, not a promise of expertise in ten days.

1. Read an introductory domain source. Make a 20-term glossary in plain language.
2. Draw the actors and the money/information flows. Mark what you do not know.
3. Read authoritative guidance for one narrow workflow. Record date and scope.
4. Ask a practitioner to walk through the last ordinary case.
5. Ask for a difficult case. Record exceptions and workarounds, with permission.
6. Trace a synthetic request from input to final status. Who owns each decision?
7. Separate observed facts, source-backed rules, inferences and unanswered questions.
8. Ask the practitioner to correct your map and glossary. Preserve corrections.
9. Turn one rule and one exception into executable acceptance cases.
10. Explain the workflow back, including what the software must never infer.

Without practitioner access, work from public examples and mark the result
**desk research only**. An AI role-play helps rehearse an interview; it is not
field evidence or a replacement for a domain reviewer.

## Worked evidence ledger

| Statement | Status | Evidence / scope | Validation still needed |
|---|---|---|---|
| A receipt is distinct from a payer authorization decision | Source-backed workflow distinction | CMS prior-authorization API guidance; US context | Actual connector's response mapping |
| Maya spends six minutes looking for documents | Fictional assumption | Cedar teaching case only | Observe the real workflow; do not quote as measured |
| D-01 carries a trusted signature flag | Fixture fact | Local lab only | Real metadata provenance and authenticity |
| Improving preparation will halve elapsed turnaround | Unsupported hypothesis | None | Separate staff work from external waiting |

For your own ledger, add source URL, exact section, checked date, relevant payer /
jurisdiction, policy effective dates where relevant, reviewer and next action.

## Interview guide

- Show me the last completed case. What happened first?
- Which record told you what to do next?
- Where did you have to leave the main system?
- What happens when that record is wrong or missing?
- Who can settle a disagreement about this requirement?
- Which steps use judgement rather than a written rule?
- What would make assistance create more work for you?

Ask about observed events before asking for opinions about a proposed AI feature.
Do not collect confidential records just to make a training project more realistic.

## Assessment

An operator calls a portal status “approved”; the connector calls it “received.”
What do you do? Identify the authoritative source, inspect the response contract,
ask the responsible domain owner, and preserve uncertainty until resolved. Do not
choose whichever label fits your intended demo.

Ready to move on when a domain reviewer can inspect your state map, challenge
three exception paths and find an explicit owner for unresolved decisions.
A reading list alone does not meet this criterion.

## Start with legitimate sources

- [ONC Health IT curriculum](https://healthit.gov/health-it-basics/health-it-curriculum-resources-educators): healthcare systems and workflow foundations. Some material is historical; do not use it for current regulatory deadlines.
- [CMS electronic prior authorization](https://www.cms.gov/priorities/electronic-prior-authorization/overview): current US policy context; verify scope for the actual payer/workflow.
- [HL7 CRD 2.2.1](https://hl7.org/fhir/us/davinci-crd/2.2.1/en/index.html): a pinned technical guide, best read after understanding the workflow.
- [GOV.UK interviewing guidance](https://www.gov.uk/service-manual/user-research/using-in-depth-interviews): plan interviews and learn from real work.
