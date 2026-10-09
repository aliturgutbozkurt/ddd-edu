---
marp: true
theme: default
paginate: true
header: "DDD & Hexagonal Architecture Masterclass | Module 06"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Module 06: Domain Events & Event-Driven Decoupling

## Capturing Past Business Facts with Java 27 Sealed Types

---

## 1. What is a Domain Event?

A Domain Event captures something that occurred in the past that domain experts care about:
- **Naming Rule**: Always in **past tense** (`OrderPlacedEvent`, `PaymentReceivedEvent`, `ShipmentDispatchedEvent`).
- **Immutable**: Events happened in the past; they can never be modified or undone.
- **Payload**: Contains the event ID, timestamp, and domain identifiers necessary for subscribers to react.

---

## 2. Java 27 Sealed Interfaces for Events

```java
public sealed interface OrderDomainEvent extends DomainEvent {
    OrderId orderId();

    record OrderCreatedEvent(UUID eventId, OrderId orderId, Instant occurredOn) implements OrderDomainEvent {}
    record OrderCancelledEvent(UUID eventId, OrderId orderId, String reason, Instant occurredOn) implements OrderDomainEvent {}
}
```
