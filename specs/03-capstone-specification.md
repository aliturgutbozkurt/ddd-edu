# Capstone Specification: Enterprise Order & Fulfillment Platform

## 1. System Vision & Architecture

The Capstone Project demonstrates an end-to-end enterprise solution composed of two distinct Bounded Contexts interacting via Domain Events and an Anti-Corruption Layer (ACL), backed by the Transactional Outbox pattern.

```
┌────────────────────────────────────────────────────────────────────────┐
│                        ORDERING BOUNDED CONTEXT                        │
│                                                                        │
│  [Driving Adapter: REST]                                               │
│            │                                                           │
│            ▼                                                           │
│  [Inbound Port: PlaceOrderUseCase]                                     │
│            │                                                           │
│            ▼                                                           │
│  [Application Service: OrderApplicationService]                        │
│            │                                                           │
│            ▼                                                           │
│  [Aggregate Root: Order] ──(Emits)──> [DomainEvent: OrderConfirmed]   │
│            │                                      │                    │
│            ▼                                      ▼                    │
│  [Driven: PostgreSQL (JPA)]            [Driven: Transactional Outbox]  │
└───────────────────────────────────────────────────┼────────────────────┘
                                                    │
                                           (Kafka / Event Bus)
                                                    │
┌───────────────────────────────────────────────────┼────────────────────┐
│                       FULFILLMENT BOUNDED CONTEXT │                    │
│                                                   ▼                    │
│  [Driving Adapter: Kafka Consumer] ──> [Anti-Corruption Layer (ACL)]   │
│                                                   │                    │
│                                                   ▼                    │
│                             [Inbound Port: CreateShipmentUseCase]      │
│                                                   │                    │
│                                                   ▼                    │
│                                    [Aggregate Root: Shipment]          │
│                                                   │                    │
│                                                   ▼                    │
│                                      [Driven: ShipmentRepository]      │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Bounded Context Specifications

### A. Ordering Bounded Context
- **Aggregate Root**: `Order`
- **Internal Entities**: `OrderItem`
- **Value Objects**:
  - `OrderId(UUID value)`
  - `CustomerId(UUID value)`
  - `Money(BigDecimal amount, Currency currency)`
  - `Address(String street, String city, String state, String zip, String country)`
  - `OrderStatus(PENDING, CONFIRMED, PAID, CANCELLED, FULFILLED)`
- **Invariants**:
  1. An order must have at least one line item before confirmation.
  2. The total amount must equal the sum of line items plus applicable shipping costs.
  3. An order can only be cancelled if it has not yet reached `SHIPPED` status.
  4. Adding line items to an existing confirmed order is strictly rejected.
- **Hexagonal Ports**:
  - Driving: `PlaceOrderUseCase`, `ConfirmOrderUseCase`, `CancelOrderUseCase`, `GetOrderSummaryQuery`
  - Driven: `OrderRepositoryPort`, `OutboxRepositoryPort`, `CustomerCreditCheckPort`

### B. Fulfillment Bounded Context
- **Aggregate Root**: `Shipment`
- **Value Objects**:
  - `ShipmentId(UUID value)`
  - `OrderId(UUID value)` (Reference by identity only)
  - `TrackingCode(String code)`
  - `Carrier(FEDEX, DHL, UPS, YURTICI)`
  - `ShipmentStatus(CREATED, PICKED, PACKED, DISPATCHED, DELIVERED)`
- **Invariants**:
  1. A shipment cannot be dispatched without a valid tracking code assigned.
  2. State transitions must follow: `CREATED` ➔ `PICKED` ➔ `PACKED` ➔ `DISPATCHED` ➔ `DELIVERED`.
- **Anti-Corruption Layer (ACL)**:
  - `OrderConfirmedEventTranslator`: Converts external `OrderConfirmedEvent` payload into a pure internal `CreateShipmentCommand`.

---

## 3. Transactional Outbox Pattern Specification

1. When `OrderApplicationService` confirms an order, both the `Order` aggregate state and the `OutboxRecord` are committed in the same database transaction.
2. A background `OutboxEventPublisher` polls pending outbox records and publishes them to the Kafka broker.
3. Upon successful acknowledgement from Kafka, the outbox record is marked as `SENT`.

---

## 4. Verification & Testing Requirements

- **Domain Unit Tests**: 100% test coverage on `Order` and `Shipment` invariant checks without any Spring context.
- **ArchUnit Tests**: Verification that neither context imports domain or adapter classes from the other context.
- **Integration Tests**: End-to-end integration test with Testcontainers (PostgreSQL + Kafka) testing the flow from REST endpoint call through Outbox dispatch to Kafka topic consumption.
