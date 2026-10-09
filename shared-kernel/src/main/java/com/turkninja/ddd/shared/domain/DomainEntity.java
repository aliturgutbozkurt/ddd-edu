package com.turkninja.ddd.shared.domain;

import java.util.Objects;

/**
 * Base abstract class for Domain Entities.
 * Entities are distinguished by their identity (ID), not by their attributes.
 *
 * @param <ID> The Value Object representing the entity's unique identifier.
 */
public abstract class DomainEntity<ID extends ValueObject> {

    protected final ID id;

    protected DomainEntity(ID id) {
        this.id = Objects.requireNonNull(id, "Entity ID must not be null");
    }

    public ID getId() {
        return id;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        DomainEntity<?> that = (DomainEntity<?>) o;
        return Objects.equals(id, that.id);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id);
    }
}
