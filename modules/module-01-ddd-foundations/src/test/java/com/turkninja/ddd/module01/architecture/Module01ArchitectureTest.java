package com.turkninja.ddd.module01.architecture;

import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.core.importer.ImportOption;
import com.turkninja.ddd.shared.architecture.HexagonalArchitectureRules;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

@DisplayName("Module 01: Hexagonal Layer Purity Verification")
class Module01ArchitectureTest {

    @Test
    @DisplayName("Domain layer must be 100% pure Java without framework dependencies")
    void shouldEnforceDomainPurity() {
        JavaClasses importedClasses = new ClassFileImporter()
                .withImportOption(ImportOption.Predefined.DO_NOT_INCLUDE_TESTS)
                .importPackages("com.turkninja.ddd.module01");

        HexagonalArchitectureRules.verifyHexagonalArchitecture(importedClasses);
    }
}
