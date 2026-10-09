package com.turkninja.ddd.capstone.saga;

import com.turkninja.ddd.capstone.fulfillment.domain.model.Shipment;
import com.turkninja.ddd.capstone.fulfillment.domain.model.ShipmentId;
import com.turkninja.ddd.capstone.ordering.domain.model.Order;
import com.turkninja.ddd.capstone.ordering.domain.model.OrderId;

import java.math.BigDecimal;
import java.util.Objects;
import java.util.UUID;

public class OrderFulfillmentSagaOrchestrator {

    public record ProcessOrderResult(Order order, Shipment shipment) {}

    public ProcessOrderResult processOrderConfirmation(OrderId orderId, BigDecimal amount, String trackingNumber) {
        Objects.requireNonNull(orderId, "OrderId required");

        // 1. Ordering Context: Create and Confirm Order
        Order order = new Order(orderId, amount);
        order.confirm();

        // 2. Anti-Corruption Layer: Translate OrderConfirmed to Shipment
        Shipment shipment = new Shipment(ShipmentId.generate(), order.getId().value());
        shipment.dispatch(trackingNumber);

        return new ProcessOrderResult(order, shipment);
    }
}
