package com.turkninja.ddd.module05.exercise;

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
