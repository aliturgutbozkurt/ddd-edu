# CLAUDE.md — Domain-Driven Design & Hexagonal Architecture Masterclass (Java 27 & Spring Boot 4)

> **Course**: Domain-Driven Design (DDD) & Hexagonal Architecture (Ports and Adapters) in Java  
> **Target Baseline**: September 2026 Curriculum  
> **Tech Stack**: Java 27 (LTS), Spring Boot 4.0+, Maven Multi-Module, ArchUnit, Testcontainers, Docker Compose  
> **Development Methodology**: Spec-Driven Development (SDD) — Addy Osmani SDD Pattern  
> **Language Policy**: Bilingual — English (EN) & Turkish (TR) Documentation, English code & domain Ubiquitous Language  

---

## 1. Spec-Driven Development (SDD) Workflow

This project adheres strictly to **Spec-Driven Development (SDD)**. Every module, architectural pattern, and exercise follows an iterative contract-first cycle:

```
┌─────────────┐     ┌──────────────┐     ┌──────────────┐     ┌────────────────┐     ┌─────────────┐
│ 1. SPEC     │ ──> │ 2. PLAN      │ ──> │ 3. TASKS     │ ──> │ 4. IMPLEMENT   │ ──> │ 5. VERIFY   │
│ Ubiquitous  │     │ Architectural│     │ Granular     │     │ Pure Domain    │     │ ArchUnit &  │
│ Language &  │     │ Blueprint &  │     │ Checklist &  │     │ First, then    │     │ Unit/Integ  │
│ Invariants  │     │ Module Ports │     │ Verification │     │ Ports/Adapters │     │ Tests       │
└─────────────┘     └──────────────┘     └──────────────┘     └────────────────┘     └─────────────┘
```

### SDD Phase Rules:
1. **Spec First (`SPEC.md` / `specs/*.md`)**:
   - Never write production code before defining the specification.
   - Define the **Ubiquitous Language** dictionary for the Bounded Context.
   - Specify **Invariants**, **Entities**, **Value Objects**, **Aggregates**, **Domain Events**, and **Port Contracts**.
   - Include Given-When-Then acceptance criteria for all domain operations.
2. **Plan (`plan.md`)**:
   - Map out dependencies between Hexagonal layers (Domain -> Application -> Ports -> Adapters).
   - Outline student milestones, homework scopes, and PDF lesson requirements.
3. **Tasks (`todo.md` / GitHub Issues)**:
   - Break implementation into atomic, testable increments.
   - Track progress transparently across both EN and TR deliverables.
4. **Implement**:
   - **Step 1**: Write pure domain models (Zero framework dependencies).
   - **Step 2**: Define Inbound (Driving) and Outbound (Driven) Port interfaces.
   - **Step 3**: Write Application Services (Use Cases) orchestrating domain logic.
   - **Step 4**: Implement Driven Adapters (Persistence, Messaging, External APIs).
   - **Step 5**: Implement Driving Adapters (REST API, Event Consumers, CLI).
5. **Verify**:
   - Domain Unit Tests (0ms external dependencies, 100% deterministic).
   - ArchUnit tests confirming zero framework leakage into Domain.
   - Slice / Integration Tests using Testcontainers (PostgreSQL, Kafka).

---

## 2. Architectural Invariants & Hexagonal Rules

Every module strictly implements **Alistair Cockburn's Hexagonal Architecture (Ports and Adapters)**:

```
                   ┌──────────────────────────────────────────────┐
                   │               INFRASTRUCTURE                 │
                   │  ┌────────────────────────────────────────┐  │
                   │  │              APPLICATION               │  │
 [Driving Adapter] │  │  ┌──────────────────────────────────┐  │  │ [Driven Adapter]
 REST Controller ─┼──┼─>│ Driving Port (Use Case)         │  │  ├─┼─> PostgreSQL / JPA
 gRPC Service    ─┼──┼─>│                                   │  │  ├─┼─> Kafka Publisher
 Event Listener  ─┼──┼─>│       Application Service         │  │  ├─┼─> Mail / Payment SPI
                   │  │  │                │                 │  │  │
                   │  │  │                ▼                 │  │  │
                   │  │  │  ┌────────────────────────────┐  │  │  │
                   │  │  │  │       DOMAIN CORE          │  │  │  │
                   │  │  │  │  - Entities & Aggregates   │  │  │  │
                   │  │  │  │  - Value Objects (Records) │  │  │  │
                   │  │  │  │  - Domain Invariants       │  │  │  │
                   │  │  │  │  - Domain Events           │  │  │  │
                   │  │  │  │  - Domain Services         │  │  │  │
                   │  │  │  └────────────────────────────┘  │  │  │
                   │  │  │                │                 │  │  │
                   │  │  │                ▼                 │  │  │
                   │  │  │  Driven Port (Repository SPI)    │  │  │
                   │  │  └──────────────────────────────────┘  │  │
                   │  └────────────────────────────────────────┘  │
                   └──────────────────────────────────────────────┘
```

