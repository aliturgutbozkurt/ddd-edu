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
# MODULE 02: Hexagonal Architecture Blueprint & Ports/Adapters
# ==============================================================================
m2_dir = "modules/module-02-hexagonal-architecture"

write_file(f"{m2_dir}/README.md", """# Module 02: Hexagonal Architecture Blueprint & Ports/Adapters Decoupling

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
""")

write_file(f"{m2_dir}/README.tr.md", """# Modül 02: Hekzagonal Mimari Taslağı ve Port/Adaptör Ayrıştırması

## 🎯 Öğrenme Hedefleri
- Alistair Cockburn'ün **Hekzagonal Mimari (Ports and Adapters)** desenini derinlemesine öğrenmek.
- Kurumsal katmanlara uygulanan **Bağımlılık Tersine Çevirme İlkesini (DIP)** kavramak.
- **Süren Portlar (Inbound/Driving)** ile **Sürülen Portlar (Outbound/Driven)** arasındaki farkları netleştirmek.
- Temiz bir dört katmanlı paket mimarisi kurmak (`domain`, `application`, `infrastructure`).
- Hekzagonal sınırları **ArchUnit** testleriyle otomasyona bağlamak.
""")

write_file(f"{m2_dir}/docs/lesson.md", """---
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
""")

write_file(f"{m2_dir}/docs/lesson.tr.md", """---
marp: true
theme: default
paginate: true
header: "DDD & Hekzagonal Mimari Masterclass | Modül 02"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Modül 02: Hekzagonal Mimari (Ports and Adapters) Taslağı

## Uzun Ömürlü Yazılımlar İçin Bağımlılıkları Tersine Çevirme

---

## 1. Geleneksel Katmanlı Mimarinin Sorunları

Klasik 3 katmanlı mimari (Controller -> Service -> DAO/Repository), yazılımcıyı veritabanı merkezli düşünmeye zorlar:

```
[UI / Controller] ──> [İş Servisi] ──> [Veritabanı / JPA Varlığı]
```

### Tehlikeler:
1. **Veritabanı Bağımlılığı**: Domain modelleri veritabanı tablolarının anlamsız aynalarına dönüşür (`@Entity`, `@Table`).
2. **Framework Sızıntısı**: Spring anotasyonları (`@Service`, `@Autowired`) iş kurallarını kirletir.
3. **Zor Test Edilebilirlik**: İş kuralını test etmek için veritabanı mocklamak veya Spring ayağa kaldırmak gerekir.

---

## 2. Hekzagonal Çözüm (Alistair Cockburn)

Hekzagonal mimari, **Saf Domain Çekirdeğini** merkeze yerleştirir. Dış dünya ile iletişim yalnızca **Portlar** üzerinden gerçekleşir:

```
[Süren Adaptör: REST / CLI]
           │
           ▼
[Gelen Port: Use Case Arayüzü]
           │
           ▼
[Uygulama Servisi] ──> [Domain Modeli]
           │
           ▼
[Giden Port: SPI Arayüzü]
           ▲
           │
[Sürülen Adaptör: PostgreSQL / Kafka]
```

### Temel Kural:
**Bağımlılıklar daima içe doğru işaret eder.** Domain dış dünyadan tamamen habersizdir.
""")

# Java Code for Module 02
write_file(f"{m2_dir}/src/main/java/com/turkninja/ddd/module02/domain/model/ProductId.java", """package com.turkninja.ddd.module02.domain.model;

import com.turkninja.ddd.shared.domain.DomainValidationException;
import com.turkninja.ddd.shared.domain.ValueObject;

import java.util.UUID;

public record ProductId(UUID value) implements ValueObject {
    public ProductId {
        if (value == null) {
            throw new DomainValidationException("ProductId cannot be null");
        }
    }

    public static ProductId generate() {
        return new ProductId(UUID.randomUUID());
    }
}
""")

