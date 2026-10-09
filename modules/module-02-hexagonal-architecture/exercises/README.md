# Exercise 02: Refactoring Monolithic Discount Logic to Hexagonal Ports

## 🎯 Business Context
The marketing department wants to apply dynamic discount policies to products. Currently, discounts are hard-coded in an old static utility class.

## 📋 Acceptance Criteria
1. Define an Inbound Port: `CalculateDiscountUseCase` with method `Money applyDiscount(ProductId id, CustomerTier tier)`.
2. Define an Outbound Port: `DiscountPolicyPort` with method `BigDecimal getDiscountPercentage(CustomerTier tier)`.
3. Implement an Application Service implementing the Inbound Port and consuming the Outbound Port.
4. Implement two driven adapters: `StandardDiscountPolicyAdapter` (0% discount) and `VipDiscountPolicyAdapter` (15% discount).
5. All domain logic must remain pure Java without framework dependencies.