### Non-Negotiable Architectural Rules:
- **Rule 1 (Domain Purity)**:
  `domain` package must contain **ZERO framework annotations** (`@Entity`, `@Table`, `@Autowired`, `@Component`, `@JsonSerialize`, etc. are strictly forbidden in domain).
  Only standard Java SE 27 APIs are allowed in `domain`.
- **Rule 2 (Direction of Dependencies)**:
  Dependencies always point inward:
  `Infrastructure (Adapters)` ➔ `Application (Use Cases)` ➔ `Domain (Core)`.
  Domain never imports from Application or Infrastructure.
- **Rule 3 (Ports are Interfaces)**:
  - **Driving (Inbound) Ports**: Use Case interfaces defined in Application or Domain (e.g., `PlaceOrderUseCase`, `CancelOrderUseCase`).
  - **Driven (Outbound) Ports**: SPI interfaces defining required secondary capabilities (e.g., `OrderRepository`, `EventPublisherPort`, `PaymentGatewayPort`).
- **Rule 4 (Persistence Decoupling)**:
  Database entities (e.g., Spring Data JPA `@Entity` or Spring Data JDBC records) belong exclusively to `infrastructure/adapters/output/persistence/`. They MUST be mapped to/from pure domain Aggregates using dedicated Mappers (`OrderEntityMapper`).
- **Rule 5 (Automated Guardrails with ArchUnit)**:
  Every module MUST have an `ArchitectureTest.java` that enforces Hexagonal layer isolation at compile/test time.

---

## 3. Java 27 & Spring Boot 4 Modern Idioms

Leverage modern language and framework capabilities across all code examples:

| Feature | DDD / Hexagonal Usage |
|---|---|
| **Java 27 Records** | Value Objects (e.g., `Money`, `EmailAddress`, `Address`) with compact constructors for invariant validation. |
| **Sealed Interfaces & Classes** | Domain Events (`sealed interface OrderEvent permits OrderCreated, OrderPaid...`) and Result/Either types. |
| **Pattern Matching with Switch** | Exhaustive handling of domain events, business commands, and domain exceptions. |
| **Virtual Threads (Project Loom)** | Enabled by default in Spring Boot 4 (`spring.threads.virtual.enabled=true`). Non-blocking I/O across outbound adapters. |
| **Stream Gatherers (JEP 485)** | Complex domain event aggregation, windowed calculations in Domain Services. |
| **Flexible Constructor Bodies (JEP 482)** | Pre-super invariant validation in Domain Entities before calling superclass constructors. |
| **Scoped Values (JEP 481)** | Secure, immutable propagation of TenantId / UserId / CorrelationId across hexagonal boundaries. |
| **Spring Boot 4 Baseline** | Spring Framework 7, Jakarta EE 11, RFC 9457 Problem Details for all driving REST adapters. |

---

## 4. Module Directory Structure Standard

Each module within `modules/` must follow this standardized layout:

```
modules/module-XX-<topic-name>/
├── README.md                      # English module overview, prerequisites & quickstart
├── README.tr.md                   # Türkçe modül özeti, önkoşullar ve hızlı başlangıç
├── pom.xml                        # Module Maven POM (inherits from root pom.xml)
├── docs/
│   ├── lesson.md                  # Comprehensive English lesson content (Marp/PDF ready)
│   ├── lesson.tr.md               # Kapsamlı Türkçe ders içeriği (Marp/PDF uyumlu)
│   └── diagrams/                  # Mermaid / PlantUML architecture & sequence diagrams
├── exercises/
│   ├── README.md                  # Homework problem statement & acceptance criteria (EN)
│   ├── README.tr.md               # Ödev soru açıklaması ve kabul kriterleri (TR)
│   └── src/                       # Starter project with failing unit tests / TODOs
├── solutions/
│   ├── README.md                  # Detailed solution walkthrough & architectural notes (EN)
│   ├── README.tr.md               # Detaylı çözüm rehberi ve mimari notlar (TR)
│   └── src/                       # Complete, production-grade reference implementation
└── src/
    ├── main/java/com/turkninja/ddd/
    │   ├── domain/                # PURE JAVA: Aggregates, Entities, Value Objects, Events
    │   │   ├── model/
    │   │   ├── event/
    │   │   └── exception/
    │   ├── application/           # USE CASES: Driving Ports & Application Services
    │   │   ├── port/
    │   │   │   ├── in/            # Driving (Inbound) Ports / Use Cases
    │   │   │   └── out/           # Driven (Outbound) Ports / SPIs
    │   │   └── service/           # Application Service Implementations
    │   └── infrastructure/        # ADAPTERS & CONFIGURATION
    │       ├── adapter/
    │       │   ├── input/         # Driving Adapters: REST, CLI, Event Listeners
    │       │   │   └── rest/
    │       │   └── output/        # Driven Adapters: JPA/JDBC, Kafka, External HTTP
    │       │       ├── persistence/
    │       │       └── messaging/
    │       └── config/            # Spring @Configuration, Bean Wiring
    └── test/java/com/turkninja/ddd/
        ├── architecture/          # ArchUnit Hexagonal Architecture verification tests
        ├── domain/                # Pure Java domain unit tests
        ├── application/           # Use case tests with mocked driven ports
        └── infrastructure/        # Integration tests with Testcontainers & MockMvc
```