write_file(f"{m2_dir}/src/main/java/com/turkninja/ddd/module02/domain/model/ProductPrice.java", """package com.turkninja.ddd.module02.domain.model;

import com.turkninja.ddd.shared.domain.DomainValidationException;
import com.turkninja.ddd.shared.domain.ValueObject;

import java.math.BigDecimal;
import java.util.Objects;

public record ProductPrice(BigDecimal amount, String currency) implements ValueObject {
    public ProductPrice {
        Objects.requireNonNull(amount, "Price amount must not be null");
        Objects.requireNonNull(currency, "Currency must not be null");
        if (amount.compareTo(BigDecimal.ZERO) < 0) {
            throw new DomainValidationException("Product price cannot be negative: " + amount);
        }
    }

    public static ProductPrice of(double amount, String currency) {
        return new ProductPrice(BigDecimal.valueOf(amount), currency);
    }
}
""")

write_file(f"{m2_dir}/src/main/java/com/turkninja/ddd/module02/domain/model/Product.java", """package com.turkninja.ddd.module02.domain.model;

import com.turkninja.ddd.shared.domain.AggregateRoot;
import com.turkninja.ddd.shared.domain.DomainValidationException;

import java.util.Objects;

public class Product extends AggregateRoot<ProductId> {
    private String name;
    private ProductPrice price;
    private boolean active;

    public Product(ProductId id, String name, ProductPrice price) {
        super(id);
        setName(name);
        this.price = Objects.requireNonNull(price, "Price cannot be null");
        this.active = true;
    }

    public void updatePrice(ProductPrice newPrice) {
        this.price = Objects.requireNonNull(newPrice, "New price cannot be null");
    }

    public void deactivate() {
        this.active = false;
    }

    private void setName(String name) {
        if (name == null || name.isBlank()) {
            throw new DomainValidationException("Product name cannot be empty");
        }
        this.name = name.trim();
    }

    public String getName() { return name; }
    public ProductPrice getPrice() { return price; }
    public boolean isActive() { return active; }
}
""")

# Inbound & Outbound Ports
write_file(f"{m2_dir}/src/main/java/com/turkninja/ddd/module02/application/port/in/RegisterProductUseCase.java", """package com.turkninja.ddd.module02.application.port.in;

import com.turkninja.ddd.module02.domain.model.ProductId;
import com.turkninja.ddd.module02.domain.model.ProductPrice;

public interface RegisterProductUseCase {
    ProductId registerProduct(RegisterProductCommand command);

    record RegisterProductCommand(String name, ProductPrice price) {}
}
""")

write_file(f"{m2_dir}/src/main/java/com/turkninja/ddd/module02/application/port/out/ProductRepositoryPort.java", """package com.turkninja.ddd.module02.application.port.out;

import com.turkninja.ddd.module02.domain.model.Product;
import com.turkninja.ddd.module02.domain.model.ProductId;

import java.util.Optional;

public interface ProductRepositoryPort {
    void save(Product product);
    Optional<Product> findById(ProductId id);
}
""")

# Application Service
write_file(f"{m2_dir}/src/main/java/com/turkninja/ddd/module02/application/service/ProductApplicationService.java", """package com.turkninja.ddd.module02.application.service;

import com.turkninja.ddd.module02.application.port.in.RegisterProductUseCase;
import com.turkninja.ddd.module02.application.port.out.ProductRepositoryPort;
import com.turkninja.ddd.module02.domain.model.Product;
import com.turkninja.ddd.module02.domain.model.ProductId;

import java.util.Objects;

public class ProductApplicationService implements RegisterProductUseCase {

    private final ProductRepositoryPort repositoryPort;

    public ProductApplicationService(ProductRepositoryPort repositoryPort) {
        this.repositoryPort = Objects.requireNonNull(repositoryPort);
    }

    @Override
    public ProductId registerProduct(RegisterProductCommand command) {
        ProductId id = ProductId.generate();
        Product product = new Product(id, command.name(), command.price());
        repositoryPort.save(product);
        return id;
    }
}
""")

# Driven Adapter (In-Memory Repository)
write_file(f"{m2_dir}/src/main/java/com/turkninja/ddd/module02/infrastructure/adapter/output/persistence/InMemoryProductRepositoryAdapter.java", """package com.turkninja.ddd.module02.infrastructure.adapter.output.persistence;

import com.turkninja.ddd.module02.application.port.out.ProductRepositoryPort;
import com.turkninja.ddd.module02.domain.model.Product;
import com.turkninja.ddd.module02.domain.model.ProductId;

import java.util.Map;
import java.util.Optional;
import java.util.concurrent.ConcurrentHashMap;

public class InMemoryProductRepositoryAdapter implements ProductRepositoryPort {

    private final Map<ProductId, Product> store = new ConcurrentHashMap<>();

    @Override
    public void save(Product product) {
        store.put(product.getId(), product);
    }

    @Override
    public Optional<Product> findById(ProductId id) {
        return Optional.ofNullable(store.get(id));
    }
}
""")

