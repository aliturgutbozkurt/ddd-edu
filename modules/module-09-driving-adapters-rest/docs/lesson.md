---
marp: true
theme: default
paginate: true
header: "DDD & Hexagonal Architecture Masterclass | Module 09"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Module 09: Driving Adapters with Spring Boot 4

## Exposing Hexagonal Use Cases via Modern REST & Problem Details

---

## 1. What is a Driving Adapter?

A Driving (Primary) Adapter initiates interaction with our system:
- Receives HTTP requests, CLI inputs, or message broker payloads.
- Converts protocol-specific requests (e.g. JSON HTTP POST) into strongly typed **Use Case Commands**.
- Calls the Inbound Port interface.
- Translates use case results or domain exceptions back to protocol responses (e.g. HTTP 201 Created or RFC 9457 Problem Details).

---

## 2. Spring Boot 4 & Virtual Threads (Loom)

In Spring Boot 4, virtual threads can be enabled by default:
```properties
spring.threads.virtual.enabled=true
```
This allows millions of concurrent requests without thread-pool starvation, making driving adapters lightning fast while retaining synchronous, readable imperative code.
