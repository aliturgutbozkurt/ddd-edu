package com.turkninja.ddd.module10.solution;

import java.util.Objects;
import java.util.UUID;
import java.util.function.Function;

/**
 * Driven Adapter implementing PaymentGatewayPort with retry resilience.
 */
public class ResilientPaymentGatewayAdapter implements PaymentGatewayPort {

    private final int maxRetries;
    private final Function<PaymentRequest, String> externalApiCall;
    private int attemptsRecorded = 0;

    public ResilientPaymentGatewayAdapter(int maxRetries, Function<PaymentRequest, String> externalApiCall) {
        this.maxRetries = maxRetries;
        this.externalApiCall = Objects.requireNonNull(externalApiCall);
    }

    @Override
    public PaymentResult charge(PaymentRequest request) {
        String lastError = null;

        for (int attempt = 1; attempt <= maxRetries; attempt++) {
            attemptsRecorded++;
            try {
                String txRef = externalApiCall.apply(request);
                return PaymentResult.success(request.paymentId(), txRef);
            } catch (Exception ex) {
                lastError = ex.getMessage();
            }
        }

        return PaymentResult.failure(request.paymentId(), "Exceeded " + maxRetries + " attempts: " + lastError);
    }

    public int getAttemptsRecorded() {
        return attemptsRecorded;
    }
}
