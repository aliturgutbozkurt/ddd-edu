package com.turkninja.ddd.module09.application.port.in;

import java.math.BigDecimal;
import java.util.UUID;

public interface TransferMoneyUseCase {
    TransferResult transfer(TransferCommand command);

    record TransferCommand(String sourceAccount, String targetAccount, BigDecimal amount) {}
    record TransferResult(UUID transactionId, boolean success, String message) {}
}
