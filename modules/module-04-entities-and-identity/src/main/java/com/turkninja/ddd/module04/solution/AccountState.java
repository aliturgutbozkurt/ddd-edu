package com.turkninja.ddd.module04.solution;

import com.turkninja.ddd.shared.domain.DomainEntity;
import com.turkninja.ddd.shared.domain.DomainValidationException;
import com.turkninja.ddd.shared.domain.ValueObject;

import java.util.UUID;

public class AccountState extends DomainEntity<AccountState.AccountId> {

    public record AccountId(UUID value) implements ValueObject {}
    public enum Status { ACTIVE, SUSPENDED, CLOSED }

    private Status status;

    public AccountState(AccountId id) {
        super(id);
        this.status = Status.ACTIVE;
    }

    public void suspend() {
        if (status == Status.CLOSED) {
            throw new DomainValidationException("Cannot suspend an already closed account");
        }
        this.status = Status.SUSPENDED;
    }

    public void close() {
        this.status = Status.CLOSED;
    }

    public void activate() {
        if (status == Status.CLOSED) {
            throw new DomainValidationException("Cannot reactivate a closed account");
        }
        this.status = Status.ACTIVE;
    }

    public Status getStatus() { return status; }
}
