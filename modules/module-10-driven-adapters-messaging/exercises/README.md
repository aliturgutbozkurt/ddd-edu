# Exercise 10: Resilient Payment Gateway Driven Adapter

## Objective
Implement an Outbound Driven Adapter (`ResilientPaymentGatewayAdapter`) satisfying the outbound SPI `PaymentGatewayPort`.
The adapter wraps an external third-party payment provider and applies a retry policy to gracefully handle transient network glitches.

## Requirements
1. Implement `PaymentGatewayPort`:
   - `PaymentResult charge(PaymentRequest request)`
2. The adapter must:
   - Retry transient failures up to `maxRetries` (default: 3).
   - If transient errors persist beyond `maxRetries`, return a failed `PaymentResult` with details instead of bubbling raw network exceptions into the domain.
   - Record total execution attempts.
3. Verify behavior with automated tests.

## Running Tests
Run: `src/test/java/com/turkninja/ddd/module10/exercise/ResilientPaymentExerciseTest.java`
Remove `@Disabled` and verify your implementation.
