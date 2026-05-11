# Statement of Applicability (SoA) — ISO/IEC 42001:2023 Annex A

```
Owner:        [TBD - AIMS Lead]
Approved by:  [TBD - Managing Member, 12th House AI, LLC]
Effective:    [TBD]
Last review:  [TBD]
Next review:  [TBD - at least annually]
Coverage:     All Annex A controls (A.2 through A.10)
```

The SoA is the **single most-cited document** in an ISO 42001 audit. For
every Annex A control it must state:

1. Whether the control is **applicable** to 12th House AI, LLC's AIMS.
2. **Justification** for the inclusion or exclusion decision.
3. **Implementation status**: `Implemented` / `Partial` / `Planned` / `N/A`.
4. **Evidence reference** — file path inside this pack.

> **Note on control numbering.** The ISO/IEC 42001:2023 Annex A in the
> published standard contains ~38 controls across 9 domains. The titles
> below paraphrase the standard for study purposes and align with the
> domain structure of the standard. **Before any real audit**, reconcile
> each row against the authoritative published text and update titles
> verbatim. Rows marked `TBD title — confirm against standard` are
> placeholders that exist in the standard but whose exact wording must
> be copied from the purchased document.

Legend: ✅ Implemented · 🟡 Partial · 🔜 Planned · ⛔ N/A

---

## A.2 — Policies related to AI

| ID | Control (paraphrased) | Applicable? | Status | Justification | Evidence |
| --- | --- | --- | --- | --- | --- |
| A.2.2 | AI policy | Yes | 🟡 | Required for any AIMS; LLC has skeleton, needs signature. | [policies/ai-policy.md](policies/ai-policy.md) |
| A.2.3 | Alignment with other organizational policies | Yes | 🔜 | LLC has no parallel policies yet to align with; cross-references will be added as Privacy/Security policies appear. | [policies/ai-policy.md](policies/ai-policy.md) § Alignment |
| A.2.4 | Review of the AI policy | Yes | 🔜 | Annual review cadence defined; first review TBD. | [policies/ai-policy.md](policies/ai-policy.md) § Review |

## A.3 — Internal organization

| ID | Control | Applicable? | Status | Justification | Evidence |
| --- | --- | --- | --- | --- | --- |
| A.3.2 | AI roles & responsibilities | Yes | 🟡 | Roles defined but RACI not signed off. | [operations/roles-responsibilities.md](operations/roles-responsibilities.md) |
| A.3.3 | Reporting of concerns (AI whistleblowing channel) | Yes | 🔜 | LLC must publish an escalation channel for AI concerns from staff and external parties. | [policies/ai-policy.md](policies/ai-policy.md) § Reporting concerns |

## A.4 — Resources for AI systems

| ID | Control | Applicable? | Status | Justification | Evidence |
| --- | --- | --- | --- | --- | --- |
| A.4.2 | Resource documentation | Yes | 🔜 | Inventory exists in skeleton; needs per-system rows filled. | [registers/ai-system-inventory.md](registers/ai-system-inventory.md) |
| A.4.3 | Data resources | Yes | 🟡 | Most demos use public corpora; LLC must record provenance per system. | [policies/data-management-policy.md](policies/data-management-policy.md) |
| A.4.4 | Tooling resources | Yes | 🟡 | Frameworks documented in repo READMEs; consolidate in inventory. | [registers/ai-system-inventory.md](registers/ai-system-inventory.md) |
| A.4.5 | System & computing resources | Yes | 🟡 | Hosting boundary varies (local vs. cloud); document per system. | [registers/ai-system-inventory.md](registers/ai-system-inventory.md) |
| A.4.6 | Human resources | Yes | 🔜 | Identify named roles; competence records in 7.2. | [operations/competence-and-awareness.md](operations/competence-and-awareness.md) |

## A.5 — Assessing impacts of AI systems

| ID | Control | Applicable? | Status | Justification | Evidence |
| --- | --- | --- | --- | --- | --- |
| A.5.2 | AI impact assessment process | Yes | 🟡 | Template defined; no filed AIIAs yet. | [templates/ai-impact-assessment.md](templates/ai-impact-assessment.md) |
| A.5.3 | Documentation of AI impact assessments | Yes | 🔜 | Filing location `registers/aiia/` created on first use. | `registers/aiia/` |
| A.5.4 | Assessing impact on individuals or groups | Yes | 🔜 | Section in AIIA template; needs population. | [templates/ai-impact-assessment.md](templates/ai-impact-assessment.md) § Individuals |
| A.5.5 | Assessing societal impacts | Yes | 🔜 | Section in AIIA template. | [templates/ai-impact-assessment.md](templates/ai-impact-assessment.md) § Society |

## A.6 — AI system lifecycle

