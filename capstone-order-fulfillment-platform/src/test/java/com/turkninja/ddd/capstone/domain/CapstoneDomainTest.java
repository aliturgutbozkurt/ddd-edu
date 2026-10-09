package com.turkninja.ddd.capstone.domain;

import com.turkninja.ddd.capstone.fulfillment.domain.model.Shipment;
import com.turkninja.ddd.capstone.fulfillment.domain.model.ShipmentId;
import com.turkninja.ddd.capstone.ordering.domain.model.Order;
import com.turkninja.ddd.capstone.ordering.domain.model.OrderId;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.math.BigDecimal;
import java.util.UUID;

import static org.assertj.core.api.Assertions.assertThat;

@DisplayName("Capstone: Ordering & Fulfillment Bounded Context Tests")
class CapstoneDomainTest {

    @Test
    @DisplayName("Ordering Aggregate enforces confirmation lifecycle")
    void testOrderConfirmation() {
        Order order = new Order(OrderId.generate(), new BigDecimal("120.00"));
        assertThat(order.getStatus()).isEqualTo(Order.Status.PENDING);

        order.confirm();
        assertThat(order.getStatus()).isEqualTo(Order.Status.CONFIRMED);
    }

    @Test
    @DisplayName("Fulfillment Aggregate enforces shipment dispatch with tracking code")
    void testShipmentDispatch() {
        UUID orderId = UUID.randomUUID();
        Shipment shipment = new Shipment(ShipmentId.generate(), orderId);

        shipment.dispatch("TRK-998877");
        assertThat(shipment.getStatus()).isEqualTo(Shipment.ShipmentStatus.DISPATCHED);
        assertThat(shipment.getTrackingCode()).isEqualTo("TRK-998877");
    }
}
