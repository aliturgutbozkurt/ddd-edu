package com.turkninja.ddd.module09.infrastructure.adapter.input.rest;

import com.turkninja.ddd.module09.application.port.in.TransferMoneyUseCase;
import com.turkninja.ddd.module09.application.port.in.TransferMoneyUseCase.TransferCommand;
import com.turkninja.ddd.module09.application.port.in.TransferMoneyUseCase.TransferResult;

import java.math.BigDecimal;
import java.util.Objects;
import java.util.UUID;

public class TransferRestController {

    public record TransferRequest(String sourceAccount, String targetAccount, BigDecimal amount) {}
    public record TransferResponse(UUID transactionId, String status, String message) {}

    private final TransferMoneyUseCase transferMoneyUseCase;

    public TransferRestController(TransferMoneyUseCase transferMoneyUseCase) {
        this.transferMoneyUseCase = Objects.requireNonNull(transferMoneyUseCase);
    }

    public TransferResponse handleTransfer(TransferRequest request) {
        TransferCommand command = new TransferCommand(
                request.sourceAccount(),
                request.targetAccount(),
                request.amount()
        );

        TransferResult result = transferMoneyUseCase.transfer(command);
        return new TransferResponse(
                result.transactionId(),
                result.success() ? "COMPLETED" : "FAILED",
                result.message()
        );
    }
}
