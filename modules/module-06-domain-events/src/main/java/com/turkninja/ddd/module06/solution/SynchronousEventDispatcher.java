package com.turkninja.ddd.module06.solution;

import com.turkninja.ddd.shared.domain.DomainEvent;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Consumer;

public class SynchronousEventDispatcher implements EventPublisherPort {

    private final List<Consumer<DomainEvent>> subscribers = new ArrayList<>();

    public void registerSubscriber(Consumer<DomainEvent> subscriber) {
        this.subscribers.add(subscriber);
    }

    @Override
    public void publish(DomainEvent event) {
        subscribers.forEach(s -> s.accept(event));
    }
}
