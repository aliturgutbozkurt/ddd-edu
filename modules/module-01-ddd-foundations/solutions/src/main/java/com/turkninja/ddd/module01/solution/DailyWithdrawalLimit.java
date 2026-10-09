package com.turkninja.ddd.module01.solution;

import com.turkninja.ddd.module01.domain.model.Currency;
import com.turkninja.ddd.module01.domain.model.Money;
import com.turkninja.ddd.shared.domain.DomainValidationException;
import com.turkninja.ddd.shared.domain.ValueObject;

import java.math.BigDecimal;
import java.util.Objects;

/**
 * Value Object specifying the maximum allowable withdrawal per calendar day.
 */
public record DailyWithdrawalLimit(Money limit) implements ValueObject {

    public DailyWithdrawalLimit {
        Objects.requireNonNull(limit, "Daily limit cannot be null");
        if (limit.amount().compareTo(BigDecimal.ZERO) < 0) {
            throw new DomainValidationException("Daily withdrawal limit cannot be negative. Given: " + limit);
        }
    }

    public static DailyWithdrawalLimit of(double amount, Currency currency) {
        return new DailyWithdrawalLimit(Money.of(amount, currency));
    }

    public Currency currency() {
        return limit.currency();
    }
}
