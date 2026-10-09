# Modül 05: Aggregate Kökleri ve Domain Değişmezleri (Invariants)

## 🎯 Öğrenme Hedefleri
- **Aggregate Desenini** işlemsel tutarlılık sınırı (consistency boundary) olarak kavramak.
- Alt varlıkları (`OrderItem`) yalnızca **Aggregate Kökü (`Order`)** üzerinden yönetmek.
- Çoklu varlık iş değişmezlerini (ör. maksimum kalem sayısı, toplam tutar hesaplaması) korumak.
- Savunmacı kopyalama (unmodifiable collections) ile referans sızıntılarını engellemek.
