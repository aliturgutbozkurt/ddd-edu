package com.turkninja.ddd.module08.domain.model;

import com.turkninja.ddd.shared.domain.ValueObject;
import java.util.UUID;

public record CustomerId(UUID value) implements ValueObject {}
