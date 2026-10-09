package com.turkninja.ddd.module05.domain.model;

import com.turkninja.ddd.shared.domain.DomainEntity;
import com.turkninja.ddd.shared.domain.DomainValidationException;
import com.turkninja.ddd.shared.domain.ValueObject;

import java.math.BigDecimal;
import java.util.UUID;

public class OrderItem extends DomainEntity<OrderItem.OrderItemId> {

    public record OrderItemId(UUID value) implements ValueObject {}

    private final String productId;
    private final int quantity;
    private final BigDecimal unitPrice;

    OrderItem(String productId, int quantity, BigDecimal unitPrice) {
        super(new OrderItemId(UUID.randomUUID()));
        if (productId == null || productId.isBlank()) throw new DomainValidationException("ProductId required");
        if (quantity <= 0) throw new DomainValidationException("Quantity must be positive");
        if (unitPrice == null || unitPrice.compareTo(BigDecimal.ZERO) <= 0) throw new DomainValidationException("UnitPrice must be positive");
        this.productId = productId;
        this.quantity = quantity;
        this.unitPrice = unitPrice;
    }

    public BigDecimal subtotal() {
        return unitPrice.multiply(BigDecimal.valueOf(quantity));
    }

    public String getProductId() { return productId; }
    public int getQuantity() { return quantity; }
    public BigDecimal getUnitPrice() { return unitPrice; }
}
