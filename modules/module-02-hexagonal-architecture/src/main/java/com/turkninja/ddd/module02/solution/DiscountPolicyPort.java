package com.turkninja.ddd.module02.solution;

import java.math.BigDecimal;

public interface DiscountPolicyPort {
    BigDecimal getDiscountPercentage(String customerTier);
}
