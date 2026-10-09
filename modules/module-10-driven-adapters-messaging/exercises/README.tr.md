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
