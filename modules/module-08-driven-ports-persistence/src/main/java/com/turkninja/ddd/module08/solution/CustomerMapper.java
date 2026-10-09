package com.turkninja.ddd.module08.solution;

import com.turkninja.ddd.module08.domain.model.Customer;
import com.turkninja.ddd.module08.domain.model.CustomerId;

public final class CustomerMapper {

    private CustomerMapper() {}

    public static CustomerJpaEntity toEntity(Customer domain) {
        return new CustomerJpaEntity(
                domain.getId().value(),
                domain.getName(),
                domain.getEmail()
        );
    }

    public static Customer toDomain(CustomerJpaEntity entity) {
        return new Customer(
                new CustomerId(entity.getId()),
                entity.getName(),
                entity.getEmail()
        );
    }
}
