package com.turkninja.ddd.module09.exercise;

import com.turkninja.ddd.module09.solution.GlobalExceptionHandler;
import com.turkninja.ddd.module09.solution.ProblemDetailRecord;
import com.turkninja.ddd.shared.domain.DomainValidationException;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

@DisplayName("Exercise 09: RFC 9457 Problem Details Exception Handler")
class ProblemDetailsExerciseTest {

    @Test
    @Disabled("TODO for student: Implement exception translation logic and enable this test")
    @DisplayName("Should translate DomainValidationException to RFC 9457 400 Bad Request")
    void shouldTranslateDomainValidationException() {
        GlobalExceptionHandler handler = new GlobalExceptionHandler();
        DomainValidationException ex = new DomainValidationException("Amount must be greater than zero");

        ProblemDetailRecord problem = handler.handleException(ex, "/api/v1/transfers");

        assertThat(problem.status()).isEqualTo(400);
        assertThat(problem.title()).isEqualTo("Domain Validation Failure");
        assertThat(problem.detail()).contains("Amount must be greater than zero");
    }
}
