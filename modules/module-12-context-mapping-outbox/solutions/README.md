# Solution 12: Anti-Corruption Layer (ACL) & Context Mapping

## Architectural Insight
When integrating bounded contexts with legacy enterprise systems, never allow external schemas or database models to bleed into your domain model. The Anti-Corruption Layer acts as a defensive membrane, sanitizing data at the boundary.

## Key Files
- `LegacyErpOrderPayload.java`: Raw external DTO representing the upstream legacy system.
- `CleanOrder.java`: Clean Java 27 domain representation.
- `LegacyOrderAclTranslator.java`: Pure ACL translator.
- `LegacyOrderAclTranslatorSolutionTest.java`: Automated test suite.
