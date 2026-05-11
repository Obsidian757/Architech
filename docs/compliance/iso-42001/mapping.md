# ISO/IEC 42001:2023 → 12th House AI, LLC Mapping

```
Owner:        [TBD - typically AIMS Lead / CTO]
Approved by:  [TBD - LLC Member / Officer]
Effective:    [TBD]
Last review:  [TBD]
Next review:  [TBD]
Coverage:     Main clauses 4–10 and Annex A.2–A.10
```

This document maps every requirement of ISO/IEC 42001:2023 to 12th House AI,
LLC, including the Architech repository as an in-scope asset. For each
requirement it states (1) the standard's intent in plain English, (2) how it
applies to the LLC, (3) the current state, (4) the evidence artifact in this
pack, and (5) the gap / next action.

---

## Part 1 — Main clauses (the management system shell)

### Clause 4 — Context of the organization

#### 4.1 Understanding the organization and its context

- **Requirement.** Identify internal/external issues relevant to the AIMS and
  its intended outcomes.
- **Applies to LLC as.** Small AI consultancy + content/tutorial publisher
  building on third-party foundation models. External issues: rapid model
  release cadence, EU AI Act, evolving US state laws, NIST AI RMF. Internal
  issues: small team, no in-house ML training, reliance on hosted APIs.
- **Current state.** Implicit only.
- **Evidence.** `registers/interested-parties.md` § "Context".
- **Gap.** Capture the context analysis explicitly. **Quick win:** 1-page
  PESTLE-style note.

#### 4.2 Understanding the needs and expectations of interested parties

- **Requirement.** Identify interested parties relevant to the AIMS and their
  relevant requirements.
- **Applies to LLC as.** Clients, end-users of client systems, model
  providers (OpenAI, Anthropic, Google, xAI, Meta, Alibaba), regulators,
  contributors to the Architech repo, learners using the tutorials.
- **Current state.** README acknowledges sponsors and learners informally.
- **Evidence.** `registers/interested-parties.md`.
- **Gap.** No formal mapping of needs/expectations to controls.

#### 4.3 Determining the scope of the AIMS

- **Requirement.** Document AIMS scope considering 4.1, 4.2, and AI systems
  the org develops/operates.
- **Applies to LLC as.** LLC + Architech + any client-facing systems.
- **Current state.** Stated in this pack's `README.md` § "Scope".
- **Evidence.** `README.md` (Scope) + `registers/ai-system-inventory.md`.
- **Gap.** Formalize scope statement, with inclusions/exclusions, in a
  signed document.

#### 4.4 AI management system

- **Requirement.** Establish, implement, maintain, continually improve the
  AIMS.
- **Evidence.** This entire pack is the AIMS scaffolding.

### Clause 5 — Leadership

#### 5.1 Leadership and commitment

- **Requirement.** Top management demonstrates leadership: integrates AIMS
  into business processes, ensures resources, communicates importance.
- **Applies to LLC as.** Managing Member of 12th House AI, LLC.
- **Evidence.** `operations/roles-responsibilities.md` § "Top management".
- **Gap.** No signed commitment statement.

#### 5.2 AI policy

- **Requirement.** Top-management-approved AI policy aligned with the org's
  purpose, with commitment to satisfying requirements and continual
  improvement.
- **Evidence.** [`policies/ai-policy.md`](policies/ai-policy.md). Maps also
  to **A.2**.

#### 5.3 Roles, responsibilities and authorities

- **Requirement.** Assign and communicate AIMS roles.
- **Evidence.** [`operations/roles-responsibilities.md`](operations/roles-responsibilities.md).
  Maps also to **A.3**.

### Clause 6 — Planning

#### 6.1 Actions to address risks and opportunities

- **Requirement.** Determine AI risks & opportunities, plan actions, perform
  an AI risk assessment, and conduct an AI system impact assessment (6.1.4
  introduced by 42001).
- **Evidence.**
  - Risk assessment & treatment: [`registers/risk-register.md`](registers/risk-register.md)
  - Per-system impact assessment: [`templates/ai-impact-assessment.md`](templates/ai-impact-assessment.md)
    (also satisfies **A.5**)

#### 6.2 AI objectives and planning to achieve them

- **Requirement.** Establish measurable AI objectives consistent with the AI
  policy.
