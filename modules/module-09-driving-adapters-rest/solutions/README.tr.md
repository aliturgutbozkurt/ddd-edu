# Çözüm 09: RFC 9457 Problem Details Dönüşümü

## Mimari Bakış
Hekzagonal Mimaride HTTP durum kodları, JSON serileştirme ve RFC 9457 yükleri yalnızca **Sürüş Adaptörü (Altyapı)** katmanına aittir. Domain modeli asla HTTP 400, 404 veya JSON yapılarını bilmez.

## Önemli Dosyalar
- `ProblemDetailRecord.java`: RFC 9457 standardını temsil eden Java 27 record yapısı.
- `GlobalExceptionHandler.java`: Domain istisnalarını RFC 9457 formatına dönüştüren adaptör sınıfı.
- `GlobalExceptionHandlerSolutionTest.java`: %100 başarılı çalışan test paketi.
