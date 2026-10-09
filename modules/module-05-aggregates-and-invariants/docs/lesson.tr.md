---
marp: true
theme: default
paginate: true
header: "DDD & Hekzagonal Mimari Masterclass | Modül 05"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Modül 05: Aggregate Kökleri ve Domain Değişmezleri

## İşlemsel Tutarlılık Sınırları ve İş Değişmezlerini Koruma

---

## 1. Aggregate Nedir?

Aggregate, veri değişiklikleri açısından tek bir birim olarak ele alınan ilişkili nesneler (Varlıklar ve Değer Nesneleri) kümesidir:
- **Aggregate Kökü (Root)**: Kümeye tek erişim noktasıdır. Dış nesneler yalnızca kökün referansını tutabilir.
- **Tutarlılık Sınırı**: Her veritabanı işlemi sonunda aggregate içindeki tüm iş kuralları tam olarak sağlanmış olmalıdır.
- **Altın Kural**: Aggregateleri küçük tutun! Diğer aggregatelere nesne referansıyla değil, **yalnızca ID ile** bağlanın.
