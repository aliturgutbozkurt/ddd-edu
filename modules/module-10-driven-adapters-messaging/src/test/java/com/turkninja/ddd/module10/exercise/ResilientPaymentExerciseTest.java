package com.turkninja.ddd.module10.exercise;

import com.turkninja.ddd.module10.solution.PaymentGatewayPort;
import com.turkninja.ddd.module10.solution.PaymentGatewayPort.PaymentRequest;
import com.turkninja.ddd.module10.solution.PaymentGatewayPort.PaymentResult;
import com.turkninja.ddd.module10.solution.ResilientPaymentGatewayAdapter;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.math.BigDecimal;

import static org.assertj.core.api.Assertions.assertThat;

@DisplayName("Exercise 10: Resilient Payment Gateway Driven Adapter")
class ResilientPaymentExerciseTest {

    @Test
    @Disabled("TODO for student: Implement retry logic in adapter and enable test")
    @DisplayName("Should retry transient errors up to maxRetries")
    void shouldRetryOnTransientError() {
        ResilientPaymentGatewayAdapter adapter = new ResilientPaymentGatewayAdapter(3, req -> {
            throw new RuntimeException("503 Gateway Timeout");
        });

        PaymentResult result = adapter.charge(new PaymentRequest("PAY-1", "CUST-1", new BigDecimal("100.00"), "USD"));

        assertThat(result.success()).isFalse();
        assertThat(adapter.getAttemptsRecorded()).isEqualTo(3);
    }
}
