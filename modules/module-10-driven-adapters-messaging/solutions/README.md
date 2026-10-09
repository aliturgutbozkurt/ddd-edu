# Solution 10: Resilient External Service Driven Adapter

## Architectural Insight
External HTTP APIs and messaging queues are volatile. Placing retry logic and circuit breakers inside the **Driven Adapter** keeps the domain core completely immune to external outages, HTTP client configurations, and transport issues.

## Key Files
- `PaymentGatewayPort.java`: Clean outbound driving interface (SPI).
- `ResilientPaymentGatewayAdapter.java`: Fault-tolerant adapter with retry loops and graceful failure results.
- `ResilientPaymentGatewaySolutionTest.java`: Unit tests asserting retry semantics and recovery.
