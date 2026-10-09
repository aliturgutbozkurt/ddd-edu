#!/usr/bin/env python3
import os

BASE_DIR = "/Users/aliturgutbozkurt/Desktop/DDD-edu"

def write_file(rel_path, content):
    full_path = os.path.join(BASE_DIR, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Created: {rel_path}")

# ==============================================================================
# MODULE 09: Modern Driving Adapters (REST) & RFC 9457 Problem Details
# ==============================================================================

# Exercises README
write_file("modules/module-09-driving-adapters-rest/exercises/README.md", """
# Exercise 09: RFC 9457 Problem Details Exception Handler

## Objective
Implement an HTTP driving adapter error-handling mechanism compliant with **RFC 9457** (`application/problem+json`).
The adapter translates pure domain exceptions (`DomainValidationException`, `ResourceNotFoundException`) into structured Problem Detail records.

## Requirements
1. Define a problem details data carrier with fields: `type` (URI), `title`, `status` (HTTP int), `detail` (string message), `instance` (URI string), and `timestamp`.
2. Implement translation logic:
   - `DomainValidationException` -> Status 400 Bad Request, type `https://api.turkninja.com/errors/validation-error`, title "Domain Validation Failure".
   - `NoSuchElementException` -> Status 404 Not Found, type `https://api.turkninja.com/errors/not-found`, title "Resource Not Found".
   - Unhandled exceptions -> Status 500 Internal Server Error.
3. Verify with unit tests.

## Running Tests
Run the exercise test in:
`src/test/java/com/turkninja/ddd/module09/exercise/ProblemDetailsExerciseTest.java`
Remove `@Disabled` and make tests pass!
""")

write_file("modules/module-09-driving-adapters-rest/exercises/README.tr.md", """
# Alıştırma 09: RFC 9457 Problem Details İstisna İşleyicisi

## Amaç
**RFC 9457** standardına (`application/problem+json`) uygun bir HTTP sürüş adaptörü hata yakalama mekanizması geliştirin.
Adaptör, saf domain istisnalarını (`DomainValidationException`, `ResourceNotFoundException`) yapılandırılmış Problem Detail kayıtlarına dönüştürür.

## Gereksinimler
1. `type` (URI), `title`, `status` (HTTP kodu), `detail` (mesaj), `instance` (istek yolu URI) ve `timestamp` içeren bir Problem Detail veri yapısı oluşturun.
2. Dönüşüm kuralları:
   - `DomainValidationException` -> HTTP 400 Bad Request, type `https://api.turkninja.com/errors/validation-error`, başlık "Domain Validation Failure".
   - `NoSuchElementException` -> HTTP 404 Not Found, type `https://api.turkninja.com/errors/not-found`, başlık "Resource Not Found".
   - Diğer istisnalar -> HTTP 500 Internal Server Error.
3. Birim testlerle doğrulayın.

## Testleri Çalıştırma
`src/test/java/com/turkninja/ddd/module09/exercise/ProblemDetailsExerciseTest.java` dosyasındaki `@Disabled` notunu kaldırarak testleri yeşile çevirin!
""")

# Solutions README
write_file("modules/module-09-driving-adapters-rest/solutions/README.md", """
# Solution 09: RFC 9457 Problem Details Translation

## Architecture Overview
In Hexagonal Architecture, HTTP status codes, JSON serialization, and RFC 9457 payloads belong exclusively to the **Driving Adapter (Infrastructure)** layer. The domain model never knows about HTTP 400, 404, or Problem Details.

## Key Files
- `ProblemDetailRecord.java`: Immutable Java 27 record representing RFC 9457.
- `GlobalExceptionHandler.java`: Adapter converting domain validation and lookup exceptions into RFC 9457 payloads.
- `GlobalExceptionHandlerSolutionTest.java`: 100% green test suite.
""")

write_file("modules/module-09-driving-adapters-rest/solutions/README.tr.md", """
# Çözüm 09: RFC 9457 Problem Details Dönüşümü

## Mimari Bakış
Hekzagonal Mimaride HTTP durum kodları, JSON serileştirme ve RFC 9457 yükleri yalnızca **Sürüş Adaptörü (Altyapı)** katmanına aittir. Domain modeli asla HTTP 400, 404 veya JSON yapılarını bilmez.

## Önemli Dosyalar
- `ProblemDetailRecord.java`: RFC 9457 standardını temsil eden Java 27 record yapısı.
- `GlobalExceptionHandler.java`: Domain istisnalarını RFC 9457 formatına dönüştüren adaptör sınıfı.
- `GlobalExceptionHandlerSolutionTest.java`: %100 başarılı çalışan test paketi.
""")

# Module 09 Solution Code
write_file("modules/module-09-driving-adapters-rest/src/main/java/com/turkninja/ddd/module09/solution/ProblemDetailRecord.java", """
package com.turkninja.ddd.module09.solution;

import java.net.URI;
import java.time.Instant;
import java.util.Map;

/**
 * Immutable RFC 9457 Problem Details representation.
 */
public record ProblemDetailRecord(
        URI type,
        String title,
        int status,
        String detail,
        URI instance,
        Instant timestamp,
        Map<String, Object> properties
) {
    public static ProblemDetailRecord of(URI type, String title, int status, String detail, URI instance) {
        return new ProblemDetailRecord(type, title, status, detail, instance, Instant.now(), Map.of());
    }

    public static ProblemDetailRecord of(URI type, String title, int status, String detail, URI instance, Map<String, Object> properties) {
        return new ProblemDetailRecord(type, title, status, detail, instance, Instant.now(), Map.copyOf(properties));
    }
}
""")

write_file("modules/module-09-driving-adapters-rest/src/main/java/com/turkninja/ddd/module09/solution/GlobalExceptionHandler.java", """
package com.turkninja.ddd.module09.solution;

import com.turkninja.ddd.shared.domain.DomainValidationException;

import java.net.URI;
import java.util.Map;
import java.util.NoSuchElementException;

/**
 * Driving adapter exception handler translating domain exceptions to RFC 9457 Problem Details.
 */
public class GlobalExceptionHandler {

    private static final URI VALIDATION_TYPE = URI.create("https://api.turkninja.com/errors/validation-error");
    private static final URI NOT_FOUND_TYPE = URI.create("https://api.turkninja.com/errors/not-found");
    private static final URI INTERNAL_ERROR_TYPE = URI.create("https://api.turkninja.com/errors/internal-error");

    public ProblemDetailRecord handleException(Exception ex, String requestPath) {
        URI instance = URI.create(requestPath);

        if (ex instanceof DomainValidationException dve) {
            return ProblemDetailRecord.of(
                    VALIDATION_TYPE,
                    "Domain Validation Failure",
                    400,
                    dve.getMessage(),
                    instance,
                    Map.of("errorCategory", "BUSINESS_RULE_VIOLATION")
            );
        }

        if (ex instanceof NoSuchElementException nse) {
            return ProblemDetailRecord.of(
                    NOT_FOUND_TYPE,
                    "Resource Not Found",
                    404,
                    nse.getMessage() != null ? nse.getMessage() : "Requested resource does not exist",
                    instance
            );
        }

        return ProblemDetailRecord.of(
                INTERNAL_ERROR_TYPE,
                "Internal Server Error",
                500,
                "An unexpected server error occurred.",
                instance
        );
    }
}
""")

# Module 09 Exercise Test
write_file("modules/module-09-driving-adapters-rest/src/test/java/com/turkninja/ddd/module09/exercise/ProblemDetailsExerciseTest.java", """
package com.turkninja.ddd.module09.exercise;

import com.turkninja.ddd.module09.solution.GlobalExceptionHandler;
import com.turkninja.ddd.module09.solution.ProblemDetailRecord;
import com.turkninja.ddd.shared.domain.DomainValidationException;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

@DisplayName("Exercise 09: RFC 9457 Problem Details Exception Handler")
class ProblemDetailsExerciseTest {

    @Test
    @Disabled("TODO for student: Implement exception translation logic and enable this test")
    @DisplayName("Should translate DomainValidationException to RFC 9457 400 Bad Request")
    void shouldTranslateDomainValidationException() {
        GlobalExceptionHandler handler = new GlobalExceptionHandler();
        DomainValidationException ex = new DomainValidationException("Amount must be greater than zero");

        ProblemDetailRecord problem = handler.handleException(ex, "/api/v1/transfers");

        assertThat(problem.status()).isEqualTo(400);
        assertThat(problem.title()).isEqualTo("Domain Validation Failure");
        assertThat(problem.detail()).contains("Amount must be greater than zero");
    }
}
""")

# Module 09 Solution Test
write_file("modules/module-09-driving-adapters-rest/src/test/java/com/turkninja/ddd/module09/solution/GlobalExceptionHandlerSolutionTest.java", """
package com.turkninja.ddd.module09.solution;

import com.turkninja.ddd.shared.domain.DomainValidationException;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.util.NoSuchElementException;

import static org.assertj.core.api.Assertions.assertThat;

@DisplayName("Solution 09: Global Exception Handler RFC 9457 Tests")
class GlobalExceptionHandlerSolutionTest {

    private final GlobalExceptionHandler handler = new GlobalExceptionHandler();

    @Test
    @DisplayName("Should translate DomainValidationException to 400 Bad Request")
    void testDomainValidationException() {
        DomainValidationException ex = new DomainValidationException("Transfer amount exceeds daily limit");
        ProblemDetailRecord record = handler.handleException(ex, "/api/transfers");

        assertThat(record.status()).isEqualTo(400);
        assertThat(record.title()).isEqualTo("Domain Validation Failure");
        assertThat(record.detail()).isEqualTo("Transfer amount exceeds daily limit");
        assertThat(record.instance().toString()).isEqualTo("/api/transfers");
        assertThat(record.properties()).containsEntry("errorCategory", "BUSINESS_RULE_VIOLATION");
    }

    @Test
    @DisplayName("Should translate NoSuchElementException to 404 Not Found")
    void testNoSuchElementException() {
        NoSuchElementException ex = new NoSuchElementException("Account not found for id ACC-123");
        ProblemDetailRecord record = handler.handleException(ex, "/api/accounts/ACC-123");

        assertThat(record.status()).isEqualTo(404);
        assertThat(record.title()).isEqualTo("Resource Not Found");
        assertThat(record.detail()).isEqualTo("Account not found for id ACC-123");
    }

    @Test
    @DisplayName("Should translate generic unexpected exception to 500 Internal Error")
    void testGenericException() {
        RuntimeException ex = new RuntimeException("Database connection timeout");
        ProblemDetailRecord record = handler.handleException(ex, "/api/transfers");

        assertThat(record.status()).isEqualTo(500);
        assertThat(record.title()).isEqualTo("Internal Server Error");
    }
}
""")

# ==============================================================================
# MODULE 10: Driven Adapters (Messaging & External Services)
# ==============================================================================

# Exercises README
write_file("modules/module-10-driven-adapters-messaging/exercises/README.md", """
# Exercise 10: Resilient Payment Gateway Driven Adapter

## Objective
Implement an Outbound Driven Adapter (`ResilientPaymentGatewayAdapter`) satisfying the outbound SPI `PaymentGatewayPort`.
The adapter wraps an external third-party payment provider and applies a retry policy to gracefully handle transient network glitches.

## Requirements
1. Implement `PaymentGatewayPort`:
   - `PaymentResult charge(PaymentRequest request)`
2. The adapter must:
   - Retry transient failures up to `maxRetries` (default: 3).
   - If transient errors persist beyond `maxRetries`, return a failed `PaymentResult` with details instead of bubbling raw network exceptions into the domain.
   - Record total execution attempts.
3. Verify behavior with automated tests.

## Running Tests
Run: `src/test/java/com/turkninja/ddd/module10/exercise/ResilientPaymentExerciseTest.java`
Remove `@Disabled` and verify your implementation.
""")

write_file("modules/module-10-driven-adapters-messaging/exercises/README.tr.md", """
# Alıştırma 10: Dayanıklı Ödeme Ağ Geçidi Sürülen Adaptörü

## Amaç
Dış dünyaya bağlanan `PaymentGatewayPort` arayüzünü gerçekleştiren bir Sürülen Adaptör (`ResilientPaymentGatewayAdapter`) geliştirin.
Adaptör, harici ödeme sağlayıcısı ile iletişim kurar ve geçici ağ kesintilerine karşı yeniden deneme (retry) politikası uygular.

## Gereksinimler
1. `PaymentGatewayPort` arayüzünü gerçekleştirin:
   - `PaymentResult charge(PaymentRequest request)`
2. Adaptör:
   - Geçici ağ hatalarında en fazla `maxRetries` (varsayılan: 3) kez deneme yapmalıdır.
   - Hatalar devam ederse domain katmanına ham ağ istisnası fırlatmak yerine zarif bir biçimde başarısız `PaymentResult` döndürmelidir.
   - Yapılan toplam deneme sayısını kaydetmelidir.
3. Birim testlerle doğrulayın.

## Testleri Çalıştırma
`src/test/java/com/turkninja/ddd/module10/exercise/ResilientPaymentExerciseTest.java` dosyasındaki `@Disabled` notunu kaldırarak alıştırmayı tamamlayın.
""")

# Solutions README
write_file("modules/module-10-driven-adapters-messaging/solutions/README.md", """
# Solution 10: Resilient External Service Driven Adapter

## Architectural Insight
External HTTP APIs and messaging queues are volatile. Placing retry logic and circuit breakers inside the **Driven Adapter** keeps the domain core completely immune to external outages, HTTP client configurations, and transport issues.

## Key Files
- `PaymentGatewayPort.java`: Clean outbound driving interface (SPI).
- `ResilientPaymentGatewayAdapter.java`: Fault-tolerant adapter with retry loops and graceful failure results.
- `ResilientPaymentGatewaySolutionTest.java`: Unit tests asserting retry semantics and recovery.
""")

write_file("modules/module-10-driven-adapters-messaging/solutions/README.tr.md", """
# Çözüm 10: Dayanıklı Harici Servis Sürülen Adaptörü

## Mimari İçgörü
Harici HTTP API'leri ve mesaj kuyrukları kesintilere açıktır. Yeniden deneme (retry) ve devre kesici (circuit breaker) mantığını **Sürülen Adaptör** içine yerleştirmek, domain çekirdeğini harici ağ hatalarından ve kütüphane bağımlılıklarından korur.

## Önemli Dosyalar
- `PaymentGatewayPort.java`: Dış dünyaya açılan temiz port arayüzü (SPI).
- `ResilientPaymentGatewayAdapter.java`: Yeniden deneme döngüsü ve zarif hata yönetimi içeren adaptör.
- `ResilientPaymentGatewaySolutionTest.java`: Yeniden deneme mantığını doğrulayan birim testler.
""")

# Module 10 Solution Code
write_file("modules/module-10-driven-adapters-messaging/src/main/java/com/turkninja/ddd/module10/solution/PaymentGatewayPort.java", """
package com.turkninja.ddd.module10.solution;

import java.math.BigDecimal;

/**
 * Outbound Driven Port (SPI) for charging credit cards / accounts.
 */
public interface PaymentGatewayPort {

    record PaymentRequest(String paymentId, String customerId, BigDecimal amount, String currency) {}

    record PaymentResult(String paymentId, boolean success, String transactionReference, String failureReason) {
        public static PaymentResult success(String paymentId, String txRef) {
            return new PaymentResult(paymentId, true, txRef, null);
        }
        public static PaymentResult failure(String paymentId, String reason) {
            return new PaymentResult(paymentId, false, null, reason);
        }
    }

    PaymentResult charge(PaymentRequest request);
}
""")

write_file("modules/module-10-driven-adapters-messaging/src/main/java/com/turkninja/ddd/module10/solution/ResilientPaymentGatewayAdapter.java", """
package com.turkninja.ddd.module10.solution;

import java.util.Objects;
import java.util.UUID;
import java.util.function.Function;

/**
 * Driven Adapter implementing PaymentGatewayPort with retry resilience.
 */
public class ResilientPaymentGatewayAdapter implements PaymentGatewayPort {

    private final int maxRetries;
    private final Function<PaymentRequest, String> externalApiCall;
    private int attemptsRecorded = 0;

    public ResilientPaymentGatewayAdapter(int maxRetries, Function<PaymentRequest, String> externalApiCall) {
        this.maxRetries = maxRetries;
        this.externalApiCall = Objects.requireNonNull(externalApiCall);
    }

    @Override
    public PaymentResult charge(PaymentRequest request) {
        String lastError = null;

        for (int attempt = 1; attempt <= maxRetries; attempt++) {
            attemptsRecorded++;
            try {
                String txRef = externalApiCall.apply(request);
                return PaymentResult.success(request.paymentId(), txRef);
            } catch (Exception ex) {
                lastError = ex.getMessage();
            }
        }

        return PaymentResult.failure(request.paymentId(), "Exceeded " + maxRetries + " attempts: " + lastError);
    }

    public int getAttemptsRecorded() {
        return attemptsRecorded;
    }
}
""")

# Module 10 Exercise Test
write_file("modules/module-10-driven-adapters-messaging/src/test/java/com/turkninja/ddd/module10/exercise/ResilientPaymentExerciseTest.java", """
package com.turkninja.ddd.module10.exercise;

import com.turkninja.ddd.module10.solution.PaymentGatewayPort;
import com.turkninja.ddd.module10.solution.PaymentGatewayPort.PaymentRequest;
import com.turkninja.ddd.module10.solution.PaymentGatewayPort.PaymentResult;
import com.turkninja.ddd.module10.solution.ResilientPaymentGatewayAdapter;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.math.BigDecimal;

import static org.assertj.core.api.Assertions.assertThat;

@DisplayName("Exercise 10: Resilient Payment Gateway Driven Adapter")
class ResilientPaymentExerciseTest {

    @Test
    @Disabled("TODO for student: Implement retry logic in adapter and enable test")
    @DisplayName("Should retry transient errors up to maxRetries")
    void shouldRetryOnTransientError() {
        ResilientPaymentGatewayAdapter adapter = new ResilientPaymentGatewayAdapter(3, req -> {
            throw new RuntimeException("503 Gateway Timeout");
        });

        PaymentResult result = adapter.charge(new PaymentRequest("PAY-1", "CUST-1", new BigDecimal("100.00"), "USD"));

        assertThat(result.success()).isFalse();
        assertThat(adapter.getAttemptsRecorded()).isEqualTo(3);
    }
}
""")

# Module 10 Solution Test
write_file("modules/module-10-driven-adapters-messaging/src/test/java/com/turkninja/ddd/module10/solution/ResilientPaymentGatewaySolutionTest.java", """
package com.turkninja.ddd.module10.solution;

import com.turkninja.ddd.module10.solution.PaymentGatewayPort.PaymentRequest;
import com.turkninja.ddd.module10.solution.PaymentGatewayPort.PaymentResult;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.math.BigDecimal;
import java.util.concurrent.atomic.AtomicInteger;

import static org.assertj.core.api.Assertions.assertThat;

@DisplayName("Solution 10: Resilient Payment Gateway Adapter Tests")
class ResilientPaymentGatewaySolutionTest {

    @Test
    @DisplayName("Should succeed on first attempt if external API responds cleanly")
    void shouldSucceedOnFirstAttempt() {
        ResilientPaymentGatewayAdapter adapter = new ResilientPaymentGatewayAdapter(3, req -> "TX_OK_999");

        PaymentResult result = adapter.charge(new PaymentRequest("PAY-01", "C-1", new BigDecimal("50.00"), "EUR"));

        assertThat(result.success()).isTrue();
        assertThat(result.transactionReference()).isEqualTo("TX_OK_999");
        assertThat(adapter.getAttemptsRecorded()).isEqualTo(1);
    }

    @Test
    @DisplayName("Should succeed on retry after transient network failure")
    void shouldSucceedAfterTransientFailure() {
        AtomicInteger count = new AtomicInteger(0);
        ResilientPaymentGatewayAdapter adapter = new ResilientPaymentGatewayAdapter(3, req -> {
            if (count.incrementAndGet() < 3) {
                throw new RuntimeException("Temporary network glitch");
            }
            return "TX_RECOVERED_123";
        });

        PaymentResult result = adapter.charge(new PaymentRequest("PAY-02", "C-2", new BigDecimal("75.00"), "TRY"));

        assertThat(result.success()).isTrue();
        assertThat(result.transactionReference()).isEqualTo("TX_RECOVERED_123");
        assertThat(adapter.getAttemptsRecorded()).isEqualTo(3);
    }

    @Test
    @DisplayName("Should gracefully return failure result when all retries are exhausted")
    void shouldReturnFailureWhenRetriesExhausted() {
        ResilientPaymentGatewayAdapter adapter = new ResilientPaymentGatewayAdapter(3, req -> {
            throw new RuntimeException("Connection refused");
        });

        PaymentResult result = adapter.charge(new PaymentRequest("PAY-03", "C-3", new BigDecimal("120.00"), "USD"));

        assertThat(result.success()).isFalse();
        assertThat(result.failureReason()).contains("Exceeded 3 attempts");
        assertThat(adapter.getAttemptsRecorded()).isEqualTo(3);
    }
}
""")

# ==============================================================================
# MODULE 11: Automated Architecture Testing with ArchUnit
# ==============================================================================

# Exercises README
write_file("modules/module-11-architecture-testing-archunit/exercises/README.md", """
# Exercise 11: Writing Custom ArchUnit Port and Adapter Rules

## Objective
Write executable architectural fitness functions using ArchUnit to enforce Hexagonal Architecture conventions:
1. Inbound driving ports must be interfaces ending in `UseCase`.
2. Outbound driven ports must be interfaces ending in `Port`.
3. Domain entities must not depend on Spring or Jackson.

## Running Tests
Run: `src/test/java/com/turkninja/ddd/module11/exercise/CustomArchRuleExerciseTest.java`
Remove `@Disabled` and pass the tests.
""")

write_file("modules/module-11-architecture-testing-archunit/exercises/README.tr.md", """
# Alıştırma 11: Özel ArchUnit Port ve Adaptör Kuralları Yazma

## Amaç
Hekzagonal Mimari kurallarını CI/CD aşamasında otomatik denetleyen ArchUnit mimari uygunluk fonksiyonları yazın:
1. Giriş sürüş portları `UseCase` ile biten arayüzler (interface) olmalıdır.
2. Çıkış sürülen portları `Port` ile biten arayüzler olmalıdır.
3. Domain varlıkları asla Spring veya Jackson kütüphanelerine bağımlı olmamalıdır.

## Testleri Çalıştırma
`src/test/java/com/turkninja/ddd/module11/exercise/CustomArchRuleExerciseTest.java` dosyasındaki `@Disabled` notunu kaldırıp testleri çalıştırın.
""")

# Solutions README
write_file("modules/module-11-architecture-testing-archunit/solutions/README.md", """
# Solution 11: Architectural Fitness Functions with ArchUnit

## Architectural Insight
Architecture diagrams in wikis rot quickly. Executable ArchUnit rules fail the build if a developer accidentally imports a Spring repository in the domain model or names a concrete adapter as an interface.

## Key Files
- `CustomHexagonalRules.java`: Static reusable ArchUnit rules.
- `CustomHexagonalRulesSolutionTest.java`: Verification suite executing against module packages.
""")

write_file("modules/module-11-architecture-testing-archunit/solutions/README.tr.md", """
# Çözüm 11: ArchUnit ile Mimari Uygunluk Fonksiyonları

## Mimari İçgörü
Dokümanlardaki mimari şemalar hızla güncelliğini yitirir. Çalıştırılabilir ArchUnit kuralları, bir geliştirici domain içine yanlışlıkla Spring repository'si eklediğinde veya isimlendirme kurallarını ihlal ettiğinde build'i anında kırar.

## Önemli Dosyalar
- `CustomHexagonalRules.java`: Yeniden kullanılabilir statik ArchUnit kuralları.
- `CustomHexagonalRulesSolutionTest.java`: Kuralları doğrulayan test paketi.
""")

# Module 11 Solution Code
write_file("modules/module-11-architecture-testing-archunit/src/main/java/com/turkninja/ddd/module11/solution/CustomHexagonalRules.java", """
package com.turkninja.ddd.module11.solution;

import com.tngtech.archunit.lang.ArchRule;

import static com.tngtech.archunit.lang.syntax.ArchRuleDefinition.classes;
import static com.tngtech.archunit.lang.syntax.ArchRuleDefinition.noClasses;

/**
 * Standardized ArchUnit rules for Hexagonal Architecture projects.
 */
public final class CustomHexagonalRules {

    private CustomHexagonalRules() {}

    public static final ArchRule USE_CASES_MUST_BE_INTERFACES =
            classes().that().haveSimpleNameEndingWith("UseCase")
                    .should().beInterfaces()
                    .allowEmptyShould(true)
                    .as("Inbound Driving Ports representing Use Cases must be Java interfaces.");

    public static final ArchRule PORTS_MUST_BE_INTERFACES =
            classes().that().haveSimpleNameEndingWith("Port")
                    .should().beInterfaces()
                    .allowEmptyShould(true)
                    .as("Outbound Ports representing SPIs must be Java interfaces.");

    public static final ArchRule DOMAIN_NO_SPRING_DEPENDENCY =
            noClasses().that().resideInAPackage("..domain..")
                    .should().dependOnClassesThat().resideInAPackage("org.springframework..")
                    .allowEmptyShould(true)
                    .as("Domain layer must have zero dependencies on org.springframework.*");
}
""")

# Module 11 Exercise Test
write_file("modules/module-11-architecture-testing-archunit/src/test/java/com/turkninja/ddd/module11/exercise/CustomArchRuleExerciseTest.java", """
package com.turkninja.ddd.module11.exercise;

import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.turkninja.ddd.module11.solution.CustomHexagonalRules;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

@DisplayName("Exercise 11: ArchUnit Architectural Rules")
class CustomArchRuleExerciseTest {

    @Test
    @Disabled("TODO for student: Implement and assert custom ArchUnit rules")
    @DisplayName("Should verify that all UseCase suffixed types are interfaces")
    void shouldEnforceUseCaseNaming() {
        JavaClasses classes = new ClassFileImporter().importPackages("com.turkninja.ddd");
        CustomHexagonalRules.USE_CASES_MUST_BE_INTERFACES.check(classes);
    }
}
""")

# Module 11 Solution Test
write_file("modules/module-11-architecture-testing-archunit/src/test/java/com/turkninja/ddd/module11/solution/CustomHexagonalRulesSolutionTest.java", """
package com.turkninja.ddd.module11.solution;

import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.core.importer.ImportOption;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

@DisplayName("Solution 11: ArchUnit Custom Rule Verification")
class CustomHexagonalRulesSolutionTest {

    private final JavaClasses classes = new ClassFileImporter()
            .withImportOption(ImportOption.Predefined.DO_NOT_INCLUDE_TESTS)
            .importPackages("com.turkninja.ddd");

    @Test
    @DisplayName("Verify UseCase interface conventions")
    void testUseCasesAreInterfaces() {
        CustomHexagonalRules.USE_CASES_MUST_BE_INTERFACES.check(classes);
    }

    @Test
    @DisplayName("Verify Port interface conventions")
    void testPortsAreInterfaces() {
        CustomHexagonalRules.PORTS_MUST_BE_INTERFACES.check(classes);
    }

    @Test
    @DisplayName("Verify zero spring dependencies in domain packages")
    void testDomainHasNoSpring() {
        CustomHexagonalRules.DOMAIN_NO_SPRING_DEPENDENCY.check(classes);
    }
}
""")

# ==============================================================================
# MODULE 12: Context Mapping & Outbox Pattern
# ==============================================================================

# Exercises README
write_file("modules/module-12-context-mapping-outbox/exercises/README.md", """
# Exercise 12: Building an Anti-Corruption Layer Translator

## Objective
Implement an Anti-Corruption Layer (ACL) translator that accepts an archaic external legacy ERP message (`LegacyErpOrderPayload`) and maps it into our clean domain order representation (`CleanOrder`).

## Requirements
1. Validate external payload:
   - If `order_ref_num` or `client_nm` is blank, throw `DomainValidationException`.
   - If `status_code` equals `"VOID"`, reject the message.
   - Parse `gross_amt` string into a valid `BigDecimal`.
2. Map to immutable `CleanOrder` without leaking any legacy field names (`gross_amt`, `tx_curr`, `client_nm`) into the domain.

## Running Tests
Run: `src/test/java/com/turkninja/ddd/module12/exercise/AclTranslatorExerciseTest.java`
Remove `@Disabled` and verify your solution.
""")

write_file("modules/module-12-context-mapping-outbox/exercises/README.tr.md", """
# Alıştırma 12: Anti-Corruption Layer (ACL) Dönüştürücüsü İnşa Etme

## Amaç
Eski ve hantal harici ERP sisteminden gelen karmaşık mesajı (`LegacyErpOrderPayload`) temiz domain modelimize (`CleanOrder`) dönüştüren bir Anti-Corruption Layer (ACL) geliştirin.

## Gereksinimler
1. Harici yükü doğrulayın:
   - `order_ref_num` veya `client_nm` boş ise `DomainValidationException` fırlatın.
   - `status_code` `"VOID"` ise işlemi reddedin.
   - `gross_amt` metnini `BigDecimal` formatına ayrıştırın.
2. Dış sistemin hantal alan adlarını (`gross_amt`, `tx_curr`, `client_nm`) domain katmanına sızdırmadan temiz `CleanOrder` modeline dönüştürün.

## Testleri Çalıştırma
`src/test/java/com/turkninja/ddd/module12/exercise/AclTranslatorExerciseTest.java` dosyasındaki `@Disabled` notunu kaldırarak testleri yeşile çevirin.
""")

# Solutions README
write_file("modules/module-12-context-mapping-outbox/solutions/README.md", """
# Solution 12: Anti-Corruption Layer (ACL) & Context Mapping

## Architectural Insight
When integrating bounded contexts with legacy enterprise systems, never allow external schemas or database models to bleed into your domain model. The Anti-Corruption Layer acts as a defensive membrane, sanitizing data at the boundary.

## Key Files
- `LegacyErpOrderPayload.java`: Raw external DTO representing the upstream legacy system.
- `CleanOrder.java`: Clean Java 27 domain representation.
- `LegacyOrderAclTranslator.java`: Pure ACL translator.
- `LegacyOrderAclTranslatorSolutionTest.java`: Automated test suite.
""")

write_file("modules/module-12-context-mapping-outbox/solutions/README.tr.md", """
# Çözüm 12: Anti-Corruption Layer (ACL) ve Bağlam Eşleme

## Mimari İçgörü
Sınırlı bağlamları (Bounded Contexts) harici eski sistemlerle entegre ederken, dış sistem modellerinin domain çekirdeğinizi kirletmesine izin vermeyin. Anti-Corruption Layer (ACL), sınırda savunma kalkanı görevi görerek gelen veriyi arındırır.

## Önemli Dosyalar
- `LegacyErpOrderPayload.java`: Dış kaynaktan gelen ham veri yapısı.
- `CleanOrder.java`: Saf Java 27 domain modeli.
- `LegacyOrderAclTranslator.java`: Koruma kalkanı görevi gören ACL dönüştürücüsü.
- `LegacyOrderAclTranslatorSolutionTest.java`: Doğrulama testleri.
""")

# Module 12 Solution Code
write_file("modules/module-12-context-mapping-outbox/src/main/java/com/turkninja/ddd/module12/solution/LegacyErpOrderPayload.java", """
package com.turkninja.ddd.module12.solution;

/**
 * Archaic legacy DTO received from external upstream ERP system.
 */
public record LegacyErpOrderPayload(
        String order_ref_num,
        String client_nm,
        String gross_amt,
        String tx_curr,
        String status_code
) {}
""")

write_file("modules/module-12-context-mapping-outbox/src/main/java/com/turkninja/ddd/module12/solution/CleanOrder.java", """
package com.turkninja.ddd.module12.solution;

import com.turkninja.ddd.shared.domain.ValueObject;

import java.math.BigDecimal;
import java.util.Objects;

/**
 * Clean bounded context domain representation.
 */
public record CleanOrder(
        String orderNumber,
        String customerName,
        BigDecimal totalAmount,
        String currency
) implements ValueObject {
    public CleanOrder {
        Objects.requireNonNull(orderNumber, "orderNumber cannot be null");
        Objects.requireNonNull(customerName, "customerName cannot be null");
        Objects.requireNonNull(totalAmount, "totalAmount cannot be null");
        Objects.requireNonNull(currency, "currency cannot be null");
    }
}
""")

write_file("modules/module-12-context-mapping-outbox/src/main/java/com/turkninja/ddd/module12/solution/LegacyOrderAclTranslator.java", """
package com.turkninja.ddd.module12.solution;

import com.turkninja.ddd.shared.domain.DomainValidationException;

import java.math.BigDecimal;

/**
 * Anti-Corruption Layer (ACL) translator protecting the domain from legacy ERP schemas.
 */
public class LegacyOrderAclTranslator {

    public CleanOrder translate(LegacyErpOrderPayload payload) {
        if (payload == null) {
            throw new DomainValidationException("Legacy payload cannot be null");
        }

        if (payload.order_ref_num() == null || payload.order_ref_num().isBlank()) {
            throw new DomainValidationException("Legacy order reference number is missing");
        }

        if (payload.client_nm() == null || payload.client_nm().isBlank()) {
            throw new DomainValidationException("Legacy client name is missing");
        }

        if ("VOID".equalsIgnoreCase(payload.status_code())) {
            throw new DomainValidationException("Cannot import VOID orders from legacy ERP");
        }

        BigDecimal amount;
        try {
            amount = new BigDecimal(payload.gross_amt());
        } catch (Exception ex) {
            throw new DomainValidationException("Invalid gross amount format: " + payload.gross_amt());
        }

        String currency = (payload.tx_curr() == null || payload.tx_curr().isBlank()) ? "USD" : payload.tx_curr().toUpperCase();

        return new CleanOrder(
                payload.order_ref_num().trim(),
                payload.client_nm().trim(),
                amount,
                currency
        );
    }
}
""")

# Module 12 Exercise Test
write_file("modules/module-12-context-mapping-outbox/src/test/java/com/turkninja/ddd/module12/exercise/AclTranslatorExerciseTest.java", """
package com.turkninja.ddd.module12.exercise;

import com.turkninja.ddd.module12.solution.CleanOrder;
import com.turkninja.ddd.module12.solution.LegacyErpOrderPayload;
import com.turkninja.ddd.module12.solution.LegacyOrderAclTranslator;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.math.BigDecimal;

import static org.assertj.core.api.Assertions.assertThat;

@DisplayName("Exercise 12: Anti-Corruption Layer Translator")
class AclTranslatorExerciseTest {

    @Test
    @Disabled("TODO for student: Implement ACL translation and enable test")
    @DisplayName("Should translate valid legacy payload into clean domain order")
    void shouldTranslateLegacyPayload() {
        LegacyOrderAclTranslator translator = new LegacyOrderAclTranslator();
        LegacyErpOrderPayload legacy = new LegacyErpOrderPayload("ERP-9912", "Acme Corp", "1500.50", "USD", "ACTIVE");

        CleanOrder clean = translator.translate(legacy);

        assertThat(clean.orderNumber()).isEqualTo("ERP-9912");
        assertThat(clean.customerName()).isEqualTo("Acme Corp");
        assertThat(clean.totalAmount()).isEqualByComparingTo(new BigDecimal("1500.50"));
    }
}
""")

# Module 12 Solution Test
write_file("modules/module-12-context-mapping-outbox/src/test/java/com/turkninja/ddd/module12/solution/LegacyOrderAclTranslatorSolutionTest.java", """
package com.turkninja.ddd.module12.solution;

import com.turkninja.ddd.shared.domain.DomainValidationException;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.math.BigDecimal;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

@DisplayName("Solution 12: Legacy Order ACL Translator Tests")
class LegacyOrderAclTranslatorSolutionTest {

    private final LegacyOrderAclTranslator translator = new LegacyOrderAclTranslator();

    @Test
    @DisplayName("Should translate valid legacy payload cleanly into domain model")
    void testValidTranslation() {
        LegacyErpOrderPayload legacy = new LegacyErpOrderPayload(
                "ERP-1001",
                "Globex Corp",
                "2450.75",
                "EUR",
                "OPEN"
        );

        CleanOrder order = translator.translate(legacy);

        assertThat(order.orderNumber()).isEqualTo("ERP-1001");
        assertThat(order.customerName()).isEqualTo("Globex Corp");
        assertThat(order.totalAmount()).isEqualByComparingTo(new BigDecimal("2450.75"));
        assertThat(order.currency()).isEqualTo("EUR");
    }

    @Test
    @DisplayName("Should reject VOID status orders")
    void testRejectVoidStatus() {
        LegacyErpOrderPayload legacy = new LegacyErpOrderPayload(
                "ERP-1002",
                "Initech",
                "100.00",
                "USD",
                "VOID"
        );

        assertThatThrownBy(() -> translator.translate(legacy))
                .isInstanceOf(DomainValidationException.class)
                .hasMessageContaining("Cannot import VOID orders");
    }

    @Test
    @DisplayName("Should throw on missing order reference")
    void testMissingOrderRef() {
        LegacyErpOrderPayload legacy = new LegacyErpOrderPayload(
                "",
                "Umbrella Corp",
                "500.00",
                "USD",
                "OPEN"
        );

        assertThatThrownBy(() -> translator.translate(legacy))
                .isInstanceOf(DomainValidationException.class)
                .hasMessageContaining("order reference number is missing");
    }
}
""")

print("All module 09-12 files generated successfully!")
