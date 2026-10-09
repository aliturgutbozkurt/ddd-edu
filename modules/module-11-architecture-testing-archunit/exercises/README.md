# Exercise 11: Writing Custom ArchUnit Port and Adapter Rules

## Objective
Write executable architectural fitness functions using ArchUnit to enforce Hexagonal Architecture conventions:
1. Inbound driving ports must be interfaces ending in `UseCase`.
2. Outbound driven ports must be interfaces ending in `Port`.
3. Domain entities must not depend on Spring or Jackson.

## Running Tests
Run: `src/test/java/com/turkninja/ddd/module11/exercise/CustomArchRuleExerciseTest.java`
Remove `@Disabled` and pass the tests.
