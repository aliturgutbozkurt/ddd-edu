package com.turkninja.ddd.module06.solution;

import com.turkninja.ddd.module06.domain.event.OrderEvent;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.time.Instant;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

import static org.assertj.core.api.Assertions.assertThat;

@DisplayName("Solution 06: Synchronous Event Dispatcher Verification")
class EventDispatcherSolutionTest {

    @Test
    @DisplayName("Dispatches domain events cleanly to registered handlers")
    void testEventDispatching() {
        SynchronousEventDispatcher dispatcher = new SynchronousEventDispatcher();
        List<String> auditLog = new ArrayList<>();

        dispatcher.registerSubscriber(event -> {
            if (event instanceof OrderEvent.OrderPaid paid) {
                auditLog.add("AUDIT: Payment logged for " + paid.orderId());
            }
        });

        UUID orderId = UUID.randomUUID();
        dispatcher.publish(new OrderEvent.OrderPaid(UUID.randomUUID(), orderId, "PAY-99", Instant.now()));

        assertThat(auditLog).hasSize(1);
        assertThat(auditLog.getFirst()).contains("AUDIT: Payment logged for " + orderId);
    }
}
