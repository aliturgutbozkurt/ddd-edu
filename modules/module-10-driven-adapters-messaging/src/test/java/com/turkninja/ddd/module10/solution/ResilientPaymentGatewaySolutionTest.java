package com.turkninja.ddd.module10.solution;

import com.turkninja.ddd.module10.solution.PaymentGatewayPort.PaymentRequest;
import com.turkninja.ddd.module10.solution.PaymentGatewayPort.PaymentResult;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.math.BigDecimal;
import java.util.concurrent.atomic.AtomicInteger;

import static org.assertj.core.api.Assertions.assertThat;

@DisplayName("Solution 10: Resilient Payment Gateway Adapter Tests")
class ResilientPaymentGatewaySolutionTest {

    @Test
    @DisplayName("Should succeed on first attempt if external API responds cleanly")
    void shouldSucceedOnFirstAttempt() {
        ResilientPaymentGatewayAdapter adapter = new ResilientPaymentGatewayAdapter(3, req -> "TX_OK_999");

        PaymentResult result = adapter.charge(new PaymentRequest("PAY-01", "C-1", new BigDecimal("50.00"), "EUR"));

        assertThat(result.success()).isTrue();
        assertThat(result.transactionReference()).isEqualTo("TX_OK_999");
        assertThat(adapter.getAttemptsRecorded()).isEqualTo(1);
    }

    @Test
    @DisplayName("Should succeed on retry after transient network failure")
    void shouldSucceedAfterTransientFailure() {
        AtomicInteger count = new AtomicInteger(0);
        ResilientPaymentGatewayAdapter adapter = new ResilientPaymentGatewayAdapter(3, req -> {
            if (count.incrementAndGet() < 3) {
                throw new RuntimeException("Temporary network glitch");
            }
            return "TX_RECOVERED_123";
        });

        PaymentResult result = adapter.charge(new PaymentRequest("PAY-02", "C-2", new BigDecimal("75.00"), "TRY"));

        assertThat(result.success()).isTrue();
        assertThat(result.transactionReference()).isEqualTo("TX_RECOVERED_123");
        assertThat(adapter.getAttemptsRecorded()).isEqualTo(3);
    }

    @Test
    @DisplayName("Should gracefully return failure result when all retries are exhausted")
    void shouldReturnFailureWhenRetriesExhausted() {
        ResilientPaymentGatewayAdapter adapter = new ResilientPaymentGatewayAdapter(3, req -> {
            throw new RuntimeException("Connection refused");
        });

        PaymentResult result = adapter.charge(new PaymentRequest("PAY-03", "C-3", new BigDecimal("120.00"), "USD"));

        assertThat(result.success()).isFalse();
        assertThat(result.failureReason()).contains("Exceeded 3 attempts");
        assertThat(adapter.getAttemptsRecorded()).isEqualTo(3);
    }
}
