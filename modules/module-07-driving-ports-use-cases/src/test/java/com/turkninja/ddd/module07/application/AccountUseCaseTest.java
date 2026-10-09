package com.turkninja.ddd.module07.application;

import com.turkninja.ddd.module07.application.port.in.CreateAccountUseCase;
import com.turkninja.ddd.module07.application.port.out.AccountRepositoryPort;
import com.turkninja.ddd.module07.application.service.AccountApplicationService;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.util.HashMap;
import java.util.Map;
import java.util.Optional;
import java.util.UUID;

import static org.assertj.core.api.Assertions.assertThat;

@DisplayName("Module 07: Inbound Port & Application Service Tests")
class AccountUseCaseTest {

    static class StubAccountRepository implements AccountRepositoryPort {
        final Map<UUID, AccountRecord> map = new HashMap<>();
        @Override
        public void save(AccountRecord account) { map.put(account.id(), account); }
        @Override
        public Optional<AccountRecord> findById(UUID id) { return Optional.ofNullable(map.get(id)); }
    }

    @Test
    @DisplayName("Application service coordinates account creation use case")
    void testCreateAccountUseCase() {
        StubAccountRepository repo = new StubAccountRepository();
        AccountApplicationService service = new AccountApplicationService(repo);

        UUID id = service.createAccount(new CreateAccountUseCase.CreateAccountCommand("John Doe", 500.0));

        assertThat(id).isNotNull();
        assertThat(repo.findById(id)).isPresent();
        assertThat(repo.findById(id).get().ownerName()).isEqualTo("John Doe");
    }
}
