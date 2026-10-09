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
# MODULE 09: Driving Adapters with Spring Boot 4
# ==============================================================================
m9 = "modules/module-09-driving-adapters-rest"
write_file(f"{m9}/README.md", """# Module 09: Driving Adapters with Spring Boot 4 (REST & Virtual Threads)

## 🎯 Learning Objectives
- Implement **Primary (Driving) Adapters** using modern Spring Boot 4 REST controllers.
- Map domain exceptions to **RFC 9457 Problem Details** (`application/problem+json`).
- Leverage **Virtual Threads (Project Loom)** for scalable, non-blocking I/O dispatch.
- Ensure HTTP DTO models never contaminate the Domain Core.
""")

write_file(f"{m9}/README.tr.md", """# Modül 09: Spring Boot 4 ile Süren (Driving) Adaptörler (REST ve Sanal İş Parçacıkları)

## 🎯 Öğrenme Hedefleri
- Modern Spring Boot 4 REST denetleyicileri ile **Birincil (Süren) Adaptörler** geliştirmek.
- Domain istisnalarını **RFC 9457 Problem Details** (`application/problem+json`) formatına dönüştürmek.
- Yüksek verimli I/O işlemleri için **Virtual Threads (Project Loom)** gücünden yararlanmak.
- HTTP DTO modellerinin Saf Domain Çekirdeğine sızmasını kesin olarak engellemek.
""")

write_file(f"{m9}/docs/lesson.md", """---
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
""")

write_file(f"{m9}/docs/lesson.tr.md", """---
marp: true
theme: default
paginate: true
header: "DDD & Hekzagonal Mimari Masterclass | Modül 09"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Modül 09: Spring Boot 4 ile Süren Adaptörler (REST ve Sanal İş Parçacıkları)

## Hekzagonal Kullanım Senaryolarını REST ve Problem Details ile Dışa Açma

---

## 1. Süren (Driving) Adaptör Nedir?

Süren Adaptör, sistemimizle etkileşimi başlatan dış katman unsurudur:
- HTTP isteklerini, CLI komutlarını veya mesaj kuyruğu verilerini yakalar.
- Protokole özgü JSON gövdesini tipe güvenli bir **Use Case Komutuna (Command)** dönüştürür.
- Gelen Port (Inbound Port) arayüzünü tetikler.
- Dönen sonucu veya fırlatılan domain istisnasını protokol yanıtına (ör. HTTP 201 veya RFC 9457 Problem Details) çevirir.
""")

write_file(f"{m9}/src/main/java/com/turkninja/ddd/module09/application/port/in/TransferMoneyUseCase.java", """package com.turkninja.ddd.module09.application.port.in;

import java.math.BigDecimal;
import java.util.UUID;

public interface TransferMoneyUseCase {
    TransferResult transfer(TransferCommand command);

    record TransferCommand(String sourceAccount, String targetAccount, BigDecimal amount) {}
    record TransferResult(UUID transactionId, boolean success, String message) {}
}
""")

write_file(f"{m9}/src/main/java/com/turkninja/ddd/module09/infrastructure/adapter/input/rest/TransferRestController.java", """package com.turkninja.ddd.module09.infrastructure.adapter.input.rest;

import com.turkninja.ddd.module09.application.port.in.TransferMoneyUseCase;
import com.turkninja.ddd.module09.application.port.in.TransferMoneyUseCase.TransferCommand;
import com.turkninja.ddd.module09.application.port.in.TransferMoneyUseCase.TransferResult;

import java.math.BigDecimal;
import java.util.Objects;
import java.util.UUID;

public class TransferRestController {

    public record TransferRequest(String sourceAccount, String targetAccount, BigDecimal amount) {}
    public record TransferResponse(UUID transactionId, String status, String message) {}

    private final TransferMoneyUseCase transferMoneyUseCase;

    public TransferRestController(TransferMoneyUseCase transferMoneyUseCase) {
        this.transferMoneyUseCase = Objects.requireNonNull(transferMoneyUseCase);
    }

    public TransferResponse handleTransfer(TransferRequest request) {
        TransferCommand command = new TransferCommand(
                request.sourceAccount(),
                request.targetAccount(),
                request.amount()
        );

        TransferResult result = transferMoneyUseCase.transfer(command);
        return new TransferResponse(
                result.transactionId(),
                result.success() ? "COMPLETED" : "FAILED",
                result.message()
        );
    }
}
""")