| ID | Control | Applicable? | Status | Justification | Evidence |
| --- | --- | --- | --- | --- | --- |
| A.6.1.2 | Objectives for responsible development | Yes | 🟡 | Top-level objectives in AI policy; refine per system. | [policies/ai-policy.md](policies/ai-policy.md) § Objectives |
| A.6.1.3 | Processes for responsible design & development | Yes | 🟡 | SDLC skeleton drafted. | [policies/ai-sdlc-procedure.md](policies/ai-sdlc-procedure.md) |
| A.6.2.2 | Requirements & specification | Yes | 🟡 | Each system must record functional + responsible-AI requirements. | [templates/model-system-card.md](templates/model-system-card.md) |
| A.6.2.3 | Documentation of AI system design & development | Yes | 🟡 | Architech READMEs partially serve this; tighten with system cards. | [templates/model-system-card.md](templates/model-system-card.md) |
| A.6.2.4 | Verification & validation | Yes | 🔜 | LLC must define test/eval procedures per system; today only manual smoke-tests via Streamlit. | [policies/ai-sdlc-procedure.md](policies/ai-sdlc-procedure.md) § V&V |
| A.6.2.5 | Deployment | Yes | 🟡 | Deployment is "user runs locally" for demos; client work needs go-live checklist. | [policies/ai-sdlc-procedure.md](policies/ai-sdlc-procedure.md) § Deployment |
| A.6.2.6 | Operation & monitoring | Yes | 🔜 | For client systems only; demos are user-operated. | [policies/ai-sdlc-procedure.md](policies/ai-sdlc-procedure.md) § Operation |
| A.6.2.7 | Technical documentation | Yes | 🟡 | Repo READMEs cover most; consolidate into system cards. | [templates/model-system-card.md](templates/model-system-card.md) |
| A.6.2.8 | Logging of events | Partial | 🔜 | Demos do not log; client systems must. | [policies/ai-sdlc-procedure.md](policies/ai-sdlc-procedure.md) § Logging |

## A.7 — Data for AI systems

| ID | Control | Applicable? | Status | Justification | Evidence |
| --- | --- | --- | --- | --- | --- |
| A.7.2 | Data for development & enhancement | Yes | 🟡 | LLC does not train foundation models; covers fine-tune / RAG corpora. | [policies/data-management-policy.md](policies/data-management-policy.md) § Sources |
| A.7.3 | Acquisition of data | Yes | 🟡 | Supplier-of-data terms must be tracked. | [policies/data-management-policy.md](policies/data-management-policy.md) § Acquisition |
| A.7.4 | Quality of data for AI systems | Yes | 🟡 | Define quality dimensions and checks per system. | [policies/data-management-policy.md](policies/data-management-policy.md) § Quality |
| A.7.5 | Data provenance | Yes | 🟡 | Each dataset must record origin, license, time of capture. | [policies/data-management-policy.md](policies/data-management-policy.md) § Provenance |
| A.7.6 | Data preparation | Yes | 🟡 | Document transforms (chunking, embeddings, filters). | [policies/data-management-policy.md](policies/data-management-policy.md) § Preparation |

## A.8 — Information for interested parties

| ID | Control | Applicable? | Status | Justification | Evidence |
| --- | --- | --- | --- | --- | --- |
| A.8.2 | System documentation & information for users | Yes | 🟡 | Architech READMEs serve learners; client systems need formal docs. | [templates/model-system-card.md](templates/model-system-card.md) |
| A.8.3 | External reporting | Yes | 🔜 | Incident & concern reporting channel. | [policies/ai-policy.md](policies/ai-policy.md) § Reporting concerns |
| A.8.4 | Communication of incidents | Yes | 🔜 | LLC must define notification SLA to affected parties. | [policies/ai-policy.md](policies/ai-policy.md) § Incidents |
| A.8.5 | Information for interested parties | Yes | 🔜 | Tailored info packs by audience: learner, client, regulator. | [registers/interested-parties.md](registers/interested-parties.md) |

## A.9 — Use of AI systems

| ID | Control | Applicable? | Status | Justification | Evidence |
| --- | --- | --- | --- | --- | --- |
| A.9.2 | Processes for responsible use | Yes | 🟡 | AUP skeleton drafted. | [policies/acceptable-use-policy.md](policies/acceptable-use-policy.md) |
| A.9.3 | Objectives for responsible use | Yes | 🟡 | Cross-referenced from AI policy. | [policies/ai-policy.md](policies/ai-policy.md) § Use |
| A.9.4 | Intended use | Yes | 🟡 | Each system card states intended + non-intended use. | [templates/model-system-card.md](templates/model-system-card.md) § Use |

## A.10 — Third-party and customer relationships

| ID | Control | Applicable? | Status | Justification | Evidence |
| --- | --- | --- | --- | --- | --- |
| A.10.2 | Allocation of responsibilities | Yes | 🟡 | RACI across value chain (model provider → LLC → client). | [policies/third-party-policy.md](policies/third-party-policy.md) § Value chain |
| A.10.3 | Suppliers | Yes | 🟡 | Foundation-model providers; tracker needed. | [policies/third-party-policy.md](policies/third-party-policy.md) § Suppliers |
| A.10.4 | Customers | Yes | 🔜 | Client-facing AI obligations & disclosures. | [policies/third-party-policy.md](policies/third-party-policy.md) § Customers |

---

## Summary by status

| Status | Count |
| --- | --- |
| ✅ Implemented | 0 |
| 🟡 Partial | 19 |
| 🔜 Planned | 17 |
| ⛔ N/A | 0 |
| **Total controls listed** | **36** |

Two controls from the canonical "~38" total are intentionally **deferred**
until the SoA is reconciled against the authoritative standard text (likely
A.6.x sub-controls on logging granularity and A.5.x sub-control on
re-assessment after material change — verify and add).

## Process

- The SoA is **versioned** in git alongside the rest of the AIMS.
- Any change to applicability or status requires a `templates/change-record.md`
  entry and management-review sign-off.
- Reviewed at least annually and after any material change to the AIMS scope.
