package com.turkninja.ddd.module10.solution;

import java.math.BigDecimal;

/**
 * Outbound Driven Port (SPI) for charging credit cards / accounts.
 */
public interface PaymentGatewayPort {

    record PaymentRequest(String paymentId, String customerId, BigDecimal amount, String currency) {}

    record PaymentResult(String paymentId, boolean success, String transactionReference, String failureReason) {
        public static PaymentResult success(String paymentId, String txRef) {
            return new PaymentResult(paymentId, true, txRef, null);
        }
        public static PaymentResult failure(String paymentId, String reason) {
            return new PaymentResult(paymentId, false, null, reason);
        }
    }

    PaymentResult charge(PaymentRequest request);
}