- **Evidence.** [`policies/ai-policy.md`](policies/ai-policy.md) § "Objectives".
- **Gap.** Objectives currently `TBD` — set 3–5 measurable objectives (e.g.,
  "100% of in-scope systems have a current AIIA", "0 high-severity AI
  incidents/quarter").

#### 6.3 Planning of changes

- **Requirement.** Changes to the AIMS or AI systems are planned, not ad-hoc.
- **Evidence.** [`templates/change-record.md`](templates/change-record.md).

### Clause 7 — Support

| Sub-clause | Topic | Evidence |
| --- | --- | --- |
| 7.1 | Resources | [`registers/ai-system-inventory.md`](registers/ai-system-inventory.md) (compute/data/tools) + A.4 |
| 7.2 | Competence | [`operations/competence-and-awareness.md`](operations/competence-and-awareness.md) |
| 7.3 | Awareness | [`operations/competence-and-awareness.md`](operations/competence-and-awareness.md) § "Awareness" |
| 7.4 | Communication | [`policies/ai-policy.md`](policies/ai-policy.md) § "Communication" |
| 7.5 | Documented information | This entire `iso-42001/` tree |

### Clause 8 — Operation

- **8.1 Operational planning & control.** AI activities are run under
  documented procedures. Evidence: [`policies/ai-sdlc-procedure.md`](policies/ai-sdlc-procedure.md)
  + change records.
- **8.2 AI risk assessment.** Performed at planned intervals and when
  changes occur. Evidence: `registers/risk-register.md` review cadence.
- **8.3 AI risk treatment.** Implements the treatment plan.
  Evidence: risk register "Treatment" column.
- **8.4 AI system impact assessment.** Performed for each AI system / use.
  Evidence: `templates/ai-impact-assessment.md` (one per system).

### Clause 9 — Performance evaluation

- **9.1 Monitoring, measurement, analysis, evaluation.** What is measured,
  by whom, how often. Evidence: `policies/ai-policy.md` § "KPIs" +
  `operations/internal-audit-procedure.md`.
- **9.2 Internal audit.** Periodic internal audits of the AIMS.
  Evidence: [`operations/internal-audit-procedure.md`](operations/internal-audit-procedure.md).
- **9.3 Management review.** Top management reviews the AIMS at planned
  intervals. Evidence: [`operations/management-review-procedure.md`](operations/management-review-procedure.md).

### Clause 10 — Improvement

- **10.1 Nonconformity and corrective action.** Address NCs and prevent
  recurrence. Evidence: `operations/internal-audit-procedure.md` § "NC handling".
- **10.2 Continual improvement.** Evidence: `operations/management-review-procedure.md`
  outputs.

---

## Part 2 — Annex A controls (the 9 domains)

Annex A is informative; controls become applicable through the **Statement
of Applicability**. See [`statement-of-applicability.md`](statement-of-applicability.md)
for the per-control applicability decision. The summary below tells you
*where in this pack* the evidence for each domain lives.

### A.2 — Policies related to AI

- **Intent.** Provide management direction and support for AI per business
  and regulatory requirements.
- **Applies to LLC as.** Top-level AI policy plus supporting policies on
  acceptable use, data, third parties, SDLC.
- **Evidence.** Every file under [`policies/`](policies/).
- **Current state.** Skeletons created in this pack; none signed.
- **Gap.** Get the AI policy signed by the Managing Member.

### A.3 — Internal organization

- **Intent.** Define internal structure to operate the AIMS.
- **Applies to LLC as.** Managing Member, AIMS Lead, optional advisory
  function; AI committee = the same one or two people for now, formally.
- **Evidence.** [`operations/roles-responsibilities.md`](operations/roles-responsibilities.md).

### A.4 — Resources for AI systems

- **Intent.** Identify and document resources (data, tooling, system,
  compute, human) for each AI system across its lifecycle.
- **Applies to LLC as.** Inventory of demo apps in Architech, dependencies
  (Streamlit, agno, LangChain, vector DBs), model providers, dev/hosting
  environments.
- **Evidence.** [`registers/ai-system-inventory.md`](registers/ai-system-inventory.md)
  with one column per resource category (data / tooling / system / compute /
  human / financial).
- **Reuse.** The top-level Architech subdirectories
  (`starter_ai_agents/`, `advanced_ai_agents/`, `rag_tutorials/`,
  `mcp_ai_agents/`, `voice_ai_agents/`, `advanced_llm_apps/`,
  `ai_agent_framework_crash_course/`) seed the inventory.

### A.5 — Assessing impacts of AI systems

- **Intent.** Establish a process for AI impact assessment (AIIA) — to
  individuals, groups, societies — and execute it.
- **Applies to LLC as.** Each new system / material change runs the AIIA
  template. Most demos in Architech have low impact (educational use, no
  PII, no automated decisions) — that decision must still be documented.
- **Evidence.** [`templates/ai-impact-assessment.md`](templates/ai-impact-assessment.md);
  filed copies live under `registers/aiia/` (folder created on first use).

### A.6 — AI system lifecycle

- **Intent.** Manage the AI system lifecycle: requirements, design,
  verification, validation, deployment, operation, monitoring, retirement.
- **Applies to LLC as.** The Architech demos already follow a loose
  lifecycle (README → code → CI workflow `.github/workflows/claude.yml`).
  Formalize it.
- **Evidence.** [`policies/ai-sdlc-procedure.md`](policies/ai-sdlc-procedure.md) +
  [`templates/change-record.md`](templates/change-record.md).

### A.7 — Data for AI systems

- **Intent.** Manage data across acquisition, quality, provenance, and
  preparation for AI systems.
- **Applies to LLC as.** Most Architech demos use either user-pasted input
  or public corpora (Wikipedia, ArXiv, news APIs). Production client work
  may involve PII; that path needs DPIAs + this control.
- **Evidence.** [`policies/data-management-policy.md`](policies/data-management-policy.md).

### A.8 — Information for interested parties

- **Intent.** Transparency. Provide documentation appropriate to each
  interested party (users, regulators, customers).
- **Applies to LLC as.** Each in-scope system needs a model/system card
  describing purpose, limitations, training data (if any), and known risks.
- **Evidence.** [`templates/model-system-card.md`](templates/model-system-card.md);
  populated cards live alongside each system's source code.

### A.9 — Use of AI systems

- **Intent.** Ensure responsible use — by the LLC and by users of LLC
  systems. Covers intended use, foreseeable misuse, monitoring during use.
- **Evidence.** [`policies/acceptable-use-policy.md`](policies/acceptable-use-policy.md).

### A.10 — Third-party and customer relationships

- **Intent.** Manage AI-relevant relationships with suppliers and customers,
  including allocation of responsibilities along the AI value chain.
- **Applies to LLC as.** **Heavy.** Every Architech demo depends on a
  foundation model provider. The LLC sits in the middle of the value chain.
- **Evidence.** [`policies/third-party-policy.md`](policies/third-party-policy.md) +
  the existing `/LICENSE` file for inbound IP.

---

## Reusable existing artifacts in this repo

| Existing file | Pulled into AIMS as |
| --- | --- |
| `/LICENSE` (MIT) | A.10 — outbound license terms for Architech consumers |
| `/README.md` (catalog of ~50+ demos) | Seed for `registers/ai-system-inventory.md` |
| `/.github/workflows/claude.yml` | A.6 — automated change control reference |
| Top-level demo dirs | One row per category in the inventory; each marked **Demo / Educational**, criticality Low |

## Notable gaps to close before any external audit

1. **No signed AI policy.** Highest priority.
2. **No completed AIIAs** for any in-scope system.
3. **No formal supplier list** — foundation-model providers used without
   documented terms tracking.
4. **No `SECURITY.md`, `CODE_OF_CONDUCT.md`, `PRIVACY.md`** at repo root.
5. **No incident response plan.** Required as part of A.6 / clause 8 in
   practice.
6. **No competence records** for the AI roles in A.3.
7. **No internal audit performed yet.** Clause 9.2 requires it on a planned
   cadence — at least annually.

## Sources used (external)

- ISO/IEC 42001:2023 — official standard (purchase from ISO).
- ISO/IEC 23894:2023 — guidance on AI risk management (companion).
- ISO/IEC 22989:2022 — AI concepts and terminology.
- NIST AI Risk Management Framework (AI RMF 1.0).
- AWS Security Blog — *AI lifecycle risk management: ISO/IEC 42001:2023 for
  AI governance.*
- Microsoft Learn — *ISO/IEC 42001:2023 AIMS standards.*
- Cloud Security Alliance — *ISO 42001: Lessons learned from auditing and
  implementing the framework* (May 2025).
- Sprinto — *ISO 42001 for Startups: A Practical Guide.*
- Hyperproof — *ISO 42001: A Practical Guide to AI Governance.*
- ISMS.online, BD Emerson, A-LIGN, AIGL, Bastion, Hicomply — Annex A
  control summaries (cross-referenced for control numbering).
