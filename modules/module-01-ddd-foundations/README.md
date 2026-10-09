# Module 01: Domain-Driven Design Foundations & Ubiquitous Language

## 🎯 Learning Objectives
- Understand the core philosophy of **Strategic Domain-Driven Design (DDD)**.
- Identify the differences between **Core Domains**, **Supporting Subdomains**, and **Generic Subdomains**.
- Learn why the **Anemic Domain Model** is an anti-pattern that violates object-oriented encapsulation.
- Build a **Rich Domain Model** in pure Java 27 without framework contamination.
- Establish a rigorous **Ubiquitous Language** for a FinTech banking context.

---

## 📂 Module Structure
- `docs/lesson.md`: Complete theoretical lecture (Marp/PDF compatible).
- `docs/lesson.tr.md`: Kapsamlı Türkçe ders anlatımı.
- `src/main/java/`: Runnable example contrasting Anemic vs Rich Domain Models.
- `src/test/java/`: Pure domain unit tests and ArchUnit layer verification tests.
- `exercises/`: Student assignment on implementing overdraft limits and transaction history.
- `solutions/`: Instructor reference solution.

---

## ⚡ Quickstart
```bash
# Run tests for Module 01
./mvnw test -pl modules/module-01-ddd-foundations
```
