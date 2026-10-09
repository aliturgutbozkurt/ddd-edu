package com.turkninja.ddd.module03.domain.model;

import com.turkninja.ddd.shared.domain.DomainValidationException;
import com.turkninja.ddd.shared.domain.ValueObject;

public record Iban(String value) implements ValueObject {
    public Iban {
        if (value == null || value.replaceAll("\\s+", "").length() < 15) {
            throw new DomainValidationException("Invalid IBAN length. Given: " + value);
        }
        value = value.replaceAll("\\s+", "").toUpperCase();
    }
}
