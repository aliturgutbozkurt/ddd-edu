---
marp: true
theme: default
paginate: true
header: "DDD & Hexagonal Architecture Masterclass | Module 05"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Module 05: Aggregates, Aggregate Roots & Domain Invariants

## Designing Transactional Boundaries and Enforcing Business Invariants

---

## 1. What is an Aggregate?

An Aggregate is a cluster of associated objects (Entities and Value Objects) that we treat as a unit for the purpose of data changes:
- **Aggregate Root**: The single entry point to the aggregate. Outside objects can ONLY hold a reference to the root.
- **Consistency Boundary**: All invariants inside the aggregate must be satisfied at the end of every transaction.
- **Rule of Thumb**: Keep aggregates small! Reference other aggregates by **ID only**, never by object reference.
