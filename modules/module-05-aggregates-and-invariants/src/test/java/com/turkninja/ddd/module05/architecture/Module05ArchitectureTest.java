package com.turkninja.ddd.module05.architecture;

import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.core.importer.ImportOption;
import com.turkninja.ddd.shared.architecture.HexagonalArchitectureRules;
import org.junit.jupiter.api.Test;

class Module05ArchitectureTest {
    @Test
    void testHexagonalIsolation() {
        JavaClasses classes = new ClassFileImporter()
                .withImportOption(ImportOption.Predefined.DO_NOT_INCLUDE_TESTS)
                .importPackages("com.turkninja.ddd.module05");
        HexagonalArchitectureRules.verifyHexagonalArchitecture(classes);
    }
}
