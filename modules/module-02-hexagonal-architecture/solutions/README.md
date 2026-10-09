# Solution 02: Hexagonal Decoupling & Inverted Dependencies

## Architectural Review
In this solution, the discount policy calculation is isolated behind a pure Java interface (`DiscountPolicyPort`), allowing diverse implementations (e.g. VIP discount, seasonal discount) without mutating domain logic.
