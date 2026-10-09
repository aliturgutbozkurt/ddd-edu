package com.turkninja.ddd.module11.solution;

import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.core.importer.ImportOption;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

@DisplayName("Solution 11: ArchUnit Custom Rule Verification")
class CustomHexagonalRulesSolutionTest {

    private final JavaClasses classes = new ClassFileImporter()
            .withImportOption(ImportOption.Predefined.DO_NOT_INCLUDE_TESTS)
            .importPackages("com.turkninja.ddd");

    @Test
    @DisplayName("Verify UseCase interface conventions")
    void testUseCasesAreInterfaces() {
        CustomHexagonalRules.USE_CASES_MUST_BE_INTERFACES.check(classes);
    }

    @Test
    @DisplayName("Verify Port interface conventions")
    void testPortsAreInterfaces() {
        CustomHexagonalRules.PORTS_MUST_BE_INTERFACES.check(classes);
    }

    @Test
    @DisplayName("Verify zero spring dependencies in domain packages")
    void testDomainHasNoSpring() {
        CustomHexagonalRules.DOMAIN_NO_SPRING_DEPENDENCY.check(classes);
    }
}
