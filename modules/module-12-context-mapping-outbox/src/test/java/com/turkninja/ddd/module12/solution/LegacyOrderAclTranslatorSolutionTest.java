package com.turkninja.ddd.module12.solution;

import com.turkninja.ddd.shared.domain.DomainValidationException;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.math.BigDecimal;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

@DisplayName("Solution 12: Legacy Order ACL Translator Tests")
class LegacyOrderAclTranslatorSolutionTest {

    private final LegacyOrderAclTranslator translator = new LegacyOrderAclTranslator();

    @Test
    @DisplayName("Should translate valid legacy payload cleanly into domain model")
    void testValidTranslation() {
        LegacyErpOrderPayload legacy = new LegacyErpOrderPayload(
                "ERP-1001",
                "Globex Corp",
                "2450.75",
                "EUR",
                "OPEN"
        );

        CleanOrder order = translator.translate(legacy);

        assertThat(order.orderNumber()).isEqualTo("ERP-1001");
        assertThat(order.customerName()).isEqualTo("Globex Corp");
        assertThat(order.totalAmount()).isEqualByComparingTo(new BigDecimal("2450.75"));
        assertThat(order.currency()).isEqualTo("EUR");
    }

    @Test
    @DisplayName("Should reject VOID status orders")
    void testRejectVoidStatus() {
        LegacyErpOrderPayload legacy = new LegacyErpOrderPayload(
                "ERP-1002",
                "Initech",
                "100.00",
                "USD",
                "VOID"
        );

        assertThatThrownBy(() -> translator.translate(legacy))
                .isInstanceOf(DomainValidationException.class)
                .hasMessageContaining("Cannot import VOID orders");
    }

    @Test
    @DisplayName("Should throw on missing order reference")
    void testMissingOrderRef() {
        LegacyErpOrderPayload legacy = new LegacyErpOrderPayload(
                "",
                "Umbrella Corp",
                "500.00",
                "USD",
                "OPEN"
        );

        assertThatThrownBy(() -> translator.translate(legacy))
                .isInstanceOf(DomainValidationException.class)
                .hasMessageContaining("order reference number is missing");
    }
}
