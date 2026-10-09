# TODO.md — Tasks & Progress Tracker

> **Course**: Domain-Driven Design & Hexagonal Architecture in Java (Sept 2026)  
> **Methodology**: Spec-Driven Development (SDD)  

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
- [ ] Create GitHub Issues for all modules, milestones, and capstone

---

## Phase 2: Core Foundations (Modules 01 - 04)

### Module 01: DDD Foundations & Ubiquitous Language
- [ ] `module-01-ddd-foundations/pom.xml`
- [ ] `module-01-ddd-foundations/README.md` (EN) & `README.tr.md` (TR)
- [ ] `module-01-ddd-foundations/docs/lesson.md` (EN) & `docs/lesson.tr.md` (TR)
- [ ] Runnable code demonstrating Anemic vs Rich Domain Model
- [ ] `exercises/`: Student exercise on Ubiquitous Language modeling
- [ ] `solutions/`: Instructor reference solution with unit tests

### Module 02: Hexagonal Architecture Blueprint & Ports/Adapters
- [ ] `module-02-hexagonal-architecture/pom.xml`
- [ ] `module-02-hexagonal-architecture/README.md` (EN) & `README.tr.md` (TR)
- [ ] `module-02-hexagonal-architecture/docs/lesson.md` (EN) & `docs/lesson.tr.md` (TR)
- [ ] Runnable code demonstrating Ports & Adapters project layout
- [ ] `exercises/`: Refactoring a 3-tier layered app to Hexagonal
- [ ] `solutions/`: Verified reference solution with clean dependency inversion

### Module 03: Value Objects & Immutability with Java 27 Records
- [ ] `module-03-value-objects/pom.xml`
- [ ] `module-03-value-objects/README.md` (EN) & `README.tr.md` (TR)
- [ ] `module-03-value-objects/docs/lesson.md` (EN) & `docs/lesson.tr.md` (TR)
- [ ] Runnable code for `Money`, `Currency`, `EmailAddress`, `PostalAddress`
- [ ] `exercises/`: Implementing custom Value Objects with compact constructors
- [ ] `solutions/`: Full reference implementation with unit tests

### Module 04: Entities, Identity & Lifecycle
- [ ] `module-04-entities-and-identity/pom.xml`
- [ ] `module-04-entities-and-identity/README.md` (EN) & `README.tr.md` (TR)
- [ ] `module-04-entities-and-identity/docs/lesson.md` (EN) & `docs/lesson.tr.md` (TR)
- [ ] Runnable code for `Customer` and `BankAccount` entities
- [ ] `exercises/`: Entity lifecycle protection and identity equality
- [ ] `solutions/`: Verified solution with comprehensive unit tests

---

## Phase 3: Tactical Domain Modeling & Port Design (Modules 05 - 08)

### Module 05: Aggregates, Aggregate Roots & Domain Invariants
- [ ] `module-05-aggregates-and-invariants/pom.xml`
- [ ] `module-05-aggregates-and-invariants/README.md` (EN) & `README.tr.md` (TR)
- [ ] `module-05-aggregates-and-invariants/docs/lesson.md` (EN) & `docs/lesson.tr.md` (TR)
- [ ] Runnable code for `Order` aggregate root with `OrderItem` children
- [ ] `exercises/`: Guard clauses and multi-entity invariant enforcement
- [ ] `solutions/`: Complete reference solution

### Module 06: Domain Events & Event-Driven Decoupling
- [ ] `module-06-domain-events/pom.xml`
- [ ] `module-06-domain-events/README.md` (EN) & `README.tr.md` (TR)
- [ ] `module-06-domain-events/docs/lesson.md` (EN) & `docs/lesson.tr.md` (TR)
- [ ] Runnable code using Java 27 sealed domain event hierarchies
- [ ] `exercises/`: Event capture within Aggregates and dispatch
- [ ] `solutions/`: Reference solution with mock dispatch tests

