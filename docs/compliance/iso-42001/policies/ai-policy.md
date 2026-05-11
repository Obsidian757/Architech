# AI Policy — 12th House AI, LLC

```
Owner:        [TBD - Managing Member]
Approved by:  [TBD - Managing Member]
Effective:    [TBD]
Last review:  [TBD]
Next review:  [TBD - annual]
Coverage:     Clause 5.2 · A.2.2 · A.2.3 · A.2.4 · A.3.3 · A.8.3 · A.8.4 · A.9.3
```

## 1. Purpose

This policy establishes the AI principles, commitments, and governance
framework of **12th House AI, LLC** ("the LLC"). It is the top-level
document of the AI Management System (AIMS) maintained under ISO/IEC
42001:2023.

## 2. Scope

Applies to:

- All AI systems the LLC develops, operates, hosts, or resells.
- All employees, contractors, advisors, and contributors of the LLC.
- The Architech repository as an in-scope LLC asset.

Excludes: foundation models operated by third-party providers (governed
under [`third-party-policy.md`](third-party-policy.md)).

## 3. Principles

The LLC commits to the following AI principles:

1. **Human oversight** — every in-scope system has a named human owner with
   the authority to disable or override it.
2. **Fairness** — known bias risks are documented in each system's AIIA and
   actively mitigated.
3. **Transparency** — every in-scope system has a public-or-internal
   system card describing purpose, limits, and known risks.
4. **Accountability** — incidents are logged, reviewed, and disclosed per
   §8 below.
5. **Security and privacy** — AI systems protect data per applicable laws
   and the LLC's data management policy.
6. **Reliability and safety** — systems are tested before deployment and
   monitored in operation, proportionate to impact.
7. **Lawfulness** — the LLC complies with applicable AI law (EU AI Act,
   relevant US state laws, sectoral regulation).

## 4. Objectives

The LLC sets the following measurable AI objectives (clause 6.2). Targets
`TBD`:

| # | Objective | Metric | Target | Owner |
| --- | --- | --- | --- | --- |
| 1 | Every in-scope system has a current AIIA. | % systems with AIIA <12 months old | 100% | AIMS Lead |
| 2 | Zero high-severity AI incidents per quarter. | Count from incident log | 0 | AIMS Lead |
| 3 | All staff complete annual responsible-AI awareness. | % staff trained | 100% | AIMS Lead |
| 4 | TBD | TBD | TBD | TBD |
| 5 | TBD | TBD | TBD | TBD |

## 5. Roles & responsibilities

Detailed in [`../operations/roles-responsibilities.md`](../operations/roles-responsibilities.md).
Headline: Managing Member is accountable; AIMS Lead is responsible.

## 6. Alignment with other policies

This policy is read together with:

- [`acceptable-use-policy.md`](acceptable-use-policy.md)
- [`data-management-policy.md`](data-management-policy.md)
- [`third-party-policy.md`](third-party-policy.md)
- [`ai-sdlc-procedure.md`](ai-sdlc-procedure.md)

When in conflict, this AI policy prevails; the conflict is logged as a
nonconformity per [`../operations/internal-audit-procedure.md`](../operations/internal-audit-procedure.md).

## 7. Communication (clause 7.4)

| Audience | Channel | Frequency |
| --- | --- | --- |
| Internal staff | Onboarding doc + annual refresh | At hire, annually |
| Clients | Statement of work + system card | Per engagement |
| Public | Architech repo README | Continuous |
| Regulators | On request | As required |

## 8. Reporting concerns and incidents (A.3.3 · A.8.3 · A.8.4)

Anyone — staff, client, end-user, member of the public — may report an AI
concern via **[TBD email or form URL]**. The AIMS Lead acknowledges
within **2 business days** and triages within **5 business days**.

**Incidents** are classified Low / Medium / High / Critical. High and
Critical incidents are reported to the Managing Member within 24 hours
and to affected parties per the table in
[`../operations/internal-audit-procedure.md`](../operations/internal-audit-procedure.md) § Incidents.

## 9. KPIs and monitoring (clause 9.1)

The objectives in §4 are reviewed quarterly. Results are an input to
management review per
[`../operations/management-review-procedure.md`](../operations/management-review-procedure.md).

## 10. Review and update (A.2.4)

This policy is reviewed:

- At least **annually**.
- After any material change to scope, law, or AIMS structure.
- After any High/Critical incident.

Changes are logged via [`../templates/change-record.md`](../templates/change-record.md).

## 11. Approval

```
Name:       [TBD]
Title:      Managing Member, 12th House AI, LLC
Signature:  [TBD]
Date:       [TBD]
```
