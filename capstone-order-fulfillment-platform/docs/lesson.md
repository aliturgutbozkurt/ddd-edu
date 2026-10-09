---
marp: true
theme: default
paginate: true
header: "DDD & Hexagonal Architecture Masterclass | Capstone Project"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Capstone Project: Enterprise Order & Fulfillment Platform

## End-to-End Enterprise DDD & Hexagonal Architecture in Action

---

## 1. System Architecture

```
[REST API: PlaceOrder] ──> [OrderApplicationService] ──> [Order Aggregate Root]
                                                              │ (Emits)
                                                              ▼
                                                   [Transactional Outbox]
                                                              │ (Publish)
                                                              ▼
                                                        [Kafka Bus]
                                                              │
                                                              ▼
                                                   [Fulfillment ACL]
                                                              │
                                                              ▼
                                                  [Shipment Aggregate Root]
```
