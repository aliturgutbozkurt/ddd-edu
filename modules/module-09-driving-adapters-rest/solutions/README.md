# Solution 09: RFC 9457 Problem Details Translation

## Architecture Overview
In Hexagonal Architecture, HTTP status codes, JSON serialization, and RFC 9457 payloads belong exclusively to the **Driving Adapter (Infrastructure)** layer. The domain model never knows about HTTP 400, 404, or Problem Details.

## Key Files
- `ProblemDetailRecord.java`: Immutable Java 27 record representing RFC 9457.
- `GlobalExceptionHandler.java`: Adapter converting domain validation and lookup exceptions into RFC 9457 payloads.
- `GlobalExceptionHandlerSolutionTest.java`: 100% green test suite.
