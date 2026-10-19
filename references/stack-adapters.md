# Conditional technology checks
Detect installed versions and actual patterns. Do not assume all technologies below exist.

## Next.js / Node / React
Inventory route handlers, API routes, server actions, middleware and runtime choices. Trace session and ownership checks at every server entry point; layout/page redirects alone do not secure APIs. Inspect cache keys and caching of personalized responses, redirects, URL fetches, unsafe HTML and client/server secret boundaries. Check proxy-derived IP trust before assessing rate limits. Confirm behavior using documentation for installed versions.

## Prisma / PostgreSQL / Supabase
Inspect raw queries, parameter boundaries, transactions, uniqueness constraints and concurrent writes. Parameterization does not automatically protect dynamically composed table/column identifiers. Establish the actual database role and access path before reasoning about RLS. A server-side privileged connection may bypass policies; a service key on a trusted server is not by itself exposure. Inspect tenant predicates, storage policies and direct client access independently. Connection saturation is an availability finding only when a credible trigger/impact is established.

## Session/OAuth providers
Inspect server verification, callback validation, cookie configuration, role freshness and session revocation. Do not infer defaults from a different library version. Verify whether the provider or application owns each control.

## Commerce and marketplaces
Test listing ownership, dealer membership, moderation permissions, private conversations, favorites, bulk imports and account export/delete. For paid promotion/subscriptions trace server price selection, payment signature, event deduplication and expiry. Separate feature requests from broken security invariants.

## Other stacks
Build an equivalent adapter from source: entry points, authentication, authorization, validation, data access, storage, async work and deployment. Mark unknown framework behavior instead of copying Node-specific assumptions.
