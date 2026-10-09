# Module 05: Aggregates, Aggregate Roots & Domain Invariants

## 🎯 Learning Objectives
- Master the **Aggregate Pattern** as a transactional consistency boundary.
- Encapsulate child entities (`OrderItem`) inside the **Aggregate Root** (`Order`).
- Guard multi-entity business invariants (e.g. maximum item count, total price calculation).
- Prevent reference leakage by returning unmodifiable collections.
