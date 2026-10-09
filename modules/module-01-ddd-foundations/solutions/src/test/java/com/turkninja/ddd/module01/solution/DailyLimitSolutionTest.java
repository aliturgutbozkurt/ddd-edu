package com.turkninja.ddd.module01.solution;

import com.turkninja.ddd.module01.domain.model.AccountNumber;
import com.turkninja.ddd.module01.domain.model.Currency;
import com.turkninja.ddd.module01.domain.model.Money;
import com.turkninja.ddd.module01.domain.model.OverdraftLimit;
import com.turkninja.ddd.module01.exercise.DailyLimitExceededException;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.time.LocalDate;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

@DisplayName("Solution 01: Enforcing Daily Withdrawal Invariants")
class DailyLimitSolutionTest {

    private final AccountNumber accountId = new AccountNumber("1122334455");

    @Test
    @DisplayName("Should successfully withdraw multiple amounts within daily limit on same day")
    void shouldAllowWithdrawalsWithinLimit() {
        LocalDate today = LocalDate.of(2026, 10, 9);
        AccountWithDailyLimit account = new AccountWithDailyLimit(
                accountId,
                OverdraftLimit.zero(Currency.USD),
                DailyWithdrawalLimit.of(500.0, Currency.USD)
        );

        account.deposit(Money.of(1000.0, Currency.USD));

        account.withdraw(Money.of(200.0, Currency.USD), today);
        assertThat(account.getBalance()).isEqualTo(Money.of(800.0, Currency.USD));
        assertThat(account.getTodayWithdrawn()).isEqualTo(Money.of(200.0, Currency.USD));

        account.withdraw(Money.of(250.0, Currency.USD), today);
        assertThat(account.getBalance()).isEqualTo(Money.of(550.0, Currency.USD));
        assertThat(account.getTodayWithdrawn()).isEqualTo(Money.of(450.0, Currency.USD));
    }

    @Test
    @DisplayName("Should throw DailyLimitExceededException when single withdrawal breaches limit")
    void shouldRejectWithdrawalExceedingDailyLimit() {
        LocalDate today = LocalDate.of(2026, 10, 9);
        AccountWithDailyLimit account = new AccountWithDailyLimit(
                accountId,
                OverdraftLimit.zero(Currency.USD),
                DailyWithdrawalLimit.of(300.0, Currency.USD)
        );

        account.deposit(Money.of(1000.0, Currency.USD));

        assertThatThrownBy(() -> account.withdraw(Money.of(350.0, Currency.USD), today))
                .isInstanceOf(DailyLimitExceededException.class)
                .hasMessageContaining("Daily limit exceeded");

        // Balance remains intact
        assertThat(account.getBalance()).isEqualTo(Money.of(1000.0, Currency.USD));
    }

    @Test
    @DisplayName("Should reset daily accumulation when withdrawal occurs on next calendar day")
    void shouldResetLimitOnNewDay() {
        LocalDate dayOne = LocalDate.of(2026, 10, 9);
        LocalDate dayTwo = LocalDate.of(2026, 10, 10);

        AccountWithDailyLimit account = new AccountWithDailyLimit(
                accountId,
                OverdraftLimit.zero(Currency.USD),
                DailyWithdrawalLimit.of(300.0, Currency.USD)
        );

        account.deposit(Money.of(1000.0, Currency.USD));

        // Withdraw 300 on day 1 (hits limit)
        account.withdraw(Money.of(300.0, Currency.USD), dayOne);
        assertThat(account.getTodayWithdrawn()).isEqualTo(Money.of(300.0, Currency.USD));

        // Withdraw on day 2 resets counter and succeeds
        account.withdraw(Money.of(200.0, Currency.USD), dayTwo);
        assertThat(account.getTodayWithdrawn()).isEqualTo(Money.of(200.0, Currency.USD));
        assertThat(account.getBalance()).isEqualTo(Money.of(500.0, Currency.USD));
    }
}
