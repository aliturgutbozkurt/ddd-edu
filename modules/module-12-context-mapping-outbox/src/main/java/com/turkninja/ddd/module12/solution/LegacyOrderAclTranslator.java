package com.turkninja.ddd.module12.solution;

import com.turkninja.ddd.shared.domain.DomainValidationException;

import java.math.BigDecimal;

/**
 * Anti-Corruption Layer (ACL) translator protecting the domain from legacy ERP schemas.
 */
public class LegacyOrderAclTranslator {

    public CleanOrder translate(LegacyErpOrderPayload payload) {
        if (payload == null) {
            throw new DomainValidationException("Legacy payload cannot be null");
        }

        if (payload.order_ref_num() == null || payload.order_ref_num().isBlank()) {
            throw new DomainValidationException("Legacy order reference number is missing");
        }

        if (payload.client_nm() == null || payload.client_nm().isBlank()) {
            throw new DomainValidationException("Legacy client name is missing");
        }

        if ("VOID".equalsIgnoreCase(payload.status_code())) {
            throw new DomainValidationException("Cannot import VOID orders from legacy ERP");
        }

        BigDecimal amount;
        try {
            amount = new BigDecimal(payload.gross_amt());
        } catch (Exception ex) {
            throw new DomainValidationException("Invalid gross amount format: " + payload.gross_amt());
        }

        String currency = (payload.tx_curr() == null || payload.tx_curr().isBlank()) ? "USD" : payload.tx_curr().toUpperCase();

        return new CleanOrder(
                payload.order_ref_num().trim(),
                payload.client_nm().trim(),
                amount,
                currency
        );
    }
}
