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
# MODULE 02: Exercise & Solution
# ==============================================================================
m2 = "modules/module-02-hexagonal-architecture"

write_file(f"{m2}/exercises/README.md", """# Exercise 02: Refactoring Monolithic Discount Logic to Hexagonal Ports

## 🎯 Business Context
The marketing department wants to apply dynamic discount policies to products. Currently, discounts are hard-coded in an old static utility class.

## 📋 Acceptance Criteria
1. Define an Inbound Port: `CalculateDiscountUseCase` with method `Money applyDiscount(ProductId id, CustomerTier tier)`.
2. Define an Outbound Port: `DiscountPolicyPort` with method `BigDecimal getDiscountPercentage(CustomerTier tier)`.
3. Implement an Application Service implementing the Inbound Port and consuming the Outbound Port.
4. Implement two driven adapters: `StandardDiscountPolicyAdapter` (0% discount) and `VipDiscountPolicyAdapter` (15% discount).
5. All domain logic must remain pure Java without framework dependencies.
""")

write_file(f"{m2}/exercises/README.tr.md", """# Alıştırma 02: Monolitik İndirim Mantığını Hekzagonal Portlara Dönüştürme

## 🎯 İş Bağlamı
Pazarlama departmanı ürünlere dinamik indirim politikaları uygulamak istiyor. Şu anda indirimler eski statik bir sınıfta sabit kodlanmış durumda.

## 📋 Kabul Kriterleri
1. Gelen Port tanımlayın: `CalculateDiscountUseCase` (`Money applyDiscount(ProductId id, CustomerTier tier)`).
2. Giden Port tanımlayın: `DiscountPolicyPort` (`BigDecimal getDiscountPercentage(CustomerTier tier)`).
3. Gelen Portu uygulayan ve Giden Portu kullanan bir Uygulama Servisi yazın.
4. İki sürülen adaptör yazın: `StandardDiscountPolicyAdapter` (%0 indirim) ve `VipDiscountPolicyAdapter` (%15 indirim).
5. Domain mantığı kesinlikle saf Java kalmalı, framework bağımlılığı içermemelidir.
""")

# Exercise test scaffold with @Disabled
write_file(f"{m2}/src/test/java/com/turkninja/ddd/module02/exercise/DiscountExerciseTest.java", """package com.turkninja.ddd.module02.exercise;

import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.fail;

@DisplayName("Exercise 02: Hexagonal Discount Port Refactoring")
class DiscountExerciseTest {

    @Test
    @Disabled("Remove @Disabled when you begin implementing Exercise 02")
    @DisplayName("Should apply VIP discount via decoupled outbound port")
    void testVipDiscountPolicy() {
        fail("TODO: Implement CalculateDiscountUseCase and verify 15% VIP discount");
    }
}
""")

# Solution implementation
write_file(f"{m2}/src/main/java/com/turkninja/ddd/module02/solution/DiscountPolicyPort.java", """package com.turkninja.ddd.module02.solution;

import java.math.BigDecimal;

public interface DiscountPolicyPort {
    BigDecimal getDiscountPercentage(String customerTier);
}
""")

write_file(f"{m2}/src/main/java/com/turkninja/ddd/module02/solution/CalculateDiscountUseCase.java", """package com.turkninja.ddd.module02.solution;

import com.turkninja.ddd.module02.domain.model.Product;
import com.turkninja.ddd.module02.domain.model.ProductPrice;

import java.math.BigDecimal;

public interface CalculateDiscountUseCase {
    ProductPrice calculateDiscountedPrice(Product product, String customerTier);
}
""")

write_file(f"{m2}/src/main/java/com/turkninja/ddd/module02/solution/DiscountApplicationService.java", """package com.turkninja.ddd.module02.solution;

import com.turkninja.ddd.module02.domain.model.Product;
import com.turkninja.ddd.module02.domain.model.ProductPrice;

import java.math.BigDecimal;
import java.util.Objects;

public class DiscountApplicationService implements CalculateDiscountUseCase {

    private final DiscountPolicyPort discountPolicyPort;

    public DiscountApplicationService(DiscountPolicyPort discountPolicyPort) {
        this.discountPolicyPort = Objects.requireNonNull(discountPolicyPort);
    }

    @Override
    public ProductPrice calculateDiscountedPrice(Product product, String customerTier) {
        BigDecimal discountPercent = discountPolicyPort.getDiscountPercentage(customerTier);
        BigDecimal originalAmount = product.getPrice().amount();
        BigDecimal discountFactor = BigDecimal.ONE.subtract(discountPercent);
        BigDecimal discountedAmount = originalAmount.multiply(discountFactor);

        return new ProductPrice(discountedAmount, product.getPrice().currency());
    }
}
""")

