package com.turkninja.ddd.module08.domain.model;

import com.turkninja.ddd.shared.domain.DomainEntity;

public class Customer extends DomainEntity<CustomerId> {
    private final String name;
    private final String email;

    public Customer(CustomerId id, String name, String email) {
        super(id);
        this.name = name;
        this.email = email;
    }

    public String getName() { return name; }
    public String getEmail() { return email; }
}
