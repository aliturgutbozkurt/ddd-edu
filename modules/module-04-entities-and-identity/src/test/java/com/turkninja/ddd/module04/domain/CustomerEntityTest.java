package com.turkninja.ddd.module04.domain;

import com.turkninja.ddd.module04.domain.model.Customer;
import com.turkninja.ddd.module04.domain.model.CustomerId;
import com.turkninja.ddd.module04.domain.model.CustomerTier;
import com.turkninja.ddd.shared.domain.DomainValidationException;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

@DisplayName("Module 04: Customer Entity & Identity Tests")
class CustomerEntityTest {

    @Test
    @DisplayName("Two customer instances with same CustomerId are equal regardless of attributes")
    void testIdentityEquality() {
        CustomerId id = CustomerId.generate();
        Customer c1 = new Customer(id, "Alice Smith", "alice@example.com");
        Customer c2 = new Customer(id, "Alice Jones", "alice.new@example.com");

        assertThat(c1).isEqualTo(c2);
        assertThat(c1.hashCode()).isEqualTo(c2.hashCode());
    }

    @Test
    @DisplayName("Should prevent tier downgrade invariant violation")
    void testTierUpgradeInvariant() {
        Customer c = new Customer(CustomerId.generate(), "Bob", "bob@example.com");
        c.upgradeTier(CustomerTier.GOLD);

        assertThatThrownBy(() -> c.upgradeTier(CustomerTier.SILVER))
                .isInstanceOf(DomainValidationException.class)
                .hasMessageContaining("Cannot downgrade tier directly");
    }
}
