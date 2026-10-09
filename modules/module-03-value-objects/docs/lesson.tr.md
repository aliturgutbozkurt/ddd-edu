---
marp: true
theme: default
paginate: true
header: "DDD & Hekzagonal Mimari Masterclass | Modül 03"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Modül 03: Değer Nesneleri ve Java 27 Record ile Değişmezlik

## İlkel Takıntısını Saf İş Değişmezleriyle Yok Etmek

---

## 1. Değer Nesnesini (Value Object) Tanımlayan Nedir?

Bir Değer Nesnesi kimliğiyle değil, öznitelikleriyle tanımlanır:
1. **Kimliksizdir**: İki nesnenin tüm alanları eşitse nesneler eşittir.
2. **Değişmezdir (Immutable)**: Oluşturulduktan sonra durumu asla değiştirilemez.
3. **Kavramsal Bütündür**: Tek başına anlamlı bir domain kavramıdır (`Money`, `EmailAddress`).
4. **Kendini Doğrular**: Bellekte asla geçersiz bir değer nesnesi var olamaz.
5. **Yan Etkisiz Davranış**: Metotlar var olan durumu değiştirmek yerine daima YENİ bir örnek döndürür.
