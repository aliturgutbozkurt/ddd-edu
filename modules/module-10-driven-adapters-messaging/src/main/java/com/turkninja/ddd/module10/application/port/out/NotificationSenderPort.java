package com.turkninja.ddd.module10.application.port.out;

public interface NotificationSenderPort {
    boolean sendNotification(NotificationMessage message);

    record NotificationMessage(String recipient, String title, String body) {}
}
