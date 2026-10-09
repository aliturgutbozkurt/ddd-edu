package com.turkninja.ddd.module05.solution;

import com.turkninja.ddd.module05.domain.model.Order;
import com.turkninja.ddd.module05.domain.model.OrderId;
import com.turkninja.ddd.shared.domain.DomainValidationException;

import java.math.BigDecimal;

public class OrderWithLimit extends Order {

    private static final BigDecimal MAX_ORDER_TOTAL = new BigDecimal("10000.00");

    public OrderWithLimit(OrderId id) {
        super(id);
    }

    @Override
    public void addItem(String productId, int quantity, BigDecimal unitPrice) {
        BigDecimal itemTotal = unitPrice.multiply(BigDecimal.valueOf(quantity));
        BigDecimal projectedTotal = calculateTotal().add(itemTotal);
        if (projectedTotal.compareTo(MAX_ORDER_TOTAL) > 0) {
            throw new DomainValidationException("Order total cannot exceed maximum allowed limit: " + MAX_ORDER_TOTAL);
        }
        super.addItem(productId, quantity, unitPrice);
    }
}
