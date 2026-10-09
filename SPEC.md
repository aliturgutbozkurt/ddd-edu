# SPEC.md — Course Specification: Domain-Driven Design & Hexagonal Architecture in Java

**Curriculum Target**: September 2026  
**Technologies**: Java 27 (LTS), Spring Boot 4.0+, Maven Multi-Module, Testcontainers, ArchUnit, Docker Compose  
**Methodology**: Spec-Driven Development (SDD) via Addy Osmani's SDD Workflow  
**Deliverables**:
- 12 Comprehensive Modules with runnable codebases
- Student Exercises (`exercises/`) with failing unit tests & clear objectives
- Instructor Solutions (`solutions/`) with 100% test coverage & architectural commentary
- Dual-language documentation (`lesson.md` in English, `lesson.tr.md` in Turkish)
- Automated PDF generation pipeline for offline study
- End-to-End Enterprise Capstone Project (`capstone-order-fulfillment-platform`)

---

## 1. Pedagogical Goals & Vision

By the end of this course, students will transition from writing anemic, database-centric, framework-coupled Spring Boot applications to mastering **Domain-Driven Design (DDD)** and **Hexagonal Architecture (Ports and Adapters)** using cutting-edge Java 27 features.

### Core Learning Outcomes:
1. **Strategic DDD Mastery**: Discover subdomains, map Bounded Contexts, construct Ubiquitous Language glossaries, and lead Event Storming workshops.
2. **Tactical DDD Rigor**: Design rich domain models using Aggregates, Entities, immutable Value Objects (Java 27 records), and Domain Invariants.
3. **Hexagonal Architecture Purity**: Completely isolate business logic from Spring Boot, database drivers, Kafka, and HTTP protocols through explicit Inbound (Driving) and Outbound (Driven) Ports.
4. **Architectural Guardrails**: Implement automated ArchUnit tests that continuously enforce hexagonal isolation in CI/CD pipelines.
5. **Modern Java 27 Idioms**: Leverage sealed hierarchies for domain events, pattern matching for business workflows, virtual threads for high-throughput adapters, and compact record constructors for domain invariant enforcement.
6. **Production-Ready Capstone**: Build a multi-bounded-context E-Commerce Order & Fulfillment system featuring the Transactional Outbox pattern, domain event dispatching, and integration testing with Testcontainers.

---

## 2. Curriculum Architecture (12 Modules)

| Module | Code & Title | Key Domain Concepts | Hexagonal / Technical Focus |
|---|---|---|---|
| **01** | `module-01-ddd-foundations` | Strategic DDD, Subdomains, Bounded Contexts, Ubiquitous Language | Domain Isolation, Anemic vs Rich Models |
| **02** | `module-02-hexagonal-architecture` | Ports and Adapters, Inward Dependencies, Layer Separation | Hexagonal Blueprint, Dependency Inversion |
| **03** | `module-03-value-objects` | Immutability, Equality by Value, Self-Validation, Side-Effect-Free | Java 27 Records, Compact Constructors |
| **04** | `module-04-entities-and-identity` | Entity Identity, Equality by ID, Entity Lifecycle, Mutability control | Entity Base Classes, Identity Generators |
| **05** | `module-05-aggregates-and-invariants` | Aggregate Roots, Consistency Boundaries, Transactional Boundaries | Guard Clauses, Enforcing Business Invariants |
| **06** | `module-06-domain-events` | Domain Events, Event Generation within Aggregates, Decoupling | Java 27 Sealed Interfaces, Event Dispatcher SPI |
| **07** | `module-07-driving-ports-use-cases` | Inbound Ports, Application Services, Command/Query Separation | Use Case Interfaces, Command Objects, DTO Mapping |
| **08** | `module-08-driven-ports-persistence` | Outbound Ports, Repository SPI, Database Independence | Spring Data JDBC / JPA Adapters, Entity Mappers |
| **09** | `module-09-driving-adapters-rest` | Driving Adapters, HTTP/REST, Content Negotiation, Error Mapping | Spring Boot 4 REST, RFC 9457 Problem Details |
| **10** | `module-10-driven-adapters-messaging` | External Services, Event Streaming, Messaging Adapters | Kafka Adapters, Resilient HTTP Clients, Testcontainers |
| **11** | `module-11-architecture-testing-archunit` | Architectural Fitness Functions, Hexagonal Enforcement | ArchUnit Rules, Package Dependency Verification |
| **12** | `module-12-context-mapping-outbox` | Context Mapping (Shared Kernel, Anti-Corruption Layer), Outbox | Transactional Outbox Pattern, At-Least-Once Delivery |

