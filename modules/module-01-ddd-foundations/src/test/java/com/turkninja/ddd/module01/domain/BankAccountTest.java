package com.turkninja.ddd.module01.domain;

import com.turkninja.ddd.module01.domain.event.AccountDomainEvent;
import com.turkninja.ddd.module01.domain.exception.InsufficientFundsException;
import com.turkninja.ddd.module01.domain.model.AccountNumber;
import com.turkninja.ddd.module01.domain.model.BankAccount;
import com.turkninja.ddd.module01.domain.model.Currency;
import com.turkninja.ddd.module01.domain.model.Money;
import com.turkninja.ddd.module01.domain.model.OverdraftLimit;
import com.turkninja.ddd.shared.domain.DomainValidationException;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

@DisplayName("Module 01: BankAccount Aggregate & Invariants Test")
class BankAccountTest {

    private final AccountNumber validAccountNumber = new AccountNumber("1234567890");

    @Nested
    @DisplayName("Account Opening & Initial State")
    class AccountOpeningTests {

        @Test
        @DisplayName("Should successfully open an account and record AccountOpenedEvent")
        void shouldOpenAccountSuccessfully() {
            OverdraftLimit overdraft = OverdraftLimit.of(200.0, Currency.USD);
            BankAccount account = BankAccount.open(validAccountNumber, overdraft);

            assertThat(account.getId()).isEqualTo(validAccountNumber);
            assertThat(account.getBalance()).isEqualTo(Money.zero(Currency.USD));
            assertThat(account.calculateAvailableFunds()).isEqualTo(Money.of(200.0, Currency.USD));

            assertThat(account.getDomainEvents())
                    .hasSize(1)
                    .first()
                    .isInstanceOf(AccountDomainEvent.AccountOpenedEvent.class);
        }

        @Test
        @DisplayName("Should throw validation exception on invalid 9-digit account number")
        void shouldRejectInvalidAccountNumber() {
            assertThatThrownBy(() -> new AccountNumber("12345"))
                    .isInstanceOf(DomainValidationException.class)
                    .hasMessageContaining("Account number must be a valid 10-digit string");
        }
    }

    @Nested
    @DisplayName("Deposit & Withdrawal Invariants")
    class TransactionInvariantTests {

        @Test
        @DisplayName("Should deposit money, update balance and record AccountDepositedEvent")
        void shouldDepositMoneySuccessfully() {
            BankAccount account = BankAccount.open(validAccountNumber, OverdraftLimit.zero(Currency.USD));
            account.clearDomainEvents();

            account.deposit(Money.of(150.0, Currency.USD));

            assertThat(account.getBalance()).isEqualTo(Money.of(150.0, Currency.USD));
            assertThat(account.getDomainEvents())
                    .hasSize(1)
                    .first()
                    .isInstanceOf(AccountDomainEvent.AccountDepositedEvent.class);
        }

        @Test
        @DisplayName("Should reject negative deposit amount")
        void shouldRejectNegativeDeposit() {
            BankAccount account = BankAccount.open(validAccountNumber, OverdraftLimit.zero(Currency.USD));

            assertThatThrownBy(() -> account.deposit(Money.of(-50.0, Currency.USD)))
                    .isInstanceOf(DomainValidationException.class);
        }

        @Test
        @DisplayName("Should withdraw money within authorized overdraft limit")
        void shouldWithdrawWithinOverdraftLimit() {
            BankAccount account = BankAccount.open(validAccountNumber, OverdraftLimit.of(100.0, Currency.USD));
            account.deposit(Money.of(50.0, Currency.USD));
            account.clearDomainEvents();

            // Total available = 50 (balance) + 100 (overdraft) = 150
            account.withdraw(Money.of(120.0, Currency.USD));

            // New balance should be -70.00
            assertThat(account.getBalance()).isEqualTo(Money.of(-70.0, Currency.USD));
            assertThat(account.getDomainEvents())
                    .hasSize(1)
                    .first()
                    .isInstanceOf(AccountDomainEvent.AccountWithdrawnEvent.class);
        }

        @Test
        @DisplayName("Should reject withdrawal exceeding balance plus overdraft limit")
        void shouldRejectWithdrawalExceedingOverdraft() {
            BankAccount account = BankAccount.open(validAccountNumber, OverdraftLimit.of(50.0, Currency.USD));
            account.deposit(Money.of(20.0, Currency.USD));

            // Available = 70.00 USD. Trying to withdraw 100.00 USD
            assertThatThrownBy(() -> account.withdraw(Money.of(100.0, Currency.USD)))
                    .isInstanceOf(InsufficientFundsException.class)
                    .hasMessageContaining("has insufficient funds");
        }

        @Test
        @DisplayName("Should reject cross-currency transactions")
        void shouldRejectCrossCurrencyOperation() {
            BankAccount account = BankAccount.open(validAccountNumber, OverdraftLimit.zero(Currency.USD));

            assertThatThrownBy(() -> account.deposit(Money.of(100.0, Currency.EUR)))
                    .isInstanceOf(DomainValidationException.class)
                    .hasMessageContaining("Cannot perform monetary operation across currencies");
        }
    }
}
