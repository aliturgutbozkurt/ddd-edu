package com.turkninja.ddd.module09.solution;

import com.turkninja.ddd.shared.domain.DomainValidationException;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.util.NoSuchElementException;

import static org.assertj.core.api.Assertions.assertThat;

@DisplayName("Solution 09: Global Exception Handler RFC 9457 Tests")
class GlobalExceptionHandlerSolutionTest {

    private final GlobalExceptionHandler handler = new GlobalExceptionHandler();

    @Test
    @DisplayName("Should translate DomainValidationException to 400 Bad Request")
    void testDomainValidationException() {
        DomainValidationException ex = new DomainValidationException("Transfer amount exceeds daily limit");
        ProblemDetailRecord record = handler.handleException(ex, "/api/transfers");

        assertThat(record.status()).isEqualTo(400);
        assertThat(record.title()).isEqualTo("Domain Validation Failure");
        assertThat(record.detail()).isEqualTo("Transfer amount exceeds daily limit");
        assertThat(record.instance().toString()).isEqualTo("/api/transfers");
        assertThat(record.properties()).containsEntry("errorCategory", "BUSINESS_RULE_VIOLATION");
    }

    @Test
    @DisplayName("Should translate NoSuchElementException to 404 Not Found")
    void testNoSuchElementException() {
        NoSuchElementException ex = new NoSuchElementException("Account not found for id ACC-123");
        ProblemDetailRecord record = handler.handleException(ex, "/api/accounts/ACC-123");

        assertThat(record.status()).isEqualTo(404);
        assertThat(record.title()).isEqualTo("Resource Not Found");
        assertThat(record.detail()).isEqualTo("Account not found for id ACC-123");
    }

    @Test
    @DisplayName("Should translate generic unexpected exception to 500 Internal Error")
    void testGenericException() {
        RuntimeException ex = new RuntimeException("Database connection timeout");
        ProblemDetailRecord record = handler.handleException(ex, "/api/transfers");

        assertThat(record.status()).isEqualTo(500);
        assertThat(record.title()).isEqualTo("Internal Server Error");
    }
}
