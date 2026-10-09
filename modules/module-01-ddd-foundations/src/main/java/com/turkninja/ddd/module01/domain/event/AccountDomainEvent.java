package com.turkninja.ddd.module01.domain.event;

import com.turkninja.ddd.module01.domain.model.AccountNumber;
import com.turkninja.ddd.module01.domain.model.Money;
import com.turkninja.ddd.shared.domain.DomainEvent;

import java.time.Instant;
import java.util.UUID;

/**
 * Sealed hierarchy of domain events in the Banking Bounded Context.
 * Leverages Java 27 sealed interfaces for exhaustive pattern matching.
 */
public sealed interface AccountDomainEvent extends DomainEvent {

    AccountNumber accountNumber();

    record AccountOpenedEvent(UUID eventId, AccountNumber accountNumber, Money initialBalance, Instant occurredOn)
            implements AccountDomainEvent {}

    record AccountDepositedEvent(UUID eventId, AccountNumber accountNumber, Money amount, Money newBalance, Instant occurredOn)
            implements AccountDomainEvent {}

    record AccountWithdrawnEvent(UUID eventId, AccountNumber accountNumber, Money amount, Money newBalance, Instant occurredOn)
            implements AccountDomainEvent {}
}
