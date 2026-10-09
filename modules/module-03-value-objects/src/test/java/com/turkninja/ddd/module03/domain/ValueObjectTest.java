package com.turkninja.ddd.module03.domain;

import com.turkninja.ddd.module03.domain.model.EmailAddress;
import com.turkninja.ddd.module03.domain.model.Iban;
import com.turkninja.ddd.shared.domain.DomainValidationException;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

@DisplayName("Module 03: Value Objects Invariant Test")
class ValueObjectTest {

    @Test
    @DisplayName("Should normalize and validate email address")
    void testEmailValidation() {
        EmailAddress email1 = new EmailAddress("User@Example.COM");
        EmailAddress email2 = new EmailAddress("user@example.com");

        assertThat(email1.value()).isEqualTo("user@example.com");
        assertThat(email1).isEqualTo(email2);
    }

    @Test
    @DisplayName("Should reject invalid email format")
    void testInvalidEmail() {
        assertThatThrownBy(() -> new EmailAddress("invalid-email"))
                .isInstanceOf(DomainValidationException.class);
    }

    @Test
    @DisplayName("Should sanitize IBAN spacing and normalize")
    void testIbanNormalization() {
        Iban iban = new Iban("TR33 0006 1005 1234 5678 9012 34");
        assertThat(iban.value()).isEqualTo("TR330006100512345678901234");
    }
}
