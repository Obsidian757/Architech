# AI System Lifecycle Procedure (SDLC)

```
Owner:        [TBD - AIMS Lead]
Approved by:  [TBD - Managing Member]
Effective:    [TBD]
Last review:  [TBD]
Next review:  [TBD - annual]
Coverage:     A.6.1.2 · A.6.1.3 · A.6.2.2 · A.6.2.3 · A.6.2.4 · A.6.2.5 · A.6.2.6 · A.6.2.7 · A.6.2.8
```

## 1. Purpose

Define the lifecycle stages every in-scope AI system passes through
and the artifacts each stage produces.

## 2. Stages

```
1. Concept  →  2. Requirements  →  3. Design  →  4. Build
        →  5. V&V  →  6. Deployment  →  7. Operation  →  8. Retirement
```

### 2.1 Concept

- Capture the use case in 1 page.
- Decide: Architech demo (educational) vs. client system.
- Run a lightweight AIIA screen.

**Artifacts:** concept note, AIIA screen (top of
[`../templates/ai-impact-assessment.md`](../templates/ai-impact-assessment.md)).

### 2.2 Requirements (A.6.2.2)

Capture both **functional** and **responsible-AI** requirements:

- Functional: what it does, inputs, outputs, SLAs.
- Responsible-AI: fairness considerations, transparency obligations,
  privacy constraints, human-oversight points.

**Artifacts:** populated **Intended use** + **Out of scope use** in the
system card.

### 2.3 Design (A.6.2.3)

- Architecture diagram (text-OK for small systems).
- Model selection rationale.
- Data sources and flows.
- Monitoring & logging plan.

**Artifacts:** system card § Architecture; AIIA risk section.

### 2.4 Build

- Implement under version control (this repo or a client repo).
- Track dependencies; pin versions for reproducibility.
- Secrets handled per supplier ToS.

### 2.5 Verification & validation (A.6.2.4)

- **Verification:** code review + automated tests where applicable.
- **Validation:** at minimum, a documented eval scenario per system.
  For LLM apps: rubric-based scoring on a small held-out set.
- Document acceptance criteria and outcomes in the system card.

### 2.6 Deployment (A.6.2.5)

Demo (Architech): merged to default branch + README run instructions.
Client system: go-live checklist below.

**Go-live checklist (client systems):**

- [ ] AIIA approved.
- [ ] System card published to client.
- [ ] Monitoring & logging enabled.
- [ ] Incident runbook delivered.
- [ ] Rollback plan documented.

### 2.7 Operation & monitoring (A.6.2.6 · A.6.2.8)

- **Demos:** user-operated; no LLC monitoring.
- **Client systems:** monitoring per system card. Log retention per
  [`data-management-policy.md`](data-management-policy.md) § 9.
- Periodic review of operational metrics feeds management review.

### 2.8 Retirement

- Notify users / clients.
- Archive system card, AIIA, eval results.
- Delete data per retention policy.
- Remove from `registers/ai-system-inventory.md`.

## 3. Change control (clause 6.3 / 8.1)

All material changes use [`../templates/change-record.md`](../templates/change-record.md).
A change is **material** if it alters intended use, data flows, model
provider, or risk classification — in which case the AIIA is re-run.

## 4. Existing automation referenced

`/.github/workflows/claude.yml` is the current CI workflow.
The SDLC formalization adds the responsibilities above on top of it,
without replacing existing engineering practices.

## 5. Review

Annual; or upon any High-severity incident; or upon a major change to
the toolchain or hosting model.
