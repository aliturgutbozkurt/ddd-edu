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