---

## 5. Course Curriculum Breakdown (12 Modules + Capstone)

- **Module 01**: Domain-Driven Design Foundations & Ubiquitous Language (Strategic DDD)
- **Module 02**: Hexagonal Architecture Blueprint & Ports/Adapters Decoupling
- **Module 03**: Value Objects & Immutability with Java 27 Records
- **Module 04**: Entities, Identity & Lifecycle in Domain Models
- **Module 05**: Aggregates, Aggregate Roots & Domain Invariants
- **Module 06**: Domain Events & Event-Driven Decoupling
- **Module 07**: Inbound (Driving) Ports & Application Services (Use Cases & CQRS Lite)
- **Module 08**: Outbound (Driven) Ports & Persistence Adapters (Spring Data JDBC / JPA Separation)
- **Module 09**: Driving Adapters with Spring Boot 4 (REST, Problem Details, Virtual Threads)
- **Module 10**: Driven Adapters for External Services & Messaging (Kafka, RestClient, Resilience4j)
- **Module 11**: Automated Architectural Governance with ArchUnit & Hexagonal Guardrails
- **Module 12**: Context Mapping, Shared Kernels & Outbox Pattern for Distributed Bounded Contexts
- **Capstone Project**: `capstone-order-fulfillment-platform` — A complete, multi-bounded-context E-Commerce & Logistics Platform built with full Hexagonal Architecture, transactional outbox, Kafka event streaming, PostgreSQL via Testcontainers, and full bilingual documentation.

---

## 6. Commands & Verification Cheat Sheet

### Build & Test
```bash
# Build all modules and run all tests
./mvnw clean verify

# Run tests for a specific module
./mvnw test -pl modules/module-05-aggregates-and-invariants

# Run only ArchUnit architectural compliance tests
./mvnw test -Dtest=*ArchitectureTest

# Start local infrastructure (PostgreSQL, Kafka, Mailpit)
docker compose up -d

# Stop local infrastructure
docker compose down -v
```

### PDF Documentation Generation
```bash
# Generate English and Turkish PDFs from Markdown lessons
./scripts/generate-pdfs.sh

# Or generate for a specific module
./scripts/generate-pdfs.sh module-01
```

---

## 7. Bilingual Content Guidelines

- **English (`.md`)**: Idiomatic technical English, precise domain terminology matching Eric Evans & Vaughn Vernon DDD literature.
- **Turkish (`.tr.md`)**: Natural, grammatically accurate Turkish software engineering terminology. Key DDD terms (Aggregate, Value Object, Bounded Context, Port, Adapter, Invariant, Ubiquitous Language) are preserved alongside clear Turkish explanations (e.g. *Değer Nesnesi (Value Object)*, *Kapsamlı Dil (Ubiquitous Language)*, *Bağlama Dayalı Sınır (Bounded Context)*).
- **Code & Ubiquitous Language**: Class names, method names, variable names, database tables, and git commits are **strictly in English**.

---

## 8. AI Pair Programming & SDD Rules for Contributors

When implementing any task in this repo:
1. Always reference the corresponding issue or spec section.
2. Ensure domain models never import `org.springframework.*` or `jakarta.persistence.*`.
3. Provide both runnable student starter exercises (`exercises/`) and verified solutions (`solutions/`).
4. Ensure all tests pass (`./mvnw test`) and ArchUnit rules remain green.
5. Create dual documentation files (`lesson.md` and `lesson.tr.md`).
