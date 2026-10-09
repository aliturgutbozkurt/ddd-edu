package com.turkninja.ddd.module08.infrastructure.adapter.output.persistence;

import com.turkninja.ddd.module08.application.port.out.CustomerRepositoryPort;
import com.turkninja.ddd.module08.domain.model.Customer;
import com.turkninja.ddd.module08.domain.model.CustomerId;

import java.util.Map;
import java.util.Optional;
import java.util.UUID;
import java.util.concurrent.ConcurrentHashMap;

public class CustomerPersistenceAdapter implements CustomerRepositoryPort {

    // Database record representation
    record CustomerDbRecord(UUID id, String name, String email) {}

    private final Map<UUID, CustomerDbRecord> databaseTable = new ConcurrentHashMap<>();

    @Override
    public void save(Customer customer) {
        CustomerDbRecord dbRecord = new CustomerDbRecord(
                customer.getId().value(),
                customer.getName(),
                customer.getEmail()
        );
        databaseTable.put(dbRecord.id(), dbRecord);
    }

    @Override
    public Optional<Customer> findById(CustomerId id) {
        CustomerDbRecord record = databaseTable.get(id.value());
        if (record == null) return Optional.empty();
        return Optional.of(new Customer(new CustomerId(record.id()), record.name(), record.email()));
    }
}