---

## 3. Capstone Project: Order & Fulfillment Enterprise Platform

The capstone project (`capstone-order-fulfillment-platform`) ties all concepts together in a production-grade enterprise system with two distinct Bounded Contexts:

1. **Ordering Bounded Context**:
   - Aggregate Root: `Order`
   - Entities: `OrderItem`
   - Value Objects: `OrderId`, `CustomerId`, `Money`, `Quantity`, `ShippingAddress`, `OrderStatus`
   - Invariants: Cannot checkout empty order; Total must equal sum of line items; Cancel only in pending state; Max credit limits enforced.
   - Domain Events: `OrderCreatedEvent`, `OrderConfirmedEvent`, `OrderCancelledEvent`
   - Hexagonal Ports:
     - Driving: `PlaceOrderUseCase`, `CancelOrderUseCase`, `GetOrderQuery`
     - Driven: `OrderRepositoryPort`, `DomainEventPublisherPort`, `InventoryCheckPort`

2. **Fulfillment Bounded Context**:
   - Aggregate Root: `Shipment`
   - Value Objects: `ShipmentId`, `TrackingNumber`, `Carrier`, `ShipmentStatus`
   - Anti-Corruption Layer (ACL): Translates `OrderConfirmedEvent` to `PrepareShipmentCommand`
   - Driven Adapters: Database persistence (PostgreSQL), Carrier API Adapter (Mocked external integration), Kafka event subscriber.

3. **Cross-Cutting Enterprise Patterns**:
   - **Transactional Outbox Pattern**: Ensures atomicity between database state transitions and Kafka event publication.
   - **ArchUnit Hexagonal Suite**: Validates that neither bounded context bleeds into the other, and domain models stay 100% pure.
   - **Full Docker Compose Stack**: PostgreSQL, Kafka, and Mailpit for end-to-end student demonstration.

---

## 4. Educational Standards & File Deliverables

Every module repository contains:
1. `README.md` & `README.tr.md`: Clear module overview, learning roadmap, and terminal commands.
2. `docs/lesson.md` & `docs/lesson.tr.md`:
   - Detailed pedagogical lecture content (60+ minute reading/lecture time).
   - Formatted with Marp / markdown-pdf metadata for direct 1-click PDF compilation.
   - Rich ASCII / Mermaid architecture diagrams.
   - Pitfalls, Best Practices, and 2026 industry context.
3. `exercises/`:
   - `README.md` & `README.tr.md`: Student assignment instructions.
   - `src/`: Starter code with unit test scaffolds where tests fail (`fail("TODO: Implement invariant...")`).
4. `solutions/`:
   - `README.md` & `README.tr.md`: Step-by-step walkthrough of the optimal solution.
   - `src/`: Complete reference implementation with 100% green tests.
5. `src/`:
   - Runnable production-quality sample application for the module with integration and ArchUnit tests.

---

## 5. Acceptance Criteria

- [ ] All 12 modules and the capstone project compile with `./mvnw clean test`.
- [ ] No Spring or persistence annotations reside inside any `domain` package.
- [ ] Every module has bilingual documentation (EN and TR).
- [ ] PDF export scripts generate high-quality educational documents.
- [ ] Automated GitHub issues exist for tracking curriculum development.
