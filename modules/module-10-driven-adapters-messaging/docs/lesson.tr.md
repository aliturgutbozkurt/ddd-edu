---
marp: true
theme: default
paginate: true
header: "DDD & Hekzagonal Mimari Masterclass | Modül 10"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Modül 10: Mesajlaşma ve Dış Servisler İçin Sürülen Adaptörler

## Kafka ve Ödeme Sağlayıcılarını Saf Giden Portlar ile Entegre Etme

---

## 1. Sürülen (Driven) Adaptör Nedir?

Sürülen Adaptör, Uygulama Servisimiz tarafından harici bir dünya ile iletişim kurmak üzere tetiklenir:
- Veritabanları (PostgreSQL, MongoDB).
- Olay kuyrukları (Apache Kafka, RabbitMQ).
- Harici HTTP API servisleri (Stripe, Kargo firmaları).
