package com.turkninja.ddd.module01.domain.exception;

import com.turkninja.ddd.module01.domain.model.AccountNumber;
import com.turkninja.ddd.module01.domain.model.Money;

/**
 * Thrown when an account withdrawal exceeds the balance plus authorized overdraft.
 */
public class InsufficientFundsException extends RuntimeException {

    private final AccountNumber accountNumber;
    private final Money requestedAmount;
    private final Money availableFunds;

    public InsufficientFundsException(AccountNumber accountNumber, Money requestedAmount, Money availableFunds) {
        super(String.format("Account %s has insufficient funds. Requested: %s, Available: %s",
                accountNumber.value(), requestedAmount, availableFunds));
        this.accountNumber = accountNumber;
        this.requestedAmount = requestedAmount;
        this.availableFunds = availableFunds;
    }

    public AccountNumber getAccountNumber() {
        return accountNumber;
    }

    public Money getRequestedAmount() {
        return requestedAmount;
    }

    public Money getAvailableFunds() {
        return availableFunds;
    }
}
