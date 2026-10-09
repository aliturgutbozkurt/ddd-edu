package com.turkninja.ddd.module01.exercise;

import com.turkninja.ddd.module01.domain.model.AccountNumber;
import com.turkninja.ddd.module01.domain.model.Currency;
import com.turkninja.ddd.module01.domain.model.Money;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;
import static org.junit.jupiter.api.Assertions.fail;

@DisplayName("Student Exercise 01: Enforcing Daily Withdrawal Invariants")
class DailyLimitExerciseTest {

    private final AccountNumber testAccount = new AccountNumber("9876543210");

    @Test
    @Disabled("Remove @Disabled when you begin implementing Exercise 01")
    @DisplayName("Should successfully withdraw when within daily limit")
    void shouldAllowWithdrawalWithinDailyLimit() {
        fail("TODO: Implement AccountWithDailyLimit aggregate and verify withdrawal stays within daily limit");
    }

    @Test
    @Disabled("Remove @Disabled when you begin implementing Exercise 01")
    @DisplayName("Should throw DailyLimitExceededException when daily accumulation exceeds limit")
    void shouldRejectWithdrawalExceedingDailyLimit() {
        fail("TODO: Implement check that throws DailyLimitExceededException when limit breached");
    }
}
