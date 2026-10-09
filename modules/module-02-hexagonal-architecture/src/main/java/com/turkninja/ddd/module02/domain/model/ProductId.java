package com.turkninja.ddd.module02.domain.model;

import com.turkninja.ddd.shared.domain.DomainValidationException;
import com.turkninja.ddd.shared.domain.ValueObject;

import java.util.UUID;

public record ProductId(UUID value) implements ValueObject {
    public ProductId {
        if (value == null) {
            throw new DomainValidationException("ProductId cannot be null");
        }
    }

    public static ProductId generate() {
        return new ProductId(UUID.randomUUID());
    }
}
