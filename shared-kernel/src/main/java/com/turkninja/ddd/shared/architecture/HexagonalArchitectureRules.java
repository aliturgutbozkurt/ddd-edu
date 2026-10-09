package com.turkninja.ddd.shared.architecture;

import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.lang.ArchRule;

import static com.tngtech.archunit.lang.syntax.ArchRuleDefinition.noClasses;

/**
 * Reusable ArchUnit architectural fitness functions for Hexagonal Architecture.
 * Guarantees layer isolation and compiles into every module's test suite.
 */
public final class HexagonalArchitectureRules {

    private HexagonalArchitectureRules() {
    }

    /**
     * Enforces that the pure Domain layer NEVER depends on outer layers
     * (Application, Infrastructure) or any framework dependencies (Spring, Jakarta JPA, Jackson).
     */
    public static final ArchRule DOMAIN_MUST_NOT_DEPEND_ON_OUTER_LAYERS =
            noClasses().that().resideInAPackage("..domain..")
                    .should().dependOnClassesThat().resideInAnyPackage(
                            "..application..",
                            "..infrastructure..",
                            "org.springframework..",
                            "jakarta.persistence..",
                            "com.fasterxml.jackson.."
                    )
                    .allowEmptyShould(true)
                    .as("Domain model must remain 100% pure Java without framework or outer-layer dependencies.");

    /**
     * Enforces that Application services/use cases do not depend directly on Infrastructure adapters.
     */
    public static final ArchRule APPLICATION_MUST_NOT_DEPEND_ON_INFRASTRUCTURE =
            noClasses().that().resideInAPackage("..application..")
                    .should().dependOnClassesThat().resideInAnyPackage("..infrastructure..")
                    .allowEmptyShould(true)
                    .as("Application layer must only communicate with outside world via Ports, not concrete Infrastructure.");

    /**
     * Verifies all rules against the provided class definitions.
     */
    public static void verifyHexagonalArchitecture(JavaClasses classes) {
        DOMAIN_MUST_NOT_DEPEND_ON_OUTER_LAYERS.check(classes);
        APPLICATION_MUST_NOT_DEPEND_ON_INFRASTRUCTURE.check(classes);
    }
}
