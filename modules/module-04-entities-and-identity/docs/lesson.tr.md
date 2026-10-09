---
marp: true
theme: default
paginate: true
header: "DDD & Hekzagonal Mimari Masterclass | Modül 04"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Modül 04: Varlıklar, Kimlik ve Yaşam Döngüsü

## Sürekliliği Korumak ve Durum Değişikliklerini Kapsüllemek

---

## 1. Varlık (Entity) Nedir?

Varlık, zaman içinde sürekliliği olan ve **kimliğiyle (identity)** ayırt edilen bir domain nesnesidir:
- Bir müşterinin adı, adresi veya e-postası değişse bile aynı müşteri olmaya devam eder.
- Aynı isme ve doğum tarihine sahip iki kişi, müşteri numaraları (`CustomerId`) farklıysa farklı varlıklardır.
