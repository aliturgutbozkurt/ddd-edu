package com.turkninja.ddd.module02.domain.model;

import com.turkninja.ddd.shared.domain.DomainValidationException;
import com.turkninja.ddd.shared.domain.ValueObject;

import java.math.BigDecimal;
import java.util.Objects;

public record ProductPrice(BigDecimal amount, String currency) implements ValueObject {
    public ProductPrice {
        Objects.requireNonNull(amount, "Price amount must not be null");
        Objects.requireNonNull(currency, "Currency must not be null");
        if (amount.compareTo(BigDecimal.ZERO) < 0) {
            throw new DomainValidationException("Product price cannot be negative: " + amount);
        }
    }

    public static ProductPrice of(double amount, String currency) {
        return new ProductPrice(BigDecimal.valueOf(amount), currency);
    }
}
