#!/usr/bin/env python3
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def write_file(rel_path, content):
    full_path = BASE_DIR / rel_path
    full_path.parent.mkdir(parents=True, exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Generated: {rel_path}")

# ==============================================================================
# MODULE 05: Exercise & Solution (Order Limit Invariant)
# ==============================================================================
m5 = "modules/module-05-aggregates-and-invariants"
write_file(f"{m5}/src/test/java/com/turkninja/ddd/module05/exercise/OrderLimitExerciseTest.java", """package com.turkninja.ddd.module05.exercise;

import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.fail;

@DisplayName("Exercise 05: Maximum Order Total Invariant")
class OrderLimitExerciseTest {

    @Test
    @Disabled("Remove @Disabled when implementing Exercise 05")
    @DisplayName("Should prevent adding item exceeding maximum order total of $10,000")
    void testOrderLimitExceeded() {
        fail("TODO: Implement aggregate invariant preventing order total > $10,000");
    }
}
""")

write_file(f"{m5}/src/main/java/com/turkninja/ddd/module05/solution/OrderWithLimit.java", """package com.turkninja.ddd.module05.solution;

import com.turkninja.ddd.module05.domain.model.Order;
import com.turkninja.ddd.module05.domain.model.OrderId;
import com.turkninja.ddd.shared.domain.DomainValidationException;

import java.math.BigDecimal;

public class OrderWithLimit extends Order {

    private static final BigDecimal MAX_ORDER_TOTAL = new BigDecimal("10000.00");

    public OrderWithLimit(OrderId id) {
        super(id);
    }

    @Override
    public void addItem(String productId, int quantity, BigDecimal unitPrice) {
        BigDecimal itemTotal = unitPrice.multiply(BigDecimal.valueOf(quantity));
        BigDecimal projectedTotal = calculateTotal().add(itemTotal);
        if (projectedTotal.compareTo(MAX_ORDER_TOTAL) > 0) {
            throw new DomainValidationException("Order total cannot exceed maximum allowed limit: " + MAX_ORDER_TOTAL);
        }
        super.addItem(productId, quantity, unitPrice);
    }
}
""")

write_file(f"{m5}/src/test/java/com/turkninja/ddd/module05/solution/OrderWithLimitSolutionTest.java", """package com.turkninja.ddd.module05.solution;

import com.turkninja.ddd.module05.domain.model.OrderId;
import com.turkninja.ddd.shared.domain.DomainValidationException;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.math.BigDecimal;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

@DisplayName("Solution 05: Maximum Order Total Limit Verification")
class OrderWithLimitSolutionTest {

    @Test
    @DisplayName("Should allow adding items within $10,000 limit")
    void testWithinLimit() {
        OrderWithLimit order = new OrderWithLimit(OrderId.generate());
        order.addItem("LAPTOP-01", 3, new BigDecimal("2500.00")); // $7,500
        assertThat(order.calculateTotal()).isEqualTo(new BigDecimal("7500.00"));
    }

    @Test
    @DisplayName("Should reject adding item exceeding $10,000 limit")
    void testExceedingLimit() {
        OrderWithLimit order = new OrderWithLimit(OrderId.generate());
        order.addItem("SERVER-01", 1, new BigDecimal("8000.00"));

        assertThatThrownBy(() -> order.addItem("SERVER-02", 1, new BigDecimal("3000.00")))
                .isInstanceOf(DomainValidationException.class)
                .hasMessageContaining("Order total cannot exceed maximum allowed limit");
    }
}
""")

# ==============================================================================
# MODULE 06: Exercise & Solution (Event Dispatcher SPI)
# ==============================================================================
m6 = "modules/module-06-domain-events"
write_file(f"{m6}/src/test/java/com/turkninja/ddd/module06/exercise/EventDispatchExerciseTest.java", """package com.turkninja.ddd.module06.exercise;

import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.fail;

@DisplayName("Exercise 06: Domain Event Dispatching")
class EventDispatchExerciseTest {

    @Test
    @Disabled("Remove @Disabled when implementing Exercise 06")
    @DisplayName("Should dispatch collected events to registered subscribers")
    void testEventDispatching() {
        fail("TODO: Implement EventPublisher SPI and verify dispatching");
    }
}
""")

write_file(f"{m6}/src/main/java/com/turkninja/ddd/module06/solution/EventPublisherPort.java", """package com.turkninja.ddd.module06.solution;

import com.turkninja.ddd.shared.domain.DomainEvent;

public interface EventPublisherPort {
    void publish(DomainEvent event);
}
""")

write_file(f"{m6}/src/main/java/com/turkninja/ddd/module06/solution/SynchronousEventDispatcher.java", """package com.turkninja.ddd.module06.solution;

import com.turkninja.ddd.shared.domain.DomainEvent;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Consumer;

public class SynchronousEventDispatcher implements EventPublisherPort {

    private final List<Consumer<DomainEvent>> subscribers = new ArrayList<>();

    public void registerSubscriber(Consumer<DomainEvent> subscriber) {
        this.subscribers.add(subscriber);
    }

    @Override
    public void publish(DomainEvent event) {
        subscribers.forEach(s -> s.accept(event));
    }
}
""")

write_file(f"{m6}/src/test/java/com/turkninja/ddd/module06/solution/EventDispatcherSolutionTest.java", """package com.turkninja.ddd.module06.solution;

import com.turkninja.ddd.module06.domain.event.OrderEvent;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.time.Instant;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

import static org.assertj.core.api.Assertions.assertThat;

@DisplayName("Solution 06: Synchronous Event Dispatcher Verification")
class EventDispatcherSolutionTest {

    @Test
    @DisplayName("Dispatches domain events cleanly to registered handlers")
    void testEventDispatching() {
        SynchronousEventDispatcher dispatcher = new SynchronousEventDispatcher();
        List<String> auditLog = new ArrayList<>();

        dispatcher.registerSubscriber(event -> {
            if (event instanceof OrderEvent.OrderPaid paid) {
                auditLog.add("AUDIT: Payment logged for " + paid.orderId());
            }
        });

        UUID orderId = UUID.randomUUID();
        dispatcher.publish(new OrderEvent.OrderPaid(UUID.randomUUID(), orderId, "PAY-99", Instant.now()));

        assertThat(auditLog).hasSize(1);
        assertThat(auditLog.getFirst()).contains("AUDIT: Payment logged for " + orderId);
    }
}
""")

# ==============================================================================
# MODULE 07: Exercise & Solution (CQRS Lite Query Port)
# ==============================================================================
m7 = "modules/module-07-driving-ports-use-cases"
write_file(f"{m7}/src/test/java/com/turkninja/ddd/module07/exercise/AccountQueryExerciseTest.java", """package com.turkninja.ddd.module07.exercise;

import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.fail;

@DisplayName("Exercise 07: CQRS Query Port")
class AccountQueryExerciseTest {

    @Test
    @Disabled("Remove @Disabled when implementing Exercise 07")
    @DisplayName("Should query account summary without modifying state")
    void testAccountSummaryQuery() {
        fail("TODO: Implement GetAccountSummaryQuery port and application handler");
    }
}
""")

write_file(f"{m7}/src/main/java/com/turkninja/ddd/module07/solution/GetAccountSummaryQuery.java", """package com.turkninja.ddd.module07.solution;

import java.util.Optional;
import java.util.UUID;

public interface GetAccountSummaryQuery {
    Optional<AccountSummaryResponse> getSummary(UUID accountId);

    record AccountSummaryResponse(UUID accountId, String ownerName, double balance, String status) {}
}
""")

write_file(f"{m7}/src/main/java/com/turkninja/ddd/module07/solution/AccountQueryService.java", """package com.turkninja.ddd.module07.solution;

import com.turkninja.ddd.module07.application.port.out.AccountRepositoryPort;

import java.util.Objects;
import java.util.Optional;
import java.util.UUID;

public class AccountQueryService implements GetAccountSummaryQuery {

    private final AccountRepositoryPort repositoryPort;

    public AccountQueryService(AccountRepositoryPort repositoryPort) {
        this.repositoryPort = Objects.requireNonNull(repositoryPort);
    }

    @Override
    public Optional<AccountSummaryResponse> getSummary(UUID accountId) {
        return repositoryPort.findById(accountId)
                .map(r -> new AccountSummaryResponse(r.id(), r.ownerName(), r.balance(), "ACTIVE"));
    }
}
""")

write_file(f"{m7}/src/test/java/com/turkninja/ddd/module07/solution/AccountQuerySolutionTest.java", """package com.turkninja.ddd.module07.solution;

import com.turkninja.ddd.module07.application.port.out.AccountRepositoryPort;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.util.Optional;
import java.util.UUID;

import static org.assertj.core.api.Assertions.assertThat;

@DisplayName("Solution 07: CQRS Query Port Verification")
class AccountQuerySolutionTest {

    @Test
    @DisplayName("Successfully queries account summary DTO without domain exposure")
    void testQueryService() {
        UUID id = UUID.randomUUID();
        AccountRepositoryPort stubRepo = new AccountRepositoryPort() {
            @Override public void save(AccountRecord account) {}
            @Override public Optional<AccountRecord> findById(UUID queryId) {
                return Optional.of(new AccountRecord(id, "Ada Lovelace", 1250.00));
            }
        };

        AccountQueryService queryService = new AccountQueryService(stubRepo);
        Optional<GetAccountSummaryQuery.AccountSummaryResponse> summary = queryService.getSummary(id);

        assertThat(summary).isPresent();
        assertThat(summary.get().ownerName()).isEqualTo("Ada Lovelace");
        assertThat(summary.get().balance()).isEqualTo(1250.00);
    }
}
""")

# ==============================================================================
# MODULE 08: Exercise & Solution (Entity-Domain Bidirectional Mapper)
# ==============================================================================
m8 = "modules/module-08-driven-ports-persistence"
write_file(f"{m8}/src/test/java/com/turkninja/ddd/module08/exercise/CustomerMapperExerciseTest.java", """package com.turkninja.ddd.module08.exercise;

import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.fail;

@DisplayName("Exercise 08: Bidirectional Domain-Entity Mapper")
class CustomerMapperExerciseTest {

    @Test
    @Disabled("Remove @Disabled when implementing Exercise 08")
    @DisplayName("Should map domain customer to database record and back")
    void testCustomerBidirectionalMapping() {
        fail("TODO: Implement CustomerMapper with zero domain leakage");
    }
}
""")

write_file(f"{m8}/src/main/java/com/turkninja/ddd/module08/solution/CustomerJpaEntity.java", """package com.turkninja.ddd.module08.solution;

import java.util.UUID;

public class CustomerJpaEntity {
    private UUID id;
    private String name;
    private String email;

    public CustomerJpaEntity() {}

    public CustomerJpaEntity(UUID id, String name, String email) {
        this.id = id;
        this.name = name;
        this.email = email;
    }

    public UUID getId() { return id; }
    public void setId(UUID id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
}
""")

write_file(f"{m8}/src/main/java/com/turkninja/ddd/module08/solution/CustomerMapper.java", """package com.turkninja.ddd.module08.solution;

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
""")

write_file(f"{m8}/src/test/java/com/turkninja/ddd/module08/solution/CustomerMapperSolutionTest.java", """package com.turkninja.ddd.module08.solution;

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
""")

# ==============================================================================
# MODULE 12 & CAPSTONE: Saga & Outbox Orchestration
# ==============================================================================
cap = "capstone-order-fulfillment-platform"
write_file(f"{cap}/src/main/java/com/turkninja/ddd/capstone/saga/OrderFulfillmentSagaOrchestrator.java", """package com.turkninja.ddd.capstone.saga;

import com.turkninja.ddd.capstone.fulfillment.domain.model.Shipment;
import com.turkninja.ddd.capstone.fulfillment.domain.model.ShipmentId;
import com.turkninja.ddd.capstone.ordering.domain.model.Order;
import com.turkninja.ddd.capstone.ordering.domain.model.OrderId;

import java.math.BigDecimal;
import java.util.Objects;
import java.util.UUID;

public class OrderFulfillmentSagaOrchestrator {

    public record ProcessOrderResult(Order order, Shipment shipment) {}

    public ProcessOrderResult processOrderConfirmation(OrderId orderId, BigDecimal amount, String trackingNumber) {
        Objects.requireNonNull(orderId, "OrderId required");

        // 1. Ordering Context: Create and Confirm Order
        Order order = new Order(orderId, amount);
        order.confirm();

        // 2. Anti-Corruption Layer: Translate OrderConfirmed to Shipment
        Shipment shipment = new Shipment(ShipmentId.generate(), order.getId().value());
        shipment.dispatch(trackingNumber);

        return new ProcessOrderResult(order, shipment);
    }
}
""")

write_file(f"{cap}/src/test/java/com/turkninja/ddd/capstone/saga/OrderFulfillmentSagaTest.java", """package com.turkninja.ddd.capstone.saga;

import com.turkninja.ddd.capstone.fulfillment.domain.model.Shipment;
import com.turkninja.ddd.capstone.ordering.domain.model.Order;
import com.turkninja.ddd.capstone.ordering.domain.model.OrderId;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.math.BigDecimal;

import static org.assertj.core.api.Assertions.assertThat;

@DisplayName("Capstone: End-to-End Order-to-Fulfillment Saga Verification")
class OrderFulfillmentSagaTest {

    @Test
    @DisplayName("Saga coordinates order confirmation and shipment dispatch cleanly across contexts")
    void testEndToEndSaga() {
        OrderFulfillmentSagaOrchestrator saga = new OrderFulfillmentSagaOrchestrator();
        OrderId orderId = OrderId.generate();

        OrderFulfillmentSagaOrchestrator.ProcessOrderResult result =
                saga.processOrderConfirmation(orderId, new BigDecimal("250.00"), "FEDEX-889900");

        assertThat(result.order().getStatus()).isEqualTo(Order.Status.CONFIRMED);
        assertThat(result.shipment().getStatus()).isEqualTo(Shipment.ShipmentStatus.DISPATCHED);
        assertThat(result.shipment().getTrackingCode()).isEqualTo("FEDEX-889900");
        assertThat(result.shipment().getOrderId()).isEqualTo(orderId.value());
    }
}
""")

print("Exercises and solutions part 2 written successfully!")
