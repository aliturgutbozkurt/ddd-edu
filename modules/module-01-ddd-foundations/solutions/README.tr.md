# Çözüm 01: Kapsamlı Dil ve Günlük Para Çekme Limit Değişmezleri

## 📖 Mimari İnceleme ve Çözüm Yaklaşımı

### 1. Değer Nesnesi (Value Object): `DailyWithdrawalLimit`
İlkel takıntıdan (Primitive Obsession) kaçınmak için çıplak `double` veya `BigDecimal` yerine, `Money` nesnesini saran değişmez bir Java 27 `record` oluşturduk. Compact constructor içinde negatif limit kontrolü yaptık.

### 2. Kümülatif Durumun `AccountWithDailyLimit` İçinde Kapsüllenmesi (Encapsulation)
Günlük limiti dışarıya servis katmanına sızdırmadan aggregate içinde çözmek için:
- Aggregate kökü, kendi içinde `todayWithdrawn` ve `lastWithdrawalDate` alanlarını tutar.
- `withdraw(Money, LocalDate)` çağrıldığında, `date.isAfter(lastWithdrawalDate)` kontrol edilir. Gün değiştiyse `todayWithdrawn` otomatik olarak sıfırlanır.
- Eğer `todayWithdrawn + requested > dailyLimit` ise işlem derhal iptal edilir ve `DailyLimitExceededException` fırlatılır.

---

## 🧪 Doğrulama
`DailyLimitSolutionTest.java` test sınıfı, sınır değerleri ve gün dönümü senaryolarını %100 başarıyla doğrular.
