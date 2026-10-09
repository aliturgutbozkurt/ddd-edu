---
marp: true
theme: default
paginate: true
header: "DDD & Hexagonal Architecture Masterclass | Module 01"
footer: "© 2026 Ali Turgut Bozkurt · TurkNinja"
---

# Module 01: Domain-Driven Design Foundations & Ubiquitous Language

## Strategic Design & The Death of the Anemic Domain Model

---

## 1. What is Domain-Driven Design (DDD)?

Domain-Driven Design, pioneered by Eric Evans in 2003, is an approach to software development that centers the design around a deeply understood business domain.

### The Two Pillars of DDD:
1. **Strategic Design**:
   - Defining what to build and what NOT to build.
   - Establishing clear system boundaries (**Bounded Contexts**).
   - Categorizing subdomains based on competitive differentiation.
2. **Tactical Design**:
   - Software design patterns that preserve domain invariants inside a Bounded Context.
   - Aggregates, Entities, Value Objects, Domain Events, Repositories, and Domain Services.

---

## 2. Subdomain Categorization

Every enterprise system is composed of multiple subdomains:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        ENTERPRISE ECOSYSTEM                            │
│                                                                        │
│  ┌─────────────────────────┐  ┌─────────────────────────────────────┐  │
│  │      CORE DOMAIN        │  │        SUPPORTING SUBDOMAIN         │  │
│  │  Custom algorithmic    │  │  Customer onboarding & KYC review   │  │
│  │  high-yield investment  │  │  (Custom-built, supporting role)    │  │
│  │  (High ROI / Bespoke)   │  │                                     │  │
│  └─────────────────────────┘  └─────────────────────────────────────┘  │
│                                                                        │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │                      GENERIC SUBDOMAIN                           │  │
│  │  Authentication, Email Delivery, PDF Export (Off-the-shelf SaaS) │  │
│  └──────────────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────────────┘
```

> **Rule of Thumb**: Spend 80% of your architectural creativity and engineering talent on the **Core Domain**. Do not over-engineer Generic Subdomains.

---

## 3. The Ubiquitous Language

A ubiquitous language is a rigorous, shared language agreed upon by **software engineers** and **domain experts** (business analysts, traders, product managers), used consistently in speech, documentation, and code.

### Anti-Pattern: Translation Layer
- *Analyst says*: "Debit the account with overdraft tolerance."
- *Developer codes*: `accountTable.setBalance(accountTable.getBalance() - amt);`
- *Bug report*: "Why did the user get negative balance when tolerance was exceeded?"

### Clean DDD Approach:
```java
// Ubiquitous Language directly encoded in code
public void withdraw(Money amount) {
    if (amount.isGreaterThan(availableFunds())) {
        throw new InsufficientFundsException(accountNumber, amount, availableFunds());
    }
    this.balance = this.balance.subtract(amount);
    recordEvent(new AccountDebitedEvent(accountNumber, amount, Instant.now()));
}
```

---

## 4. Anemic vs. Rich Domain Models

### The Anemic Model Anti-Pattern (Martin Fowler):
An entity that is nothing more than a bag of getters and setters. All business logic leaks into monolithic procedural "Service" classes.

```java
// ANEMIC: Completely exposed state, zero business invariants
public class AnemicAccount {
    private String id;
    private BigDecimal balance;
    
    public BigDecimal getBalance() { return balance; }
    public void setBalance(BigDecimal balance) { this.balance = balance; }
}
```
**Why this fails**:
- Anyone can call `setBalance(new BigDecimal("-1000000"))`.
- Invariants are duplicated across multiple controller/service callers.
- Concurrency bugs thrive because data is separated from behavior.

---

## 5. The Rich Domain Model in Java 27

In a rich domain model, state and behavior are encapsulated together. An entity cannot be constructed or mutated into an invalid state.

```java
public class BankAccount extends AggregateRoot<AccountNumber> {

    private Money balance;
    private final OverdraftLimit overdraftLimit;

    public BankAccount(AccountNumber id, OverdraftLimit overdraftLimit) {
        super(id);
        this.balance = Money.zero(overdraftLimit.currency());
        this.overdraftLimit = Objects.requireNonNull(overdraftLimit);
    }

    public void deposit(Money amount) {
        if (!amount.isPositive()) {
            throw new DomainValidationException("Deposit amount must be positive");
        }
        this.balance = this.balance.add(amount);
        recordEvent(new AccountDepositedEvent(id, amount, Instant.now()));
    }

    public void withdraw(Money amount) {
        Money totalAvailable = this.balance.add(overdraftLimit.amount());
        if (amount.isGreaterThan(totalAvailable)) {
            throw new InsufficientFundsException(id, amount, totalAvailable);
        }
        this.balance = this.balance.subtract(amount);
        recordEvent(new AccountWithdrawnEvent(id, amount, Instant.now()));
    }
}
```

---

## 6. Key Takeaways

1. **Strategic Before Tactical**: Never write code without agreeing on the Bounded Context and Ubiquitous Language.
2. **Eliminate Public Setters**: Use meaningful domain methods (`deposit()`, `withdraw()`, `freeze()`) instead of generic mutators.
3. **Keep the Core Pure**: The domain must never depend on Spring, Hibernate, or Jackson.
