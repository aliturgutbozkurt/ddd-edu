---
marp: true
theme: default
paginate: true
header: "DDD & Hekzagonal Mimari Masterclass | Modül 01"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Modül 01: Domain-Driven Design Temelleri ve Kapsamlı Dil (Ubiquitous Language)

## Stratejik Tasarım ve Anemik Domain Modelinin Sonu

---

## 1. Domain-Driven Design (DDD) Nedir?

Eric Evans tarafından 2003 yılında ortaya konan Domain-Driven Design (Alana Dayalı Tasarım), yazılım geliştirmeyi derinlemesine anlaşılan bir iş alanı (domain) etrafında yapılandıran bir felsefedir.

### DDD'nin İki Temel Ayağı:
1. **Stratejik Tasarım (Strategic Design)**:
   - Neyin inşa edileceğini ve neyin ASLA inşa edilmeyeceğini belirlemek.
   - Sistemin açık sınırlarını (**Bounded Contexts**) çizmek.
   - Rekabetçi farklılaşmaya göre alt alanları (subdomains) sınıflandırmak.
2. **Taktiksel Tasarım (Tactical Design)**:
   - Bounded Context içerisindeki iş değişmezlerini (invariants) koruyan yazılım desenleri.
   - Aggregateler, Varlıklar (Entities), Değer Nesneleri (Value Objects), Domain Olayları (Domain Events), Repository'ler ve Domain Servisleri.

---

## 2. Alt Alan (Subdomain) Sınıflandırması

Kurumsal bir ekosistem farklı dinamiklere sahip alt alanlardan oluşur:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        KURUMSAL EKOSİSTEM                              │
│                                                                        │
│  ┌─────────────────────────┐  ┌─────────────────────────────────────┐  │
│  │     ÇEKİRDEK ALAN       │  │       DESTEKLEYİCİ ALT ALAN         │  │
│  │  (Core Domain)          │  │     (Supporting Subdomain)          │  │
│  │  Şirkete rekabet avantajı│  │  Müşteri kimlik doğrulama & KYC     │  │
│  │  sağlayan özgün algoritmik│  │  (Şirkete özel ama fark yaratmayan) │  │
│  │  fintech modülü         │  │                                     │  │
│  └─────────────────────────┘  └─────────────────────────────────────┘  │
│                                                                        │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │                   GENEL ALT ALAN (Generic Subdomain)             │  │
│  │  Kimlik Yönetimi (OAuth), SMS/E-posta gönderimi, PDF Raporlama   │  │
│  │  (Piyasada hazır çözümü olan standart modüller)                  │  │
│  └──────────────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────────────┘
```

> **Altın Kural**: Mühendislik dehanızın ve zamanınızın en az %80'ini **Çekirdek Alana (Core Domain)** harcayın. Genel alt alanları baştan yazarak vakit kaybetmeyin.

---

## 3. Kapsamlı Dil (Ubiquitous Language)

Kapsamlı Dil; **yazılım mühendisleri** ile **alan uzmanlarının** (iş analistleri, hazine uzmanları, ürün yöneticileri) üzerinde anlaştığı ve konuşurken, doküman yazarken ve kod yazarken birebir aynı anlamda kullandığı ortak sözlüktür.

### Anti-Desen: Zihinsel Çeviri Katmanı
- *Analist der ki*: "Kredili mevduat limitini aşmadan hesaptan para çek."
- *Geliştirici kodlar*: `hesapTablosu.setBakiye(hesapTablosu.getBakiye() - tutar);`
- *Hata Kaydı*: "Kullanıcı limiti aştığı halde bakiye eksiye düştü, neden hata fırlatılmadı?"

### Temiz DDD Yaklaşımı:
```java
// Kapsamlı Dil doğrudan kodun kendisidir!
public void withdraw(Money amount) {
    if (amount.isGreaterThan(availableFunds())) {
        throw new InsufficientFundsException(accountNumber, amount, availableFunds());
    }
    this.balance = this.balance.subtract(amount);
    recordEvent(new AccountDebitedEvent(accountNumber, amount, Instant.now()));
}
```

---

## 4. Anemik vs. Zengin Domain Modelleri

### Anemik Model Anti-Deseni (Martin Fowler):
Yalnızca getter ve setter'lardan ibaret olan, hiçbir davranış barındırmayan veri torbalarıdır. Tüm iş mantığı monolitik, prosedürel "Service" sınıflarına sızar.

```java
// ANEMİK: Korumasız veri durumu, sıfır iş kuralı
public class AnemicAccount {
    private String id;
    private BigDecimal balance;
    
    public BigDecimal getBalance() { return balance; }
    public void setBalance(BigDecimal balance) { this.balance = balance; }
}
```
**Neden Tehlikelidir?**:
- Herhangi bir kod `setBalance(new BigDecimal("-1000000"))` çağırabilir.
- Kurallar birden fazla servis/controller katmanında kopyalanır.
- Veri ile davranış ayrıldığı için eşzamanlılık (concurrency) hataları kaçınılmazdır.

---

## 5. Modern Java 27 ile Zengin Domain Modeli

Zengin bir domain modelinde durum (state) ve davranış (behavior) bir aradadır. Bir varlık asla geçersiz bir durumda oluşturulamaz ve mutasyona uğratılamaz.

```java
public class BankAccount extends AggregateRoot<AccountNumber> {

    private Money balance;
    private final OverdraftLimit overdraftLimit;

    public BankAccount(AccountNumber id, OverdraftLimit overdraftLimit) {
        super(id);
        this.balance = Money.zero(overdraftLimit.currency());
        this.overdraftLimit = Objects.requireNonNull(overdraftLimit);
    }

    public void deposit(Money amount) {
        if (!amount.isPositive()) {
            throw new DomainValidationException("Yatırılan tutar pozitif olmalıdır.");
        }
        this.balance = this.balance.add(amount);
        recordEvent(new AccountDepositedEvent(id, amount, Instant.now()));
    }

    public void withdraw(Money amount) {
        Money totalAvailable = this.balance.add(overdraftLimit.amount());
        if (amount.isGreaterThan(totalAvailable)) {
            throw new InsufficientFundsException(id, amount, totalAvailable);
        }
        this.balance = this.balance.subtract(amount);
        recordEvent(new AccountWithdrawnEvent(id, amount, Instant.now()));
    }
}
```

---

## 6. Özet ve Çıkarımlar

1. **Önce Stratejik, Sonra Taktiksel**: Bounded Context sınırlarını ve Kapsamlı Dili belirlemeden kod yazmayın.
2. **Genel Setter'ları Yok Edin**: `setBalance()` yerine `deposit()`, `withdraw()`, `freeze()` gibi alana özgü metotlar kullanın.
3. **Çekirdeği Saf Tutun**: Domain katmanı asla Spring, JPA veya Jackson kütüphanelerine bağımlı olmamalıdır.