write_file(f"{m9}/src/test/java/com/turkninja/ddd/module09/infrastructure/TransferRestControllerTest.java", """package com.turkninja.ddd.module09.infrastructure;

import com.turkninja.ddd.module09.application.port.in.TransferMoneyUseCase;
import com.turkninja.ddd.module09.infrastructure.adapter.input.rest.TransferRestController;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.math.BigDecimal;
import java.util.UUID;

import static org.assertj.core.api.Assertions.assertThat;

@DisplayName("Module 09: Driving REST Adapter Tests")
class TransferRestControllerTest {

    @Test
    @DisplayName("REST Controller translates request to use case command and wraps response")
    void testHandleTransfer() {
        UUID expectedTxId = UUID.randomUUID();
        TransferMoneyUseCase mockUseCase = command ->
                new TransferMoneyUseCase.TransferResult(expectedTxId, true, "Transfer completed");

        TransferRestController controller = new TransferRestController(mockUseCase);
        TransferRestController.TransferResponse response = controller.handleTransfer(
                new TransferRestController.TransferRequest("ACC-1", "ACC-2", new BigDecimal("150.00")));

        assertThat(response.transactionId()).isEqualTo(expectedTxId);
        assertThat(response.status()).isEqualTo("COMPLETED");
        assertThat(response.message()).isEqualTo("Transfer completed");
    }
}
""")

write_file(f"{m9}/src/test/java/com/turkninja/ddd/module09/architecture/Module09ArchitectureTest.java", """package com.turkninja.ddd.module09.architecture;

import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.core.importer.ImportOption;
import com.turkninja.ddd.shared.architecture.HexagonalArchitectureRules;
import org.junit.jupiter.api.Test;

class Module09ArchitectureTest {
    @Test
    void testHexagonalIsolation() {
        JavaClasses classes = new ClassFileImporter()
                .withImportOption(ImportOption.Predefined.DO_NOT_INCLUDE_TESTS)
                .importPackages("com.turkninja.ddd.module09");
        HexagonalArchitectureRules.verifyHexagonalArchitecture(classes);
    }
}
""")
write_file(f"{m9}/src/test/resources/archunit.properties", "archRule.failOnEmptyShould=false\n")
write_file(f"{m9}/exercises/README.md", "# Exercise 09: RFC 9457 Problem Details Exception Handler\n")
write_file(f"{m9}/exercises/README.tr.md", "# Alıştırma 09: RFC 9457 Problem Details İstisna İşleyicisi\n")
write_file(f"{m9}/solutions/README.md", "# Solution 09: Modern REST Driving Adapter\n")
write_file(f"{m9}/solutions/README.tr.md", "# Çözüm 09: Modern REST Süren Adaptör\n")

# ==============================================================================
# MODULE 10: Driven Adapters for Messaging & External Services
# ==============================================================================
m10 = "modules/module-10-driven-adapters-messaging"
write_file(f"{m10}/README.md", """# Module 10: Driven Adapters for External Services & Messaging (Kafka & RestClient)

## 🎯 Learning Objectives
- Design and implement **Secondary (Driven) Adapters** for message brokers (Kafka) and external APIs.
- Keep the domain core insulated from third-party client SDKs.
- Apply resilience patterns (timeouts, retries, fallbacks) within adapters.
- Test driven adapters using Testcontainers.
""")

write_file(f"{m10}/README.tr.md", """# Modül 10: Mesajlaşma ve Dış Servisler İçin Sürülen Adaptörler (Kafka ve RestClient)

## 🎯 Öğrenme Hedefleri
- Mesaj kuyrukları (Kafka) ve üçüncü parti API'ler için **İkincil (Sürülen) Adaptörler** geliştirmek.
- Saf domain çekirdeğini harici SDK kirliliklerinden izole etmek.
- Adaptör katmanında dayanıklılık (resilience - timeout, retry, fallback) desenlerini uygulamak.
- Sürülen adaptörleri Testcontainers ile güvenle test etmek.
""")

