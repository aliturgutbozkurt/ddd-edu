package com.turkninja.ddd.module06.solution;

import com.turkninja.ddd.shared.domain.DomainEvent;

public interface EventPublisherPort {
    void publish(DomainEvent event);
}
