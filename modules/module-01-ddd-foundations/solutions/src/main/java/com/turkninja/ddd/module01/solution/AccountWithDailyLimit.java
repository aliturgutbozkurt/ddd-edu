package com.turkninja.ddd.module01.solution;

import com.turkninja.ddd.module01.domain.exception.InsufficientFundsException;
import com.turkninja.ddd.module01.domain.model.AccountNumber;
import com.turkninja.ddd.module01.domain.model.Money;
import com.turkninja.ddd.module01.domain.model.OverdraftLimit;
import com.turkninja.ddd.module01.exercise.DailyLimitExceededException;
import com.turkninja.ddd.shared.domain.AggregateRoot;
import com.turkninja.ddd.shared.domain.DomainValidationException;

import java.time.LocalDate;
import java.util.Objects;

/**
 * Rich Domain Aggregate Root implementing both Overdraft and Daily Withdrawal limits.
 */
public class AccountWithDailyLimit extends AggregateRoot<AccountNumber> {

    private Money balance;
    private final OverdraftLimit overdraftLimit;
    private final DailyWithdrawalLimit dailyLimit;

    private Money todayWithdrawn;
    private LocalDate lastWithdrawalDate;

    public AccountWithDailyLimit(AccountNumber id, OverdraftLimit overdraftLimit, DailyWithdrawalLimit dailyLimit) {
        super(id);
        this.overdraftLimit = Objects.requireNonNull(overdraftLimit);
        this.dailyLimit = Objects.requireNonNull(dailyLimit);
        this.balance = Money.zero(overdraftLimit.currency());
        this.todayWithdrawn = Money.zero(dailyLimit.currency());
        this.lastWithdrawalDate = LocalDate.now();
    }

    public void deposit(Money amount) {
        if (!amount.isPositive()) {
            throw new DomainValidationException("Deposit amount must be strictly positive");
        }
        this.balance = this.balance.add(amount);
    }

    public void withdraw(Money amount, LocalDate withdrawalDate) {
        if (!amount.isPositive()) {
            throw new DomainValidationException("Withdrawal amount must be strictly positive");
        }

        // Reset daily accumulator if on a new calendar day
        if (withdrawalDate.isAfter(this.lastWithdrawalDate)) {
            this.todayWithdrawn = Money.zero(dailyLimit.currency());
            this.lastWithdrawalDate = withdrawalDate;
        }

        // Check Daily Limit Invariant
        Money projectedDailyTotal = this.todayWithdrawn.add(amount);
        if (projectedDailyTotal.isGreaterThan(this.dailyLimit.limit())) {
            Money remainingLimit = this.dailyLimit.limit().subtract(this.todayWithdrawn);
            throw new DailyLimitExceededException(amount, remainingLimit);
        }

        // Check Overall Account Funds Invariant
        Money availableFunds = this.balance.add(this.overdraftLimit.amount());
        if (amount.isGreaterThan(availableFunds)) {
            throw new InsufficientFundsException(id, amount, availableFunds);
        }

        this.balance = this.balance.subtract(amount);
        this.todayWithdrawn = projectedDailyTotal;
    }

    public Money getBalance() {
        return balance;
    }

    public Money getTodayWithdrawn() {
        return todayWithdrawn;
    }

    public DailyWithdrawalLimit getDailyLimit() {
        return dailyLimit;
    }
}