write_file(f"{m10}/docs/lesson.md", """---
marp: true
theme: default
paginate: true
header: "DDD & Hexagonal Architecture Masterclass | Module 10"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Module 10: Driven Adapters for Messaging & External Services

## Integrating with Kafka and Payment Providers via Pure Outbound Ports

---

## 1. What is a Driven Adapter?

A Driven (Secondary) Adapter is triggered by our Application Service to interact with an external dependency:
- Database engines (PostgreSQL, MongoDB).
- Message brokers (Apache Kafka, RabbitMQ).
- External HTTP APIs (Stripe, Twilio, Shipping Carriers).

---

## 2. Inverting Dependencies for Resilient Messaging

The Application layer defines:
```java
public interface EventPublisherPort {
    void publish(DomainEvent event);
}
```
The Infrastructure layer provides:
```java
public class KafkaEventPublisherAdapter implements EventPublisherPort {
    @Override
    public void publish(DomainEvent event) { ... }
}
```
""")

write_file(f"{m10}/docs/lesson.tr.md", """---
marp: true
theme: default
paginate: true
header: "DDD & Hekzagonal Mimari Masterclass | Modül 10"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Modül 10: Mesajlaşma ve Dış Servisler İçin Sürülen Adaptörler

## Kafka ve Ödeme Sağlayıcılarını Saf Giden Portlar ile Entegre Etme

---

## 1. Sürülen (Driven) Adaptör Nedir?

Sürülen Adaptör, Uygulama Servisimiz tarafından harici bir dünya ile iletişim kurmak üzere tetiklenir:
- Veritabanları (PostgreSQL, MongoDB).
- Olay kuyrukları (Apache Kafka, RabbitMQ).
- Harici HTTP API servisleri (Stripe, Kargo firmaları).
""")

write_file(f"{m10}/src/main/java/com/turkninja/ddd/module10/application/port/out/NotificationSenderPort.java", """package com.turkninja.ddd.module10.application.port.out;

public interface NotificationSenderPort {
    boolean sendNotification(NotificationMessage message);

    record NotificationMessage(String recipient, String title, String body) {}
}
""")

write_file(f"{m10}/src/main/java/com/turkninja/ddd/module10/infrastructure/adapter/output/messaging/SimulatedMessagePublisherAdapter.java", """package com.turkninja.ddd.module10.infrastructure.adapter.output.messaging;

import com.turkninja.ddd.module10.application.port.out.NotificationSenderPort;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class SimulatedMessagePublisherAdapter implements NotificationSenderPort {

    private final List<NotificationMessage> publishedMessages = new ArrayList<>();

    @Override
    public boolean sendNotification(NotificationMessage message) {
        publishedMessages.add(message);
        return true;
    }

    public List<NotificationMessage> getPublishedMessages() {
        return Collections.unmodifiableList(publishedMessages);
    }
}
""")

write_file(f"{m10}/src/test/java/com/turkninja/ddd/module10/infrastructure/MessagePublisherAdapterTest.java", """package com.turkninja.ddd.module10.infrastructure;

import com.turkninja.ddd.module10.application.port.out.NotificationSenderPort;
import com.turkninja.ddd.module10.infrastructure.adapter.output.messaging.SimulatedMessagePublisherAdapter;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

@DisplayName("Module 10: Driven Messaging Adapter Tests")
class MessagePublisherAdapterTest {

    @Test
    @DisplayName("Should publish notification message via driven adapter")
    void testMessagePublishing() {
        SimulatedMessagePublisherAdapter adapter = new SimulatedMessagePublisherAdapter();
        boolean success = adapter.sendNotification(
                new NotificationSenderPort.NotificationMessage("alice@example.com", "Order Update", "Your order has shipped!"));

        assertThat(success).isTrue();
        assertThat(adapter.getPublishedMessages()).hasSize(1);
        assertThat(adapter.getPublishedMessages().getFirst().title()).isEqualTo("Order Update");
    }
}
""")

write_file(f"{m10}/src/test/java/com/turkninja/ddd/module10/architecture/Module10ArchitectureTest.java", """package com.turkninja.ddd.module10.architecture;

import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.core.importer.ImportOption;
import com.turkninja.ddd.shared.architecture.HexagonalArchitectureRules;
import org.junit.jupiter.api.Test;

class Module10ArchitectureTest {
    @Test
    void testHexagonalIsolation() {
        JavaClasses classes = new ClassFileImporter()
                .withImportOption(ImportOption.Predefined.DO_NOT_INCLUDE_TESTS)
                .importPackages("com.turkninja.ddd.module10");
        HexagonalArchitectureRules.verifyHexagonalArchitecture(classes);
    }
}
""")
write_file(f"{m10}/src/test/resources/archunit.properties", "archRule.failOnEmptyShould=false\n")
write_file(f"{m10}/exercises/README.md", "# Exercise 10: Resilient HTTP Client Driven Adapter\n")
write_file(f"{m10}/exercises/README.tr.md", "# Alıştırma 10: Dayanıklı HTTP İstemcisi Sürülen Adaptörü\n")
write_file(f"{m10}/solutions/README.md", "# Solution 10: Driven Messaging & Resilient SPI Adapters\n")
write_file(f"{m10}/solutions/README.tr.md", "# Çözüm 10: Sürülen Mesajlaşma ve Dayanıklı SPI Adaptörleri\n")

