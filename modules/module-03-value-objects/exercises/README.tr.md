# Alıştırma 03: Vergi Numarası ve Posta Kodu Değer Nesnelerini Kodlama

## 🎯 İş Bağlamı
Faturalandırma hatalarını önlemek için kurumsal vergi kimlik numaraları ve posta kodları sıkı kurallarla doğrulanmalıdır.

## 📋 Kabul Kriterleri
1. `TaxNumber`: Tam olarak 10 sayısal basamaktan oluşmalıdır.
2. `TaxNumber`: Tamamı sıfırlardan oluşamaz (`0000000000` geçersizdir).
3. `PostalCode`: Boşluklardan arındırılmış (trimmed) ve dolu olmalıdır.
4. Compact constructor geçersiz durumlarda `DomainValidationException` fırlatmalıdır.
