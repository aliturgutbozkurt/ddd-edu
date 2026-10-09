package com.turkninja.ddd.module01.domain.model;

import com.turkninja.ddd.shared.domain.DomainValidationException;
import com.turkninja.ddd.shared.domain.ValueObject;

import java.math.BigDecimal;
import java.util.Objects;

/**
 * Value Object defining authorized negative overdraft tolerance.
 */
public record OverdraftLimit(Money amount) implements ValueObject {

    public OverdraftLimit {
        Objects.requireNonNull(amount, "Overdraft amount cannot be null");
        if (amount.amount().compareTo(BigDecimal.ZERO) < 0) {
            throw new DomainValidationException("Overdraft limit cannot be negative. Given: " + amount);
        }
    }

    public static OverdraftLimit zero(Currency currency) {
        return new OverdraftLimit(Money.zero(currency));
    }

    public static OverdraftLimit of(double amount, Currency currency) {
        return new OverdraftLimit(Money.of(amount, currency));
    }

    public Currency currency() {
        return amount.currency();
    }
}
