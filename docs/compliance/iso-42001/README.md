# ISO/IEC 42001 Starter AIMS Pack

This directory holds the **AI Management System (AIMS) starter pack** for
**12th House AI, LLC**, organized against **ISO/IEC 42001:2023**.

It is a **study-grade** artifact set — built to support PECB ISO/IEC 42001
Lead Auditor exam preparation and to seed a real AIMS that the LLC can grow
into. It is **not** a certified or audit-ready set. Every document contains
`TBD` placeholders the organization must fill before any real audit.

## How the pack is structured

```
iso-42001/
├── README.md                          (this file — index & how-to-use)
├── mapping.md                         Standard → 12th House AI mapping
├── statement-of-applicability.md      All 38 Annex A controls + applicability
├── policies/                          Top-level documented policies
├── registers/                         Living records (risks, systems, parties)
├── templates/                         Reusable per-system / per-change forms
└── operations/                        Procedures the AIMS runs on
```

Each document begins with a header block:

```
Owner:        [TBD]
Approved by:  [TBD]
Effective:    [TBD]
Last review:  [TBD]
Next review:  [TBD]
Clause / Control coverage: <e.g., 5.2, A.2.2, A.2.3>
```

This block is what an auditor scans first — keep it filled.

## How to use it (Lead Auditor study path)

1. Read `mapping.md` end to end. It walks every main clause (4–10) and every
   Annex A domain (A.2–A.10) and shows how each maps to 12th House AI, LLC.
2. Open `statement-of-applicability.md`. Decide applicable/not applicable for
   each of the 38 controls and write the justification. The SoA is the
   single most-referenced document in an external audit.
3. Open each policy in `policies/` and replace `TBD` with concrete content.
4. Maintain `registers/risk-register.md` as you onboard each new AI system.
5. For every new AI system or material change, run the template in
   `templates/ai-impact-assessment.md` and produce a
   `templates/model-system-card.md` for it.
6. Run `operations/internal-audit-procedure.md` and
   `operations/management-review-procedure.md` at the cadences they specify.

## Scope of this AIMS

- **Organization in scope:** 12th House AI, LLC.
- **AI systems in scope:** All AI systems the LLC develops, operates, or
  resells, including the Architech demo/tutorial collection in this repo
  and any client-facing systems built from those patterns. Specifics live in
  `registers/ai-system-inventory.md`.
- **Boundaries:** Third-party foundation models (OpenAI, Anthropic, Google,
  xAI, Meta, Alibaba) are out of scope for the LLC's AIMS as *developers*
  but in scope as *suppliers* under A.10. See `policies/third-party-policy.md`.

## Standard reference

- **ISO/IEC 42001:2023** — Information technology — Artificial intelligence —
  Management system.
- Main clauses 4–10 define the management system.
- Annex A (informative) provides 9 control domains and ~38 controls.
- Annex B (informative) provides implementation guidance for Annex A.
- Annex C lists potential AI-related organizational objectives and risk sources.
- Annex D covers use across domains and sectors.

External sources used to build this pack are listed at the bottom of
`mapping.md`.

## Conventions in this pack

- **TBD** — placeholder for org-specific content you must supply.
- **N/A — <reason>** — declared not applicable; reason must be in the SoA.
- **[link]** — internal cross-reference; keep links live as you rename files.
- Dates use `YYYY-MM-DD`. Review cadence defaults to annual unless stated.
