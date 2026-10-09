package com.turkninja.ddd.module08.solution;

import com.turkninja.ddd.module08.domain.model.Customer;
import com.turkninja.ddd.module08.domain.model.CustomerId;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.util.UUID;

import static org.assertj.core.api.Assertions.assertThat;

@DisplayName("Solution 08: Customer Mapper Verification")
class CustomerMapperSolutionTest {

    @Test
    @DisplayName("Cleanly maps between JPA entity and pure domain model")
    void testBidirectionalMapping() {
        CustomerId id = new CustomerId(UUID.randomUUID());
        Customer domain = new Customer(id, "Margaret Hamilton", "margaret@mit.edu");

        CustomerJpaEntity entity = CustomerMapper.toEntity(domain);
        assertThat(entity.getId()).isEqualTo(id.value());
        assertThat(entity.getName()).isEqualTo("Margaret Hamilton");

        Customer reconstituted = CustomerMapper.toDomain(entity);
        assertThat(reconstituted.getId()).isEqualTo(domain.getId());
        assertThat(reconstituted.getName()).isEqualTo(domain.getName());
    }
}
