#!/usr/bin/env python3
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def write_file(rel_path, content):
    full_path = BASE_DIR / rel_path
    full_path.parent.mkdir(parents=True, exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Generated: {rel_path}")

# ==============================================================================
# MODULE 06: Domain Events & Event-Driven Decoupling
# ==============================================================================
m6 = "modules/module-06-domain-events"
write_file(f"{m6}/README.md", """# Module 06: Domain Events & Event-Driven Decoupling

## 🎯 Learning Objectives
- Understand **Domain Events** as first-class citizens in DDD representing historical facts.
- Leverage **Java 27 sealed interfaces** for type-safe, exhaustive domain event pattern matching.
- Collect events inside Aggregate Roots and dispatch them after state changes.
- Decouple side effects (notifications, downstream systems) from core domain logic.
""")

write_file(f"{m6}/README.tr.md", """# Modül 06: Domain Olayları (Domain Events) ve Olay Tabanlı Ayrıştırma

## 🎯 Öğrenme Hedefleri
- **Domain Olaylarını (Domain Events)** geçmişte gerçekleşmiş değişmez gerçekler olarak konumlandırmak.
- Tipe güvenli ve eksiksiz pattern matching için **Java 27 sealed interface** hiyerarşilerini kullanmak.
- Olayları Aggregate Kökü içinde biriktirip işlem başarıyla tamamlandığında yayınlamak.
- Yan etkileri (bildirimler, harici sistemler) çekirdek domain mantığından tamamen ayırmak.
""")

write_file(f"{m6}/docs/lesson.md", """---
marp: true
theme: default
paginate: true
header: "DDD & Hexagonal Architecture Masterclass | Module 06"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Module 06: Domain Events & Event-Driven Decoupling

## Capturing Past Business Facts with Java 27 Sealed Types

---

## 1. What is a Domain Event?

A Domain Event captures something that occurred in the past that domain experts care about:
- **Naming Rule**: Always in **past tense** (`OrderPlacedEvent`, `PaymentReceivedEvent`, `ShipmentDispatchedEvent`).
- **Immutable**: Events happened in the past; they can never be modified or undone.
- **Payload**: Contains the event ID, timestamp, and domain identifiers necessary for subscribers to react.

---

## 2. Java 27 Sealed Interfaces for Events

```java
public sealed interface OrderDomainEvent extends DomainEvent {
    OrderId orderId();

    record OrderCreatedEvent(UUID eventId, OrderId orderId, Instant occurredOn) implements OrderDomainEvent {}
    record OrderCancelledEvent(UUID eventId, OrderId orderId, String reason, Instant occurredOn) implements OrderDomainEvent {}
}
```
""")

write_file(f"{m6}/docs/lesson.tr.md", """---
marp: true
theme: default
paginate: true
header: "DDD & Hekzagonal Mimari Masterclass | Modül 06"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Modül 06: Domain Olayları ve Olay Tabanlı Ayrıştırma

## Geçmiş İş Gerçeklerini Java 27 Sealed Tipleriyle Modelleme

---

## 1. Domain Olayı (Domain Event) Nedir?

Domain uzmanlarının ilgilendiği, geçmişte gerçekleşmiş bir iş olayını temsil eder:
- **İsimlendirme**: Daima **geçmiş zaman** kipiyle adlandırılır (`OrderPlacedEvent`, `PaymentReceivedEvent`).
- **Değişmezdir**: Geçmiş değiştirilemez; olaylar silinemez veya mutasyona uğratılamaz.
- **İçerik**: Olay kimliği, UTC zaman damgası ve tüketicilerin aksiyon alabilmesi için gerekli domain verilerini barındırır.
""")

write_file(f"{m6}/src/main/java/com/turkninja/ddd/module06/domain/event/OrderEvent.java", """package com.turkninja.ddd.module06.domain.event;

import com.turkninja.ddd.shared.domain.DomainEvent;

import java.time.Instant;
import java.util.UUID;

public sealed interface OrderEvent extends DomainEvent {

    UUID orderId();

    record OrderCreated(UUID eventId, UUID orderId, Instant occurredOn) implements OrderEvent {}
    record OrderPaid(UUID eventId, UUID orderId, String paymentRef, Instant occurredOn) implements OrderEvent {}
    record OrderCancelled(UUID eventId, UUID orderId, String reason, Instant occurredOn) implements OrderEvent {}
}
""")

write_file(f"{m6}/src/test/java/com/turkninja/ddd/module06/domain/DomainEventTest.java", """package com.turkninja.ddd.module06.domain;

import com.turkninja.ddd.module06.domain.event.OrderEvent;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.time.Instant;
import java.util.UUID;

import static org.assertj.core.api.Assertions.assertThat;

@DisplayName("Module 06: Domain Events Sealed Hierarchy Test")
class DomainEventTest {

    @Test
    @DisplayName("Pattern matching handles sealed domain events exhaustively")
    void testPatternMatchingEvents() {
        UUID orderId = UUID.randomUUID();
        OrderEvent event = new OrderEvent.OrderPaid(UUID.randomUUID(), orderId, "PAY-12345", Instant.now());

        String result = switch (event) {
            case OrderEvent.OrderCreated created -> "Created: " + created.orderId();
            case OrderEvent.OrderPaid paid -> "Paid: " + paid.paymentRef();
            case OrderEvent.OrderCancelled cancelled -> "Cancelled: " + cancelled.reason();
        };

        assertThat(result).isEqualTo("Paid: PAY-12345");
    }
}
""")

write_file(f"{m6}/src/test/java/com/turkninja/ddd/module06/architecture/Module06ArchitectureTest.java", """package com.turkninja.ddd.module06.architecture;

import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.core.importer.ImportOption;
import com.turkninja.ddd.shared.architecture.HexagonalArchitectureRules;
import org.junit.jupiter.api.Test;

class Module06ArchitectureTest {
    @Test
    void testHexagonalIsolation() {
        JavaClasses classes = new ClassFileImporter()
                .withImportOption(ImportOption.Predefined.DO_NOT_INCLUDE_TESTS)
                .importPackages("com.turkninja.ddd.module06");
        HexagonalArchitectureRules.verifyHexagonalArchitecture(classes);
    }
}
""")
write_file(f"{m6}/src/test/resources/archunit.properties", "archRule.failOnEmptyShould=false\n")
write_file(f"{m6}/exercises/README.md", "# Exercise 06: Implementing Domain Event Dispatcher SPI\n")
write_file(f"{m6}/exercises/README.tr.md", "# Alıştırma 06: Domain Olay Yayıncısı SPI Arayüzü Uygulama\n")
write_file(f"{m6}/solutions/README.md", "# Solution 06: Event Dispatching with Decoupled Handlers\n")
write_file(f"{m6}/solutions/README.tr.md", "# Çözüm 06: Ayrıştırılmış İşleyiciler ile Olay Dağıtımı\n")

# ==============================================================================
# MODULE 07: Inbound (Driving) Ports & Application Services
# ==============================================================================
m7 = "modules/module-07-driving-ports-use-cases"
write_file(f"{m7}/README.md", """# Module 07: Inbound (Driving) Ports & Application Services (CQRS Lite)

## 🎯 Learning Objectives
- Formally define **Use Cases** as Inbound (Driving) Ports.
- Implement **Application Services** as transaction coordinators.
- Separate Commands (mutations) from Queries (read models) via CQRS Lite.
- Protect the Domain Core from outer DTO representations.
""")

write_file(f"{m7}/README.tr.md", """# Modül 07: Gelen (Driving) Portlar ve Uygulama Servisleri (CQRS Lite)

## 🎯 Öğrenme Hedefleri
- **Kullanım Senaryolarını (Use Cases)** Gelen Portlar olarak tasarlamak.
- **Uygulama Servislerini** işlemleri koordine eden yapılar olarak kodlamak.
- CQRS Lite yaklaşımıyla Komutları (Command) ve Sorguları (Query) ayırmak.
- Saf domain modelini dış DTO yapılarından korumak.
""")

write_file(f"{m7}/docs/lesson.md", """---
marp: true
theme: default
paginate: true
header: "DDD & Hexagonal Architecture Masterclass | Module 07"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Module 07: Inbound (Driving) Ports & Application Services

## Orchestrating Use Cases Without Polluting Domain Logic

---

## 1. What is an Inbound (Driving) Port?

An Inbound Port represents a specific use case the application offers to the external world:
- It is an **interface** defined in `application/port/in/`.
- Callers (REST Controllers, CLI commands, Kafka message consumers) communicate ONLY through this interface.

```java
public interface PlaceOrderUseCase {
    OrderId placeOrder(PlaceOrderCommand command);
}
```
""")

write_file(f"{m7}/docs/lesson.tr.md", """---
marp: true
theme: default
paginate: true
header: "DDD & Hekzagonal Mimari Masterclass | Modül 07"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Modül 07: Gelen (Driving) Portlar ve Uygulama Servisleri

## Domain Mantığını Kirletmeden Kullanım Senaryolarını Yönetme

---

## 1. Gelen (Driving) Port Nedir?

Gelen Port, uygulamanın dış dünyaya sunduğu somut bir kullanım senaryosunu (Use Case) temsil eder:
- `application/port/in/` paketinde tanımlanan saf bir **Java arayüzüdür**.
- Dış adaptörler (REST Controller, CLI, Kafka dinleyicisi) yalnızca bu arayüzle konuşur.
""")

write_file(f"{m7}/src/main/java/com/turkninja/ddd/module07/application/port/in/CreateAccountUseCase.java", """package com.turkninja.ddd.module07.application.port.in;

import java.util.UUID;

public interface CreateAccountUseCase {
    UUID createAccount(CreateAccountCommand command);

    record CreateAccountCommand(String ownerName, double initialDeposit) {}
}
""")

write_file(f"{m7}/src/main/java/com/turkninja/ddd/module07/application/port/out/AccountRepositoryPort.java", """package com.turkninja.ddd.module07.application.port.out;

import java.util.Optional;
import java.util.UUID;

public interface AccountRepositoryPort {
    void save(AccountRecord account);
    Optional<AccountRecord> findById(UUID id);

    record AccountRecord(UUID id, String ownerName, double balance) {}
}
""")

write_file(f"{m7}/src/main/java/com/turkninja/ddd/module07/application/service/AccountApplicationService.java", """package com.turkninja.ddd.module07.application.service;

import com.turkninja.ddd.module07.application.port.in.CreateAccountUseCase;
import com.turkninja.ddd.module07.application.port.out.AccountRepositoryPort;

import java.util.Objects;
import java.util.UUID;

public class AccountApplicationService implements CreateAccountUseCase {

    private final AccountRepositoryPort repositoryPort;

    public AccountApplicationService(AccountRepositoryPort repositoryPort) {
        this.repositoryPort = Objects.requireNonNull(repositoryPort);
    }

    @Override
    public UUID createAccount(CreateAccountCommand command) {
        UUID accountId = UUID.randomUUID();
        AccountRepositoryPort.AccountRecord record = new AccountRepositoryPort.AccountRecord(
                accountId, command.ownerName(), command.initialDeposit());
        repositoryPort.save(record);
        return accountId;
    }
}
""")

write_file(f"{m7}/src/test/java/com/turkninja/ddd/module07/application/AccountUseCaseTest.java", """package com.turkninja.ddd.module07.application;

import com.turkninja.ddd.module07.application.port.in.CreateAccountUseCase;
import com.turkninja.ddd.module07.application.port.out.AccountRepositoryPort;
import com.turkninja.ddd.module07.application.service.AccountApplicationService;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.util.HashMap;
import java.util.Map;
import java.util.Optional;
import java.util.UUID;

import static org.assertj.core.api.Assertions.assertThat;

@DisplayName("Module 07: Inbound Port & Application Service Tests")
class AccountUseCaseTest {

    static class StubAccountRepository implements AccountRepositoryPort {
        final Map<UUID, AccountRecord> map = new HashMap<>();
        @Override
        public void save(AccountRecord account) { map.put(account.id(), account); }
        @Override
        public Optional<AccountRecord> findById(UUID id) { return Optional.ofNullable(map.get(id)); }
    }

    @Test
    @DisplayName("Application service coordinates account creation use case")
    void testCreateAccountUseCase() {
        StubAccountRepository repo = new StubAccountRepository();
        AccountApplicationService service = new AccountApplicationService(repo);

        UUID id = service.createAccount(new CreateAccountUseCase.CreateAccountCommand("John Doe", 500.0));

        assertThat(id).isNotNull();
        assertThat(repo.findById(id)).isPresent();
        assertThat(repo.findById(id).get().ownerName()).isEqualTo("John Doe");
    }
}
""")

write_file(f"{m7}/src/test/java/com/turkninja/ddd/module07/architecture/Module07ArchitectureTest.java", """package com.turkninja.ddd.module07.architecture;

import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.core.importer.ImportOption;
import com.turkninja.ddd.shared.architecture.HexagonalArchitectureRules;
import org.junit.jupiter.api.Test;

class Module07ArchitectureTest {
    @Test
    void testHexagonalIsolation() {
        JavaClasses classes = new ClassFileImporter()
                .withImportOption(ImportOption.Predefined.DO_NOT_INCLUDE_TESTS)
                .importPackages("com.turkninja.ddd.module07");
        HexagonalArchitectureRules.verifyHexagonalArchitecture(classes);
    }
}
""")
write_file(f"{m7}/src/test/resources/archunit.properties", "archRule.failOnEmptyShould=false\n")
write_file(f"{m7}/exercises/README.md", "# Exercise 07: Implementing CQRS Query Port and Application Handler\n")
write_file(f"{m7}/exercises/README.tr.md", "# Alıştırma 07: CQRS Sorgu Portu ve Uygulama İşleyicisi Yazma\n")
write_file(f"{m7}/solutions/README.md", "# Solution 07: Inbound Command & Query Ports\n")
write_file(f"{m7}/solutions/README.tr.md", "# Çözüm 07: Gelen Komut ve Sorgu Portları\n")

# ==============================================================================
# MODULE 08: Outbound (Driven) Ports & Persistence Adapters
# ==============================================================================
m8 = "modules/module-08-driven-ports-persistence"
write_file(f"{m8}/README.md", """# Module 08: Outbound (Driven) Ports & Persistence Adapters

## 🎯 Learning Objectives
- Design **Outbound Ports (Repository SPI)** with complete database agnosticism.
- Separate database persistence models (`OrderJpaEntity`) from rich Domain models (`Order`).
- Implement bidirectional mapping cleanly without reflection or ORM contamination.
- Prevent lazy-loading leaks and database transaction coupling in the domain core.
""")

write_file(f"{m8}/README.tr.md", """# Modül 08: Giden (Driven) Portlar ve Kalıcılık (Persistence) Adaptörleri

## 🎯 Öğrenme Hedefleri
- Veritabanından tamamen bağımsız **Giden Portlar (Repository SPI)** tasarlamak.
- Veritabanı tablolarını (`OrderJpaEntity`) saf Domain modellerinden (`Order`) ayrı tutmak.
- İki yönlü haritalamayı (bidirectional mapping) domain modeline zarar vermeden uygulamak.
- Tembel yükleme (lazy-loading) hatalarını ve veritabanı kilitlenmelerini domainden uzak tutmak.
""")

write_file(f"{m8}/docs/lesson.md", """---
marp: true
theme: default
paginate: true
header: "DDD & Hexagonal Architecture Masterclass | Module 08"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Module 08: Outbound (Driven) Ports & Persistence Adapters

## Decoupling Persistence from Domain Logic

---

## 1. Why Not Use JPA Annotations in Domain Entities?

Placing `@Entity`, `@Table`, and `@Id` inside domain entities violates Hexagonal Architecture:
- JPA requires default no-arg constructors (violating invariant validation).
- JPA requires non-final fields and mutable collections.
- Database schema changes force domain model refactoring.

---

## 2. The Driven Persistence Adapter Pattern

```
[Domain Aggregate: Order]
           ▲
           │ (Mappers)
           ▼
[Persistence Adapter: OrderPersistenceAdapter] ──> [Spring Data / JPA Entity]
```
""")

write_file(f"{m8}/docs/lesson.tr.md", """---
marp: true
theme: default
paginate: true
header: "DDD & Hekzagonal Mimari Masterclass | Modül 08"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Modül 08: Giden (Driven) Portlar ve Kalıcılık Adaptörleri

## Veritabanını Domain Mantığından Tamamen Ayrıştırmak

---

## 1. Neden Domain Varlıklarında JPA Anotasyonları Kullanılmaz?

Domain sınıflarına `@Entity`, `@Table` koymak Hekzagonal Mimariyi bozar:
- JPA varsayılan parametresiz yapıcı (no-arg constructor) ister (değişmezlik doğrulamalarını deler).
- JPA final olmayan alanlar ve değiştirilebilir koleksiyonlar bekler.
- Veritabanı şema değişiklikleri domain modelini zorla değiştirmeye sebep olur.
""")

write_file(f"{m8}/src/main/java/com/turkninja/ddd/module08/domain/model/CustomerId.java", """package com.turkninja.ddd.module08.domain.model;

import com.turkninja.ddd.shared.domain.ValueObject;
import java.util.UUID;

public record CustomerId(UUID value) implements ValueObject {}
""")

write_file(f"{m8}/src/main/java/com/turkninja/ddd/module08/domain/model/Customer.java", """package com.turkninja.ddd.module08.domain.model;

import com.turkninja.ddd.shared.domain.DomainEntity;

public class Customer extends DomainEntity<CustomerId> {
    private final String name;
    private final String email;

    public Customer(CustomerId id, String name, String email) {
        super(id);
        this.name = name;
        this.email = email;
    }

    public String getName() { return name; }
    public String getEmail() { return email; }
}
""")

write_file(f"{m8}/src/main/java/com/turkninja/ddd/module08/application/port/out/CustomerRepositoryPort.java", """package com.turkninja.ddd.module08.application.port.out;

import com.turkninja.ddd.module08.domain.model.Customer;
import com.turkninja.ddd.module08.domain.model.CustomerId;

import java.util.Optional;

public interface CustomerRepositoryPort {
    void save(Customer customer);
    Optional<Customer> findById(CustomerId id);
}
""")

write_file(f"{m8}/src/main/java/com/turkninja/ddd/module08/infrastructure/adapter/output/persistence/CustomerPersistenceAdapter.java", """package com.turkninja.ddd.module08.infrastructure.adapter.output.persistence;

import com.turkninja.ddd.module08.application.port.out.CustomerRepositoryPort;
import com.turkninja.ddd.module08.domain.model.Customer;
import com.turkninja.ddd.module08.domain.model.CustomerId;

import java.util.Map;
import java.util.Optional;
import java.util.UUID;
import java.util.concurrent.ConcurrentHashMap;

public class CustomerPersistenceAdapter implements CustomerRepositoryPort {

    // Database record representation
    record CustomerDbRecord(UUID id, String name, String email) {}

    private final Map<UUID, CustomerDbRecord> databaseTable = new ConcurrentHashMap<>();

    @Override
    public void save(Customer customer) {
        CustomerDbRecord dbRecord = new CustomerDbRecord(
                customer.getId().value(),
                customer.getName(),
                customer.getEmail()
        );
        databaseTable.put(dbRecord.id(), dbRecord);
    }

    @Override
    public Optional<Customer> findById(CustomerId id) {
        CustomerDbRecord record = databaseTable.get(id.value());
        if (record == null) return Optional.empty();
        return Optional.of(new Customer(new CustomerId(record.id()), record.name(), record.email()));
    }
}
""")

write_file(f"{m8}/src/test/java/com/turkninja/ddd/module08/infrastructure/CustomerPersistenceAdapterTest.java", """package com.turkninja.ddd.module08.infrastructure;

import com.turkninja.ddd.module08.domain.model.Customer;
import com.turkninja.ddd.module08.domain.model.CustomerId;
import com.turkninja.ddd.module08.infrastructure.adapter.output.persistence.CustomerPersistenceAdapter;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.util.UUID;

import static org.assertj.core.api.Assertions.assertThat;

@DisplayName("Module 08: Driven Persistence Adapter Tests")
class CustomerPersistenceAdapterTest {

    @Test
    @DisplayName("Should save and reconstitute pure domain customer through persistence adapter")
    void testSaveAndReconstituteCustomer() {
        CustomerPersistenceAdapter adapter = new CustomerPersistenceAdapter();
        CustomerId id = new CustomerId(UUID.randomUUID());
        Customer customer = new Customer(id, "Grace Hopper", "grace@navy.mil");

        adapter.save(customer);

        assertThat(adapter.findById(id)).isPresent();
        assertThat(adapter.findById(id).get().getName()).isEqualTo("Grace Hopper");
    }
}
""")

write_file(f"{m8}/src/test/java/com/turkninja/ddd/module08/architecture/Module08ArchitectureTest.java", """package com.turkninja.ddd.module08.architecture;

import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.core.importer.ImportOption;
import com.turkninja.ddd.shared.architecture.HexagonalArchitectureRules;
import org.junit.jupiter.api.Test;

class Module08ArchitectureTest {
    @Test
    void testHexagonalIsolation() {
        JavaClasses classes = new ClassFileImporter()
                .withImportOption(ImportOption.Predefined.DO_NOT_INCLUDE_TESTS)
                .importPackages("com.turkninja.ddd.module08");
        HexagonalArchitectureRules.verifyHexagonalArchitecture(classes);
    }
}
""")
write_file(f"{m8}/src/test/resources/archunit.properties", "archRule.failOnEmptyShould=false\n")
write_file(f"{m8}/exercises/README.md", "# Exercise 08: Database Table to Domain Aggregate Mapper\n")
write_file(f"{m8}/exercises/README.tr.md", "# Alıştırma 08: Veritabanı Tablosundan Domain Köküne Haritalama\n")
write_file(f"{m8}/solutions/README.md", "# Solution 08: Clean Persistence Decoupling\n")
write_file(f"{m8}/solutions/README.tr.md", "# Çözüm 08: Kalıcılık Katmanını Temizce Ayrıştırma\n")

print("Modules 06, 07, 08 generated successfully!")
