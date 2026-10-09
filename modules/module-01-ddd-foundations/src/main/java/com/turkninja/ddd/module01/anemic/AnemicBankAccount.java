package com.turkninja.ddd.module01.anemic;

import java.math.BigDecimal;

/**
 * ⚠️ ANTI-PATTERN: The Anemic Domain Model.
 * This class is merely a passive data container with public getters and setters.
 * All invariants are abandoned, inviting corrupt state and concurrency race conditions.
 */
public class AnemicBankAccount {

    private String accountNumber;
    private BigDecimal balance;
    private BigDecimal overdraftLimit;
    private String currency;

    public String getAccountNumber() {
        return accountNumber;
    }

    public void setAccountNumber(String accountNumber) {
        this.accountNumber = accountNumber;
    }

    public BigDecimal getBalance() {
        return balance;
    }

    public void setBalance(BigDecimal balance) {
        this.balance = balance;
    }

    public BigDecimal getOverdraftLimit() {
        return overdraftLimit;
    }

    public void setOverdraftLimit(BigDecimal overdraftLimit) {
        this.overdraftLimit = overdraftLimit;
    }

    public String getCurrency() {
        return currency;
    }

    public void setCurrency(String currency) {
        this.currency = currency;
    }
}
