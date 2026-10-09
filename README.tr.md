# 🏛️ Java ile Domain-Driven Design & Hekzagonal Mimari Masterclass

[![Java 27](https://img.shields.io/badge/Java-27%20LTS-orange.svg)](https://openjdk.org/)
[![Spring Boot 4](https://img.shields.io/badge/Spring%20Boot-4.0%2B-brightgreen.svg)](https://spring.io/projects/spring-boot)
[![Mimari](https://img.shields.io/badge/Mimari-Hekzagonal%20%2F%20Port%20ve%20Adapt%C3%B6rler-blue.svg)](https://alistair.cockburn.us/hexagonal-architecture/)
[![Metodoloji](https://img.shields.io/badge/Metodoloji-Spec--Driven%20Development%20(SDD)-purple.svg)](./SPEC.md)
[![Lisans](https://img.shields.io/badge/Lisans-MIT-yellow.svg)](./LICENSE)
[![Bilingual](https://img.shields.io/badge/Dil-English%20%7C%20T%C3%BCrk%C3%A7e-red.svg)](./README.md)

> **Müfredat Hedefi**: Eylül 2026 Standartları  
> **İngilizce Dokümantasyon**: [README.md](./README.md)  
> **Geliştirme Metodolojisi**: Addy Osmani'nin SDD (Spec-Driven Development) İş Akışı  

**Domain-Driven Design (DDD - Alana Dayalı Tasarım)** ve **Hekzagonal Mimari (Ports and Adapters)** kapsamlı eğitim deposuna hoş geldiniz. Bu müfredat, soyut mimari teorileri gerçek dünya, üretime hazır kurumsal Java uygulamalarıyla buluşturmak için tasarlanmıştır.

---

## 🎯 Kursun Öne Çıkan Özellikleri

- **Saf Domain Çekirdeği (Pure Domain Core)**: Domain mantığı içerisinde kesinlikle framework bağımlılığı bulunmaz (`org.springframework.*` veya `jakarta.persistence.*` kullanmak yasaktır).
- **Hekzagonal Mimari**: Kullanım senaryolarının (Use Cases) Gelen (Driving) ve Giden (Driven) Portlar üzerinden dış dünyadan tamamen izole edilmesi.
- **Modern Java 27 Özellikleri**: Compact constructor ile kendini doğrulayan Java Record Değer Nesneleri (Value Objects), Sealed Interface ile modellenen Domain Olayları (Domain Events), Switch Pattern Matching ve Virtual Threads (Project Loom).
- **Otomatik Mimari Denetimi (ArchUnit)**: Mimari kuralların bozulmasını sürekli engelleyen otomatik ArchUnit testleri.
- **Spec-Driven Development (SDD)**: Addy Osmani'nin spec-first iş akışı (`SPEC.md` ➔ `plan.md` ➔ `todo.md` ➔ Geliştirme ➔ ArchUnit Doğrulama).
- **Çift Format ve Çift Dil**: Her modülde derinlemesine `.md` ders anlatımları, tek tıkla derlenen `.pdf` versiyonları, öğrenci alıştırmaları (`exercises/`) ve doğrulanmış referans çözümleri (`solutions/`) hem **Türkçe** hem **İngilizce** sunulur.
- **Kurumsal Bitirme Projesi (Capstone)**: Transactional Outbox, Kafka olay akışı ve Testcontainers içeren çoklu Bounded Context E-Ticaret Sipariş ve Dağıtım platformu.

---

## 📐 Hekzagonal Mimari Şeması

```
                            ┌──────────────────────────────────────────────┐
                            │               ALTYAPI (INFRASTRUCTURE)       │
                            │  ┌────────────────────────────────────────┐  │
                            │  │            UYGULAMA (APPLICATION)      │  │
 [Süren Adaptör - Driving]  │  │  ┌──────────────────────────────────┐  │  │ [Sürülen Adaptör - Driven]
 REST Denetleyicisi         ─┼──┼─>│ Süren Port (Use Case)           │  │  ├─┼─> PostgreSQL / JPA
 CLI Komut Koşucusu         ─┼──┼─>│                                   │  │  ├─┼─> Kafka Olay Yayıncısı
 Kafka Mesaj Tüketicisi     ─┼──┼─>│       Uygulama Servisi            │  │  ├─┼─> Ödeme Ağ Geçidi SPI
                            │  │  │                │                 │  │  │
                            │  │  │                ▼                 │  │  │
                            │  │  │  ┌────────────────────────────┐  │  │  │
                            │  │  │  │        SAF DOMAIN          │  │  │  │
                            │  │  │  │  - Varlıklar & Aggregateler│  │  │  │
                            │  │  │  │  - Değer Nesneleri (Record)│  │  │  │
                            │  │  │  │  - İş Mantığı Değişmezleri │  │  │  │
                            │  │  │  │  - Domain Olayları (Sealed)│  │  │  │
                            │  │  │  │  - Domain Servisleri       │  │  │  │
                            │  │  │  └────────────────────────────┘  │  │  │
                            │  │  │                │                 │  │  │
                            │  │  │                ▼                 │  │  │
                            │  │  │  Sürülen Port (Repository SPI)   │  │  │
                            │  │  └──────────────────────────────────┘  │  │
                            │  └────────────────────────────────────────┘  │
                            └──────────────────────────────────────────────┘
```

---

## 📚 12 Modüllük Eğitim Planı

| # | Modül Klasörü | Temel Domain Kavramları | Teknik ve Hekzagonal Odak | Ders & PDF |
|---|---|---|---|---|
| **01** | [`module-01-ddd-foundations`](./modules/module-01-ddd-foundations) | Kapsamlı Dil (Ubiquitous Language), Alt Alanlar | Anemik vs Zengin Domain Modeli | [TR](./modules/module-01-ddd-foundations/docs/lesson.tr.md) · [EN](./modules/module-01-ddd-foundations/docs/lesson.md) |
| **02** | [`module-02-hexagonal-architecture`](./modules/module-02-hexagonal-architecture) | Portlar ve Adaptörler, Bağımlılık Tersine Çevirme | Katman sınırları ve paket yapısı | [TR](./modules/module-02-hexagonal-architecture/docs/lesson.tr.md) · [EN](./modules/module-02-hexagonal-architecture/docs/lesson.md) |
| **03** | [`module-03-value-objects`](./modules/module-03-value-objects) | Değişmezlik (Immutability), Değer Eşitliği | Java 27 Record & Compact Constructors | [TR](./modules/module-03-value-objects/docs/lesson.tr.md) · [EN](./modules/module-03-value-objects/docs/lesson.md) |
| **04** | [`module-04-entities-and-identity`](./modules/module-04-entities-and-identity) | Kimlik (Identity), Varlık Eşitliği, Yaşam Döngüsü | Kimlik Tipleri, Doğal vs Yapay Kimlikler | [TR](./modules/module-04-entities-and-identity/docs/lesson.tr.md) · [EN](./modules/module-04-entities-and-identity/docs/lesson.md) |
| **05** | [`module-05-aggregates-and-invariants`](./modules/module-05-aggregates-and-invariants) | Aggregate Kökleri, Tutarlılık Sınırları | Çoklu Varlık Değişmezleri (Invariants) | [TR](./modules/module-05-aggregates-and-invariants/docs/lesson.tr.md) · [EN](./modules/module-05-aggregates-and-invariants/docs/lesson.md) |
| **06** | [`module-06-domain-events`](./modules/module-06-domain-events) | Domain Olayları, Yan Etki Ayrıştırması | Java 27 Sealed Interface & Dağıtıcı SPI | [TR](./modules/module-06-domain-events/docs/lesson.tr.md) · [EN](./modules/module-06-domain-events/docs/lesson.md) |
| **07** | [`module-07-driving-ports-use-cases`](./modules/module-07-driving-ports-use-cases) | Süren Portlar, Uygulama Servisleri | CQRS Lite, Komut İşleyiciler ve DTO Haritalama | [TR](./modules/module-07-driving-ports-use-cases/docs/lesson.tr.md) · [EN](./modules/module-07-driving-ports-use-cases/docs/lesson.md) |
| **08** | [`module-08-driven-ports-persistence`](./modules/module-08-driven-ports-persistence) | Sürülen Portlar, Repository SPI | Spring Data JPA / JDBC Adaptörleri, Mappers | [TR](./modules/module-08-driven-ports-persistence/docs/lesson.tr.md) · [EN](./modules/module-08-driven-ports-persistence/docs/lesson.md) |
| **09** | [`module-09-driving-adapters-rest`](./modules/module-09-driving-adapters-rest) | REST Adaptörleri, Problem Details (RFC 9457) | Spring Boot 4 Virtual Threads (Loom) | [TR](./modules/module-09-driving-adapters-rest/docs/lesson.tr.md) · [EN](./modules/module-09-driving-adapters-rest/docs/lesson.md) |
| **10** | [`module-10-driven-adapters-messaging`](./modules/module-10-driven-adapters-messaging) | Dış Servis SPI'ları, Kafka Olay Akışı | Dayanıklı RestClient ve Testcontainers | [TR](./modules/module-10-driven-adapters-messaging/docs/lesson.tr.md) · [EN](./modules/module-10-driven-adapters-messaging/docs/lesson.md) |
| **11** | [`module-11-architecture-testing-archunit`](./modules/module-11-architecture-testing-archunit) | Kod Olarak Mimari, Uygunluk Fonksiyonları | ArchUnit 1.4+ Hekzagonal Kural Paketi | [TR](./modules/module-11-architecture-testing-archunit/docs/lesson.tr.md) · [EN](./modules/module-11-architecture-testing-archunit/docs/lesson.md) |
| **12** | [`module-12-context-mapping-outbox`](./modules/module-12-context-mapping-outbox) | Bağlam Eşleme, Yozlaşma Önleme Katmanı (ACL) | Transactional Outbox Deseni & At-Least-Once | [TR](./modules/module-12-context-mapping-outbox/docs/lesson.tr.md) · [EN](./modules/module-12-context-mapping-outbox/docs/lesson.md) |
| **🏁** | [`capstone-order-fulfillment-platform`](./capstone-order-fulfillment-platform) | Kurumsal Çoklu Bounded Context Sistemi | Tam Hekzagonal Paket, Kafka, Outbox & Docker | [TR](./capstone-order-fulfillment-platform/docs/lesson.tr.md) · [EN](./capstone-order-fulfillment-platform/docs/lesson.md) |

---

## 🚀 Hızlı Başlangıç ve Öğrenci Rehberi

### Gereksinimler
- JDK 25 veya 27 (OpenJDK / Temurin tavsiye edilir)
- Docker Desktop veya OrbStack (PostgreSQL ve Kafka çalıştırmak için)
- Maven 3.9+ (veya proje içerisindeki `./mvnw` wrapper aracı)

### Projeyi Derleme ve Testleri Çalıştırma
```bash
# Tüm modülleri derle, domain birim testlerini ve ArchUnit kurallarını doğrula
./mvnw clean test

# Yalnızca belirli bir modülün testlerini çalıştır
./mvnw test -pl modules/module-05-aggregates-and-invariants

# Sadece mimari uygunluk (ArchUnit) testlerini çalıştır
./mvnw test -Dtest=*ArchitectureTest
```

### Yerel Altyapıyı Başlatma (Docker Compose)
```bash
# PostgreSQL (5432), Kafka (9092) ve Mailpit (8025) servislerini başlat
docker compose up -d

# Servis durumlarını kontrol et
docker compose ps

# Çalışma bitince servisleri kapat
docker compose down -v
```

### Ders PDF Belgelerini Üretme
```bash
# Tüm modüllerin ders anlatımlarını Türkçe ve İngilizce PDF formatına dönüştür
./scripts/generate-pdfs.sh

# Veya sadece belirli bir modül için üret
./scripts/generate-pdfs.sh module-03
```

---

## 🛠️ Spec-Driven Development (SDD) İş Akışı

Bu proje, Addy Osmani'nin Spec-Driven Development yaklaşımını uygular:

1. **Önce Şartname (Spec First)**: Domain gereksinimleri, değişmezler ve port sözleşmeleri için [`SPEC.md`](./SPEC.md) ve [`specs/`](./specs/) inceleyin.
2. **Uygulama Planı**: Mimari aşamalar ve sıralama için [`plan.md`](./plan.md) dosyasını inceleyin.
3. **Görev Takibi**: Görev ilerlemesi için [`todo.md`](./todo.md) ve [GitHub Issues](https://github.com/aliturgutbozkurt/ddd-edu/issues) takip edin.
4. **Geliştirici Kuralları**: Mimari kurallar ve kodlama standartları için [`CLAUDE.md`](./CLAUDE.md) dosyasını referans alın.

---

## 📄 Lisans
Bu eğitim projesi [MIT Lisansı](./LICENSE) kapsamında açık kaynak olarak sunulmuştur.
