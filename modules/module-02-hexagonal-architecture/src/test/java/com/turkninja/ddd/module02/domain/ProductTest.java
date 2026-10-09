package com.turkninja.ddd.module02.domain;

import com.turkninja.ddd.module02.domain.model.Product;
import com.turkninja.ddd.module02.domain.model.ProductId;
import com.turkninja.ddd.module02.domain.model.ProductPrice;
import com.turkninja.ddd.shared.domain.DomainValidationException;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

@DisplayName("Module 02: Product Aggregate & Port Tests")
class ProductTest {

    @Test
    @DisplayName("Should successfully create product with valid invariant checks")
    void shouldCreateProduct() {
        ProductId id = ProductId.generate();
        Product product = new Product(id, "Domain Driven Design Book", ProductPrice.of(49.99, "USD"));

        assertThat(product.getId()).isEqualTo(id);
        assertThat(product.getName()).isEqualTo("Domain Driven Design Book");
        assertThat(product.isActive()).isTrue();
    }

    @Test
    @DisplayName("Should reject blank product name")
    void shouldRejectBlankName() {
        assertThatThrownBy(() -> new Product(ProductId.generate(), "   ", ProductPrice.of(10.0, "USD")))
                .isInstanceOf(DomainValidationException.class)
                .hasMessageContaining("Product name cannot be empty");
    }
}
