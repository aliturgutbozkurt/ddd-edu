package com.turkninja.ddd.capstone.ordering.domain.model;

import com.turkninja.ddd.shared.domain.ValueObject;
import java.util.UUID;

public record OrderId(UUID value) implements ValueObject {
    public static OrderId generate() { return new OrderId(UUID.randomUUID()); }
}
