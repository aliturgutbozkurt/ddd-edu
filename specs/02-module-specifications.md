# Functional & Domain Specifications: Modules 01 to 12

This specification defines the functional domain scenarios, ubiquitous languages, and acceptance criteria for all 12 modules in the curriculum.

---

## Module 01: DDD Foundations & Ubiquitous Language
- **Domain Context**: FinTech Personal Banking Subdomain
- **Ubiquitous Language**:
  - `BankAccount`: An account held by a customer at a financial institution.
  - `AccountNumber`: An 11-digit formatted identifier with checksum verification.
  - `TransactionType`: Deposit, Withdrawal, Transfer.
  - `OverdraftLimit`: The authorized negative balance permitted for a premium account.
- **Acceptance Scenarios**:
  - *Given* an account with balance $100 and overdraft limit $50, *when* a withdrawal of $120 is requested, *then* the account balance becomes -$20.
  - *Given* an account with balance $100 and overdraft limit $50, *when* a withdrawal of $160 is requested, *then* a `InsufficientFundsException` is thrown and balance remains $100.

---

## Module 02: Hexagonal Architecture Blueprint & Ports/Adapters
- **Domain Context**: E-Commerce Product Catalog
- **Hexagonal Boundary**:
  - Driving Port: `RegisterProductUseCase`, `FindProductQuery`
  - Driven Port: `ProductRepositoryPort`
  - Driving Adapter: `ProductRestController`
  - Driven Adapter: `InMemoryProductRepositoryAdapter` (and later PostgreSQL)
- **Acceptance Scenarios**:
  - Domain package has zero imports outside of standard `java.*`.
  - Application Service coordinates product registration through `ProductRepositoryPort`.

---

## Module 03: Value Objects & Immutability with Java 27 Records
- **Domain Context**: International Currency & Customer Profile
- **Value Objects**:
  - `Money(BigDecimal amount, Currency currency)`: Invariant: amount cannot be null, scale is 2, addition/subtraction only between identical currencies.
  - `EmailAddress(String value)`: Invariant: RFC 5322 regex validation, normalized to lowercase.
  - `PostalCode(String code, Country country)`: Invariant: Valid format based on country code.
- **Acceptance Scenarios**:
  - Adding `Money(10.00, USD)` to `Money(5.00, USD)` returns a new instance `Money(15.00, USD)`.
  - Adding `Money(10.00, USD)` to `Money(5.00, EUR)` throws `CurrencyMismatchException`.
  - Constructing `EmailAddress("invalid-email")` throws `InvalidEmailException`.

---

## Module 04: Entities, Identity & Lifecycle
- **Domain Context**: Customer Identity & Membership Management
- **Entity**: `Customer` with `CustomerId(UUID value)`
- **Key Concepts**:
  - Two customers with different names but identical `CustomerId` are equal (`equals()` and `hashCode()` based purely on `CustomerId`).
  - Controlled lifecycle mutations via business methods (`updateContactDetails`, `upgradeMembershipTier`).
- **Acceptance Scenarios**:
  - `customerA.equals(customerB)` evaluates to `true` when their IDs match, even if addresses differ.

---

## Module 05: Aggregates, Aggregate Roots & Domain Invariants
- **Domain Context**: Order Management & Line Item Rules
- **Aggregate Root**: `Order`
- **Internal Entity**: `OrderItem` (accessible ONLY through `Order`)
- **Value Objects**: `OrderId`, `ProductId`, `Quantity`, `Money`
- **Invariants**:
  - Total line items cannot exceed 50 items.
  - Total order value must match sum of line items.
  - Cannot add items once order state is `CONFIRMED` or `SHIPPED`.
- **Acceptance Scenarios**:
  - Attempting to add an item to an order in `CONFIRMED` state throws `InvalidOrderStateException`.
  - Attempting to modify `OrderItem` directly from outside the aggregate is impossible due to defensive copying.

---

