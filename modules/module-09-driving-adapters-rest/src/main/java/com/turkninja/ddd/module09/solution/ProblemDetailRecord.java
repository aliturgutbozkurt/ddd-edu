package com.turkninja.ddd.module09.solution;

import java.net.URI;
import java.time.Instant;
import java.util.Map;

/**
 * Immutable RFC 9457 Problem Details representation.
 */
public record ProblemDetailRecord(
        URI type,
        String title,
        int status,
        String detail,
        URI instance,
        Instant timestamp,
        Map<String, Object> properties
) {
    public static ProblemDetailRecord of(URI type, String title, int status, String detail, URI instance) {
        return new ProblemDetailRecord(type, title, status, detail, instance, Instant.now(), Map.of());
    }

    public static ProblemDetailRecord of(URI type, String title, int status, String detail, URI instance, Map<String, Object> properties) {
        return new ProblemDetailRecord(type, title, status, detail, instance, Instant.now(), Map.copyOf(properties));
    }
}
