# Çözüm 11: ArchUnit ile Mimari Uygunluk Fonksiyonları

## Mimari İçgörü
Dokümanlardaki mimari şemalar hızla güncelliğini yitirir. Çalıştırılabilir ArchUnit kuralları, bir geliştirici domain içine yanlışlıkla Spring repository'si eklediğinde veya isimlendirme kurallarını ihlal ettiğinde build'i anında kırar.

## Önemli Dosyalar
- `CustomHexagonalRules.java`: Yeniden kullanılabilir statik ArchUnit kuralları.
- `CustomHexagonalRulesSolutionTest.java`: Kuralları doğrulayan test paketi.
