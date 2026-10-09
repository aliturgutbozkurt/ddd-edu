package com.turkninja.ddd.module02.solution;

import com.turkninja.ddd.module02.domain.model.Product;
import com.turkninja.ddd.module02.domain.model.ProductPrice;

import java.math.BigDecimal;

public interface CalculateDiscountUseCase {
    ProductPrice calculateDiscountedPrice(Product product, String customerTier);
}
