---
marp: true
theme: default
paginate: true
header: "DDD & Hexagonal Architecture Masterclass | Module 07"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Module 07: Inbound (Driving) Ports & Application Services

## Orchestrating Use Cases Without Polluting Domain Logic

---

## 1. What is an Inbound (Driving) Port?

An Inbound Port represents a specific use case the application offers to the external world:
- It is an **interface** defined in `application/port/in/`.
- Callers (REST Controllers, CLI commands, Kafka message consumers) communicate ONLY through this interface.

```java
public interface PlaceOrderUseCase {
    OrderId placeOrder(PlaceOrderCommand command);
}
```
