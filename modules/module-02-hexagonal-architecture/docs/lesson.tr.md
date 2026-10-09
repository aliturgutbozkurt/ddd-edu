---
marp: true
theme: default
paginate: true
header: "DDD & Hekzagonal Mimari Masterclass | Modül 02"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Modül 02: Hekzagonal Mimari (Ports and Adapters) Taslağı

## Uzun Ömürlü Yazılımlar İçin Bağımlılıkları Tersine Çevirme

---

## 1. Geleneksel Katmanlı Mimarinin Sorunları

Klasik 3 katmanlı mimari (Controller -> Service -> DAO/Repository), yazılımcıyı veritabanı merkezli düşünmeye zorlar:

```
[UI / Controller] ──> [İş Servisi] ──> [Veritabanı / JPA Varlığı]
```

### Tehlikeler:
1. **Veritabanı Bağımlılığı**: Domain modelleri veritabanı tablolarının anlamsız aynalarına dönüşür (`@Entity`, `@Table`).
2. **Framework Sızıntısı**: Spring anotasyonları (`@Service`, `@Autowired`) iş kurallarını kirletir.
3. **Zor Test Edilebilirlik**: İş kuralını test etmek için veritabanı mocklamak veya Spring ayağa kaldırmak gerekir.

---

## 2. Hekzagonal Çözüm (Alistair Cockburn)

Hekzagonal mimari, **Saf Domain Çekirdeğini** merkeze yerleştirir. Dış dünya ile iletişim yalnızca **Portlar** üzerinden gerçekleşir:

```
[Süren Adaptör: REST / CLI]
           │
           ▼
[Gelen Port: Use Case Arayüzü]
           │
           ▼
[Uygulama Servisi] ──> [Domain Modeli]
           │
           ▼
[Giden Port: SPI Arayüzü]
           ▲
           │
[Sürülen Adaptör: PostgreSQL / Kafka]
```

### Temel Kural:
**Bağımlılıklar daima içe doğru işaret eder.** Domain dış dünyadan tamamen habersizdir.
