package com.turkninja.ddd.module03.solution;

import com.turkninja.ddd.shared.domain.DomainValidationException;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

@DisplayName("Solution 03: TaxNumber Invariant Verification")
class TaxNumberSolutionTest {

    @Test
    @DisplayName("Valid 10-digit tax number is accepted")
    void testValidTaxNumber() {
        TaxNumber tax = new TaxNumber("1234567890");
        assertThat(tax.value()).isEqualTo("1234567890");
    }

    @Test
    @DisplayName("All-zeros tax number is rejected")
    void testAllZerosTaxNumber() {
        assertThatThrownBy(() -> new TaxNumber("0000000000"))
                .isInstanceOf(DomainValidationException.class);
    }
}
