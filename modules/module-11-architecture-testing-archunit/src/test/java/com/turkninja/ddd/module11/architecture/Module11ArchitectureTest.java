package com.turkninja.ddd.module11.architecture;

import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.core.importer.ImportOption;
import com.turkninja.ddd.shared.architecture.HexagonalArchitectureRules;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static com.tngtech.archunit.lang.syntax.ArchRuleDefinition.classes;

@DisplayName("Module 11: Comprehensive ArchUnit Governance Tests")
class Module11ArchitectureTest {

    @Test
    @DisplayName("Should enforce that domain layer remains pure Java")
    void testDomainPurity() {
        JavaClasses classes = new ClassFileImporter()
                .withImportOption(ImportOption.Predefined.DO_NOT_INCLUDE_TESTS)
                .importPackages("com.turkninja.ddd.module11");

        HexagonalArchitectureRules.verifyHexagonalArchitecture(classes);
    }

    @Test
    @DisplayName("Value objects must implement ValueObject marker interface")
    void testValueObjectConventions() {
        JavaClasses classes = new ClassFileImporter()
                .withImportOption(ImportOption.Predefined.DO_NOT_INCLUDE_TESTS)
                .importPackages("com.turkninja.ddd.module11.domain");

        classes().that().haveSimpleNameEndingWith("Item")
                .should().implement(com.turkninja.ddd.shared.domain.ValueObject.class)
                .allowEmptyShould(true)
                .check(classes);
    }
}
