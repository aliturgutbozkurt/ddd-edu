package com.turkninja.ddd.module07.application.port.out;

import java.util.Optional;
import java.util.UUID;

public interface AccountRepositoryPort {
    void save(AccountRecord account);
    Optional<AccountRecord> findById(UUID id);

    record AccountRecord(UUID id, String ownerName, double balance) {}
}
