# Solution 11: Architectural Fitness Functions with ArchUnit

## Architectural Insight
Architecture diagrams in wikis rot quickly. Executable ArchUnit rules fail the build if a developer accidentally imports a Spring repository in the domain model or names a concrete adapter as an interface.

## Key Files
- `CustomHexagonalRules.java`: Static reusable ArchUnit rules.
- `CustomHexagonalRulesSolutionTest.java`: Verification suite executing against module packages.