# ==============================================================================
# MODULE 11: Automated Architectural Governance with ArchUnit
# ==============================================================================
m11 = "modules/module-11-architecture-testing-archunit"
write_file(f"{m11}/README.md", """# Module 11: Automated Architectural Governance with ArchUnit Guardrails

## 🎯 Learning Objectives
- Write **Architecture as Code** to permanently eliminate architectural erosion.
- Prevent Spring and Jakarta annotations from leaking into the Domain Core.
- Verify that Adapters never bypass Use Cases to directly access Domain Aggregates.
- Integrate ArchUnit rules into standard continuous integration (CI) pipelines.
""")

write_file(f"{m11}/README.tr.md", """# Modül 11: ArchUnit ile Otomatik Mimari Denetimi ve Korkuluklar (Guardrails)

## 🎯 Öğrenme Hedefleri
- Mimari erozyonu sonsuza kadar durdurmak için **Kod Olarak Mimari (Architecture as Code)** yazmak.
- Spring ve Jakarta anotasyonlarının Saf Domain Çekirdeğine sızmasını kesin olarak yasaklamak.
- Adaptörlerin Use Case katmanını atlayıp doğrudan Domain nesnelerine erişmesini engellemek.
- ArchUnit kurallarını sürekli entegrasyon (CI) boru hatlarına entegre etmek.
""")

write_file(f"{m11}/docs/lesson.md", """---
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
""")

write_file(f"{m11}/docs/lesson.tr.md", """---
marp: true
theme: default
paginate: true
header: "DDD & Hekzagonal Mimari Masterclass | Modül 11"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Modül 11: ArchUnit ile Otomatik Mimari Denetimi

## Kod Olarak Mimari: Hekzagonal Sınırları Derleme Zamanında Güvenceye Alma

---

## 1. Mimari Erozyon Nedir?

Otomatik denetimler olmadan yazılım projeleri zamanla çürür:
- Ekibe yeni katılan biri domain varlığı içine Spring'in `@Transactional` anotasyonunu ekler.
- Bir REST denetleyicisi Port katmanını atlayıp doğrudan veritabanı tablosuna yazar.
- Sonuç: Hekzagonal mimari çöker ve yine monolitik çamura dönüşür.
""")

write_file(f"{m11}/src/main/java/com/turkninja/ddd/module11/domain/PricedItem.java", """package com.turkninja.ddd.module11.domain;

import com.turkninja.ddd.shared.domain.ValueObject;
import java.math.BigDecimal;

public record PricedItem(String sku, BigDecimal price) implements ValueObject {}
""")

write_file(f"{m11}/src/test/java/com/turkninja/ddd/module11/architecture/Module11ArchitectureTest.java", """package com.turkninja.ddd.module11.architecture;

import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.core.importer.ImportOption;
import com.turkninja.ddd.shared.architecture.HexagonalArchitectureRules;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static com.tngtech.archunit.lang.syntax.ArchRuleDefinition.classes;

@DisplayName("Module 11: Comprehensive ArchUnit Governance Tests")
class Module11ArchitectureTest {

    @Test
    @DisplayName("Should enforce that domain layer remains pure Java")
    void testDomainPurity() {
        JavaClasses classes = new ClassFileImporter()
                .withImportOption(ImportOption.Predefined.DO_NOT_INCLUDE_TESTS)
                .importPackages("com.turkninja.ddd.module11");

        HexagonalArchitectureRules.verifyHexagonalArchitecture(classes);
    }

    @Test
    @DisplayName("Value objects must implement ValueObject marker interface")
    void testValueObjectConventions() {
        JavaClasses classes = new ClassFileImporter()
                .withImportOption(ImportOption.Predefined.DO_NOT_INCLUDE_TESTS)
                .importPackages("com.turkninja.ddd.module11.domain");

        classes().that().haveSimpleNameEndingWith("Item")
                .should().implement(com.turkninja.ddd.shared.domain.ValueObject.class)
                .allowEmptyShould(true)
                .check(classes);
    }
}
""")
write_file(f"{m11}/src/test/resources/archunit.properties", "archRule.failOnEmptyShould=false\n")
write_file(f"{m11}/exercises/README.md", "# Exercise 11: Writing Custom ArchUnit Port and Adapter Rules\n")
write_file(f"{m11}/exercises/README.tr.md", "# Alıştırma 11: Özel ArchUnit Port ve Adaptör Kuralları Yazma\n")
write_file(f"{m11}/solutions/README.md", "# Solution 11: Production-Ready Architectural Test Suite\n")
write_file(f"{m11}/solutions/README.tr.md", "# Çözüm 11: Üretime Hazır Mimari Test Paketi\n")

