package com.turkninja.ddd.module01.domain.model;

import com.turkninja.ddd.module01.domain.event.AccountDomainEvent.AccountDepositedEvent;
import com.turkninja.ddd.module01.domain.event.AccountDomainEvent.AccountOpenedEvent;
import com.turkninja.ddd.module01.domain.event.AccountDomainEvent.AccountWithdrawnEvent;
import com.turkninja.ddd.module01.domain.exception.InsufficientFundsException;
import com.turkninja.ddd.shared.domain.AggregateRoot;
import com.turkninja.ddd.shared.domain.DomainValidationException;

import java.time.Instant;
import java.util.Objects;
import java.util.UUID;

/**
 * Rich Domain Aggregate Root for Bank Account.
 * Guarantees business invariants:
 * - State cannot be set arbitrarily; only mutated through domain actions.
 * - Balance cannot drop below the authorized overdraft limit.
 * - Records domain events upon every successful state transition.
 */
public class BankAccount extends AggregateRoot<AccountNumber> {

    private Money balance;
    private final OverdraftLimit overdraftLimit;

    private BankAccount(AccountNumber id, Money initialBalance, OverdraftLimit overdraftLimit) {
        super(id);
        this.balance = Objects.requireNonNull(initialBalance);
        this.overdraftLimit = Objects.requireNonNull(overdraftLimit);
        recordEvent(new AccountOpenedEvent(UUID.randomUUID(), id, initialBalance, Instant.now()));
    }

    public static BankAccount open(AccountNumber id, OverdraftLimit overdraftLimit) {
        return new BankAccount(id, Money.zero(overdraftLimit.currency()), overdraftLimit);
    }

    public static BankAccount openWithInitialDeposit(AccountNumber id, Money initialDeposit, OverdraftLimit overdraftLimit) {
        if (!initialDeposit.isPositive()) {
            throw new DomainValidationException("Initial deposit must be positive");
        }
        return new BankAccount(id, initialDeposit, overdraftLimit);
    }

    public void deposit(Money amount) {
        if (!amount.isPositive()) {
            throw new DomainValidationException("Deposit amount must be strictly positive");
        }
        this.balance = this.balance.add(amount);
        recordEvent(new AccountDepositedEvent(UUID.randomUUID(), id, amount, this.balance, Instant.now()));
    }

    public void withdraw(Money amount) {
        if (!amount.isPositive()) {
            throw new DomainValidationException("Withdrawal amount must be strictly positive");
        }

        Money availableFunds = this.balance.add(this.overdraftLimit.amount());
        if (amount.isGreaterThan(availableFunds)) {
            throw new InsufficientFundsException(id, amount, availableFunds);
        }

        this.balance = this.balance.subtract(amount);
        recordEvent(new AccountWithdrawnEvent(UUID.randomUUID(), id, amount, this.balance, Instant.now()));
    }

    public Money getBalance() {
        return balance;
    }

    public OverdraftLimit getOverdraftLimit() {
        return overdraftLimit;
    }

    public Money calculateAvailableFunds() {
        return this.balance.add(this.overdraftLimit.amount());
    }
}
