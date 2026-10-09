package com.turkninja.ddd.module08.infrastructure;

import com.turkninja.ddd.module08.domain.model.Customer;
import com.turkninja.ddd.module08.domain.model.CustomerId;
import com.turkninja.ddd.module08.infrastructure.adapter.output.persistence.CustomerPersistenceAdapter;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.util.UUID;

import static org.assertj.core.api.Assertions.assertThat;

@DisplayName("Module 08: Driven Persistence Adapter Tests")
class CustomerPersistenceAdapterTest {

    @Test
    @DisplayName("Should save and reconstitute pure domain customer through persistence adapter")
    void testSaveAndReconstituteCustomer() {
        CustomerPersistenceAdapter adapter = new CustomerPersistenceAdapter();
        CustomerId id = new CustomerId(UUID.randomUUID());
        Customer customer = new Customer(id, "Grace Hopper", "grace@navy.mil");

        adapter.save(customer);

        assertThat(adapter.findById(id)).isPresent();
        assertThat(adapter.findById(id).get().getName()).isEqualTo("Grace Hopper");
    }
}
