# Module 08: Outbound (Driven) Ports & Persistence Adapters

## 🎯 Learning Objectives
- Design **Outbound Ports (Repository SPI)** with complete database agnosticism.
- Separate database persistence models (`OrderJpaEntity`) from rich Domain models (`Order`).
- Implement bidirectional mapping cleanly without reflection or ORM contamination.
- Prevent lazy-loading leaks and database transaction coupling in the domain core.
