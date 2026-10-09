# Modül 01: Domain-Driven Design Temelleri ve Kapsamlı Dil (Ubiquitous Language)

## 🎯 Öğrenme Hedefleri
- **Stratejik Domain-Driven Design (DDD)** felsefesini kavramak.
- **Çekirdek Alan (Core Domain)**, **Destekleyici Alt Alan (Supporting Subdomain)** ve **Genel Alt Alan (Generic Subdomain)** ayrımlarını öğrenmek.
- **Anemik Domain Modeli (Anemic Domain Model)** anti-deseninin nesne yönelimli enkapsülasyonu nasıl ihlal ettiğini görmek.
- Framework kirliliği olmadan saf Java 27 ile **Zengin Domain Modeli (Rich Domain Model)** inşa etmek.
- Bir FinTech bankacılık bağlamı için net bir **Kapsamlı Dil (Ubiquitous Language)** sözlüğü oluşturmak.

---

## 📂 Modül Yapısı
- `docs/lesson.tr.md`: Kapsamlı Türkçe ders anlatımı (Marp/PDF uyumlu).
- `docs/lesson.md`: İngilizce ders içeriği.
- `src/main/java/`: Anemik ve Zengin model karşılaştırmalı çalıştırılabilir örnek kodlar.
- `src/test/java/`: Saf domain birim testleri ve ArchUnit mimari testleri.
- `exercises/`: Kredili mevduat ve işlem geçmişi iş kurallarını uygulama ödevi.
- `solutions/`: Eğitmen referans çözümü.

---

## ⚡ Hızlı Başlangıç
```bash
# Modül 01 testlerini çalıştır
./mvnw test -pl modules/module-01-ddd-foundations
```
