# 🏛️ Domain-Driven Design & Hexagonal Architecture Masterclass in Java

[![Java 27](https://img.shields.io/badge/Java-27%20LTS-orange.svg)](https://openjdk.org/)
[![Spring Boot 4](https://img.shields.io/badge/Spring%20Boot-4.0%2B-brightgreen.svg)](https://spring.io/projects/spring-boot)
[![Architecture](https://img.shields.io/badge/Architecture-Hexagonal%20%2F%20Ports%20%26%20Adapters-blue.svg)](https://alistair.cockburn.us/hexagonal-architecture/)
[![Methodology](https://img.shields.io/badge/Methodology-Spec--Driven%20Development%20(SDD)-purple.svg)](./SPEC.md)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Bilingual](https://img.shields.io/badge/Language-English%20%7C%20T%C3%BCrk%C3%A7e-red.svg)](./README.tr.md)

> **Curriculum Target**: September 2026 Baseline  
> **Türkçe Dokümantasyon**: [README.tr.md](./README.tr.md)  
> **Development Methodology**: Spec-Driven Development (SDD) following Addy Osmani's SDD Workflow  

Welcome to the **Domain-Driven Design (DDD) & Hexagonal Architecture (Ports and Adapters)** comprehensive course repository. This curriculum is engineered to bridge the gap between abstract architectural theory and real-world, production-ready enterprise Java development.

---

## 🎯 Course Highlights

- **Pure Domain Core**: Zero framework dependencies inside domain logic (`org.springframework.*` or `jakarta.persistence.*` are strictly prohibited).
- **Hexagonal Architecture**: Complete decoupling of application use cases via Inbound (Driving) and Outbound (Driven) Ports.
- **Modern Java 27 Idioms**: Value Objects powered by Java Records with compact constructors, Domain Events modeled with Sealed Interfaces, Pattern Matching with switch expressions, and Virtual Threads (Project Loom).
- **Automated Architectural Governance**: ArchUnit tests compiled directly into test suites to permanently prevent architectural degradation.
- **Spec-Driven Development (SDD)**: Addy Osmani's spec-first workflow (`SPEC.md` ➔ `plan.md` ➔ `todo.md` ➔ Implementation ➔ ArchUnit Verification).
- **Dual-Format & Bilingual**: Every module includes in-depth `.md` lesson guides, 1-click printable `.pdf` versions, practical exercises (`exercises/`) with starter test suites, and verified reference solutions (`solutions/`) in both **English** and **Turkish**.
- **Enterprise Capstone Project**: An end-to-end, multi-bounded-context E-Commerce Order & Fulfillment platform with Transactional Outbox, Kafka event streaming, and Testcontainers.

---

## 📐 Hexagonal Architecture Blueprint

```
                            ┌──────────────────────────────────────────────┐
                            │               INFRASTRUCTURE                 │
                            │  ┌────────────────────────────────────────┐  │
                            │  │              APPLICATION               │  │
 [Driving Adapter]          │  │  ┌──────────────────────────────────┐  │  │ [Driven Adapter]
 REST Controller (Web MVC) ─┼──┼─>│ Driving Port (Use Case)         │  │  ├─┼─> PostgreSQL / JPA
 CLI Runner                 ─┼──┼─>│                                   │  │  ├─┼─> Kafka Event Publisher
 Kafka Message Consumer     ─┼──┼─>│       Application Service         │  │  ├─┼─> External Payment SPI
                            │  │  │                │                 │  │  │
                            │  │  │                ▼                 │  │  │
                            │  │  │  ┌────────────────────────────┐  │  │  │
                            │  │  │  │       DOMAIN CORE          │  │  │  │
                            │  │  │  │  - Entities & Aggregates   │  │  │  │
                            │  │  │  │  - Value Objects (Records) │  │  │  │
                            │  │  │  │  - Business Invariants     │  │  │  │
                            │  │  │  │  - Domain Events (Sealed)  │  │  │  │
                            │  │  │  │  - Domain Services         │  │  │  │
                            │  │  │  └────────────────────────────┘  │  │  │
                            │  │  │                │                 │  │  │
                            │  │  │                ▼                 │  │  │
                            │  │  │  Driven Port (Repository SPI)    │  │  │
                            │  │  └──────────────────────────────────┘  │  │
                            │  └────────────────────────────────────────┘  │
                            └──────────────────────────────────────────────┘
```

---

## 📚 12-Module Syllabus & Learning Path

| # | Module Folder | Key Domain Concepts | Tech & Hexagonal Focus | Docs & PDF |
|---|---|---|---|---|
| **01** | [`module-01-ddd-foundations`](./modules/module-01-ddd-foundations) | Ubiquitous Language, Subdomains, Bounded Contexts | Anemic vs Rich Domain Model | [EN](./modules/module-01-ddd-foundations/docs/lesson.md) · [TR](./modules/module-01-ddd-foundations/docs/lesson.tr.md) |
| **02** | [`module-02-hexagonal-architecture`](./modules/module-02-hexagonal-architecture) | Ports & Adapters, Dependency Inversion | Layer boundaries & Package layout | [EN](./modules/module-02-hexagonal-architecture/docs/lesson.md) · [TR](./modules/module-02-hexagonal-architecture/docs/lesson.tr.md) |
| **03** | [`module-03-value-objects`](./modules/module-03-value-objects) | Immutability, Equality by Value, Self-Validation | Java 27 Records & Compact Constructors | [EN](./modules/module-03-value-objects/docs/lesson.md) · [TR](./modules/module-03-value-objects/docs/lesson.tr.md) |
| **04** | [`module-04-entities-and-identity`](./modules/module-04-entities-and-identity) | Identity, Entity Equality, Lifecycle Mutation | Identity Types, Natural vs Surrogate IDs | [EN](./modules/module-04-entities-and-identity/docs/lesson.md) · [TR](./modules/module-04-entities-and-identity/docs/lesson.tr.md) |
| **05** | [`module-05-aggregates-and-invariants`](./modules/module-05-aggregates-and-invariants) | Aggregate Roots, Consistency Boundaries | Multi-entity Invariants, Defensive Copies | [EN](./modules/module-05-aggregates-and-invariants/docs/lesson.md) · [TR](./modules/module-05-aggregates-and-invariants/docs/lesson.tr.md) |
| **06** | [`module-06-domain-events`](./modules/module-06-domain-events) | Domain Events, Side-effect Decoupling | Java 27 Sealed Interfaces & Dispatcher SPI | [EN](./modules/module-06-domain-events/docs/lesson.md) · [TR](./modules/module-06-domain-events/docs/lesson.tr.md) |
| **07** | [`module-07-driving-ports-use-cases`](./modules/module-07-driving-ports-use-cases) | Driving Ports, Application Services | CQRS Lite, Command Handlers & DTO Mapping | [EN](./modules/module-07-driving-ports-use-cases/docs/lesson.md) · [TR](./modules/module-07-driving-ports-use-cases/docs/lesson.tr.md) |
| **08** | [`module-08-driven-ports-persistence`](./modules/module-08-driven-ports-persistence) | Outbound Ports, Repository SPI | Spring Data JPA / JDBC Adapters, Mappers | [EN](./modules/module-08-driven-ports-persistence/docs/lesson.md) · [TR](./modules/module-08-driven-ports-persistence/docs/lesson.tr.md) |
| **09** | [`module-09-driving-adapters-rest`](./modules/module-09-driving-adapters-rest) | REST Adapters, Problem Details (RFC 9457) | Spring Boot 4 Virtual Threads (Loom) | [EN](./modules/module-09-driving-adapters-rest/docs/lesson.md) · [TR](./modules/module-09-driving-adapters-rest/docs/lesson.tr.md) |
| **10** | [`module-10-driven-adapters-messaging`](./modules/module-10-driven-adapters-messaging) | External SPIs, Kafka Event Streaming | Resilient RestClient & Testcontainers | [EN](./modules/module-10-driven-adapters-messaging/docs/lesson.md) · [TR](./modules/module-10-driven-adapters-messaging/docs/lesson.tr.md) |
| **11** | [`module-11-architecture-testing-archunit`](./modules/module-11-architecture-testing-archunit) | Architecture as Code, Fitness Functions | ArchUnit 1.4+ Hexagonal Rule Suite | [EN](./modules/module-11-architecture-testing-archunit/docs/lesson.md) · [TR](./modules/module-11-architecture-testing-archunit/docs/lesson.tr.md) |
| **12** | [`module-12-context-mapping-outbox`](./modules/module-12-context-mapping-outbox) | Context Mapping, Anti-Corruption Layer (ACL) | Transactional Outbox Pattern & At-Least-Once | [EN](./modules/module-12-context-mapping-outbox/docs/lesson.md) · [TR](./modules/module-12-context-mapping-outbox/docs/lesson.tr.md) |
| **🏁** | [`capstone-order-fulfillment-platform`](./capstone-order-fulfillment-platform) | Enterprise Multi-Bounded Context System | Full Hexagonal Suite, Kafka, Outbox & Docker | [EN](./capstone-order-fulfillment-platform/docs/lesson.md) · [TR](./capstone-order-fulfillment-platform/docs/lesson.tr.md) |

---

## 🚀 Quickstart & Student Guide

### Prerequisites
- JDK 25 or 27 (OpenJDK / Temurin recommended)
- Docker Desktop or OrbStack (for running PostgreSQL and Kafka)
- Maven 3.9+ (or use the included `./mvnw` wrapper)

### Build and Run All Tests
```bash
# Verify all modules, pure domain tests, and ArchUnit compliance
./mvnw clean test

# Run tests for a specific module
./mvnw test -pl modules/module-05-aggregates-and-invariants

# Run only architectural fitness tests
./mvnw test -Dtest=*ArchitectureTest
```

### Start Local Infrastructure (Docker Compose)
```bash
# Start PostgreSQL (5432), Kafka (9092), and Mailpit (8025)
docker compose up -d

# Check health status
docker compose ps

# Tear down when finished
docker compose down -v
```

### Generate Lesson PDFs
```bash
# Generate PDF documentation for all modules in both English and Turkish
./scripts/generate-pdfs.sh

# Or generate for a specific module
./scripts/generate-pdfs.sh module-03
```

---

## 🛠️ Spec-Driven Development (SDD) Workflow

This project follows Addy Osmani's Spec-Driven Development methodology:

1. **Specification First**: View [`SPEC.md`](./SPEC.md) and [`specs/`](./specs/) for domain requirements, invariants, and port contracts.
2. **Delivery Plan**: View [`plan.md`](./plan.md) for architectural milestones and sequencing.
3. **Task Tracking**: View [`todo.md`](./todo.md) and [GitHub Issues](https://github.com/aliturgutbozkurt/ddd-edu/issues).
4. **Developer Guidance**: View [`CLAUDE.md`](./CLAUDE.md) for architectural invariants and coding standards.

---

## 📄 License
This educational repository is open-sourced under the [MIT License](./LICENSE).
