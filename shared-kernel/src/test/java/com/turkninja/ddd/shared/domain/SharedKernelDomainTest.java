package com.turkninja.ddd.shared.domain;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.time.Instant;
import java.util.UUID;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

class SharedKernelDomainTest {

    record SampleId(UUID value) implements ValueObject {
        SampleId {
            if (value == null) {
                throw new DomainValidationException("SampleId cannot be null");
            }
        }
    }

    record SampleDomainEvent(UUID eventId, Instant occurredOn, String payload) implements DomainEvent {}

    static class SampleAggregate extends AggregateRoot<SampleId> {
        private String name;

        SampleAggregate(SampleId id, String name) {
            super(id);
            if (name == null || name.isBlank()) {
                throw new DomainValidationException("Name cannot be blank");
            }
            this.name = name;
        }

        void updateName(String newName) {
            if (newName == null || newName.isBlank()) {
                throw new DomainValidationException("New name cannot be blank");
            }
            this.name = newName;
            recordEvent(new SampleDomainEvent(UUID.randomUUID(), Instant.now(), newName));
        }

        public String getName() {
            return name;
        }
    }

    @Test
    @DisplayName("AggregateRoot records domain events and clears them upon request")
    void testAggregateEventLifecycle() {
        SampleId id = new SampleId(UUID.randomUUID());
        SampleAggregate aggregate = new SampleAggregate(id, "Initial");

        assertThat(aggregate.getDomainEvents()).isEmpty();

        aggregate.updateName("Updated");
        assertThat(aggregate.getDomainEvents()).hasSize(1);
        assertThat(aggregate.getName()).isEqualTo("Updated");

        aggregate.clearDomainEvents();
        assertThat(aggregate.getDomainEvents()).isEmpty();
    }

    @Test
    @DisplayName("Validation exception is thrown on invalid state")
    void testValidationFailure() {
        assertThatThrownBy(() -> new SampleId(null))
                .isInstanceOf(DomainValidationException.class)
                .hasMessageContaining("SampleId cannot be null");
    }
}
