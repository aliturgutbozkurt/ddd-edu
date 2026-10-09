---
marp: true
theme: default
paginate: true
header: "DDD & Hexagonal Architecture Masterclass | Module 02"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Module 02: Hexagonal Architecture (Ports and Adapters) Blueprint

## Inverting Dependencies for Long-Lived Maintainability

---

## 1. The Problem with Traditional Layered Architecture

Traditional 3-tier architecture (Controller -> Service -> DAO / Database) forces developers to think database-first:

```
[UI / Controller] ──> [Business Service] ──> [Database / JPA Entity]
```

### The Pitfalls:
1. **Database Coupling**: Domain models become anemic reflections of database tables (`@Entity`, `@Table`).
2. **Framework Leakage**: Spring annotations (`@Service`, `@Autowired`) infect core business rules.
3. **Difficult Testing**: Testing business logic requires mocking databases and booting Spring context.

---

## 2. The Hexagonal Solution (Alistair Cockburn)

Hexagonal architecture places the **Domain Core** at the center, surrounded by Application Use Cases, accessed exclusively via **Ports**:

```
[Driving Adapter: REST / CLI]
           │
           ▼
[Inbound Port: Use Case Interface]
           │
           ▼
[Application Service] ──> [Domain Model]
           │
           ▼
[Outbound Port: SPI Interface]
           ▲
           │
[Driven Adapter: PostgreSQL / Kafka]
```

### Core Invariant:
**Dependencies always point inward.** The domain knows nothing about the outside world.
