# 🎓 Capstone Project: Enterprise Order & Fulfillment Platform

## 🎯 Architecture Overview
This graduation project demonstrates a complete, production-grade enterprise system featuring:
- **Two Distinct Bounded Contexts**: Ordering Context & Fulfillment Context.
- **Hexagonal Architecture**: Complete layer isolation with Driving & Driven ports.
- **Transactional Outbox Pattern**: Zero event loss between database commits and event streaming.
- **Anti-Corruption Layer (ACL)**: Clean boundary protection between bounded contexts.
- **Automated ArchUnit Test Suite**: Verification that bounded contexts do not bleed into each other.
