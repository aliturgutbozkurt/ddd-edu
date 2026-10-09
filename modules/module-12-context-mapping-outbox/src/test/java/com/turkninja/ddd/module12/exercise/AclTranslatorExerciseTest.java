package com.turkninja.ddd.module12.exercise;

import com.turkninja.ddd.module12.solution.CleanOrder;
import com.turkninja.ddd.module12.solution.LegacyErpOrderPayload;
import com.turkninja.ddd.module12.solution.LegacyOrderAclTranslator;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.math.BigDecimal;

import static org.assertj.core.api.Assertions.assertThat;

@DisplayName("Exercise 12: Anti-Corruption Layer Translator")
class AclTranslatorExerciseTest {

    @Test
    @Disabled("TODO for student: Implement ACL translation and enable test")
    @DisplayName("Should translate valid legacy payload into clean domain order")
    void shouldTranslateLegacyPayload() {
        LegacyOrderAclTranslator translator = new LegacyOrderAclTranslator();
        LegacyErpOrderPayload legacy = new LegacyErpOrderPayload("ERP-9912", "Acme Corp", "1500.50", "USD", "ACTIVE");

        CleanOrder clean = translator.translate(legacy);

        assertThat(clean.orderNumber()).isEqualTo("ERP-9912");
        assertThat(clean.customerName()).isEqualTo("Acme Corp");
        assertThat(clean.totalAmount()).isEqualByComparingTo(new BigDecimal("1500.50"));
    }
}
