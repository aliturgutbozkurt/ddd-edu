package com.turkninja.ddd.module04.solution;

import com.turkninja.ddd.shared.domain.DomainValidationException;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.util.UUID;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

@DisplayName("Solution 04: Account State Lifecycle Verification")
class AccountStateSolutionTest {

    @Test
    @DisplayName("Account transitions cleanly from active to suspended to active")
    void testStateTransitions() {
        AccountState account = new AccountState(new AccountState.AccountId(UUID.randomUUID()));
        assertThat(account.getStatus()).isEqualTo(AccountState.Status.ACTIVE);

        account.suspend();
        assertThat(account.getStatus()).isEqualTo(AccountState.Status.SUSPENDED);

        account.activate();
        assertThat(account.getStatus()).isEqualTo(AccountState.Status.ACTIVE);
    }

    @Test
    @DisplayName("Cannot reactivate a closed account")
    void testReactivatingClosedAccount() {
        AccountState account = new AccountState(new AccountState.AccountId(UUID.randomUUID()));
        account.close();

        assertThatThrownBy(account::activate)
                .isInstanceOf(DomainValidationException.class)
                .hasMessageContaining("Cannot reactivate a closed account");
    }
}
