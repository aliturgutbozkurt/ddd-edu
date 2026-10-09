package com.turkninja.ddd.module12.domain;

import com.turkninja.ddd.shared.domain.ValueObject;
import java.time.Instant;
import java.util.UUID;

public record OutboxRecord(UUID id, String eventType, String payload, Instant occurredOn, boolean processed)
        implements ValueObject {

    public static OutboxRecord create(String eventType, String payload) {
        return new OutboxRecord(UUID.randomUUID(), eventType, payload, Instant.now(), false);
    }

    public OutboxRecord markProcessed() {
        return new OutboxRecord(this.id, this.eventType, this.payload, this.occurredOn, true);
    }
}