write_file(f"{m2}/src/test/java/com/turkninja/ddd/module02/solution/DiscountSolutionTest.java", """package com.turkninja.ddd.module02.solution;

import com.turkninja.ddd.module02.domain.model.Product;
import com.turkninja.ddd.module02.domain.model.ProductId;
import com.turkninja.ddd.module02.domain.model.ProductPrice;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.math.BigDecimal;

import static org.assertj.core.api.Assertions.assertThat;

@DisplayName("Solution 02: Hexagonal Discount Calculation")
class DiscountSolutionTest {

    @Test
    @DisplayName("Should apply 20% discount policy correctly via Outbound Port")
    void testDiscountCalculation() {
        DiscountPolicyPort stubPolicy = tier -> "VIP".equalsIgnoreCase(tier) ? new BigDecimal("0.20") : BigDecimal.ZERO;
        DiscountApplicationService service = new DiscountApplicationService(stubPolicy);

        Product product = new Product(ProductId.generate(), "Software Architecture Book", ProductPrice.of(100.00, "USD"));

        ProductPrice vipPrice = service.calculateDiscountedPrice(product, "VIP");
        assertThat(vipPrice.amount()).isEqualByComparingTo("80.00");

        ProductPrice regularPrice = service.calculateDiscountedPrice(product, "STANDARD");
        assertThat(regularPrice.amount()).isEqualByComparingTo("100.00");
    }
}
""")

# ==============================================================================
# MODULE 03: Exercise & Solution (TaxNumber & PostalCode)
# ==============================================================================
m3 = "modules/module-03-value-objects"

write_file(f"{m3}/exercises/README.md", """# Exercise 03: Implementing TaxNumber and PostalCode Value Objects

## 🎯 Business Context
Corporate tax identification numbers and postal codes must be strictly formatted to prevent invoicing errors.

## 📋 Acceptance Criteria
1. `TaxNumber`: Must contain exactly 10 numeric digits.
2. `TaxNumber`: Cannot be all zeros (e.g. `0000000000`).
3. `PostalCode`: Must be trimmed and non-empty.
4. Compact constructor must validate invariants and throw `DomainValidationException`.
""")

write_file(f"{m3}/exercises/README.tr.md", """# Alıştırma 03: Vergi Numarası ve Posta Kodu Değer Nesnelerini Kodlama

## 🎯 İş Bağlamı
Faturalandırma hatalarını önlemek için kurumsal vergi kimlik numaraları ve posta kodları sıkı kurallarla doğrulanmalıdır.

## 📋 Kabul Kriterleri
1. `TaxNumber`: Tam olarak 10 sayısal basamaktan oluşmalıdır.
2. `TaxNumber`: Tamamı sıfırlardan oluşamaz (`0000000000` geçersizdir).
3. `PostalCode`: Boşluklardan arındırılmış (trimmed) ve dolu olmalıdır.
4. Compact constructor geçersiz durumlarda `DomainValidationException` fırlatmalıdır.
""")

write_file(f"{m3}/src/test/java/com/turkninja/ddd/module03/exercise/TaxNumberExerciseTest.java", """package com.turkninja.ddd.module03.exercise;

import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.fail;

@DisplayName("Exercise 03: TaxNumber Value Object Validation")
class TaxNumberExerciseTest {

    @Test
    @Disabled("Remove @Disabled when you begin implementing Exercise 03")
    @DisplayName("Should validate 10-digit tax number")
    void testTaxNumberValidation() {
        fail("TODO: Implement TaxNumber record with 10-digit invariant");
    }
}
""")

write_file(f"{m3}/src/main/java/com/turkninja/ddd/module03/solution/TaxNumber.java", """package com.turkninja.ddd.module03.solution;

import com.turkninja.ddd.shared.domain.DomainValidationException;
import com.turkninja.ddd.shared.domain.ValueObject;

import java.util.regex.Pattern;

public record TaxNumber(String value) implements ValueObject {
    private static final Pattern PATTERN = Pattern.compile("^\\\\d{10}$");

    public TaxNumber {
        if (value == null || !PATTERN.matcher(value).matches() || "0000000000".equals(value)) {
            throw new DomainValidationException("Tax number must be a non-zero 10-digit numeric string. Given: " + value);
        }
    }
}
""")

