package com.turkninja.ddd.module02.application.port.in;

import com.turkninja.ddd.module02.domain.model.ProductId;
import com.turkninja.ddd.module02.domain.model.ProductPrice;

public interface RegisterProductUseCase {
    ProductId registerProduct(RegisterProductCommand command);

    record RegisterProductCommand(String name, ProductPrice price) {}
}
