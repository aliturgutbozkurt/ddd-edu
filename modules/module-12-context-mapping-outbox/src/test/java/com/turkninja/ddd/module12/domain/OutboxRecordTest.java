package com.turkninja.ddd.module12.domain;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

@DisplayName("Module 12: Transactional Outbox Tests")
class OutboxRecordTest {

    @Test
    @DisplayName("Should create outbox record and mark processed immutably")
    void testOutboxRecordLifecycle() {
        OutboxRecord initial = OutboxRecord.create("OrderCreatedEvent", "{\"orderId\":\"123\"}");
        assertThat(initial.processed()).isFalse();

        OutboxRecord processed = initial.markProcessed();
        assertThat(processed.processed()).isTrue();
        assertThat(processed.id()).isEqualTo(initial.id());
    }
}
