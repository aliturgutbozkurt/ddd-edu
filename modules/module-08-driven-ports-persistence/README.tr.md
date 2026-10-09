# Modül 08: Giden (Driven) Portlar ve Kalıcılık (Persistence) Adaptörleri

## 🎯 Öğrenme Hedefleri
- Veritabanından tamamen bağımsız **Giden Portlar (Repository SPI)** tasarlamak.
- Veritabanı tablolarını (`OrderJpaEntity`) saf Domain modellerinden (`Order`) ayrı tutmak.
- İki yönlü haritalamayı (bidirectional mapping) domain modeline zarar vermeden uygulamak.
- Tembel yükleme (lazy-loading) hatalarını ve veritabanı kilitlenmelerini domainden uzak tutmak.
