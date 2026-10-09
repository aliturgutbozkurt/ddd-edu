package com.turkninja.ddd.module11.solution;

import com.tngtech.archunit.lang.ArchRule;

import static com.tngtech.archunit.lang.syntax.ArchRuleDefinition.classes;
import static com.tngtech.archunit.lang.syntax.ArchRuleDefinition.noClasses;

/**
 * Standardized ArchUnit rules for Hexagonal Architecture projects.
 */
public final class CustomHexagonalRules {

    private CustomHexagonalRules() {}

    public static final ArchRule USE_CASES_MUST_BE_INTERFACES =
            classes().that().haveSimpleNameEndingWith("UseCase")
                    .should().beInterfaces()
                    .allowEmptyShould(true)
                    .as("Inbound Driving Ports representing Use Cases must be Java interfaces.");

    public static final ArchRule PORTS_MUST_BE_INTERFACES =
            classes().that().haveSimpleNameEndingWith("Port")
                    .should().beInterfaces()
                    .allowEmptyShould(true)
                    .as("Outbound Ports representing SPIs must be Java interfaces.");

    public static final ArchRule DOMAIN_NO_SPRING_DEPENDENCY =
            noClasses().that().resideInAPackage("..domain..")
                    .should().dependOnClassesThat().resideInAPackage("org.springframework..")
                    .allowEmptyShould(true)
                    .as("Domain layer must have zero dependencies on org.springframework.*");
}
