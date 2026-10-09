---
marp: true
theme: default
paginate: true
header: "DDD & Hekzagonal Mimari Masterclass | Modül 06"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Modül 06: Domain Olayları ve Olay Tabanlı Ayrıştırma

## Geçmiş İş Gerçeklerini Java 27 Sealed Tipleriyle Modelleme

---

## 1. Domain Olayı (Domain Event) Nedir?

Domain uzmanlarının ilgilendiği, geçmişte gerçekleşmiş bir iş olayını temsil eder:
- **İsimlendirme**: Daima **geçmiş zaman** kipiyle adlandırılır (`OrderPlacedEvent`, `PaymentReceivedEvent`).
- **Değişmezdir**: Geçmiş değiştirilemez; olaylar silinemez veya mutasyona uğratılamaz.
- **İçerik**: Olay kimliği, UTC zaman damgası ve tüketicilerin aksiyon alabilmesi için gerekli domain verilerini barındırır.
