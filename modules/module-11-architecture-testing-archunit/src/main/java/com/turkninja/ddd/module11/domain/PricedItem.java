package com.turkninja.ddd.module11.domain;

import com.turkninja.ddd.shared.domain.ValueObject;
import java.math.BigDecimal;

public record PricedItem(String sku, BigDecimal price) implements ValueObject {}
