package com.turkninja.ddd.module07.application.service;

import com.turkninja.ddd.module07.application.port.in.CreateAccountUseCase;
import com.turkninja.ddd.module07.application.port.out.AccountRepositoryPort;

import java.util.Objects;
import java.util.UUID;

public class AccountApplicationService implements CreateAccountUseCase {

    private final AccountRepositoryPort repositoryPort;

    public AccountApplicationService(AccountRepositoryPort repositoryPort) {
        this.repositoryPort = Objects.requireNonNull(repositoryPort);
    }

    @Override
    public UUID createAccount(CreateAccountCommand command) {
        UUID accountId = UUID.randomUUID();
        AccountRepositoryPort.AccountRecord record = new AccountRepositoryPort.AccountRecord(
                accountId, command.ownerName(), command.initialDeposit());
        repositoryPort.save(record);
        return accountId;
    }
}
