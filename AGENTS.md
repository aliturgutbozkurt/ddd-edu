# AGENTS.md — Agent Guidelines for DDD & Hexagonal Architecture Course

This repository contains educational materials, runnable codebases, homework exercises, and a capstone project for **Domain-Driven Design (DDD) & Hexagonal Architecture in Java 27 & Spring Boot 4 (September 2026 Curriculum)**.

## Core Rules for All Agents:
1. **Spec-Driven First**: Always refer to `SPEC.md`, `specs/`, and `plan.md` before generating code.
2. **Domain Layer Integrity**:
   - `domain` packages must NEVER import Spring (`org.springframework.*`), Jakarta persistence (`jakarta.persistence.*`), or Jackson annotations (`com.fasterxml.jackson.*`).
   - Use standard Java 27 APIs (records, sealed types, pattern matching).
3. **Ports & Adapters Boundary**:
   - Inbound / Driving Ports = interfaces representing Use Cases (Application layer).
   - Outbound / Driven Ports = interfaces representing SPIs (Application or Domain layer).
   - Adapters = implementations in `infrastructure` package.
4. **ArchUnit Compliance**:
   - Every module must include ArchUnit tests validating that architecture rules are not broken.
5. **Bilingual Requirement**:
   - All modules must contain both English (`lesson.md`, `README.md`) and Turkish (`lesson.tr.md`, `README.tr.md`) documentation and exercise explanations.
6. **Student Usability**:
   - Starter code in `exercises/` must fail initially with clear TODO markers.
   - Reference code in `solutions/` must be 100% working and pass all tests.
