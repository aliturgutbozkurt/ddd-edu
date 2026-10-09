package com.turkninja.ddd.module02.architecture;

import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.core.importer.ImportOption;
import com.turkninja.ddd.shared.architecture.HexagonalArchitectureRules;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

@DisplayName("Module 02: ArchUnit Hexagonal Rule Verification")
class Module02ArchitectureTest {

    @Test
    @DisplayName("Module 02 must strictly obey Hexagonal layer dependencies")
    void verifyHexagonalRules() {
        JavaClasses classes = new ClassFileImporter()
                .withImportOption(ImportOption.Predefined.DO_NOT_INCLUDE_TESTS)
                .importPackages("com.turkninja.ddd.module02");

        HexagonalArchitectureRules.verifyHexagonalArchitecture(classes);
    }
}
