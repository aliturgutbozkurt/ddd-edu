package com.turkninja.ddd.capstone.ordering.domain.model;

import com.turkninja.ddd.shared.domain.AggregateRoot;
import com.turkninja.ddd.shared.domain.DomainValidationException;

import java.math.BigDecimal;
import java.util.Objects;

public class Order extends AggregateRoot<OrderId> {

    public enum Status { PENDING, CONFIRMED, CANCELLED }

    private Status status;
    private final BigDecimal totalAmount;

    public Order(OrderId id, BigDecimal totalAmount) {
        super(id);
        Objects.requireNonNull(totalAmount, "Total amount cannot be null");
        if (totalAmount.compareTo(BigDecimal.ZERO) <= 0) {
            throw new DomainValidationException("Total order amount must be positive");
        }
        this.totalAmount = totalAmount;
        this.status = Status.PENDING;
    }

    public void confirm() {
        if (this.status != Status.PENDING) {
            throw new DomainValidationException("Only pending orders can be confirmed");
        }
        this.status = Status.CONFIRMED;
    }

    public Status getStatus() { return status; }
    public BigDecimal getTotalAmount() { return totalAmount; }
}
