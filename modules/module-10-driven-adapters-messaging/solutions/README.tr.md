# Çözüm 10: Dayanıklı Harici Servis Sürülen Adaptörü

## Mimari İçgörü
Harici HTTP API'leri ve mesaj kuyrukları kesintilere açıktır. Yeniden deneme (retry) ve devre kesici (circuit breaker) mantığını **Sürülen Adaptör** içine yerleştirmek, domain çekirdeğini harici ağ hatalarından ve kütüphane bağımlılıklarından korur.

## Önemli Dosyalar
- `PaymentGatewayPort.java`: Dış dünyaya açılan temiz port arayüzü (SPI).
- `ResilientPaymentGatewayAdapter.java`: Yeniden deneme döngüsü ve zarif hata yönetimi içeren adaptör.
- `ResilientPaymentGatewaySolutionTest.java`: Yeniden deneme mantığını doğrulayan birim testler.
