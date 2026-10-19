# Evidence and triage
## Evidence status
- reproduced: an isolated test exercised the relevant real path and demonstrated unauthorized behavior, with steps, expected/actual results and execution evidence.
- code-confirmed: a complete reachable source trace demonstrates the flaw; relevant guards have been inspected. Runtime testing is absent; explicitly list environment assumptions.
- unverified: missing configuration, incomplete trace, scanner-only alert, uncertain advisory match, or unexecuted hypothesis. Exclude from confirmed totals.

Confidence high/medium/low describes evidentiary certainty; severity describes impact. Do not call an unverified suspicion high-confidence. Tool warnings are candidates until reviewed.

## Severity
- critical: realistically reachable broad takeover, arbitrary server execution, or comparably severe compromise with few prerequisites.
- high: substantial unauthorized access/modification, meaningful privilege escalation or sensitive data exposure.
- medium: bounded meaningful impact, or stronger prerequisites that materially restrict exploitation.
- low: limited demonstrated security impact.
- informational: hardening or contextual observation without demonstrated exploitability.
Explain the actual preconditions and affected population. Not every theoretical dependency exploit is reachable. Do not downgrade a genuine flaw merely because no runtime environment is available.

## Required finding evidence
Stable ID; title; severity; confidence; evidence status; exact path and line range; snapshot/commit in scope; affected endpoint; actor and prerequisites; source-to-sink trace; checked controls; expected/actual behavior; redacted evidence; validation method and result; business impact; minimal fix; regression test; residual assumptions.

## Reject common false positives
A missing route-local guard may be enforced upstream. ORM use neither proves nor disproves injection. Public data access can be intended. Client-side hiding is not server authorization. Missing CSP is not by itself demonstrated XSS. Missing rate limiting needs a concrete abuse path and impact. A failing test caused by missing dependencies proves no vulnerability. A green mocked unit test proves no complete security boundary. Do not claim a security patch shipped from a diff alone.

## findings.json contract
Top-level keys: schema_version (1), scope (object), findings (array).
Scope requires nonempty repository, revision and date strings; use 'unavailable: reason' when necessary. status is partial or completed; limitations is an array of strings. Completed means the declared review plan is complete, not that the system is secure.
Every finding requires nonempty text fields: id, title, location, preconditions, flow, controls_checked, impact, evidence, validation, remediation, retest. location includes path and line(s); validation states what ran versus what remains proposed. Allowed severity: critical, high, medium, low, informational. Allowed confidence: high, medium, low. Allowed evidence_status: reproduced, code-confirmed, unverified. IDs must be unique. Use informational for hardening observations, and keep them outside confirmed vulnerability counts. Never mark unverified evidence with high confidence.
