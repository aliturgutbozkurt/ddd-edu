# Exercise 09: RFC 9457 Problem Details Exception Handler

## Objective
Implement an HTTP driving adapter error-handling mechanism compliant with **RFC 9457** (`application/problem+json`).
The adapter translates pure domain exceptions (`DomainValidationException`, `ResourceNotFoundException`) into structured Problem Detail records.

## Requirements
1. Define a problem details data carrier with fields: `type` (URI), `title`, `status` (HTTP int), `detail` (string message), `instance` (URI string), and `timestamp`.
2. Implement translation logic:
   - `DomainValidationException` -> Status 400 Bad Request, type `https://api.turkninja.com/errors/validation-error`, title "Domain Validation Failure".
   - `NoSuchElementException` -> Status 404 Not Found, type `https://api.turkninja.com/errors/not-found`, title "Resource Not Found".
   - Unhandled exceptions -> Status 500 Internal Server Error.
3. Verify with unit tests.

## Running Tests
Run the exercise test in:
`src/test/java/com/turkninja/ddd/module09/exercise/ProblemDetailsExerciseTest.java`
Remove `@Disabled` and make tests pass!
