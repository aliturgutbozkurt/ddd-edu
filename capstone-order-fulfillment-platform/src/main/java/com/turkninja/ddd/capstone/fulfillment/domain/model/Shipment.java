package com.turkninja.ddd.capstone.fulfillment.domain.model;

import com.turkninja.ddd.shared.domain.AggregateRoot;
import com.turkninja.ddd.shared.domain.DomainValidationException;

import java.util.Objects;
import java.util.UUID;

public class Shipment extends AggregateRoot<ShipmentId> {

    public enum ShipmentStatus { CREATED, DISPATCHED, DELIVERED }

    private final UUID orderId;
    private String trackingCode;
    private ShipmentStatus status;

    public Shipment(ShipmentId id, UUID orderId) {
        super(id);
        this.orderId = Objects.requireNonNull(orderId, "OrderId required");
        this.status = ShipmentStatus.CREATED;
    }

    public void dispatch(String trackingCode) {
        if (trackingCode == null || trackingCode.isBlank()) {
            throw new DomainValidationException("Tracking code required for dispatch");
        }
        this.trackingCode = trackingCode.trim();
        this.status = ShipmentStatus.DISPATCHED;
    }

    public UUID getOrderId() { return orderId; }
    public String getTrackingCode() { return trackingCode; }
    public ShipmentStatus getStatus() { return status; }
}
