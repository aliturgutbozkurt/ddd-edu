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
# MODULE 03: Value Objects & Immutability with Java 27 Records
# ==============================================================================
m3 = "modules/module-03-value-objects"
write_file(f"{m3}/README.md", """# Module 03: Value Objects & Immutability with Java 27 Records

## 🎯 Learning Objectives
- Master the design of **Value Objects** according to Eric Evans and Martin Fowler.
- Eliminate **Primitive Obsession** by encapsulating domain primitives into rich types.
- Understand value equality (`equals` / `hashCode` based on attributes).
- Enforce immutability and self-validation using **Java 27 record compact constructors**.
- Implement arithmetic operations with zero side effects (pure functions returning new instances).
""")

write_file(f"{m3}/README.tr.md", """# Modül 03: Değer Nesneleri (Value Objects) ve Java 27 Record ile Değişmezlik

## 🎯 Öğrenme Hedefleri
- **Değer Nesnelerinin (Value Objects)** kurallarını derinlemesine öğrenmek.
- Çıplak String ve double kullanımından kaynaklanan **İlkel Takıntısını (Primitive Obsession)** yok etmek.
- Değer eşitliğini (özellik bazlı `equals` / `hashCode`) kavramak.
- **Java 27 record compact constructor** kullanarak kendini doğrulayan değişmez nesneler üretmek.
- Yan etkisiz (side-effect free) matematiksel işlemler yazmak.
""")

write_file(f"{m3}/docs/lesson.md", """---
marp: true
theme: default
paginate: true
header: "DDD & Hexagonal Architecture Masterclass | Module 03"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Module 03: Value Objects & Immutability with Java 27 Records

## Replacing Primitive Obsession with Pure Invariant Encapsulation

---

## 1. What Makes a Value Object?

A Value Object is defined by its attributes, NOT by an identity:
1. **No Identity**: If two Value Objects have identical fields, they are equal.
2. **Immutability**: Once constructed, its state can NEVER change.
3. **Conceptual Whole**: Represents a complete domain concept (`Money`, `EmailAddress`, `PostalAddress`).
4. **Self-Validating**: An invalid Value Object can NEVER exist in memory.
5. **Side-Effect-Free Behavior**: Methods return new instances instead of mutating existing state.

---

## 2. Eliminating Primitive Obsession

### The Anti-Pattern:
```java
// Danger: What is the currency? Can price be -500? Can tax be null?
public void processPayment(String email, double price, double tax) { ... }
```

### The Java 27 Record Solution:
```java
public record EmailAddress(String value) implements ValueObject {
    private static final Pattern PATTERN = Pattern.compile("^[A-Za-z0-9+_.-]+@(.+)$");
    public EmailAddress {
        if (value == null || !PATTERN.matcher(value).matches()) {
            throw new DomainValidationException("Invalid email format: " + value);
        }
        value = value.toLowerCase().trim();
    }
}
```
""")

write_file(f"{m3}/docs/lesson.tr.md", """---
marp: true
theme: default
paginate: true
header: "DDD & Hekzagonal Mimari Masterclass | Modül 03"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Modül 03: Değer Nesneleri ve Java 27 Record ile Değişmezlik

## İlkel Takıntısını Saf İş Değişmezleriyle Yok Etmek

---

## 1. Değer Nesnesini (Value Object) Tanımlayan Nedir?

Bir Değer Nesnesi kimliğiyle değil, öznitelikleriyle tanımlanır:
1. **Kimliksizdir**: İki nesnenin tüm alanları eşitse nesneler eşittir.
2. **Değişmezdir (Immutable)**: Oluşturulduktan sonra durumu asla değiştirilemez.
3. **Kavramsal Bütündür**: Tek başına anlamlı bir domain kavramıdır (`Money`, `EmailAddress`).
4. **Kendini Doğrular**: Bellekte asla geçersiz bir değer nesnesi var olamaz.
5. **Yan Etkisiz Davranış**: Metotlar var olan durumu değiştirmek yerine daima YENİ bir örnek döndürür.
""")

write_file(f"{m3}/src/main/java/com/turkninja/ddd/module03/domain/model/EmailAddress.java", """package com.turkninja.ddd.module03.domain.model;

import com.turkninja.ddd.shared.domain.DomainValidationException;
import com.turkninja.ddd.shared.domain.ValueObject;

import java.util.regex.Pattern;

public record EmailAddress(String value) implements ValueObject {
    private static final Pattern EMAIL_PATTERN = Pattern.compile("^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+$");

    public EmailAddress {
        if (value == null || !EMAIL_PATTERN.matcher(value).matches()) {
            throw new DomainValidationException("Invalid email address format: " + value);
        }
        value = value.toLowerCase().trim();
    }
}
""")

