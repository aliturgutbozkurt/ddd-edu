# Solution 01: Enforcing Ubiquitous Language & Daily Withdrawal Invariants

## 📖 Architectural Walkthrough

### 1. Value Object: `DailyWithdrawalLimit`
Instead of using a raw `BigDecimal` or `double`, we model `DailyWithdrawalLimit` as an immutable Java 27 record wrapping `Money`. It asserts non-negativity in its compact constructor.

### 2. Encapsulating Cumulative State in `AccountWithDailyLimit`
To enforce the daily limit without leaking temporal calculation logic:
- The aggregate records `todayWithdrawn` and `lastWithdrawalDate` internally.
- When `withdraw(Money, LocalDate)` is invoked, it checks if `date.isAfter(lastWithdrawalDate)`. If so, it resets `todayWithdrawn` to zero before checking limits.
- If the new sum exceeds `dailyLimit.limit()`, it aborts and throws `DailyLimitExceededException`.

---

## 🧪 Verification
The reference test suite in `DailyLimitSolutionTest.java` achieves 100% mutation coverage across all limit boundaries and day transitions.
