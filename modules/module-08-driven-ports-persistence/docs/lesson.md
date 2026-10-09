---
marp: true
theme: default
paginate: true
header: "DDD & Hexagonal Architecture Masterclass | Module 08"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Module 08: Outbound (Driven) Ports & Persistence Adapters

## Decoupling Persistence from Domain Logic

---

## 1. Why Not Use JPA Annotations in Domain Entities?

Placing `@Entity`, `@Table`, and `@Id` inside domain entities violates Hexagonal Architecture:
- JPA requires default no-arg constructors (violating invariant validation).
- JPA requires non-final fields and mutable collections.
- Database schema changes force domain model refactoring.

---

## 2. The Driven Persistence Adapter Pattern

```
[Domain Aggregate: Order]
           ▲
           │ (Mappers)
           ▼
[Persistence Adapter: OrderPersistenceAdapter] ──> [Spring Data / JPA Entity]
```
