package com.turkninja.ddd.module02.domain.model;

import com.turkninja.ddd.shared.domain.AggregateRoot;
import com.turkninja.ddd.shared.domain.DomainValidationException;

import java.util.Objects;

public class Product extends AggregateRoot<ProductId> {
    private String name;
    private ProductPrice price;
    private boolean active;

    public Product(ProductId id, String name, ProductPrice price) {
        super(id);
        setName(name);
        this.price = Objects.requireNonNull(price, "Price cannot be null");
        this.active = true;
    }

    public void updatePrice(ProductPrice newPrice) {
        this.price = Objects.requireNonNull(newPrice, "New price cannot be null");
    }

    public void deactivate() {
        this.active = false;
    }

    private void setName(String name) {
        if (name == null || name.isBlank()) {
            throw new DomainValidationException("Product name cannot be empty");
        }
        this.name = name.trim();
    }

    public String getName() { return name; }
    public ProductPrice getPrice() { return price; }
    public boolean isActive() { return active; }
}
