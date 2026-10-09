package com.turkninja.ddd.module08.application.port.out;

import com.turkninja.ddd.module08.domain.model.Customer;
import com.turkninja.ddd.module08.domain.model.CustomerId;

import java.util.Optional;

public interface CustomerRepositoryPort {
    void save(Customer customer);
    Optional<Customer> findById(CustomerId id);
}