# ==============================================================================
# MODULE 12: Context Mapping & Transactional Outbox Pattern
# ==============================================================================
m12 = "modules/module-12-context-mapping-outbox"
write_file(f"{m12}/README.md", """# Module 12: Context Mapping, Anti-Corruption Layer (ACL) & Transactional Outbox

## 🎯 Learning Objectives
- Map relationships between Bounded Contexts using **Strategic Context Mapping**.
- Implement an **Anti-Corruption Layer (ACL)** to protect pure internal domain models.
- Solve the dual-write problem using the **Transactional Outbox Pattern**.
- Guarantee **at-least-once event delivery** across distributed architectures.
""")

write_file(f"{m12}/README.tr.md", """# Modül 12: Bağlam Eşleme (Context Mapping), ACL ve Transactional Outbox Deseni

## 🎯 Öğrenme Hedefleri
- Bounded Context ilişkilerini **Stratejik Bağlam Eşleme (Context Mapping)** ile tasarlamak.
- Kendi domainimizi dış sistemlerin kirli modellerinden korumak için **Yozlaşma Önleme Katmanı (ACL)** kurmak.
- Çift yazma (dual-write) problemini **Transactional Outbox Deseni** ile çözmek.
- Dağıtık mimarilerde **en az bir kez teslimat (at-least-once delivery)** garantisi sağlamak.
""")

write_file(f"{m12}/docs/lesson.md", """---
marp: true
theme: default
paginate: true
header: "DDD & Hexagonal Architecture Masterclass | Module 12"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Module 12: Context Mapping & Transactional Outbox Pattern

## Integrating Distributed Bounded Contexts Reliably

---

## 1. The Dual-Write Problem

When updating a database and publishing an event to Kafka in the same use case:
- If the database commit succeeds but Kafka crashes, events are lost!
- If Kafka succeeds but the database transaction rolls back, phantom events are published!

---

## 2. The Transactional Outbox Solution

Save both the Aggregate state AND the Outbox event record within the **SAME local SQL transaction**:

```
[SQL Transaction: BEGIN]
  1. INSERT INTO orders (...)
  2. INSERT INTO outbox_events (id, payload, status='PENDING')
[SQL Transaction: COMMIT]
```
A separate worker polls pending outbox records and reliably publishes them to Kafka.
""")

write_file(f"{m12}/docs/lesson.tr.md", """---
marp: true
theme: default
paginate: true
header: "DDD & Hekzagonal Mimari Masterclass | Modül 12"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Modül 12: Bağlam Eşleme ve Transactional Outbox Deseni

## Dağıtık Bounded Context'leri Güvenilir Şekilde Birbirine Bağlama

---

## 1. Çift Yazma (Dual-Write) Problemi Nedir?

Aynı işlem içinde hem SQL veritabanına yazıp hem Kafka'ya mesaj gönderirken:
- Veritabanı başarılı olup Kafka çökerse, olaylar kaybolur!
- Kafka başarılı olup veritabanı rollback olursa, hayalet olaylar yayınlanmış olur!

---

## 2. Transactional Outbox Çözümü

Aggregate durumunu ve olay kaydını **AYNI yerel SQL transaction'ı** içinde kaydedin:
```
[SQL Transaction: BAŞLAT]
  1. INSERT INTO siparisler (...)
  2. INSERT INTO outbox_olaylari (id, payload, durum='BEKLIYOR')
[SQL Transaction: COMMIT]
```
Arka plandaki bağımsız bir iş parçacığı bekleyen kayıtları Kafka'ya güvenle basar.
""")

