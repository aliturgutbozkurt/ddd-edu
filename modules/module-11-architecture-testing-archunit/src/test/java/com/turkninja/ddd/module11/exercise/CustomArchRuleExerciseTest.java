package com.turkninja.ddd.module11.exercise;

import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.turkninja.ddd.module11.solution.CustomHexagonalRules;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

@DisplayName("Exercise 11: ArchUnit Architectural Rules")
class CustomArchRuleExerciseTest {

    @Test
    @Disabled("TODO for student: Implement and assert custom ArchUnit rules")
    @DisplayName("Should verify that all UseCase suffixed types are interfaces")
    void shouldEnforceUseCaseNaming() {
        JavaClasses classes = new ClassFileImporter().importPackages("com.turkninja.ddd");
        CustomHexagonalRules.USE_CASES_MUST_BE_INTERFACES.check(classes);
    }
}
