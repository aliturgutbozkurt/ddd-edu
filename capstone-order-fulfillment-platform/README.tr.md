# 🎓 Bitirme Projesi: Kurumsal Sipariş ve Dağıtım Platformu

## 🎯 Mimari Genel Bakış
Bu bitirme projesi, gerçek dünya standartlarında tam donanımlı kurumsal bir sistem sunar:
- **İki Bağımsız Bounded Context**: Sipariş Bağlamı (Ordering) ve Dağıtım Bağlamı (Fulfillment).
- **Hekzagonal Mimari**: Süren ve Sürülen portlarla tam katman izolasyonu.
- **Transactional Outbox Deseni**: Veritabanı ve Kafka arasında sıfır veri kaybı garantisi.
- **Yozlaşma Önleme Katmanı (ACL)**: Bounded context'ler arasında temiz sınır koruması.
- **Otomatik ArchUnit Test Paketi**: Bağlamların birbirine sızmadığını doğrulayan mimari testler.
