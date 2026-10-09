package com.turkninja.ddd.module02.solution;

import com.turkninja.ddd.module02.domain.model.Product;
import com.turkninja.ddd.module02.domain.model.ProductPrice;

import java.math.BigDecimal;
import java.util.Objects;

public class DiscountApplicationService implements CalculateDiscountUseCase {

    private final DiscountPolicyPort discountPolicyPort;

    public DiscountApplicationService(DiscountPolicyPort discountPolicyPort) {
        this.discountPolicyPort = Objects.requireNonNull(discountPolicyPort);
    }

    @Override
    public ProductPrice calculateDiscountedPrice(Product product, String customerTier) {
        BigDecimal discountPercent = discountPolicyPort.getDiscountPercentage(customerTier);
        BigDecimal originalAmount = product.getPrice().amount();
        BigDecimal discountFactor = BigDecimal.ONE.subtract(discountPercent);
        BigDecimal discountedAmount = originalAmount.multiply(discountFactor);

        return new ProductPrice(discountedAmount, product.getPrice().currency());
    }
}
