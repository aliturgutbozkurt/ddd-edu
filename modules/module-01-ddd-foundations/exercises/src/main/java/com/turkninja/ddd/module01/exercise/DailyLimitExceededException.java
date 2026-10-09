package com.turkninja.ddd.module01.exercise;

import com.turkninja.ddd.module01.domain.model.Money;

public class DailyLimitExceededException extends RuntimeException {

    private final Money requestedAmount;
    private final Money remainingDailyLimit;

    public DailyLimitExceededException(Money requestedAmount, Money remainingDailyLimit) {
        super(String.format("Daily limit exceeded. Requested: %s, Remaining Limit: %s",
                requestedAmount, remainingDailyLimit));
        this.requestedAmount = requestedAmount;
        this.remainingDailyLimit = remainingDailyLimit;
    }

    public Money getRequestedAmount() {
        return requestedAmount;
    }

    public Money getRemainingDailyLimit() {
        return remainingDailyLimit;
    }
}
