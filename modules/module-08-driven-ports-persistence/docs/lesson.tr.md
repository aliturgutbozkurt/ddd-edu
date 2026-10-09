---
marp: true
theme: default
paginate: true
header: "DDD & Hekzagonal Mimari Masterclass | Modül 08"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Modül 08: Giden (Driven) Portlar ve Kalıcılık Adaptörleri

## Veritabanını Domain Mantığından Tamamen Ayrıştırmak

---

## 1. Neden Domain Varlıklarında JPA Anotasyonları Kullanılmaz?

Domain sınıflarına `@Entity`, `@Table` koymak Hekzagonal Mimariyi bozar:
- JPA varsayılan parametresiz yapıcı (no-arg constructor) ister (değişmezlik doğrulamalarını deler).
- JPA final olmayan alanlar ve değiştirilebilir koleksiyonlar bekler.
- Veritabanı şema değişiklikleri domain modelini zorla değiştirmeye sebep olur.
