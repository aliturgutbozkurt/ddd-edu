package com.turkninja.ddd.shared.domain;

import java.io.Serializable;
import java.time.Instant;
import java.util.UUID;

/**
 * Marker interface for all Domain Events across all Bounded Contexts.
 * Every domain event represents an immutable statement of fact that occurred in the past.
 */
public interface DomainEvent extends Serializable {

    /**
     * Unique identifier for this specific event instance (idempotency key).
     */
    UUID eventId();

    /**
     * Timestamp at which the event occurred in UTC.
     */
    Instant occurredOn();
}
