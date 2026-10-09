package com.turkninja.ddd.capstone.architecture;

import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.core.importer.ImportOption;
import com.turkninja.ddd.shared.architecture.HexagonalArchitectureRules;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static com.tngtech.archunit.lang.syntax.ArchRuleDefinition.noClasses;

@DisplayName("Capstone: Multi-Bounded Context Architectural Boundary Tests")
class CapstoneArchitectureTest {

    @Test
    @DisplayName("Ordering context must not depend on Fulfillment internal domain classes")
    void verifyBoundedContextIsolation() {
        JavaClasses classes = new ClassFileImporter()
                .withImportOption(ImportOption.Predefined.DO_NOT_INCLUDE_TESTS)
                .importPackages("com.turkninja.ddd.capstone");

        HexagonalArchitectureRules.verifyHexagonalArchitecture(classes);

        noClasses().that().resideInAPackage("..ordering..")
                .should().dependOnClassesThat().resideInAPackage("..fulfillment..")
                .allowEmptyShould(true)
                .as("Ordering Context must remain completely decoupled from Fulfillment Context.")
                .check(classes);
    }
}
