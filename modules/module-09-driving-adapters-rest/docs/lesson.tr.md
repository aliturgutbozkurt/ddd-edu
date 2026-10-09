---
marp: true
theme: default
paginate: true
header: "DDD & Hekzagonal Mimari Masterclass | Modül 09"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Modül 09: Spring Boot 4 ile Süren Adaptörler (REST ve Sanal İş Parçacıkları)

## Hekzagonal Kullanım Senaryolarını REST ve Problem Details ile Dışa Açma

---

## 1. Süren (Driving) Adaptör Nedir?

Süren Adaptör, sistemimizle etkileşimi başlatan dış katman unsurudur:
- HTTP isteklerini, CLI komutlarını veya mesaj kuyruğu verilerini yakalar.
- Protokole özgü JSON gövdesini tipe güvenli bir **Use Case Komutuna (Command)** dönüştürür.
- Gelen Port (Inbound Port) arayüzünü tetikler.
- Dönen sonucu veya fırlatılan domain istisnasını protokol yanıtına (ör. HTTP 201 veya RFC 9457 Problem Details) çevirir.