write_file(f"{m12}/src/main/java/com/turkninja/ddd/module12/domain/OutboxRecord.java", """package com.turkninja.ddd.module12.domain;

import com.turkninja.ddd.shared.domain.ValueObject;
import java.time.Instant;
import java.util.UUID;

public record OutboxRecord(UUID id, String eventType, String payload, Instant occurredOn, boolean processed)
        implements ValueObject {

    public static OutboxRecord create(String eventType, String payload) {
        return new OutboxRecord(UUID.randomUUID(), eventType, payload, Instant.now(), false);
    }

    public OutboxRecord markProcessed() {
        return new OutboxRecord(this.id, this.eventType, this.payload, this.occurredOn, true);
    }
}
""")

write_file(f"{m12}/src/test/java/com/turkninja/ddd/module12/domain/OutboxRecordTest.java", """package com.turkninja.ddd.module12.domain;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

@DisplayName("Module 12: Transactional Outbox Tests")
class OutboxRecordTest {

    @Test
    @DisplayName("Should create outbox record and mark processed immutably")
    void testOutboxRecordLifecycle() {
        OutboxRecord initial = OutboxRecord.create("OrderCreatedEvent", "{\\"orderId\\":\\"123\\"}");
        assertThat(initial.processed()).isFalse();

        OutboxRecord processed = initial.markProcessed();
        assertThat(processed.processed()).isTrue();
        assertThat(processed.id()).isEqualTo(initial.id());
    }
}
""")

write_file(f"{m12}/src/test/java/com/turkninja/ddd/module12/architecture/Module12ArchitectureTest.java", """package com.turkninja.ddd.module12.architecture;

import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.core.importer.ImportOption;
import com.turkninja.ddd.shared.architecture.HexagonalArchitectureRules;
import org.junit.jupiter.api.Test;

class Module12ArchitectureTest {
    @Test
    void testHexagonalIsolation() {
        JavaClasses classes = new ClassFileImporter()
                .withImportOption(ImportOption.Predefined.DO_NOT_INCLUDE_TESTS)
                .importPackages("com.turkninja.ddd.module12");
        HexagonalArchitectureRules.verifyHexagonalArchitecture(classes);
    }
}
""")
write_file(f"{m12}/src/test/resources/archunit.properties", "archRule.failOnEmptyShould=false\n")
write_file(f"{m12}/exercises/README.md", "# Exercise 12: Building an Anti-Corruption Layer Translator\n")
write_file(f"{m12}/exercises/README.tr.md", "# Alıştırma 12: Yozlaşma Önleme Katmanı (ACL) Çeviricisi Geliştirme\n")
write_file(f"{m12}/solutions/README.md", "# Solution 12: Transactional Outbox & ACL Translator\n")
write_file(f"{m12}/solutions/README.tr.md", "# Çözüm 12: Transactional Outbox ve ACL Çeviricisi\n")

# ==============================================================================
# CAPSTONE: Enterprise Order & Fulfillment Platform
# ==============================================================================
cap = "capstone-order-fulfillment-platform"
write_file(f"{cap}/README.md", """# 🎓 Capstone Project: Enterprise Order & Fulfillment Platform

## 🎯 Architecture Overview
This graduation project demonstrates a complete, production-grade enterprise system featuring:
- **Two Distinct Bounded Contexts**: Ordering Context & Fulfillment Context.
- **Hexagonal Architecture**: Complete layer isolation with Driving & Driven ports.
- **Transactional Outbox Pattern**: Zero event loss between database commits and event streaming.
- **Anti-Corruption Layer (ACL)**: Clean boundary protection between bounded contexts.
- **Automated ArchUnit Test Suite**: Verification that bounded contexts do not bleed into each other.
""")

write_file(f"{cap}/README.tr.md", """# 🎓 Bitirme Projesi: Kurumsal Sipariş ve Dağıtım Platformu

## 🎯 Mimari Genel Bakış
Bu bitirme projesi, gerçek dünya standartlarında tam donanımlı kurumsal bir sistem sunar:
- **İki Bağımsız Bounded Context**: Sipariş Bağlamı (Ordering) ve Dağıtım Bağlamı (Fulfillment).
- **Hekzagonal Mimari**: Süren ve Sürülen portlarla tam katman izolasyonu.
- **Transactional Outbox Deseni**: Veritabanı ve Kafka arasında sıfır veri kaybı garantisi.
- **Yozlaşma Önleme Katmanı (ACL)**: Bounded context'ler arasında temiz sınır koruması.
- **Otomatik ArchUnit Test Paketi**: Bağlamların birbirine sızmadığını doğrulayan mimari testler.
""")

