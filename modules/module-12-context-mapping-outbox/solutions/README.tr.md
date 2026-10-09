# Çözüm 12: Anti-Corruption Layer (ACL) ve Bağlam Eşleme

## Mimari İçgörü
Sınırlı bağlamları (Bounded Contexts) harici eski sistemlerle entegre ederken, dış sistem modellerinin domain çekirdeğinizi kirletmesine izin vermeyin. Anti-Corruption Layer (ACL), sınırda savunma kalkanı görevi görerek gelen veriyi arındırır.

## Önemli Dosyalar
- `LegacyErpOrderPayload.java`: Dış kaynaktan gelen ham veri yapısı.
- `CleanOrder.java`: Saf Java 27 domain modeli.
- `LegacyOrderAclTranslator.java`: Koruma kalkanı görevi gören ACL dönüştürücüsü.
- `LegacyOrderAclTranslatorSolutionTest.java`: Doğrulama testleri.
