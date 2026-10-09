# Exercise 12: Building an Anti-Corruption Layer Translator

## Objective
Implement an Anti-Corruption Layer (ACL) translator that accepts an archaic external legacy ERP message (`LegacyErpOrderPayload`) and maps it into our clean domain order representation (`CleanOrder`).

## Requirements
1. Validate external payload:
   - If `order_ref_num` or `client_nm` is blank, throw `DomainValidationException`.
   - If `status_code` equals `"VOID"`, reject the message.
   - Parse `gross_amt` string into a valid `BigDecimal`.
2. Map to immutable `CleanOrder` without leaking any legacy field names (`gross_amt`, `tx_curr`, `client_nm`) into the domain.

## Running Tests
Run: `src/test/java/com/turkninja/ddd/module12/exercise/AclTranslatorExerciseTest.java`
Remove `@Disabled` and verify your solution.