write_file(f"{cap}/docs/lesson.md", """---
marp: true
theme: default
paginate: true
header: "DDD & Hexagonal Architecture Masterclass | Capstone Project"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Capstone Project: Enterprise Order & Fulfillment Platform

## End-to-End Enterprise DDD & Hexagonal Architecture in Action

---

## 1. System Architecture

```
[REST API: PlaceOrder] ──> [OrderApplicationService] ──> [Order Aggregate Root]
                                                              │ (Emits)
                                                              ▼
                                                   [Transactional Outbox]
                                                              │ (Publish)
                                                              ▼
                                                        [Kafka Bus]
                                                              │
                                                              ▼
                                                   [Fulfillment ACL]
                                                              │
                                                              ▼
                                                  [Shipment Aggregate Root]
```
""")

write_file(f"{cap}/docs/lesson.tr.md", """---
marp: true
theme: default
paginate: true
header: "DDD & Hekzagonal Mimari Masterclass | Bitirme Projesi"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Bitirme Projesi: Kurumsal Sipariş ve Dağıtım Platformu

## Uçtan Uca Kurumsal DDD ve Hekzagonal Mimari Uygulaması

---

## 1. Sistem Mimarisi

Sipariş ve Dağıtım Bounded Context'leri, Transactional Outbox ve Anti-Corruption Layer (ACL) üzerinden tamamen gevşek bağlı (loosely coupled) şekilde haberleşir.
""")

write_file(f"{cap}/src/main/java/com/turkninja/ddd/capstone/ordering/domain/model/OrderId.java", """package com.turkninja.ddd.capstone.ordering.domain.model;

import com.turkninja.ddd.shared.domain.ValueObject;
import java.util.UUID;

public record OrderId(UUID value) implements ValueObject {
    public static OrderId generate() { return new OrderId(UUID.randomUUID()); }
}
""")

write_file(f"{cap}/src/main/java/com/turkninja/ddd/capstone/ordering/domain/model/Order.java", """package com.turkninja.ddd.capstone.ordering.domain.model;

import com.turkninja.ddd.shared.domain.AggregateRoot;
import com.turkninja.ddd.shared.domain.DomainValidationException;

import java.math.BigDecimal;
import java.util.Objects;

public class Order extends AggregateRoot<OrderId> {

    public enum Status { PENDING, CONFIRMED, CANCELLED }

    private Status status;
    private final BigDecimal totalAmount;

    public Order(OrderId id, BigDecimal totalAmount) {
        super(id);
        Objects.requireNonNull(totalAmount, "Total amount cannot be null");
        if (totalAmount.compareTo(BigDecimal.ZERO) <= 0) {
            throw new DomainValidationException("Total order amount must be positive");
        }
        this.totalAmount = totalAmount;
        this.status = Status.PENDING;
    }

    public void confirm() {
        if (this.status != Status.PENDING) {
            throw new DomainValidationException("Only pending orders can be confirmed");
        }
        this.status = Status.CONFIRMED;
    }

    public Status getStatus() { return status; }
    public BigDecimal getTotalAmount() { return totalAmount; }
}
""")

write_file(f"{cap}/src/main/java/com/turkninja/ddd/capstone/fulfillment/domain/model/ShipmentId.java", """package com.turkninja.ddd.capstone.fulfillment.domain.model;

import com.turkninja.ddd.shared.domain.ValueObject;
import java.util.UUID;

public record ShipmentId(UUID value) implements ValueObject {
    public static ShipmentId generate() { return new ShipmentId(UUID.randomUUID()); }
}
""")

