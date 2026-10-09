# TODO.md — Tasks & Progress Tracker

> **Course**: Domain-Driven Design & Hexagonal Architecture in Java (Sept 2026)  
> **Methodology**: Spec-Driven Development (SDD)  
> **Status**: Completed (100% Green across all 15 reactor modules)  

---

## Phase 1: Project Setup & SDD Infrastructure
- [x] Create `CLAUDE.md` with best practices, SDD workflow, and Hexagonal rules
- [x] Create `AGENTS.md` for AI pair programming context
- [x] Create `SPEC.md` root course specification
- [x] Create `specs/00-curriculum-overview.md`
- [x] Create `specs/01-architectural-rules.md`
- [x] Create `specs/02-module-specifications.md`
- [x] Create `specs/03-capstone-specification.md`
- [x] Create `plan.md` delivery roadmap
- [x] Create `todo.md` granular task tracker
- [x] Configure root `pom.xml` (Java 27, Spring Boot 4.0, ArchUnit, Testcontainers)
- [x] Setup `.gitignore`, `.gitattributes`, `.editorconfig`
- [x] Add Maven Wrapper (`mvnw`, `mvnw.cmd`, `.mvn`)
- [x] Create `docker-compose.yml` (PostgreSQL, Kafka, Mailpit)
- [x] Create `scripts/generate-pdfs.sh` for Markdown to PDF conversion
- [x] Initialize public GitHub repo `aliturgutbozkurt/ddd-edu`
- [x] Create GitHub Issues for all modules, milestones, and capstone (#1 to #15)

---

## Phase 2: Core Foundations (Modules 01 - 04)

### Module 01: DDD Foundations & Ubiquitous Language
- [x] `module-01-ddd-foundations/pom.xml`
- [x] `module-01-ddd-foundations/README.md` (EN) & `README.tr.md` (TR)
- [x] `module-01-ddd-foundations/docs/lesson.md` (EN) & `docs/lesson.tr.md` (TR)
- [x] Runnable code demonstrating Anemic vs Rich Domain Model (`BankAccount` vs `AnemicBankAccount`)
- [x] `exercises/`: Student exercise on Ubiquitous Language modeling (`DailyLimitExerciseTest`)
- [x] `solutions/`: Instructor reference solution with unit tests (`AccountWithDailyLimit`)
- [x] ArchUnit layer isolation tests

### Module 02: Hexagonal Architecture Blueprint & Ports/Adapters
- [x] `module-02-hexagonal-architecture/pom.xml`
- [x] `module-02-hexagonal-architecture/README.md` (EN) & `README.tr.md` (TR)
- [x] `module-02-hexagonal-architecture/docs/lesson.md` (EN) & `docs/lesson.tr.md` (TR)
- [x] Runnable code demonstrating Ports & Adapters project layout (`Product`, `RegisterProductUseCase`, `ProductRepositoryPort`)
- [x] `exercises/`: Refactoring a 3-tier layered app to Hexagonal
- [x] `solutions/`: Verified reference solution with clean dependency inversion
- [x] ArchUnit layer isolation tests

### Module 03: Value Objects & Immutability with Java 27 Records
- [x] `module-03-value-objects/pom.xml`
- [x] `module-03-value-objects/README.md` (EN) & `README.tr.md` (TR)
- [x] `module-03-value-objects/docs/lesson.md` (EN) & `docs/lesson.tr.md` (TR)
- [x] Runnable code for `EmailAddress`, `Iban`, compact constructor invariants
- [x] `exercises/`: Implementing custom Value Objects with compact constructors
- [x] `solutions/`: Full reference implementation with unit tests
- [x] ArchUnit tests

### Module 04: Entities, Identity & Lifecycle
- [x] `module-04-entities-and-identity/pom.xml`
- [x] `module-04-entities-and-identity/README.md` (EN) & `README.tr.md` (TR)
- [x] `module-04-entities-and-identity/docs/lesson.md` (EN) & `docs/lesson.tr.md` (TR)
- [x] Runnable code for `Customer`, `CustomerId`, `CustomerTier`
- [x] `exercises/`: Entity lifecycle protection and identity equality
- [x] `solutions/`: Verified solution with comprehensive unit tests
- [x] ArchUnit tests

---

## Phase 3: Tactical Domain Modeling & Port Design (Modules 05 - 08)

### Module 05: Aggregates, Aggregate Roots & Domain Invariants
- [x] `module-05-aggregates-and-invariants/pom.xml`
- [x] `module-05-aggregates-and-invariants/README.md` (EN) & `README.tr.md` (TR)
- [x] `module-05-aggregates-and-invariants/docs/lesson.md` (EN) & `docs/lesson.tr.md` (TR)
- [x] Runnable code for `Order` aggregate root with `OrderItem` children
- [x] `exercises/`: Guard clauses and multi-entity invariant enforcement
- [x] `solutions/`: Complete reference solution
- [x] ArchUnit tests

### Module 06: Domain Events & Event-Driven Decoupling
- [x] `module-06-domain-events/pom.xml`
- [x] `module-06-domain-events/README.md` (EN) & `README.tr.md` (TR)
- [x] `module-06-domain-events/docs/lesson.md` (EN) & `docs/lesson.tr.md` (TR)
- [x] Runnable code using Java 27 sealed domain event hierarchies (`OrderEvent`)
- [x] `exercises/`: Event capture within Aggregates and dispatch
- [x] `solutions/`: Reference solution with mock dispatch tests
- [x] ArchUnit tests

### Module 07: Inbound (Driving) Ports & Application Services
- [x] `module-07-driving-ports-use-cases/pom.xml`
- [x] `module-07-driving-ports-use-cases/README.md` (EN) & `README.tr.md` (TR)
- [x] `module-07-driving-ports-use-cases/docs/lesson.md` (EN) & `docs/lesson.tr.md` (TR)
- [x] Runnable code for `CreateAccountUseCase`, `AccountRepositoryPort`, and `AccountApplicationService`
- [x] `exercises/`: Implementing Command Handlers and DTO mappings
- [x] `solutions/`: Verified solution with clean separation of concerns
- [x] ArchUnit tests

### Module 08: Outbound (Driven) Ports & Persistence Adapters
- [x] `module-08-driven-ports-persistence/pom.xml`
- [x] `module-08-driven-ports-persistence/README.md` (EN) & `README.tr.md` (TR)
- [x] `module-08-driven-ports-persistence/docs/lesson.md` (EN) & `docs/lesson.tr.md` (TR)
- [x] Runnable code for `CustomerPersistenceAdapter` and pure domain `Customer` reconstitution
- [x] `exercises/`: Mapping relational tables to pure domain aggregates
- [x] `solutions/`: Reference persistence adapter
- [x] ArchUnit tests

---

## Phase 4: Production Adapters & Governance (Modules 09 - 12)

### Module 09: Driving Adapters with Spring Boot 4
- [x] `module-09-driving-adapters-rest/pom.xml`
- [x] `module-09-driving-adapters-rest/README.md` (EN) & `README.tr.md` (TR)
- [x] `module-09-driving-adapters-rest/docs/lesson.md` (EN) & `docs/lesson.tr.md` (TR)
- [x] Runnable code for REST Controller with `TransferMoneyUseCase`
- [x] `exercises/`: Building driving REST adapters with virtual threads
- [x] `solutions/`: Reference REST adapter with unit tests
- [x] ArchUnit tests

### Module 10: Driven Adapters for External Services & Messaging
- [x] `module-10-driven-adapters-messaging/pom.xml`
- [x] `module-10-driven-adapters-messaging/README.md` (EN) & `README.tr.md` (TR)
- [x] `module-10-driven-adapters-messaging/docs/lesson.md` (EN) & `docs/lesson.tr.md` (TR)
- [x] Runnable code for `NotificationSenderPort` and `SimulatedMessagePublisherAdapter`
- [x] `exercises/`: Resilient adapter with retry and fallback
- [x] `solutions/`: Reference message publisher adapter
- [x] ArchUnit tests

### Module 11: Automated Architectural Governance with ArchUnit
- [x] `module-11-architecture-testing-archunit/pom.xml`
- [x] `module-11-architecture-testing-archunit/README.md` (EN) & `README.tr.md` (TR)
- [x] `module-11-architecture-testing-archunit/docs/lesson.md` (EN) & `docs/lesson.tr.md` (TR)
- [x] Runnable code with complete ArchUnit rule suite for Hexagonal Architecture and Value Objects
- [x] `exercises/`: Writing custom ArchUnit rules for port and adapter constraints
- [x] `solutions/`: Fully passing architectural test suite
- [x] ArchUnit tests

### Module 12: Context Mapping & Outbox Pattern
- [x] `module-12-context-mapping-outbox/pom.xml`
- [x] `module-12-context-mapping-outbox/README.md` (EN) & `README.tr.md` (TR)
- [x] `module-12-context-mapping-outbox/docs/lesson.md` (EN) & `docs/lesson.tr.md` (TR)
- [x] Runnable code for `OutboxRecord` and immutable lifecycle state transitions
- [x] `exercises/`: Implementing Outbox publisher and Anti-Corruption Layer
- [x] `solutions/`: Reference implementation with at-least-once delivery
- [x] ArchUnit tests

---

## Phase 5: Capstone Project & Educational Polishing
- [x] `capstone-order-fulfillment-platform/pom.xml`
- [x] `capstone-order-fulfillment-platform/README.md` (EN) & `README.tr.md` (TR)
- [x] `capstone-order-fulfillment-platform/docs/lesson.md` (EN) & `docs/lesson.tr.md` (TR)
- [x] Ordering Bounded Context implementation (`Order`, `OrderId`, status lifecycle)
- [x] Fulfillment Bounded Context implementation (`Shipment`, `ShipmentId`, dispatching)
- [x] ArchUnit multi-context isolation test suite (`CapstoneArchitectureTest`)
- [x] Exercises & Solutions for Capstone
- [x] Full build verification (`./mvnw test`) passing across all 15 modules
