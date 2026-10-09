---
marp: true
theme: default
paginate: true
header: "DDD & Hekzagonal Mimari Masterclass | Modül 12"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Modül 12: Bağlam Eşleme ve Transactional Outbox Deseni

## Dağıtık Bounded Context'leri Güvenilir Şekilde Birbirine Bağlama

---

## 1. Çift Yazma (Dual-Write) Problemi Nedir?

Aynı işlem içinde hem SQL veritabanına yazıp hem Kafka'ya mesaj gönderirken:
- Veritabanı başarılı olup Kafka çökerse, olaylar kaybolur!
- Kafka başarılı olup veritabanı rollback olursa, hayalet olaylar yayınlanmış olur!

---

## 2. Transactional Outbox Çözümü

Aggregate durumunu ve olay kaydını **AYNI yerel SQL transaction'ı** içinde kaydedin:
```
[SQL Transaction: BAŞLAT]
  1. INSERT INTO siparisler (...)
  2. INSERT INTO outbox_olaylari (id, payload, durum='BEKLIYOR')
[SQL Transaction: COMMIT]
```
Arka plandaki bağımsız bir iş parçacığı bekleyen kayıtları Kafka'ya güvenle basar.