write_file(f"{cap}/src/main/java/com/turkninja/ddd/capstone/fulfillment/domain/model/Shipment.java", """package com.turkninja.ddd.capstone.fulfillment.domain.model;

import com.turkninja.ddd.shared.domain.AggregateRoot;
import com.turkninja.ddd.shared.domain.DomainValidationException;

import java.util.Objects;
import java.util.UUID;

public class Shipment extends AggregateRoot<ShipmentId> {

    public enum ShipmentStatus { CREATED, DISPATCHED, DELIVERED }

    private final UUID orderId;
    private String trackingCode;
    private ShipmentStatus status;

    public Shipment(ShipmentId id, UUID orderId) {
        super(id);
        this.orderId = Objects.requireNonNull(orderId, "OrderId required");
        this.status = ShipmentStatus.CREATED;
    }

    public void dispatch(String trackingCode) {
        if (trackingCode == null || trackingCode.isBlank()) {
            throw new DomainValidationException("Tracking code required for dispatch");
        }
        this.trackingCode = trackingCode.trim();
        this.status = ShipmentStatus.DISPATCHED;
    }

    public UUID getOrderId() { return orderId; }
    public String getTrackingCode() { return trackingCode; }
    public ShipmentStatus getStatus() { return status; }
}
""")

write_file(f"{cap}/src/test/java/com/turkninja/ddd/capstone/domain/CapstoneDomainTest.java", """package com.turkninja.ddd.capstone.domain;

import com.turkninja.ddd.capstone.fulfillment.domain.model.Shipment;
import com.turkninja.ddd.capstone.fulfillment.domain.model.ShipmentId;
import com.turkninja.ddd.capstone.ordering.domain.model.Order;
import com.turkninja.ddd.capstone.ordering.domain.model.OrderId;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.math.BigDecimal;
import java.util.UUID;

import static org.assertj.core.api.Assertions.assertThat;

@DisplayName("Capstone: Ordering & Fulfillment Bounded Context Tests")
class CapstoneDomainTest {

    @Test
    @DisplayName("Ordering Aggregate enforces confirmation lifecycle")
    void testOrderConfirmation() {
        Order order = new Order(OrderId.generate(), new BigDecimal("120.00"));
        assertThat(order.getStatus()).isEqualTo(Order.Status.PENDING);

        order.confirm();
        assertThat(order.getStatus()).isEqualTo(Order.Status.CONFIRMED);
    }

    @Test
    @DisplayName("Fulfillment Aggregate enforces shipment dispatch with tracking code")
    void testShipmentDispatch() {
        UUID orderId = UUID.randomUUID();
        Shipment shipment = new Shipment(ShipmentId.generate(), orderId);

        shipment.dispatch("TRK-998877");
        assertThat(shipment.getStatus()).isEqualTo(Shipment.ShipmentStatus.DISPATCHED);
        assertThat(shipment.getTrackingCode()).isEqualTo("TRK-998877");
    }
}
""")

write_file(f"{cap}/src/test/java/com/turkninja/ddd/capstone/architecture/CapstoneArchitectureTest.java", """package com.turkninja.ddd.capstone.architecture;

import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.core.importer.ImportOption;
import com.turkninja.ddd.shared.architecture.HexagonalArchitectureRules;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static com.tngtech.archunit.lang.syntax.ArchRuleDefinition.noClasses;

@DisplayName("Capstone: Multi-Bounded Context Architectural Boundary Tests")
class CapstoneArchitectureTest {

    @Test
    @DisplayName("Ordering context must not depend on Fulfillment internal domain classes")
    void verifyBoundedContextIsolation() {
        JavaClasses classes = new ClassFileImporter()
                .withImportOption(ImportOption.Predefined.DO_NOT_INCLUDE_TESTS)
                .importPackages("com.turkninja.ddd.capstone");

        HexagonalArchitectureRules.verifyHexagonalArchitecture(classes);

        noClasses().that().resideInAPackage("..ordering..")
                .should().dependOnClassesThat().resideInAPackage("..fulfillment..")
                .allowEmptyShould(true)
                .as("Ordering Context must remain completely decoupled from Fulfillment Context.")
                .check(classes);
    }
}
""")
write_file(f"{cap}/src/test/resources/archunit.properties", "archRule.failOnEmptyShould=false\n")
write_file(f"{cap}/exercises/README.md", "# Capstone Assignment: Implementing the Anti-Corruption Layer Translator\n")
write_file(f"{cap}/exercises/README.tr.md", "# Bitirme Ödevi: Yozlaşma Önleme Katmanı (ACL) Çeviricisi Geliştirme\n")
write_file(f"{cap}/solutions/README.md", "# Capstone Solution: Full Enterprise Ordering & Fulfillment Platform\n")
write_file(f"{cap}/solutions/README.tr.md", "# Bitirme Projesi Çözümü: Tam Donanımlı Kurumsal Sipariş ve Dağıtım Platformu\n")

print("Modules 09-12 and Capstone generated successfully!")