write_file(f"{m3}/src/main/java/com/turkninja/ddd/module03/domain/model/Iban.java", """package com.turkninja.ddd.module03.domain.model;

import com.turkninja.ddd.shared.domain.DomainValidationException;
import com.turkninja.ddd.shared.domain.ValueObject;

public record Iban(String value) implements ValueObject {
    public Iban {
        if (value == null || value.replaceAll("\\\\s+", "").length() < 15) {
            throw new DomainValidationException("Invalid IBAN length. Given: " + value);
        }
        value = value.replaceAll("\\\\s+", "").toUpperCase();
    }
}
""")

write_file(f"{m3}/src/test/java/com/turkninja/ddd/module03/domain/ValueObjectTest.java", """package com.turkninja.ddd.module03.domain;

import com.turkninja.ddd.module03.domain.model.EmailAddress;
import com.turkninja.ddd.module03.domain.model.Iban;
import com.turkninja.ddd.shared.domain.DomainValidationException;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

@DisplayName("Module 03: Value Objects Invariant Test")
class ValueObjectTest {

    @Test
    @DisplayName("Should normalize and validate email address")
    void testEmailValidation() {
        EmailAddress email1 = new EmailAddress("User@Example.COM");
        EmailAddress email2 = new EmailAddress("user@example.com");

        assertThat(email1.value()).isEqualTo("user@example.com");
        assertThat(email1).isEqualTo(email2);
    }

    @Test
    @DisplayName("Should reject invalid email format")
    void testInvalidEmail() {
        assertThatThrownBy(() -> new EmailAddress("invalid-email"))
                .isInstanceOf(DomainValidationException.class);
    }

    @Test
    @DisplayName("Should sanitize IBAN spacing and normalize")
    void testIbanNormalization() {
        Iban iban = new Iban("TR33 0006 1005 1234 5678 9012 34");
        assertThat(iban.value()).isEqualTo("TR330006100512345678901234");
    }
}
""")

write_file(f"{m3}/src/test/java/com/turkninja/ddd/module03/architecture/Module03ArchitectureTest.java", """package com.turkninja.ddd.module03.architecture;

import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.core.importer.ImportOption;
import com.turkninja.ddd.shared.architecture.HexagonalArchitectureRules;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

@DisplayName("Module 03: ArchUnit Architecture Verification")
class Module03ArchitectureTest {
    @Test
    void testHexagonalIsolation() {
        JavaClasses classes = new ClassFileImporter()
                .withImportOption(ImportOption.Predefined.DO_NOT_INCLUDE_TESTS)
                .importPackages("com.turkninja.ddd.module03");
        HexagonalArchitectureRules.verifyHexagonalArchitecture(classes);
    }
}
""")
write_file(f"{m3}/src/test/resources/archunit.properties", "archRule.failOnEmptyShould=false\n")
write_file(f"{m3}/exercises/README.md", "# Exercise 03: Implementing TaxNumber and PostalAddress Value Objects\n")
write_file(f"{m3}/exercises/README.tr.md", "# Alıştırma 03: Vergi Numarası ve Posta Adresi Değer Nesnelerini Kodlama\n")
write_file(f"{m3}/solutions/README.md", "# Solution 03: Value Objects with Compact Constructors\n")
write_file(f"{m3}/solutions/README.tr.md", "# Çözüm 03: Compact Constructor ile Değer Nesneleri\n")

# ==============================================================================
# MODULE 04: Entities, Identity & Lifecycle
# ==============================================================================
m4 = "modules/module-04-entities-and-identity"
write_file(f"{m4}/README.md", """# Module 04: Entities, Identity & Lifecycle in Domain Models

## 🎯 Learning Objectives
- Understand why **Entities** are defined by **Identity**, not attributes.
- Master Identity generation strategies: **UUID v7 (time-ordered)** vs natural business keys.
- Prevent state corruption by eliminating public setters and providing intention-revealing methods.
- Implement `equals()` and `hashCode()` strictly based on entity identity.
""")

