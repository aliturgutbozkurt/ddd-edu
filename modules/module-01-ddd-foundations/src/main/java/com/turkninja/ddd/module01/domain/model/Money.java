package com.turkninja.ddd.module01.domain.model;

import com.turkninja.ddd.shared.domain.DomainValidationException;
import com.turkninja.ddd.shared.domain.ValueObject;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.Objects;

/**
 * Value Object representing monetary value with currency.
 * Invariant: Amount is rounded to 2 decimal places; operations only allowed on matching currency.
 */
public record Money(BigDecimal amount, Currency currency) implements ValueObject, Comparable<Money> {

    public Money {
        Objects.requireNonNull(amount, "Amount must not be null");
        Objects.requireNonNull(currency, "Currency must not be null");
        amount = amount.setScale(2, RoundingMode.HALF_EVEN);
    }

    public static Money of(double amount, Currency currency) {
        return new Money(BigDecimal.valueOf(amount), currency);
    }

    public static Money of(String amount, Currency currency) {
        return new Money(new BigDecimal(amount), currency);
    }

    public static Money zero(Currency currency) {
        return new Money(BigDecimal.ZERO, currency);
    }

    public Money add(Money other) {
        assertSameCurrency(other);
        return new Money(this.amount.add(other.amount), this.currency);
    }

    public Money subtract(Money other) {
        assertSameCurrency(other);
        return new Money(this.amount.subtract(other.amount), this.currency);
    }

    public boolean isPositive() {
        return this.amount.compareTo(BigDecimal.ZERO) > 0;
    }

    public boolean isGreaterThan(Money other) {
        assertSameCurrency(other);
        return this.compareTo(other) > 0;
    }

    private void assertSameCurrency(Money other) {
        Objects.requireNonNull(other, "Money operand cannot be null");
        if (this.currency != other.currency) {
            throw new DomainValidationException(
                    "Cannot perform monetary operation across currencies: " + this.currency + " vs " + other.currency);
        }
    }

    @Override
    public int compareTo(Money o) {
        assertSameCurrency(o);
        return this.amount.compareTo(o.amount);
    }
}
