---
marp: true
theme: default
paginate: true
header: "DDD & Hexagonal Architecture Masterclass | Module 11"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Module 11: Automated Architectural Governance with ArchUnit

## Architecture as Code: Enforcing Hexagonal Boundaries at Compile Time

---

## 1. What is Architecture Erosion?

Without automated checks, codebases naturally decay over time:
- A junior developer imports Spring's `@Transactional` directly into a domain entity.
- A REST controller bypasses an Inbound Port to mutate a repository directly.
- The hexagonal boundaries break down into an unmaintainable monolith.

---

## 2. ArchUnit: The Solution

ArchUnit executes within standard JUnit 5 test suites to verify architectural rules:
```java
@ArchTest
static final ArchRule domain_must_be_pure =
    noClasses().that().resideInAPackage("..domain..")
        .should().dependOnClassesThat().resideInAnyPackage("org.springframework..");
```
