package com.turkninja.ddd.capstone.saga;

import com.turkninja.ddd.capstone.fulfillment.domain.model.Shipment;
import com.turkninja.ddd.capstone.ordering.domain.model.Order;
import com.turkninja.ddd.capstone.ordering.domain.model.OrderId;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.math.BigDecimal;

import static org.assertj.core.api.Assertions.assertThat;

@DisplayName("Capstone: End-to-End Order-to-Fulfillment Saga Verification")
class OrderFulfillmentSagaTest {

    @Test
    @DisplayName("Saga coordinates order confirmation and shipment dispatch cleanly across contexts")
    void testEndToEndSaga() {
        OrderFulfillmentSagaOrchestrator saga = new OrderFulfillmentSagaOrchestrator();
        OrderId orderId = OrderId.generate();

        OrderFulfillmentSagaOrchestrator.ProcessOrderResult result =
                saga.processOrderConfirmation(orderId, new BigDecimal("250.00"), "FEDEX-889900");

        assertThat(result.order().getStatus()).isEqualTo(Order.Status.CONFIRMED);
        assertThat(result.shipment().getStatus()).isEqualTo(Shipment.ShipmentStatus.DISPATCHED);
        assertThat(result.shipment().getTrackingCode()).isEqualTo("FEDEX-889900");
        assertThat(result.shipment().getOrderId()).isEqualTo(orderId.value());
    }
}
