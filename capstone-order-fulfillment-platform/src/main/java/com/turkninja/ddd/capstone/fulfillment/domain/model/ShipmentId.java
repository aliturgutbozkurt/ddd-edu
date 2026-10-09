package com.turkninja.ddd.capstone.fulfillment.domain.model;

import com.turkninja.ddd.shared.domain.ValueObject;
import java.util.UUID;

public record ShipmentId(UUID value) implements ValueObject {
    public static ShipmentId generate() { return new ShipmentId(UUID.randomUUID()); }
}
