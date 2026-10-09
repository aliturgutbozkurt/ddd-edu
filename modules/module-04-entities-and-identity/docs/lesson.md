---
marp: true
theme: default
paginate: true
header: "DDD & Hexagonal Architecture Masterclass | Module 04"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Module 04: Entities, Identity & Lifecycle in Domain Models

## Preserving Continuity and Encapsulating State Changes

---

## 1. What is an Entity?

An Entity represents an individual business object that has **thread of continuity** and identity over time:
- Even if all attributes change (name, address, email), the customer remains the SAME customer.
- Two customers with identical names and birthdates are NOT the same customer if their `CustomerId` differs.

---

## 2. Equality by Identity

```java
public abstract class DomainEntity<ID extends ValueObject> {
    protected final ID id;
    
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        DomainEntity<?> that = (DomainEntity<?>) o;
        return Objects.equals(id, that.id);
    }
}
```
