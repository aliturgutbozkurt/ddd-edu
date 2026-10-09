# Exercise 01: Enforcing Ubiquitous Language & Daily Withdrawal Invariants

## 🎯 Task Objectives
In this exercise, you will extend the `BankAccount` rich aggregate root to enforce a critical business invariant: **Daily Withdrawal Limit**.

### Business Rules (Invariants):
1. **Daily Limit Constraint**: A bank account has a `DailyWithdrawalLimit` (Value Object).
2. **Accumulation**: The aggregate root must track the total amount withdrawn in the current calendar day.
3. **Breach Rejection**: If a withdrawal request causes today's total withdrawals to exceed `DailyWithdrawalLimit`, the operation MUST throw `DailyLimitExceededException` and the account balance must remain unchanged.
4. **Day Roll-Over**: If a withdrawal occurs on a new calendar day, the daily withdrawal total resets automatically.
5. **Domain Event**: Upon successful withdrawal, record a `DailyLimitUpdatedEvent`.

---

## 🛠️ Instructions
1. Open the starter test class in `exercises/src/test/java/DailyLimitTest.java`.
2. Observe the failing tests marked with `fail("TODO: Implement daily limit invariant")`.
3. Implement `DailyWithdrawalLimit` value object and update `BankAccount`.
4. Run `./mvnw test` until all tests turn green.
