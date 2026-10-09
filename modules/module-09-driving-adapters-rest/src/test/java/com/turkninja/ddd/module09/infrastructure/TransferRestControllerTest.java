package com.turkninja.ddd.module09.infrastructure;

import com.turkninja.ddd.module09.application.port.in.TransferMoneyUseCase;
import com.turkninja.ddd.module09.infrastructure.adapter.input.rest.TransferRestController;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.math.BigDecimal;
import java.util.UUID;

import static org.assertj.core.api.Assertions.assertThat;

@DisplayName("Module 09: Driving REST Adapter Tests")
class TransferRestControllerTest {

    @Test
    @DisplayName("REST Controller translates request to use case command and wraps response")
    void testHandleTransfer() {
        UUID expectedTxId = UUID.randomUUID();
        TransferMoneyUseCase mockUseCase = command ->
                new TransferMoneyUseCase.TransferResult(expectedTxId, true, "Transfer completed");

        TransferRestController controller = new TransferRestController(mockUseCase);
        TransferRestController.TransferResponse response = controller.handleTransfer(
                new TransferRestController.TransferRequest("ACC-1", "ACC-2", new BigDecimal("150.00")));

        assertThat(response.transactionId()).isEqualTo(expectedTxId);
        assertThat(response.status()).isEqualTo("COMPLETED");
        assertThat(response.message()).isEqualTo("Transfer completed");
    }
}
