package com.turkninja.ddd.module10.infrastructure.adapter.output.messaging;

import com.turkninja.ddd.module10.application.port.out.NotificationSenderPort;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class SimulatedMessagePublisherAdapter implements NotificationSenderPort {

    private final List<NotificationMessage> publishedMessages = new ArrayList<>();

    @Override
    public boolean sendNotification(NotificationMessage message) {
        publishedMessages.add(message);
        return true;
    }

    public List<NotificationMessage> getPublishedMessages() {
        return Collections.unmodifiableList(publishedMessages);
    }
}