## Module 06: Domain Events & Event-Driven Decoupling
- **Domain Context**: Order Fulfillment Lifecycle Events
- **Sealed Domain Events**:
  ```java
  public sealed interface OrderDomainEvent permits OrderPlacedEvent, OrderPaidEvent, OrderCancelledEvent {
      OrderId orderId();
      Instant occurredOn();
  }
  ```
- **Acceptance Scenarios**:
  - When `order.place()` is called, an `OrderPlacedEvent` is recorded in the order's internal event queue.
  - Calling `order.clearDomainEvents()` empties the queue after dispatch.

---

## Module 07: Inbound (Driving) Ports & Application Services
- **Domain Context**: Use Case Orchestration & Command Handlers
- **Driving Ports**:
  - `PlaceOrderUseCase.execute(PlaceOrderCommand command)`
  - `CancelOrderUseCase.execute(CancelOrderCommand command)`
- **Application Services**:
  - Loads Aggregate via `OrderRepositoryPort`, invokes domain business method, saves aggregate, dispatches events via `DomainEventPublisherPort`.
- **Acceptance Scenarios**:
  - Application service orchestrates use case without exposing internal domain state to the caller.

---

## Module 08: Outbound (Driven) Ports & Persistence Adapters
- **Domain Context**: Spring Data JDBC / JPA Persistence Mapping
- **Driven Port**: `OrderRepositoryPort` (Interface returning `Optional<Order>`)
- **Driven Adapter**:
  - `OrderJpaEntity` and `OrderItemJpaEntity` (with JPA `@Table`, `@Id`, `@Column`).
  - `OrderPersistenceAdapter` implements `OrderRepositoryPort`.
  - `OrderMapper` cleanly maps between `Order` (Domain Aggregate) and `OrderJpaEntity`.
- **Acceptance Scenarios**:
  - Saving an order successfully persists relations in relational database tables.
  - Retrieving an order returns a fully reconstituted pure Java Aggregate Root.

---

## Module 09: Driving Adapters with Spring Boot 4
- **Domain Context**: Modern RESTful API & Error Handling
- **Driving Adapter**: `OrderRestController`
- **Features**:
  - Spring Boot 4 virtual threads enabled.
  - Request DTOs mapped to Application Commands (`PlaceOrderRequest` ➔ `PlaceOrderCommand`).
  - Response mapped to DTO.
  - `@RestControllerAdvice` translates domain exceptions (`OrderNotFoundException`, `DomainValidationException`) to standard RFC 9457 Problem Details (`application/problem+json`).

---

## Module 10: Driven Adapters for External Services & Messaging
- **Domain Context**: Kafka Event Publishing & Payment Gateway Integration
- **Driven Ports**: `DomainEventPublisherPort`, `PaymentGatewayPort`
- **Driven Adapters**:
  - `KafkaOrderEventPublisherAdapter` using Spring Kafka.
  - `StripePaymentGatewayAdapter` using modern Spring `RestClient` with resilience retries.
- **Acceptance Scenarios**:
  - Emitting an `OrderPaidEvent` delivers a JSON message to topic `orders.events` in Kafka.
  - Verified with Testcontainers in automated integration test.

---

## Module 11: Automated Architectural Governance with ArchUnit
- **Domain Context**: Architectural Enforcement Test Suite
- **Rules Verified**:
  - 100% domain isolation.
  - Proper port and adapter naming conventions (`*UseCase`, `*Port`, `*Adapter`).
  - Prohibiting circular dependencies between bounded packages.

---

## Module 12: Context Mapping & Outbox Pattern for Distributed Systems
- **Domain Context**: Order to Shipping Context Integration via Outbox
- **Components**:
  - `OutboxTable`: stores serialized domain events in the same SQL transaction as aggregate state.
  - `OutboxEventPublisher`: scheduled background worker or CDC publisher that pushes unhandled events to Kafka with at-least-once guarantee.
  - `AntiCorruptionLayer`: Shipping Context translates external order event into internal shipping domain model.
