---
marp: true
theme: default
paginate: true
header: "DDD & Hexagonal Architecture Masterclass | Module 12"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Module 12: Context Mapping & Transactional Outbox Pattern

## Integrating Distributed Bounded Contexts Reliably

---

## 1. The Dual-Write Problem

When updating a database and publishing an event to Kafka in the same use case:
- If the database commit succeeds but Kafka crashes, events are lost!
- If Kafka succeeds but the database transaction rolls back, phantom events are published!

---

## 2. The Transactional Outbox Solution

Save both the Aggregate state AND the Outbox event record within the **SAME local SQL transaction**:

```
[SQL Transaction: BEGIN]
  1. INSERT INTO orders (...)
  2. INSERT INTO outbox_events (id, payload, status='PENDING')
[SQL Transaction: COMMIT]
```
A separate worker polls pending outbox records and reliably publishes them to Kafka.
