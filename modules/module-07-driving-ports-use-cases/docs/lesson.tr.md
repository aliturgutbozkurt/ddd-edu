---
marp: true
theme: default
paginate: true
header: "DDD & Hekzagonal Mimari Masterclass | Modül 07"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Modül 07: Gelen (Driving) Portlar ve Uygulama Servisleri

## Domain Mantığını Kirletmeden Kullanım Senaryolarını Yönetme

---

## 1. Gelen (Driving) Port Nedir?

Gelen Port, uygulamanın dış dünyaya sunduğu somut bir kullanım senaryosunu (Use Case) temsil eder:
- `application/port/in/` paketinde tanımlanan saf bir **Java arayüzüdür**.
- Dış adaptörler (REST Controller, CLI, Kafka dinleyicisi) yalnızca bu arayüzle konuşur.
