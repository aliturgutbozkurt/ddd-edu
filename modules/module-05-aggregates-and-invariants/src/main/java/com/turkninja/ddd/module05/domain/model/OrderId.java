package com.turkninja.ddd.module05.domain.model;

import com.turkninja.ddd.shared.domain.DomainValidationException;
import com.turkninja.ddd.shared.domain.ValueObject;

import java.util.UUID;

public record OrderId(UUID value) implements ValueObject {
    public OrderId {
        if (value == null) throw new DomainValidationException("OrderId cannot be null");
    }

    public static OrderId generate() {
        return new OrderId(UUID.randomUUID());
    }
}
