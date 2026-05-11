# Change Record — Template

```
Change ID:    CR-[YYYYMMDD]-[seq]
System(s):    [TBD - system IDs from inventory]
Raised by:    [TBD]
Approved by:  [TBD - AIMS Lead]
Effective:    [TBD]
Coverage:     Clause 6.3 · 8.1 · A.6.2.5
```

> **Usage.** Copy to `registers/changes/CR-<id>.md` for every material
> change to an in-scope AI system or to the AIMS itself. Material
> changes include changes to intended use, model provider, training /
> fine-tune corpora, data flows, monitoring, or risk classification.

## 1. Description

- **What is changing:** TBD
- **Why:** TBD
- **Components affected:** TBD
- **Scope:** AIMS / System / Both. TBD

## 2. Risk assessment of the change

- Does this change a system's AIIA inputs? **Y / N**
  - If Y, run a fresh AIIA or update the existing one.
- Does this introduce a new supplier? **Y / N**
  - If Y, update `registers/ai-system-inventory.md` § Suppliers.
- Does this affect personal data handling? **Y / N**
  - If Y, update DPIA.

## 3. Test & validation plan

- **Verification:** TBD
- **Validation:** TBD
- **Rollback plan:** TBD

## 4. Approvals

| Role | Name | Decision | Date |
| --- | --- | --- | --- |
| AIMS Lead | TBD | Approve / Reject | TBD |
| Managing Member (if material) | TBD | Approve / Reject | TBD |

## 5. Implementation

- **Implemented on:** TBD
- **Verified on:** TBD
- **Documentation updated:** SoA / inventory / system card / risk
  register / AIIA — tick all that apply.

## 6. Post-implementation review

- **Observed effects:** TBD
- **Nonconformities raised:** link to NC IDs in
  [`../operations/internal-audit-procedure.md`](../operations/internal-audit-procedure.md)
  § "Nonconformity log".
- **Lessons learned:** TBD
