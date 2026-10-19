# Tool execution discipline
1. Inspect project manifests and relevant scripts before running them. Even tests/builds can connect to production, run migrations, send mail or execute installation hooks.
2. Prefer already installed tools and locked dependencies. Do not silently download or install a scanner. Record unavailable tools and continue manual review.
3. Establish network/cloud usage: source upload, dependency metadata transmission, telemetry, external API costs and credentials. Obtain authorization where not already given.
4. Use only an isolated test environment with synthetic secrets/data. Disable external side effects. Avoid broad environment dumps.
5. Record version, scan scope, redacted command, exit code, result location and limitations. A nonzero exit can mean findings OR failure: check the tool's documented semantics.

Potential tools, when available and appropriate:
- Semgrep: static patterns; review matches against control flow and suppress false positives with reasons.
- Package-manager audit or OSV-compatible tooling: installed version/advisory matches; independently assess production presence and reachability.
- Gitleaks-compatible secret scanner: enable redaction; do not include discovered values in reports. History scanning is a separate, declared scope.
- Browser/HTTP tests: synthetic authorized accounts, low request counts, exact allowed origin list; deny outbound redirects outside scope.
- ZAP-compatible dynamic tooling: use only with explicit active-test scope and test environment. Do not start an automatic attack scan because a URL was supplied.

No scanner is required for a valid partial manual review. Never auto-run `audit fix`, migrations, mass updates, destructive probes or production exploit payloads as part of report-only auditing.
