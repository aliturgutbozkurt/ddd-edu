# Alıştırma 11: Özel ArchUnit Port ve Adaptör Kuralları Yazma

## Amaç
Hekzagonal Mimari kurallarını CI/CD aşamasında otomatik denetleyen ArchUnit mimari uygunluk fonksiyonları yazın:
1. Giriş sürüş portları `UseCase` ile biten arayüzler (interface) olmalıdır.
2. Çıkış sürülen portları `Port` ile biten arayüzler olmalıdır.
3. Domain varlıkları asla Spring veya Jackson kütüphanelerine bağımlı olmamalıdır.

## Testleri Çalıştırma
`src/test/java/com/turkninja/ddd/module11/exercise/CustomArchRuleExerciseTest.java` dosyasındaki `@Disabled` notunu kaldırıp testleri çalıştırın.
