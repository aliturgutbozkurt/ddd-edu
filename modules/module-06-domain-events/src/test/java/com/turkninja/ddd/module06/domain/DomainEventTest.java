package com.turkninja.ddd.module06.domain;

import com.turkninja.ddd.module06.domain.event.OrderEvent;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.time.Instant;
import java.util.UUID;

import static org.assertj.core.api.Assertions.assertThat;

@DisplayName("Module 06: Domain Events Sealed Hierarchy Test")
class DomainEventTest {

    @Test
    @DisplayName("Pattern matching handles sealed domain events exhaustively")
    void testPatternMatchingEvents() {
        UUID orderId = UUID.randomUUID();
        OrderEvent event = new OrderEvent.OrderPaid(UUID.randomUUID(), orderId, "PAY-12345", Instant.now());

        String result = switch (event) {
            case OrderEvent.OrderCreated created -> "Created: " + created.orderId();
            case OrderEvent.OrderPaid paid -> "Paid: " + paid.paymentRef();
            case OrderEvent.OrderCancelled cancelled -> "Cancelled: " + cancelled.reason();
        };

        assertThat(result).isEqualTo("Paid: PAY-12345");
    }
}