write_file(f"{m4}/README.tr.md", """# Modül 04: Varlıklar (Entities), Kimlik ve Yaşam Döngüsü

## 🎯 Öğrenme Hedefleri
- **Varlıkların (Entities)** öznitelikleriyle değil, **Kimlikleriyle (Identity)** tanımlandığını öğrenmek.
- Kimlik oluşturma stratejilerini (zaman sıralı **UUID v7** ve doğal iş anahtarları) kavramak.
- Genel setter'ları kaldırıp niyet bildiren (intention-revealing) iş metotları yazarak veri bütünlüğünü korumak.
- `equals()` ve `hashCode()` metotlarını yalnızca kimlik üzerinden yapılandırmak.
""")

write_file(f"{m4}/docs/lesson.md", """---
marp: true
theme: default
paginate: true
header: "DDD & Hexagonal Architecture Masterclass | Module 04"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Module 04: Entities, Identity & Lifecycle in Domain Models

## Preserving Continuity and Encapsulating State Changes

---

## 1. What is an Entity?

An Entity represents an individual business object that has **thread of continuity** and identity over time:
- Even if all attributes change (name, address, email), the customer remains the SAME customer.
- Two customers with identical names and birthdates are NOT the same customer if their `CustomerId` differs.

---

## 2. Equality by Identity

```java
public abstract class DomainEntity<ID extends ValueObject> {
    protected final ID id;
    
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        DomainEntity<?> that = (DomainEntity<?>) o;
        return Objects.equals(id, that.id);
    }
}
```
""")

write_file(f"{m4}/docs/lesson.tr.md", """---
marp: true
theme: default
paginate: true
header: "DDD & Hekzagonal Mimari Masterclass | Modül 04"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Modül 04: Varlıklar, Kimlik ve Yaşam Döngüsü

## Sürekliliği Korumak ve Durum Değişikliklerini Kapsüllemek

---

## 1. Varlık (Entity) Nedir?

Varlık, zaman içinde sürekliliği olan ve **kimliğiyle (identity)** ayırt edilen bir domain nesnesidir:
- Bir müşterinin adı, adresi veya e-postası değişse bile aynı müşteri olmaya devam eder.
- Aynı isme ve doğum tarihine sahip iki kişi, müşteri numaraları (`CustomerId`) farklıysa farklı varlıklardır.
""")

write_file(f"{m4}/src/main/java/com/turkninja/ddd/module04/domain/model/CustomerId.java", """package com.turkninja.ddd.module04.domain.model;

import com.turkninja.ddd.shared.domain.DomainValidationException;
import com.turkninja.ddd.shared.domain.ValueObject;

import java.util.UUID;

public record CustomerId(UUID value) implements ValueObject {
    public CustomerId {
        if (value == null) {
            throw new DomainValidationException("CustomerId cannot be null");
        }
    }

    public static CustomerId generate() {
        return new CustomerId(UUID.randomUUID());
    }
}
""")

write_file(f"{m4}/src/main/java/com/turkninja/ddd/module04/domain/model/CustomerTier.java", """package com.turkninja.ddd.module04.domain.model;

public enum CustomerTier {
    STANDARD, SILVER, GOLD, PLATINUM
}
""")

write_file(f"{m4}/src/main/java/com/turkninja/ddd/module04/domain/model/Customer.java", """package com.turkninja.ddd.module04.domain.model;

import com.turkninja.ddd.shared.domain.DomainEntity;
import com.turkninja.ddd.shared.domain.DomainValidationException;

import java.util.Objects;

public class Customer extends DomainEntity<CustomerId> {
    private String fullName;
    private String email;
    private CustomerTier tier;

    public Customer(CustomerId id, String fullName, String email) {
        super(id);
        updateContactDetails(fullName, email);
        this.tier = CustomerTier.STANDARD;
    }

    public void updateContactDetails(String fullName, String email) {
        if (fullName == null || fullName.isBlank()) {
            throw new DomainValidationException("Customer name cannot be blank");
        }
        if (email == null || !email.contains("@")) {
            throw new DomainValidationException("Invalid customer email: " + email);
        }
        this.fullName = fullName.trim();
        this.email = email.trim().toLowerCase();
    }

    public void upgradeTier(CustomerTier newTier) {
        Objects.requireNonNull(newTier, "Tier cannot be null");
        if (newTier.ordinal() < this.tier.ordinal()) {
            throw new DomainValidationException("Cannot downgrade tier directly: " + this.tier + " -> " + newTier);
        }
        this.tier = newTier;
    }

    public String getFullName() { return fullName; }
    public String getEmail() { return email; }
    public CustomerTier getTier() { return tier; }
}
""")

