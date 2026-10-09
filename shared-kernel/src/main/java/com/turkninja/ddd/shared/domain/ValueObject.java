package com.turkninja.ddd.shared.domain;

import java.io.Serializable;

/**
 * Marker interface for Value Objects in the domain.
 * <p>
 * In modern Java 27, Value Objects are almost universally implemented as
 * immutable {@code record} types with compact constructors for invariant validation.
 */
public interface ValueObject extends Serializable {
}
