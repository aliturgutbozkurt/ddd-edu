package com.turkninja.ddd.module04.domain.model;

import com.turkninja.ddd.shared.domain.DomainEntity;
import com.turkninja.ddd.shared.domain.DomainValidationException;

import java.util.Objects;

public class Customer extends DomainEntity<CustomerId> {
    private String fullName;
    private String email;
    private CustomerTier tier;

    public Customer(CustomerId id, String fullName, String email) {
        super(id);
        updateContactDetails(fullName, email);
        this.tier = CustomerTier.STANDARD;
    }

    public void updateContactDetails(String fullName, String email) {
        if (fullName == null || fullName.isBlank()) {
            throw new DomainValidationException("Customer name cannot be blank");
        }
        if (email == null || !email.contains("@")) {
            throw new DomainValidationException("Invalid customer email: " + email);
        }
        this.fullName = fullName.trim();
        this.email = email.trim().toLowerCase();
    }

    public void upgradeTier(CustomerTier newTier) {
        Objects.requireNonNull(newTier, "Tier cannot be null");
        if (newTier.ordinal() < this.tier.ordinal()) {
            throw new DomainValidationException("Cannot downgrade tier directly: " + this.tier + " -> " + newTier);
        }
        this.tier = newTier;
    }

    public String getFullName() { return fullName; }
    public String getEmail() { return email; }
    public CustomerTier getTier() { return tier; }
}