write_file(f"{m4}/src/test/java/com/turkninja/ddd/module04/domain/CustomerEntityTest.java", """package com.turkninja.ddd.module04.domain;

import com.turkninja.ddd.module04.domain.model.Customer;
import com.turkninja.ddd.module04.domain.model.CustomerId;
import com.turkninja.ddd.module04.domain.model.CustomerTier;
import com.turkninja.ddd.shared.domain.DomainValidationException;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

@DisplayName("Module 04: Customer Entity & Identity Tests")
class CustomerEntityTest {

    @Test
    @DisplayName("Two customer instances with same CustomerId are equal regardless of attributes")
    void testIdentityEquality() {
        CustomerId id = CustomerId.generate();
        Customer c1 = new Customer(id, "Alice Smith", "alice@example.com");
        Customer c2 = new Customer(id, "Alice Jones", "alice.new@example.com");

        assertThat(c1).isEqualTo(c2);
        assertThat(c1.hashCode()).isEqualTo(c2.hashCode());
    }

    @Test
    @DisplayName("Should prevent tier downgrade invariant violation")
    void testTierUpgradeInvariant() {
        Customer c = new Customer(CustomerId.generate(), "Bob", "bob@example.com");
        c.upgradeTier(CustomerTier.GOLD);

        assertThatThrownBy(() -> c.upgradeTier(CustomerTier.SILVER))
                .isInstanceOf(DomainValidationException.class)
                .hasMessageContaining("Cannot downgrade tier directly");
    }
}
""")

write_file(f"{m4}/src/test/java/com/turkninja/ddd/module04/architecture/Module04ArchitectureTest.java", """package com.turkninja.ddd.module04.architecture;

import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.core.importer.ImportOption;
import com.turkninja.ddd.shared.architecture.HexagonalArchitectureRules;
import org.junit.jupiter.api.Test;

class Module04ArchitectureTest {
    @Test
    void testHexagonalIsolation() {
        JavaClasses classes = new ClassFileImporter()
                .withImportOption(ImportOption.Predefined.DO_NOT_INCLUDE_TESTS)
                .importPackages("com.turkninja.ddd.module04");
        HexagonalArchitectureRules.verifyHexagonalArchitecture(classes);
    }
}
""")
write_file(f"{m4}/src/test/resources/archunit.properties", "archRule.failOnEmptyShould=false\n")
write_file(f"{m4}/exercises/README.md", "# Exercise 04: Implementing Natural Identity and Lifecycle Mutations\n")
write_file(f"{m4}/exercises/README.tr.md", "# Alıştırma 04: Doğal Kimlik ve Yaşam Döngüsü Mutasyonları\n")
write_file(f"{m4}/solutions/README.md", "# Solution 04: Encapsulated Entity Lifecycle\n")
write_file(f"{m4}/solutions/README.tr.md", "# Çözüm 04: Kapsüllenmiş Varlık Yaşam Döngüsü\n")

# ==============================================================================
# MODULE 05: Aggregates, Aggregate Roots & Domain Invariants
# ==============================================================================
m5 = "modules/module-05-aggregates-and-invariants"
write_file(f"{m5}/README.md", """# Module 05: Aggregates, Aggregate Roots & Domain Invariants

## 🎯 Learning Objectives
- Master the **Aggregate Pattern** as a transactional consistency boundary.
- Encapsulate child entities (`OrderItem`) inside the **Aggregate Root** (`Order`).
- Guard multi-entity business invariants (e.g. maximum item count, total price calculation).
- Prevent reference leakage by returning unmodifiable collections.
""")

write_file(f"{m5}/README.tr.md", """# Modül 05: Aggregate Kökleri ve Domain Değişmezleri (Invariants)

## 🎯 Öğrenme Hedefleri
- **Aggregate Desenini** işlemsel tutarlılık sınırı (consistency boundary) olarak kavramak.
- Alt varlıkları (`OrderItem`) yalnızca **Aggregate Kökü (`Order`)** üzerinden yönetmek.
- Çoklu varlık iş değişmezlerini (ör. maksimum kalem sayısı, toplam tutar hesaplaması) korumak.
- Savunmacı kopyalama (unmodifiable collections) ile referans sızıntılarını engellemek.
""")

