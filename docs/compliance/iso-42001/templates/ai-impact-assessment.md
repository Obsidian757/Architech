# AI Impact Assessment (AIIA) — Template

```
System ID:    [TBD - from ai-system-inventory.md]
Version:      [TBD]
Owner:        [TBD]
Approved by:  [TBD - AIMS Lead]
Effective:    [TBD]
Last review:  [TBD]
Next review:  [TBD - annual or on material change]
Coverage:     A.5.2 · A.5.3 · A.5.4 · A.5.5 · Clause 6.1.4 · 8.4
```

> **Usage.** Copy this file to `registers/aiia/<system-id>-<yyyymmdd>.md`
> and complete each section. The AIMS Lead approves before the system
> is deployed or materially changed.

## 1. Screen (lightweight)

A 1-page screen at concept stage. If all answers are "No", proceed
with the full assessment at requirements stage.

- [ ] Does the system make consequential decisions about individuals?
- [ ] Does the system process personal data?
- [ ] Could the system materially influence behavior, opinion, or
      access to opportunity?
- [ ] Is the system safety-critical (physical or financial harm
      possible)?
- [ ] Will outputs be presented as authoritative to end-users?

Screen result: **Low / Medium / High** (highest single answer wins).

## 2. System summary

- **Purpose:** TBD
- **Intended use:** TBD
- **Out-of-scope use:** TBD
- **Foreseeable misuse:** TBD
- **Users:** TBD
- **Affected non-users (third parties):** TBD

## 3. Data flows

```
[source] → [preparation] → [model] → [post-processing] → [output] → [user/system]
```

Document each leg: sensitivity, jurisdiction, retention, third-party
involvement.

## 4. Impact on individuals (A.5.4)

| Dimension | Identified impact | Likelihood | Severity | Mitigation |
| --- | --- | --- | --- | --- |
| Privacy | TBD | TBD | TBD | TBD |
| Autonomy | TBD | TBD | TBD | TBD |
| Dignity / non-discrimination | TBD | TBD | TBD | TBD |
| Safety | TBD | TBD | TBD | TBD |
| Economic | TBD | TBD | TBD | TBD |
| Right to remedy / contestability | TBD | TBD | TBD | TBD |

## 5. Impact on groups & society (A.5.5)

| Dimension | Identified impact | Mitigation |
| --- | --- | --- |
| Disparate impact on protected groups | TBD | TBD |
| Environmental (compute, energy) | TBD | TBD |
| Information ecosystem (mis/disinformation) | TBD | TBD |
| Labor / displacement | TBD | TBD |
| Concentration of power | TBD | TBD |

## 6. Personal data

- [ ] No personal data involved.
- [ ] Personal data involved — lawful basis: TBD. Link to DPIA: TBD.

## 7. Risk register linkage

List risk IDs from
[`../registers/risk-register.md`](../registers/risk-register.md) that
apply, plus any system-specific additions captured in
`registers/risk-system-<id>.md`.

## 8. Decision

- [ ] **Proceed** — residual risks acceptable; controls in place.
- [ ] **Proceed with conditions** — list conditions and target dates.
- [ ] **Do not proceed** — rationale.

## 9. Re-assessment triggers

- Annual review.
- Change in model provider, training data, or intended use.
- High/Critical incident.
- Material change in applicable law.

## 10. Approval

```
Approved by: [TBD]   Role: AIMS Lead
Date:        [TBD]
```
