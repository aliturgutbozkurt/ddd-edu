package com.turkninja.ddd.shared.domain;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Objects;

/**
 * Base class for all Aggregate Roots.
 * Manages consistency boundaries, transactional encapsulation, and records domain events.
 *
 * @param <ID> Strongly typed identifier Value Object.
 */
public abstract class AggregateRoot<ID extends ValueObject> extends DomainEntity<ID> {

    private final List<DomainEvent> domainEvents = new ArrayList<>();

    protected AggregateRoot(ID id) {
        super(id);
    }

    /**
     * Records a new domain event that occurred as a result of an aggregate command execution.
     */
    protected void recordEvent(DomainEvent event) {
        Objects.requireNonNull(event, "Domain event must not be null");
        this.domainEvents.add(event);
    }

    /**
     * Returns an unmodifiable snapshot of recorded domain events waiting to be dispatched.
     */
    public List<DomainEvent> getDomainEvents() {
        return Collections.unmodifiableList(domainEvents);
    }

    /**
     * Clears all recorded domain events. Should be called after successful dispatch.
     */
    public void clearDomainEvents() {
        this.domainEvents.clear();
    }
}
