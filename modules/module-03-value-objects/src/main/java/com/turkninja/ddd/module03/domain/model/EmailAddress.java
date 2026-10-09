package com.turkninja.ddd.module03.domain.model;

import com.turkninja.ddd.shared.domain.DomainValidationException;
import com.turkninja.ddd.shared.domain.ValueObject;

import java.util.regex.Pattern;

public record EmailAddress(String value) implements ValueObject {
    private static final Pattern EMAIL_PATTERN = Pattern.compile("^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+$");

    public EmailAddress {
        if (value == null || !EMAIL_PATTERN.matcher(value).matches()) {
            throw new DomainValidationException("Invalid email address format: " + value);
        }
        value = value.toLowerCase().trim();
    }
}
