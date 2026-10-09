package com.turkninja.ddd.module05.domain.model;

import com.turkninja.ddd.shared.domain.AggregateRoot;
import com.turkninja.ddd.shared.domain.DomainValidationException;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Order extends AggregateRoot<OrderId> {

    public enum Status { PENDING, CONFIRMED, CANCELLED }

    private final List<OrderItem> items = new ArrayList<>();
    private Status status;

    public Order(OrderId id) {
        super(id);
        this.status = Status.PENDING;
    }

    public void addItem(String productId, int quantity, BigDecimal unitPrice) {
        if (status != Status.PENDING) {
            throw new DomainValidationException("Cannot add items to an order in status: " + status);
        }
        if (items.size() >= 50) {
            throw new DomainValidationException("Order cannot exceed 50 line items");
        }
        items.add(new OrderItem(productId, quantity, unitPrice));
    }

    public void confirm() {
        if (items.isEmpty()) {
            throw new DomainValidationException("Cannot confirm an empty order");
        }
        if (status != Status.PENDING) {
            throw new DomainValidationException("Only pending orders can be confirmed");
        }
        this.status = Status.CONFIRMED;
    }

    public BigDecimal calculateTotal() {
        return items.stream()
                .map(OrderItem::subtotal)
                .reduce(BigDecimal.ZERO, BigDecimal::add);
    }

    public List<OrderItem> getItems() {
        return Collections.unmodifiableList(items);
    }

    public Status getStatus() { return status; }
}
