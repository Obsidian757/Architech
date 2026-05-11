# Internal Audit Procedure

```
Owner:        [TBD - AIMS Lead]
Approved by:  [TBD - Managing Member]
Effective:    [TBD]
Last review:  [TBD]
Next review:  [TBD - annual]
Coverage:     Clause 9.1 · 9.2 · 10.1 · 10.2 · A.8.4
```

## 1. Purpose

Verify the AIMS conforms to ISO/IEC 42001:2023 and to the LLC's own
documented requirements, and that it is effectively implemented.

## 2. Programme

- **Frequency.** At least **annually**; partial audits more frequently
  for areas with recent incidents or material changes.
- **Coverage.** Across one or more cycles, every clause (4–10) and
  every applicable Annex A control must be audited.
- **Independence.** Auditor must not audit their own work. For a small
  LLC, the AIMS Lead may audit operational areas they did not
  implement; the Managing Member may audit AIMS Lead work; or an
  external advisor may be engaged.

## 3. Audit plan template

| Field | Value |
| --- | --- |
| Audit ID | IA-YYYY-NN |
| Scope | TBD (clauses/controls/systems in scope) |
| Auditor | TBD |
| Auditees | TBD |
| Dates | TBD |
| Criteria | ISO/IEC 42001:2023 + this AIMS pack |
| Methods | Document review, interview, observation, sampling |

## 4. Conduct

1. **Opening meeting.** Confirm scope, criteria, schedule.
2. **Evidence gathering.** Collect objective evidence; record sampling.
3. **Findings.** Classify as: Conformity / Observation / Minor NC /
   Major NC.
4. **Closing meeting.** Communicate findings to auditees.
5. **Report.** Issue within 5 business days of closing.

## 5. Nonconformity (NC) handling (clause 10.1)

Maintained in `registers/nc-log.md` (created on first NC). Fields:

| Field | Notes |
| --- | --- |
| NC ID | NC-YYYY-NN |
| Source | Audit ID / incident / customer complaint |
| Clause/control | Reference |
| Description | What was observed |
| Severity | Minor / Major |
| Root cause | TBD |
| Correction | Immediate fix |
| Corrective action | Action to prevent recurrence |
| Owner | TBD |
| Target date | TBD |
| Verified closed | Date + verifier |

## 6. Incidents (A.8.4)

An **incident** is any unintended event resulting in (a) an in-scope
system behaving outside its intended use, (b) harm or near-miss to a
user or third party, (c) a confidentiality / integrity / availability
event, or (d) a supplier breach affecting the LLC.

| Severity | Definition | Response SLA | Notification |
| --- | --- | --- | --- |
| Low | No user impact; near-miss | 30 days | Internal log |
| Medium | Minor user impact, mitigated quickly | 7 days | Affected users |
| High | Material user impact OR data exposure | 24 h triage, 72 h disclosure | Affected users + Managing Member; regulators if required |
| Critical | Safety, large-scale harm, public exposure | Immediate | Managing Member; affected users; regulators; legal counsel |

Incidents are logged in `registers/incident-log.md` (created on first
incident) and feed the risk register and management review.

## 7. Continual improvement (clause 10.2)

- Trend analysis on the NC log and incident log at every management
  review.
- Closed NCs are retained as evidence for at least 3 years.

## 8. Records

Audit plans, audit reports, NC log, incident log are retained for at
least 3 years, indexed by ID.