write_file(f"{m3}/src/test/java/com/turkninja/ddd/module03/solution/TaxNumberSolutionTest.java", """package com.turkninja.ddd.module03.solution;

import com.turkninja.ddd.shared.domain.DomainValidationException;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

@DisplayName("Solution 03: TaxNumber Invariant Verification")
class TaxNumberSolutionTest {

    @Test
    @DisplayName("Valid 10-digit tax number is accepted")
    void testValidTaxNumber() {
        TaxNumber tax = new TaxNumber("1234567890");
        assertThat(tax.value()).isEqualTo("1234567890");
    }

    @Test
    @DisplayName("All-zeros tax number is rejected")
    void testAllZerosTaxNumber() {
        assertThatThrownBy(() -> new TaxNumber("0000000000"))
                .isInstanceOf(DomainValidationException.class);
    }
}
""")

# ==============================================================================
# MODULE 04: Exercise & Solution (Account Status State Machine)
# ==============================================================================
m4 = "modules/module-04-entities-and-identity"

write_file(f"{m4}/src/test/java/com/turkninja/ddd/module04/exercise/AccountStatusExerciseTest.java", """package com.turkninja.ddd.module04.exercise;

import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.fail;

@DisplayName("Exercise 04: Entity Lifecycle & State Machine")
class AccountStatusExerciseTest {

    @Test
    @Disabled("Remove @Disabled when you begin implementing Exercise 04")
    @DisplayName("Should prevent modifying closed account")
    void testClosedAccountProtection() {
        fail("TODO: Implement state transition invariants for account lifecycle");
    }
}
""")

write_file(f"{m4}/src/main/java/com/turkninja/ddd/module04/solution/AccountState.java", """package com.turkninja.ddd.module04.solution;

import com.turkninja.ddd.shared.domain.DomainEntity;
import com.turkninja.ddd.shared.domain.DomainValidationException;
import com.turkninja.ddd.shared.domain.ValueObject;

import java.util.UUID;

public class AccountState extends DomainEntity<AccountState.AccountId> {

    public record AccountId(UUID value) implements ValueObject {}
    public enum Status { ACTIVE, SUSPENDED, CLOSED }

    private Status status;

    public AccountState(AccountId id) {
        super(id);
        this.status = Status.ACTIVE;
    }

    public void suspend() {
        if (status == Status.CLOSED) {
            throw new DomainValidationException("Cannot suspend an already closed account");
        }
        this.status = Status.SUSPENDED;
    }

    public void close() {
        this.status = Status.CLOSED;
    }

    public void activate() {
        if (status == Status.CLOSED) {
            throw new DomainValidationException("Cannot reactivate a closed account");
        }
        this.status = Status.ACTIVE;
    }

    public Status getStatus() { return status; }
}
""")

write_file(f"{m4}/src/test/java/com/turkninja/ddd/module04/solution/AccountStateSolutionTest.java", """package com.turkninja.ddd.module04.solution;

import com.turkninja.ddd.shared.domain.DomainValidationException;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.util.UUID;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

@DisplayName("Solution 04: Account State Lifecycle Verification")
class AccountStateSolutionTest {

    @Test
    @DisplayName("Account transitions cleanly from active to suspended to active")
    void testStateTransitions() {
        AccountState account = new AccountState(new AccountState.AccountId(UUID.randomUUID()));
        assertThat(account.getStatus()).isEqualTo(AccountState.Status.ACTIVE);

        account.suspend();
        assertThat(account.getStatus()).isEqualTo(AccountState.Status.SUSPENDED);

        account.activate();
        assertThat(account.getStatus()).isEqualTo(AccountState.Status.ACTIVE);
    }

    @Test
    @DisplayName("Cannot reactivate a closed account")
    void testReactivatingClosedAccount() {
        AccountState account = new AccountState(new AccountState.AccountId(UUID.randomUUID()));
        account.close();

        assertThatThrownBy(account::activate)
                .isInstanceOf(DomainValidationException.class)
                .hasMessageContaining("Cannot reactivate a closed account");
    }
}
""")

print("Exercises and solutions for Modules 02, 03, 04 written successfully!")
