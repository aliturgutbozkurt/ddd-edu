package com.turkninja.ddd.module02.solution;

import com.turkninja.ddd.module02.domain.model.Product;
import com.turkninja.ddd.module02.domain.model.ProductId;
import com.turkninja.ddd.module02.domain.model.ProductPrice;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.math.BigDecimal;

import static org.assertj.core.api.Assertions.assertThat;

@DisplayName("Solution 02: Hexagonal Discount Calculation")
class DiscountSolutionTest {

    @Test
    @DisplayName("Should apply 20% discount policy correctly via Outbound Port")
    void testDiscountCalculation() {
        DiscountPolicyPort stubPolicy = tier -> "VIP".equalsIgnoreCase(tier) ? new BigDecimal("0.20") : BigDecimal.ZERO;
        DiscountApplicationService service = new DiscountApplicationService(stubPolicy);

        Product product = new Product(ProductId.generate(), "Software Architecture Book", ProductPrice.of(100.00, "USD"));

        ProductPrice vipPrice = service.calculateDiscountedPrice(product, "VIP");
        assertThat(vipPrice.amount()).isEqualByComparingTo("80.00");

        ProductPrice regularPrice = service.calculateDiscountedPrice(product, "STANDARD");
        assertThat(regularPrice.amount()).isEqualByComparingTo("100.00");
    }
}