### Module 07: Inbound (Driving) Ports & Application Services
- [ ] `module-07-driving-ports-use-cases/pom.xml`
- [ ] `module-07-driving-ports-use-cases/README.md` (EN) & `README.tr.md` (TR)
- [ ] `module-07-driving-ports-use-cases/docs/lesson.md` (EN) & `docs/lesson.tr.md` (TR)
- [ ] Runnable code for `PlaceOrderUseCase` and `CancelOrderUseCase`
- [ ] `exercises/`: Implementing Command Handlers and DTO mappings
- [ ] `solutions/`: Verified solution with clean separation of concerns

### Module 08: Outbound (Driven) Ports & Persistence Adapters
- [ ] `module-08-driven-ports-persistence/pom.xml`
- [ ] `module-08-driven-ports-persistence/README.md` (EN) & `README.tr.md` (TR)
- [ ] `module-08-driven-ports-persistence/docs/lesson.md` (EN) & `docs/lesson.tr.md` (TR)
- [ ] Runnable code for Spring Data JDBC / JPA persistence adapter
- [ ] `exercises/`: Mapping relational tables to pure domain aggregates
- [ ] `solutions/`: Reference persistence adapter with Testcontainers

---

## Phase 4: Production Adapters & Governance (Modules 09 - 12)

### Module 09: Driving Adapters with Spring Boot 4
- [ ] `module-09-driving-adapters-rest/pom.xml`
- [ ] `module-09-driving-adapters-rest/README.md` (EN) & `README.tr.md` (TR)
- [ ] `module-09-driving-adapters-rest/docs/lesson.md` (EN) & `docs/lesson.tr.md` (TR)
- [ ] Runnable code for REST Controller with RFC 9457 Problem Details
- [ ] `exercises/`: Building driving REST adapters with virtual threads
- [ ] `solutions/`: Reference REST adapter with MockMvc tests

### Module 10: Driven Adapters for External Services & Messaging
- [ ] `module-10-driven-adapters-messaging/pom.xml`
- [ ] `module-10-driven-adapters-messaging/README.md` (EN) & `README.tr.md` (TR)
- [ ] `module-10-driven-adapters-messaging/docs/lesson.md` (EN) & `docs/lesson.tr.md` (TR)
- [ ] Runnable code for Kafka event publisher adapter and HTTP client
- [ ] `exercises/`: Resilient adapter with retry and fallback
- [ ] `solutions/`: Reference Kafka adapter with Testcontainers

### Module 11: Automated Architectural Governance with ArchUnit
- [ ] `module-11-architecture-testing-archunit/pom.xml`
- [ ] `module-11-architecture-testing-archunit/README.md` (EN) & `README.tr.md` (TR)
- [ ] `module-11-architecture-testing-archunit/docs/lesson.md` (EN) & `docs/lesson.tr.md` (TR)
- [ ] Runnable code with complete ArchUnit rule suite for Hexagonal Architecture
- [ ] `exercises/`: Writing custom ArchUnit rules for port and adapter constraints
- [ ] `solutions/`: Fully passing architectural test suite

### Module 12: Context Mapping & Outbox Pattern
- [ ] `module-12-context-mapping-outbox/pom.xml`
- [ ] `module-12-context-mapping-outbox/README.md` (EN) & `README.tr.md` (TR)
- [ ] `module-12-context-mapping-outbox/docs/lesson.md` (EN) & `docs/lesson.tr.md` (TR)
- [ ] Runnable code for Transactional Outbox pattern with Kafka
- [ ] `exercises/`: Implementing Outbox publisher and Anti-Corruption Layer
- [ ] `solutions/`: Reference implementation with at-least-once delivery

---

## Phase 5: Capstone Project & Educational Polishing
- [ ] `capstone-order-fulfillment-platform/pom.xml`
- [ ] `capstone-order-fulfillment-platform/README.md` (EN) & `README.tr.md` (TR)
- [ ] Ordering Bounded Context implementation (Hexagonal Architecture)
- [ ] Fulfillment Bounded Context implementation (Hexagonal Architecture)
- [ ] Transactional Outbox & Kafka event dispatching
- [ ] End-to-end integration tests with Testcontainers
- [ ] ArchUnit boundary tests for multi-bounded contexts
- [ ] Exercises & Solutions for Capstone
- [ ] PDF compilation of all modules (`./scripts/generate-pdfs.sh`)
