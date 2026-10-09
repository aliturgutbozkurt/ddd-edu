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
