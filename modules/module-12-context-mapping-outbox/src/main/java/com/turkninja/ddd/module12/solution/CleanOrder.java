package com.turkninja.ddd.module12.solution;

import com.turkninja.ddd.shared.domain.ValueObject;

import java.math.BigDecimal;
import java.util.Objects;

/**
 * Clean bounded context domain representation.
 */
public record CleanOrder(
        String orderNumber,
        String customerName,
        BigDecimal totalAmount,
        String currency
) implements ValueObject {
    public CleanOrder {
        Objects.requireNonNull(orderNumber, "orderNumber cannot be null");
        Objects.requireNonNull(customerName, "customerName cannot be null");
        Objects.requireNonNull(totalAmount, "totalAmount cannot be null");
        Objects.requireNonNull(currency, "currency cannot be null");
    }
}
