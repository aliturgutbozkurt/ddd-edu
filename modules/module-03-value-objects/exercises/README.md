# Exercise 03: Implementing TaxNumber and PostalCode Value Objects

## 🎯 Business Context
Corporate tax identification numbers and postal codes must be strictly formatted to prevent invoicing errors.

## 📋 Acceptance Criteria
1. `TaxNumber`: Must contain exactly 10 numeric digits.
2. `TaxNumber`: Cannot be all zeros (e.g. `0000000000`).
3. `PostalCode`: Must be trimmed and non-empty.
4. Compact constructor must validate invariants and throw `DomainValidationException`.
