package com.turkninja.ddd.module07.application.port.in;

import java.util.UUID;

public interface CreateAccountUseCase {
    UUID createAccount(CreateAccountCommand command);

    record CreateAccountCommand(String ownerName, double initialDeposit) {}
}
