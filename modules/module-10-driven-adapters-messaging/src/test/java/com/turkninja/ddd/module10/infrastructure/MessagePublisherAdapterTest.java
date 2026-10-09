package com.turkninja.ddd.module10.infrastructure;

import com.turkninja.ddd.module10.application.port.out.NotificationSenderPort;
import com.turkninja.ddd.module10.infrastructure.adapter.output.messaging.SimulatedMessagePublisherAdapter;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

@DisplayName("Module 10: Driven Messaging Adapter Tests")
class MessagePublisherAdapterTest {

    @Test
    @DisplayName("Should publish notification message via driven adapter")
    void testMessagePublishing() {
        SimulatedMessagePublisherAdapter adapter = new SimulatedMessagePublisherAdapter();
        boolean success = adapter.sendNotification(
                new NotificationSenderPort.NotificationMessage("alice@example.com", "Order Update", "Your order has shipped!"));

        assertThat(success).isTrue();
        assertThat(adapter.getPublishedMessages()).hasSize(1);
        assertThat(adapter.getPublishedMessages().getFirst().title()).isEqualTo("Order Update");
    }
}
