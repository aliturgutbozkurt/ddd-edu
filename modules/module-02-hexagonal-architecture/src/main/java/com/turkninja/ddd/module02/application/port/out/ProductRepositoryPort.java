package com.turkninja.ddd.module02.application.port.out;

import com.turkninja.ddd.module02.domain.model.Product;
import com.turkninja.ddd.module02.domain.model.ProductId;

import java.util.Optional;

public interface ProductRepositoryPort {
    void save(Product product);
    Optional<Product> findById(ProductId id);
}
