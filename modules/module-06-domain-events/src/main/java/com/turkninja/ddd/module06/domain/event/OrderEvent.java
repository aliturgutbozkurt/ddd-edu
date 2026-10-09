package com.turkninja.ddd.module06.domain.event;

import com.turkninja.ddd.shared.domain.DomainEvent;

import java.time.Instant;
import java.util.UUID;

public sealed interface OrderEvent extends DomainEvent {

    UUID orderId();

    record OrderCreated(UUID eventId, UUID orderId, Instant occurredOn) implements OrderEvent {}
    record OrderPaid(UUID eventId, UUID orderId, String paymentRef, Instant occurredOn) implements OrderEvent {}
    record OrderCancelled(UUID eventId, UUID orderId, String reason, Instant occurredOn) implements OrderEvent {}
}