write_file(f"{m5}/docs/lesson.md", """---
marp: true
theme: default
paginate: true
header: "DDD & Hexagonal Architecture Masterclass | Module 05"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Module 05: Aggregates, Aggregate Roots & Domain Invariants

## Designing Transactional Boundaries and Enforcing Business Invariants

---

## 1. What is an Aggregate?

An Aggregate is a cluster of associated objects (Entities and Value Objects) that we treat as a unit for the purpose of data changes:
- **Aggregate Root**: The single entry point to the aggregate. Outside objects can ONLY hold a reference to the root.
- **Consistency Boundary**: All invariants inside the aggregate must be satisfied at the end of every transaction.
- **Rule of Thumb**: Keep aggregates small! Reference other aggregates by **ID only**, never by object reference.
""")

write_file(f"{m5}/docs/lesson.tr.md", """---
marp: true
theme: default
paginate: true
header: "DDD & Hekzagonal Mimari Masterclass | Modül 05"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Modül 05: Aggregate Kökleri ve Domain Değişmezleri

## İşlemsel Tutarlılık Sınırları ve İş Değişmezlerini Koruma

---

## 1. Aggregate Nedir?

Aggregate, veri değişiklikleri açısından tek bir birim olarak ele alınan ilişkili nesneler (Varlıklar ve Değer Nesneleri) kümesidir:
- **Aggregate Kökü (Root)**: Kümeye tek erişim noktasıdır. Dış nesneler yalnızca kökün referansını tutabilir.
- **Tutarlılık Sınırı**: Her veritabanı işlemi sonunda aggregate içindeki tüm iş kuralları tam olarak sağlanmış olmalıdır.
- **Altın Kural**: Aggregateleri küçük tutun! Diğer aggregatelere nesne referansıyla değil, **yalnızca ID ile** bağlanın.
""")

write_file(f"{m5}/src/main/java/com/turkninja/ddd/module05/domain/model/OrderId.java", """package com.turkninja.ddd.module05.domain.model;

import com.turkninja.ddd.shared.domain.DomainValidationException;
import com.turkninja.ddd.shared.domain.ValueObject;

import java.util.UUID;

public record OrderId(UUID value) implements ValueObject {
    public OrderId {
        if (value == null) throw new DomainValidationException("OrderId cannot be null");
    }

    public static OrderId generate() {
        return new OrderId(UUID.randomUUID());
    }
}
""")

write_file(f"{m5}/src/main/java/com/turkninja/ddd/module05/domain/model/OrderItem.java", """package com.turkninja.ddd.module05.domain.model;

import com.turkninja.ddd.shared.domain.DomainEntity;
import com.turkninja.ddd.shared.domain.DomainValidationException;
import com.turkninja.ddd.shared.domain.ValueObject;

import java.math.BigDecimal;
import java.util.UUID;

public class OrderItem extends DomainEntity<OrderItem.OrderItemId> {

    public record OrderItemId(UUID value) implements ValueObject {}

    private final String productId;
    private final int quantity;
    private final BigDecimal unitPrice;

    OrderItem(String productId, int quantity, BigDecimal unitPrice) {
        super(new OrderItemId(UUID.randomUUID()));
        if (productId == null || productId.isBlank()) throw new DomainValidationException("ProductId required");
        if (quantity <= 0) throw new DomainValidationException("Quantity must be positive");
        if (unitPrice == null || unitPrice.compareTo(BigDecimal.ZERO) <= 0) throw new DomainValidationException("UnitPrice must be positive");
        this.productId = productId;
        this.quantity = quantity;
        this.unitPrice = unitPrice;
    }

    public BigDecimal subtotal() {
        return unitPrice.multiply(BigDecimal.valueOf(quantity));
    }

    public String getProductId() { return productId; }
    public int getQuantity() { return quantity; }
    public BigDecimal getUnitPrice() { return unitPrice; }
}
""")

