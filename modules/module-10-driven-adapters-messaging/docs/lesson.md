---
marp: true
theme: default
paginate: true
header: "DDD & Hexagonal Architecture Masterclass | Module 10"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Module 10: Driven Adapters for Messaging & External Services

## Integrating with Kafka and Payment Providers via Pure Outbound Ports

---

## 1. What is a Driven Adapter?

A Driven (Secondary) Adapter is triggered by our Application Service to interact with an external dependency:
- Database engines (PostgreSQL, MongoDB).
- Message brokers (Apache Kafka, RabbitMQ).
- External HTTP APIs (Stripe, Twilio, Shipping Carriers).

---

## 2. Inverting Dependencies for Resilient Messaging

The Application layer defines:
```java
public interface EventPublisherPort {
    void publish(DomainEvent event);
}
```
The Infrastructure layer provides:
```java
public class KafkaEventPublisherAdapter implements EventPublisherPort {
    @Override
    public void publish(DomainEvent event) { ... }
}
```
