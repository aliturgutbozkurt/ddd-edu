---
marp: true
theme: default
paginate: true
header: "DDD & Hekzagonal Mimari Masterclass | Modül 11"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Modül 11: ArchUnit ile Otomatik Mimari Denetimi

## Kod Olarak Mimari: Hekzagonal Sınırları Derleme Zamanında Güvenceye Alma

---

## 1. Mimari Erozyon Nedir?

Otomatik denetimler olmadan yazılım projeleri zamanla çürür:
- Ekibe yeni katılan biri domain varlığı içine Spring'in `@Transactional` anotasyonunu ekler.
- Bir REST denetleyicisi Port katmanını atlayıp doğrudan veritabanı tablosuna yazar.
- Sonuç: Hekzagonal mimari çöker ve yine monolitik çamura dönüşür.
