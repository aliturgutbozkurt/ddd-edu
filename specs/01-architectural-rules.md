# Architectural Specification: Hexagonal Architecture & ArchUnit Enforcement

## 1. Hexagonal Layers & Package Structure

Every module in this course follows a strict four-ring hexagonal model:

```
com.turkninja.ddd.<module>
├── domain/                      # Ring 0: The Core (Pure Java SE 27)
│   ├── model/                   # Entities, Aggregates, Value Objects
│   ├── event/                   # Sealed Domain Events
│   └── exception/               # Pure domain business exceptions
│
├── application/                 # Ring 1: Application Use Cases
│   ├── port/
│   │   ├── in/                  # Driving (Inbound) Ports: Use Cases & Queries
│   │   └── out/                 # Driven (Outbound) Ports: SPIs (Repositories, Gateways)
│   └── service/                 # Application Services implementing Inbound Ports
│
└── infrastructure/              # Ring 2: Adapters & Framework Configuration
    ├── adapter/
    │   ├── input/               # Driving Adapters (REST, GraphQL, gRPC, CLI)
    │   │   └── rest/
    │   └── output/              # Driven Adapters (JPA, JDBC, Kafka, HTTP Clients)
    │       ├── persistence/
    │       └── messaging/
    └── config/                  # Spring Boot 4 @Configuration beans & DI wiring
```

---

## 2. Layer Dependency Constraints (Formal Specifications)

| Source Layer | Permitted Outgoing Dependencies | Strictly Forbidden Dependencies |
|---|---|---|
| **`domain..`** | `java.base`, `java.time`, `java.math`, `java.util` | `application..`, `infrastructure..`, `org.springframework..`, `jakarta.persistence..`, `com.fasterxml.jackson..` |
| **`application.port.in..`** | `domain..`, `java..` | `infrastructure..`, `org.springframework..` |
| **`application.port.out..`** | `domain..`, `java..` | `infrastructure..`, `org.springframework..` |
| **`application.service..`** | `domain..`, `application.port..`, `java..` | `infrastructure..`, `jakarta.persistence..` (Only transaction management allowed if explicitly configured) |
| **`infrastructure..`** | `domain..`, `application..`, `org.springframework..`, `jakarta..` | Other unrelated module internals |

---

## 3. Automated ArchUnit Fitness Rules (Executable Spec)

Every module's `src/test/java/.../architecture/ArchitectureTest.java` MUST verify the following five rules:

```java
@AnalyzeClasses(packages = "com.turkninja.ddd")
class HexagonalArchitectureTest {

    @ArchTest
    static final ArchRule domain_must_not_depend_on_outer_layers =
        noClasses().that().resideInAPackage("..domain..")
            .should().dependOnClassesThat().resideInAnyPackage("..application..", "..infrastructure..");

    @ArchTest
    static final ArchRule domain_must_not_use_spring_or_jakarta =
        noClasses().that().resideInAPackage("..domain..")
            .should().dependOnClassesThat().resideInAnyPackage("org.springframework..", "jakarta.persistence..");

    @ArchTest
    static final ArchRule application_must_not_depend_on_infrastructure =
        noClasses().that().resideInAPackage("..application..")
            .should().dependOnClassesThat().resideInAnyPackage("..infrastructure..");

    @ArchTest
    static final ArchRule driving_adapters_must_only_access_inbound_ports =
        classes().that().resideInAPackage("..infrastructure.adapter.input..")
            .should().onlyAccessClassesThat().resideInAnyPackage(
                "..infrastructure..",
                "..application.port.in..",
                "..domain..",
                "java..",
                "org.springframework.."
            );

    @ArchTest
    static final ArchRule driven_adapters_must_implement_outbound_ports =
        classes().that().resideInAPackage("..infrastructure.adapter.output..")
            .and().haveSimpleNameEndingWith("Adapter")
            .should().implement(DescribedPredicate.describe(
                "an outbound port interface",
                javaClass -> javaClass.getRawInterfaces().stream()
                    .anyMatch(i -> i.getPackageName().contains("application.port.out"))
            ));
}
```

---

## 4. Value Object & Aggregate Rules

1. **Value Objects**:
   - Must be implemented as Java 27 `record`.
   - Compact constructors must validate invariants and throw `DomainValidationException` on invalid values.
   - Must be immutable with no setters or side effects.
2. **Entities & Aggregate Roots**:
   - Must have a strongly typed ID (Value Object, e.g., `OrderId`, not a primitive `Long` or `UUID`).
   - Must encapsulate internal state; return immutable collections (`Collections.unmodifiableList`).
   - Must record Domain Events internally via an internal list, exposed via `getDomainEvents()` and cleared via `clearDomainEvents()`.