write_file(f"{m5}/src/main/java/com/turkninja/ddd/module05/domain/model/Order.java", """package com.turkninja.ddd.module05.domain.model;

import com.turkninja.ddd.shared.domain.AggregateRoot;
import com.turkninja.ddd.shared.domain.DomainValidationException;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Order extends AggregateRoot<OrderId> {

    public enum Status { PENDING, CONFIRMED, CANCELLED }

    private final List<OrderItem> items = new ArrayList<>();
    private Status status;

    public Order(OrderId id) {
        super(id);
        this.status = Status.PENDING;
    }

    public void addItem(String productId, int quantity, BigDecimal unitPrice) {
        if (status != Status.PENDING) {
            throw new DomainValidationException("Cannot add items to an order in status: " + status);
        }
        if (items.size() >= 50) {
            throw new DomainValidationException("Order cannot exceed 50 line items");
        }
        items.add(new OrderItem(productId, quantity, unitPrice));
    }

    public void confirm() {
        if (items.isEmpty()) {
            throw new DomainValidationException("Cannot confirm an empty order");
        }
        if (status != Status.PENDING) {
            throw new DomainValidationException("Only pending orders can be confirmed");
        }
        this.status = Status.CONFIRMED;
    }

    public BigDecimal calculateTotal() {
        return items.stream()
                .map(OrderItem::subtotal)
                .reduce(BigDecimal.ZERO, BigDecimal::add);
    }

    public List<OrderItem> getItems() {
        return Collections.unmodifiableList(items);
    }

    public Status getStatus() { return status; }
}
""")

write_file(f"{m5}/src/test/java/com/turkninja/ddd/module05/domain/OrderAggregateTest.java", """package com.turkninja.ddd.module05.domain;

import com.turkninja.ddd.module05.domain.model.Order;
import com.turkninja.ddd.module05.domain.model.OrderId;
import com.turkninja.ddd.shared.domain.DomainValidationException;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.math.BigDecimal;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

@DisplayName("Module 05: Order Aggregate & Consistency Boundary Tests")
class OrderAggregateTest {

    @Test
    @DisplayName("Should correctly calculate order total from line items")
    void testOrderTotalCalculation() {
        Order order = new Order(OrderId.generate());
        order.addItem("PROD-001", 2, new BigDecimal("25.00")); // 50.00
        order.addItem("PROD-002", 1, new BigDecimal("30.00")); // 30.00

        assertThat(order.calculateTotal()).isEqualTo(new BigDecimal("80.00"));
        assertThat(order.getItems()).hasSize(2);
    }

    @Test
    @DisplayName("Should prevent confirming an empty order")
    void testEmptyOrderConfirmation() {
        Order order = new Order(OrderId.generate());

        assertThatThrownBy(order::confirm)
                .isInstanceOf(DomainValidationException.class)
                .hasMessageContaining("Cannot confirm an empty order");
    }

    @Test
    @DisplayName("Should reject adding items to a confirmed order")
    void testAddingItemsToConfirmedOrder() {
        Order order = new Order(OrderId.generate());
        order.addItem("PROD-001", 1, new BigDecimal("10.00"));
        order.confirm();

        assertThatThrownBy(() -> order.addItem("PROD-002", 1, new BigDecimal("20.00")))
                .isInstanceOf(DomainValidationException.class)
                .hasMessageContaining("Cannot add items to an order in status: CONFIRMED");
    }
}
""")

write_file(f"{m5}/src/test/java/com/turkninja/ddd/module05/architecture/Module05ArchitectureTest.java", """package com.turkninja.ddd.module05.architecture;

import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.core.importer.ImportOption;
import com.turkninja.ddd.shared.architecture.HexagonalArchitectureRules;
import org.junit.jupiter.api.Test;

class Module05ArchitectureTest {
    @Test
    void testHexagonalIsolation() {
        JavaClasses classes = new ClassFileImporter()
                .withImportOption(ImportOption.Predefined.DO_NOT_INCLUDE_TESTS)
                .importPackages("com.turkninja.ddd.module05");
        HexagonalArchitectureRules.verifyHexagonalArchitecture(classes);
    }
}
""")
write_file(f"{m5}/src/test/resources/archunit.properties", "archRule.failOnEmptyShould=false\n")
write_file(f"{m5}/exercises/README.md", "# Exercise 05: Aggregate Invariant on Maximum Total Order Limit\n")
write_file(f"{m5}/exercises/README.tr.md", "# Alıştırma 05: Maksimum Sipariş Tutarı Aggregate Değişmezi\n")
write_file(f"{m5}/solutions/README.md", "# Solution 05: Aggregate Invariant Enforcement\n")
write_file(f"{m5}/solutions/README.tr.md", "# Çözüm 05: Aggregate Değişmezlerinin Korunması\n")

print("Modules 03, 04, 05 generated successfully!")
