package com.turkninja.ddd.module03.solution;

import com.turkninja.ddd.shared.domain.DomainValidationException;
import com.turkninja.ddd.shared.domain.ValueObject;

import java.util.regex.Pattern;

public record TaxNumber(String value) implements ValueObject {
    private static final Pattern PATTERN = Pattern.compile("^\\d{10}$");

    public TaxNumber {
        if (value == null || !PATTERN.matcher(value).matches() || "0000000000".equals(value)) {
            throw new DomainValidationException("Tax number must be a non-zero 10-digit numeric string. Given: " + value);
        }
    }
}
