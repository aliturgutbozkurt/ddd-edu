---
marp: true
theme: default
paginate: true
header: "DDD & Hexagonal Architecture Masterclass | Module 03"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Module 03: Value Objects & Immutability with Java 27 Records

## Replacing Primitive Obsession with Pure Invariant Encapsulation

---

## 1. What Makes a Value Object?

A Value Object is defined by its attributes, NOT by an identity:
1. **No Identity**: If two Value Objects have identical fields, they are equal.
2. **Immutability**: Once constructed, its state can NEVER change.
3. **Conceptual Whole**: Represents a complete domain concept (`Money`, `EmailAddress`, `PostalAddress`).
4. **Self-Validating**: An invalid Value Object can NEVER exist in memory.
5. **Side-Effect-Free Behavior**: Methods return new instances instead of mutating existing state.

---

## 2. Eliminating Primitive Obsession

### The Anti-Pattern:
```java
// Danger: What is the currency? Can price be -500? Can tax be null?
public void processPayment(String email, double price, double tax) { ... }
```

### The Java 27 Record Solution:
```java
public record EmailAddress(String value) implements ValueObject {
    private static final Pattern PATTERN = Pattern.compile("^[A-Za-z0-9+_.-]+@(.+)$");
    public EmailAddress {
        if (value == null || !PATTERN.matcher(value).matches()) {
            throw new DomainValidationException("Invalid email format: " + value);
        }
        value = value.toLowerCase().trim();
    }
}
```
