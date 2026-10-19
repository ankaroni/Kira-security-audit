# Security review matrix
For each applicable area record evidence, not just a checkmark. Mark non-applicable with a reason. This is a practical checklist, not a claim of complete OWASP coverage.

| Area | Investigate | Useful falsification or test |
|---|---|---|
| Authentication | Login/reset/magic links, account enumeration, token expiry/reuse, OAuth state/PKCE where applicable, MFA recovery | Expired/reused token fails; redirect target and callback binding hold |
| Sessions | Cookie flags/scope, CSRF protections, token verification, logout/revocation, role changes | Old sessions lose rights when required; cross-origin writes are rejected |
| Authorization | Anonymous access, IDOR/BOLA, function-level permissions, mass assignment, tenant boundaries | A/B users plus admin; alter IDs and protected fields; inspect shared checks |
| APIs | Validation/coercion, query limits, field filtering, batch operations, GraphQL complexity | Oversized batches and unauthorized fields are bounded without load testing |
| Injection | SQL/raw ORM, command execution, templates, NoSQL, LDAP where present | Trace untrusted values into actual sink; parameterized values differ from identifiers |
| Browser boundaries | Reflected/stored/DOM XSS, unsafe HTML/URLs, CORS, CSRF, redirects, framing | Determine actual context/encoding and reachable victim action; CORS alone is not CSRF protection |
| SSRF | Imports, previews, image/PDF fetchers, redirects, URL parsers, egress | Inspect host/IP checks across redirects and DNS; use local fixtures, never cloud metadata |
| Uploads/files | Size/type/content checks, traversal, archives, executable content, storage ACLs | Synthetic files; normalized paths, private object access, signed URL scope/expiry |
| Data/crypto | Sensitive response fields/logs, encryption use, randomness, key placement, exports/deletion | Inspect actual response serialization and redaction; never reproduce with real PII |
| Payments/webhooks | Signature over correct payload, event replay, amount/currency source, idempotency, refunds | Synthetic signed fixtures, duplicate/out-of-order events, server-side entitlement decisions |
| Business logic | State transitions, concurrent claims, inventory/quota, coupons, moderation, ownership transfer | Local concurrent requests; database constraints/transactions and invariant checks |
| Resource abuse | Login/reset/translation/upload quotas, distributed rate limits, timeouts, job retries | Inspect shared limiter key/trust and bounded work; no live brute force or load test |
| Infrastructure | Debug endpoints, trusted proxy handling, headers/TLS, environment separation, public buckets | Distinguish source defaults from actual deployment; avoid claiming unseen config |
| Supply chain/CI | Lockfiles, known advisories, install hooks, workflow permissions, fork PR secrets | Pin advisory/package/version; assess reachability separately from vulnerable version |
| Jobs/realtime | Queue authorization, poison/replay messages, cron access, websocket subscription isolation | Verify identity at subscribe and message/action time; tenant-safe cache keys |

Primary references to consult as needed:
- OWASP WSTG: https://owasp.org/www-project-web-security-testing-guide/
- OWASP ASVS: https://owasp.org/www-project-application-security-verification-standard/
- OWASP API Security: https://owasp.org/www-project-api-security/
- CWE: https://cwe.mitre.org/
Use exact versioned control IDs only after checking that version. These links are reference entry points, not proof of compliance.
