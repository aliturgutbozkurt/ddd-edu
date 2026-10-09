package com.turkninja.ddd.module05.domain;

import com.turkninja.ddd.module05.domain.model.Order;
import com.turkninja.ddd.module05.domain.model.OrderId;
import com.turkninja.ddd.shared.domain.DomainValidationException;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.math.BigDecimal;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

@DisplayName("Module 05: Order Aggregate & Consistency Boundary Tests")
class OrderAggregateTest {

    @Test
    @DisplayName("Should correctly calculate order total from line items")
    void testOrderTotalCalculation() {
        Order order = new Order(OrderId.generate());
        order.addItem("PROD-001", 2, new BigDecimal("25.00")); // 50.00
        order.addItem("PROD-002", 1, new BigDecimal("30.00")); // 30.00

        assertThat(order.calculateTotal()).isEqualTo(new BigDecimal("80.00"));
        assertThat(order.getItems()).hasSize(2);
    }

    @Test
    @DisplayName("Should prevent confirming an empty order")
    void testEmptyOrderConfirmation() {
        Order order = new Order(OrderId.generate());

        assertThatThrownBy(order::confirm)
                .isInstanceOf(DomainValidationException.class)
                .hasMessageContaining("Cannot confirm an empty order");
    }

    @Test
    @DisplayName("Should reject adding items to a confirmed order")
    void testAddingItemsToConfirmedOrder() {
        Order order = new Order(OrderId.generate());
        order.addItem("PROD-001", 1, new BigDecimal("10.00"));
        order.confirm();

        assertThatThrownBy(() -> order.addItem("PROD-002", 1, new BigDecimal("20.00")))
                .isInstanceOf(DomainValidationException.class)
                .hasMessageContaining("Cannot add items to an order in status: CONFIRMED");
    }
}
