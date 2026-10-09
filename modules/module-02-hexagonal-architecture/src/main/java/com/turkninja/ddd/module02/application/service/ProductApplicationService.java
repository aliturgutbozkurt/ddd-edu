package com.turkninja.ddd.module02.application.service;

import com.turkninja.ddd.module02.application.port.in.RegisterProductUseCase;
import com.turkninja.ddd.module02.application.port.out.ProductRepositoryPort;
import com.turkninja.ddd.module02.domain.model.Product;
import com.turkninja.ddd.module02.domain.model.ProductId;

import java.util.Objects;

public class ProductApplicationService implements RegisterProductUseCase {

    private final ProductRepositoryPort repositoryPort;

    public ProductApplicationService(ProductRepositoryPort repositoryPort) {
        this.repositoryPort = Objects.requireNonNull(repositoryPort);
    }

    @Override
    public ProductId registerProduct(RegisterProductCommand command) {
        ProductId id = ProductId.generate();
        Product product = new Product(id, command.name(), command.price());
        repositoryPort.save(product);
        return id;
    }
}
