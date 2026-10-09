package com.turkninja.ddd.module04.domain.model;

import com.turkninja.ddd.shared.domain.DomainValidationException;
import com.turkninja.ddd.shared.domain.ValueObject;

import java.util.UUID;

public record CustomerId(UUID value) implements ValueObject {
    public CustomerId {
        if (value == null) {
            throw new DomainValidationException("CustomerId cannot be null");
        }
    }

    public static CustomerId generate() {
        return new CustomerId(UUID.randomUUID());
    }
}
