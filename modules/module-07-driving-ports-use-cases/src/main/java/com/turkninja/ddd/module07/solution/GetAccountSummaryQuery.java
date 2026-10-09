package com.turkninja.ddd.module07.solution;

import java.util.Optional;
import java.util.UUID;

public interface GetAccountSummaryQuery {
    Optional<AccountSummaryResponse> getSummary(UUID accountId);

    record AccountSummaryResponse(UUID accountId, String ownerName, double balance, String status) {}
}
