package com.turkninja.ddd.module05.solution;

import com.turkninja.ddd.module05.domain.model.OrderId;
import com.turkninja.ddd.shared.domain.DomainValidationException;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.math.BigDecimal;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

@DisplayName("Solution 05: Maximum Order Total Limit Verification")
class OrderWithLimitSolutionTest {

    @Test
    @DisplayName("Should allow adding items within $10,000 limit")
    void testWithinLimit() {
        OrderWithLimit order = new OrderWithLimit(OrderId.generate());
        order.addItem("LAPTOP-01", 3, new BigDecimal("2500.00")); // $7,500
        assertThat(order.calculateTotal()).isEqualTo(new BigDecimal("7500.00"));
    }

    @Test
    @DisplayName("Should reject adding item exceeding $10,000 limit")
    void testExceedingLimit() {
        OrderWithLimit order = new OrderWithLimit(OrderId.generate());
        order.addItem("SERVER-01", 1, new BigDecimal("8000.00"));

        assertThatThrownBy(() -> order.addItem("SERVER-02", 1, new BigDecimal("3000.00")))
                .isInstanceOf(DomainValidationException.class)
                .hasMessageContaining("Order total cannot exceed maximum allowed limit");
    }
}
