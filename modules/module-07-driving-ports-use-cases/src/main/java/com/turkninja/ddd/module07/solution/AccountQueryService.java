package com.turkninja.ddd.module07.solution;

import com.turkninja.ddd.module07.application.port.out.AccountRepositoryPort;

import java.util.Objects;
import java.util.Optional;
import java.util.UUID;

public class AccountQueryService implements GetAccountSummaryQuery {

    private final AccountRepositoryPort repositoryPort;

    public AccountQueryService(AccountRepositoryPort repositoryPort) {
        this.repositoryPort = Objects.requireNonNull(repositoryPort);
    }

    @Override
    public Optional<AccountSummaryResponse> getSummary(UUID accountId) {
        return repositoryPort.findById(accountId)
                .map(r -> new AccountSummaryResponse(r.id(), r.ownerName(), r.balance(), "ACTIVE"));
    }
}
