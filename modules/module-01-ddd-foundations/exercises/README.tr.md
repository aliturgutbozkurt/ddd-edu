# Alıştırma 01: Kapsamlı Dil ve Günlük Para Çekme Limit Değişmezleri

## 🎯 Görev Hedefleri
Bu alıştırmada, `BankAccount` zengin aggregate kökünü genişleterek kritik bir iş kuralını uygulayacaksınız: **Günlük Para Çekme Limiti (Daily Withdrawal Limit)**.

### İş Değişmezleri (Invariants):
1. **Günlük Limit Kısıtı**: Her banka hesabının bir `DailyWithdrawalLimit` (Değer Nesnesi) olmalıdır.
2. **Kümülatif Takip**: Aggregate kök, mevcut takvim gününde çekilen toplam tutarı güvenli bir şekilde takip etmelidir.
3. **Limit Aşımı Reddi**: Yapılmak istenen para çekme işlemi o günkü çekim toplamını `DailyWithdrawalLimit` değerinin üzerine çıkaracaksa, işlem `DailyLimitExceededException` fırlatmalı ve bakiye kesinlikle değişmemelidir.
4. **Gün Dönümü Sıfırlaması**: Yeni bir takvim gününe geçildiğinde gün içi çekim toplamı otomatik olarak sıfırlanmalıdır.
5. **Domain Olayı**: Başarılı bir çekim işleminden sonra `DailyLimitUpdatedEvent` fırlatılmalıdır.

---

## 🛠️ Yönergeler
1. `exercises/src/test/java/DailyLimitTest.java` test sınıfını açın.
2. `fail("TODO: Günlük limit iş kuralını uygulayın")` ile işaretlenmiş testleri inceleyin.
3. `DailyWithdrawalLimit` değer nesnesini ve `BankAccount` içindeki mantığı kodlayın.
4. `./mvnw test` komutuyla tüm testler yeşile dönene kadar çalışın.
