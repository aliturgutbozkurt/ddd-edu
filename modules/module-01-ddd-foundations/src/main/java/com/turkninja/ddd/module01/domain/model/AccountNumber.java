package com.turkninja.ddd.module01.domain.model;

import com.turkninja.ddd.shared.domain.DomainValidationException;
import com.turkninja.ddd.shared.domain.ValueObject;

import java.util.regex.Pattern;

/**
 * Value Object representing a bank account number.
 * Must match a 10-digit numeric pattern.
 */
public record AccountNumber(String value) implements ValueObject {

    private static final Pattern ACCOUNT_PATTERN = Pattern.compile("^\\d{10}$");

    public AccountNumber {
        if (value == null || !ACCOUNT_PATTERN.matcher(value).matches()) {
            throw new DomainValidationException("Account number must be a valid 10-digit string. Given: " + value);
        }
    }
}
