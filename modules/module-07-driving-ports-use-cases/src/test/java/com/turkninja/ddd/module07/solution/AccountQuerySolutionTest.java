package com.turkninja.ddd.module07.solution;

import com.turkninja.ddd.module07.application.port.out.AccountRepositoryPort;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.util.Optional;
import java.util.UUID;

import static org.assertj.core.api.Assertions.assertThat;

@DisplayName("Solution 07: CQRS Query Port Verification")
class AccountQuerySolutionTest {

    @Test
    @DisplayName("Successfully queries account summary DTO without domain exposure")
    void testQueryService() {
        UUID id = UUID.randomUUID();
        AccountRepositoryPort stubRepo = new AccountRepositoryPort() {
            @Override public void save(AccountRecord account) {}
            @Override public Optional<AccountRecord> findById(UUID queryId) {
                return Optional.of(new AccountRecord(id, "Ada Lovelace", 1250.00));
            }
        };

        AccountQueryService queryService = new AccountQueryService(stubRepo);
        Optional<GetAccountSummaryQuery.AccountSummaryResponse> summary = queryService.getSummary(id);

        assertThat(summary).isPresent();
        assertThat(summary.get().ownerName()).isEqualTo("Ada Lovelace");
        assertThat(summary.get().balance()).isEqualTo(1250.00);
    }
}
