package com.turkninja.ddd.module09.solution;

import com.turkninja.ddd.shared.domain.DomainValidationException;

import java.net.URI;
import java.util.Map;
import java.util.NoSuchElementException;

/**
 * Driving adapter exception handler translating domain exceptions to RFC 9457 Problem Details.
 */
public class GlobalExceptionHandler {

    private static final URI VALIDATION_TYPE = URI.create("https://api.turkninja.com/errors/validation-error");
    private static final URI NOT_FOUND_TYPE = URI.create("https://api.turkninja.com/errors/not-found");
    private static final URI INTERNAL_ERROR_TYPE = URI.create("https://api.turkninja.com/errors/internal-error");

    public ProblemDetailRecord handleException(Exception ex, String requestPath) {
        URI instance = URI.create(requestPath);

        if (ex instanceof DomainValidationException dve) {
            return ProblemDetailRecord.of(
                    VALIDATION_TYPE,
                    "Domain Validation Failure",
                    400,
                    dve.getMessage(),
                    instance,
                    Map.of("errorCategory", "BUSINESS_RULE_VIOLATION")
            );
        }

        if (ex instanceof NoSuchElementException nse) {
            return ProblemDetailRecord.of(
                    NOT_FOUND_TYPE,
                    "Resource Not Found",
                    404,
                    nse.getMessage() != null ? nse.getMessage() : "Requested resource does not exist",
                    instance
            );
        }

        return ProblemDetailRecord.of(
                INTERNAL_ERROR_TYPE,
                "Internal Server Error",
                500,
                "An unexpected server error occurred.",
                instance
        );
    }
}
