package com.turkninja.ddd.module12.solution;

/**
 * Archaic legacy DTO received from external upstream ERP system.
 */
public record LegacyErpOrderPayload(
        String order_ref_num,
        String client_nm,
        String gross_amt,
        String tx_curr,
        String status_code
) {}
