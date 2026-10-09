package com.turkninja.ddd.shared.domain;

/**
 * Thrown whenever a domain invariant or business rule constraint is violated.
 * Pure Java exception with zero framework dependencies.
 */
public class DomainValidationException extends RuntimeException {

    public DomainValidationException(String message) {
        super(message);
    }

    public DomainValidationException(String message, Throwable cause) {
        super(message, cause);
    }
}