# Tests
write_file(f"{m2_dir}/src/test/java/com/turkninja/ddd/module02/domain/ProductTest.java", """package com.turkninja.ddd.module02.domain;

import com.turkninja.ddd.module02.domain.model.Product;
import com.turkninja.ddd.module02.domain.model.ProductId;
import com.turkninja.ddd.module02.domain.model.ProductPrice;
import com.turkninja.ddd.shared.domain.DomainValidationException;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

@DisplayName("Module 02: Product Aggregate & Port Tests")
class ProductTest {

    @Test
    @DisplayName("Should successfully create product with valid invariant checks")
    void shouldCreateProduct() {
        ProductId id = ProductId.generate();
        Product product = new Product(id, "Domain Driven Design Book", ProductPrice.of(49.99, "USD"));

        assertThat(product.getId()).isEqualTo(id);
        assertThat(product.getName()).isEqualTo("Domain Driven Design Book");
        assertThat(product.isActive()).isTrue();
    }

    @Test
    @DisplayName("Should reject blank product name")
    void shouldRejectBlankName() {
        assertThatThrownBy(() -> new Product(ProductId.generate(), "   ", ProductPrice.of(10.0, "USD")))
                .isInstanceOf(DomainValidationException.class)
                .hasMessageContaining("Product name cannot be empty");
    }
}
""")

write_file(f"{m2_dir}/src/test/java/com/turkninja/ddd/module02/architecture/Module02ArchitectureTest.java", """package com.turkninja.ddd.module02.architecture;

import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.core.importer.ImportOption;
import com.turkninja.ddd.shared.architecture.HexagonalArchitectureRules;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

@DisplayName("Module 02: ArchUnit Hexagonal Rule Verification")
class Module02ArchitectureTest {

    @Test
    @DisplayName("Module 02 must strictly obey Hexagonal layer dependencies")
    void verifyHexagonalRules() {
        JavaClasses classes = new ClassFileImporter()
                .withImportOption(ImportOption.Predefined.DO_NOT_INCLUDE_TESTS)
                .importPackages("com.turkninja.ddd.module02");

        HexagonalArchitectureRules.verifyHexagonalArchitecture(classes);
    }
}
""")

write_file(f"{m2_dir}/src/test/resources/archunit.properties", "archRule.failOnEmptyShould=false\n")

# Exercises & Solutions
write_file(f"{m2_dir}/exercises/README.md", """# Exercise 02: Refactoring Monolithic Catalog to Hexagonal Inbound Ports

## Objective
Refactor the provided procedural order pricing service to use an Inbound Port (`CalculateOrderDiscountUseCase`) and an Outbound Port (`DiscountPolicyPort`).
""")

write_file(f"{m2_dir}/exercises/README.tr.md", """# Alıştırma 02: Monolitik Katalog Kodunu Hekzagonal Portlara Dönüştürme

## Hedef
Verilen prosedürel sipariş indirim servisini bir Gelen Port (`CalculateOrderDiscountUseCase`) ve bir Giden Port (`DiscountPolicyPort`) kullanarak hekzagonal mimariye refactor edin.
""")

write_file(f"{m2_dir}/solutions/README.md", """# Solution 02: Hexagonal Decoupling & Inverted Dependencies

## Architectural Review
In this solution, the discount policy calculation is isolated behind a pure Java interface (`DiscountPolicyPort`), allowing diverse implementations (e.g. VIP discount, seasonal discount) without mutating domain logic.
""")

write_file(f"{m2_dir}/solutions/README.tr.md", """# Çözüm 02: Hekzagonal Ayrıştırma ve Tersine Çevrilmiş Bağımlılıklar

## Mimari İnceleme
Bu çözümde, indirim politikası hesaplaması saf bir Java arayüzü (`DiscountPolicyPort`) arkasında soyutlanmış ve domain mantığı bozulmadan esnek kural adaptörleri uygulanabilir hale getirilmiştir.
""")

print("Module 02 scaffolded successfully.")
