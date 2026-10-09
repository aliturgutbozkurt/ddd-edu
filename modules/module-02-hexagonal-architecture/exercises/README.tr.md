# Alıştırma 02: Monolitik İndirim Mantığını Hekzagonal Portlara Dönüştürme

## 🎯 İş Bağlamı
Pazarlama departmanı ürünlere dinamik indirim politikaları uygulamak istiyor. Şu anda indirimler eski statik bir sınıfta sabit kodlanmış durumda.

## 📋 Kabul Kriterleri
1. Gelen Port tanımlayın: `CalculateDiscountUseCase` (`Money applyDiscount(ProductId id, CustomerTier tier)`).
2. Giden Port tanımlayın: `DiscountPolicyPort` (`BigDecimal getDiscountPercentage(CustomerTier tier)`).
3. Gelen Portu uygulayan ve Giden Portu kullanan bir Uygulama Servisi yazın.
4. İki sürülen adaptör yazın: `StandardDiscountPolicyAdapter` (%0 indirim) ve `VipDiscountPolicyAdapter` (%15 indirim).
5. Domain mantığı kesinlikle saf Java kalmalı, framework bağımlılığı içermemelidir.
