# Module 02: Hexagonal Architecture Blueprint & Ports/Adapters Decoupling

## 🎯 Learning Objectives
- Master **Alistair Cockburn's Hexagonal Architecture (Ports and Adapters)**.
- Understand the **Dependency Inversion Principle (DIP)** applied to enterprise system layers.
- Formally distinguish **Inbound (Driving) Ports** from **Outbound (Driven) Ports**.
- Structure a clean four-ring package hierarchy (`domain`, `application`, `infrastructure`).
- Verify hexagonal boundaries using automated **ArchUnit** tests.

---

## 📂 Structure
- `docs/lesson.md` & `docs/lesson.tr.md`: In-depth architectural blueprint lecture notes.
- `src/main/java/`: Production-grade Product Catalog bounded context with Inbound/Outbound ports and adapters.
- `src/test/java/`: Domain and ArchUnit layer verification tests.
- `exercises/`: Student refactoring task from layered to hexagonal.
- `solutions/`: Verified reference solution.
