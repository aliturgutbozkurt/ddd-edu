package com.turkninja.ddd.module02.infrastructure.adapter.output.persistence;

import com.turkninja.ddd.module02.application.port.out.ProductRepositoryPort;
import com.turkninja.ddd.module02.domain.model.Product;
import com.turkninja.ddd.module02.domain.model.ProductId;

import java.util.Map;
import java.util.Optional;
import java.util.concurrent.ConcurrentHashMap;

public class InMemoryProductRepositoryAdapter implements ProductRepositoryPort {

    private final Map<ProductId, Product> store = new ConcurrentHashMap<>();

    @Override
    public void save(Product product) {
        store.put(product.getId(), product);
    }

    @Override
    public Optional<Product> findById(ProductId id) {
        return Optional.ofNullable(store.get(id));
    }
}
