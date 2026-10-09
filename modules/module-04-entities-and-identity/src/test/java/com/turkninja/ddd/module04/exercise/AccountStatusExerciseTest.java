package com.turkninja.ddd.module04.exercise;

import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.fail;

@DisplayName("Exercise 04: Entity Lifecycle & State Machine")
class AccountStatusExerciseTest {

    @Test
    @Disabled("Remove @Disabled when you begin implementing Exercise 04")
    @DisplayName("Should prevent modifying closed account")
    void testClosedAccountProtection() {
        fail("TODO: Implement state transition invariants for account lifecycle");
    }
}
