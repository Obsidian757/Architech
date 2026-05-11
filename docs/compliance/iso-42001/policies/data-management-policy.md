# Data Management Policy for AI Systems

```
Owner:        [TBD - AIMS Lead]
Approved by:  [TBD - Managing Member]
Effective:    [TBD]
Last review:  [TBD]
Next review:  [TBD - annual]
Coverage:     A.7.2 · A.7.3 · A.7.4 · A.7.5 · A.7.6 · A.4.3
```

## 1. Purpose

Govern how data is acquired, evaluated, used, and retained for AI
systems in scope.

## 2. Scope

All data used by in-scope AI systems for any of: fine-tuning,
retrieval-augmented generation (RAG), prompt construction, evaluation,
operational logging.

> **Note.** 12th House AI, LLC does **not** train foundation models.
> "Training data" in this policy refers to fine-tuning corpora, RAG
> indexes, and evaluation datasets.

## 3. Sources (A.7.2)

For each data source, record:

- Origin (URL, vendor, internal generation).
- License and permitted uses.
- Sensitivity classification (Public / Internal / Confidential / PII).
- Whether it contains personal data; if so, lawful basis.

## 4. Acquisition (A.7.3)

- Public data: capture URL + timestamp + license.
- Vendor data: track contract reference in `third-party-policy.md`.
- User-provided data (client engagements): governed by the engagement
  agreement; default is "process for engagement only, delete on close".

## 5. Quality (A.7.4)

Each system declares which quality dimensions apply and how they are
measured. Default dimensions:

| Dimension | How measured |
| --- | --- |
| Accuracy | Spot-check sample size [TBD] |
| Completeness | Field-coverage check |
| Consistency | Schema validation |
| Timeliness | Max age policy per system |
| Representativeness | Documented sampling rationale |
| Privacy minimization | No fields beyond stated purpose |

Failures are tracked in the system's AIIA risk section.

## 6. Provenance (A.7.5)

Every dataset has a provenance record with:

- Origin & acquisition date.
- License text or URL.
- Chain of custody (who handled it, where stored).
- Any transformations applied (linking to A.7.6 preparation steps).

For RAG corpora used in Architech demos (e.g., Wikipedia, ArXiv, news
feeds), provenance is captured in the demo's README.

## 7. Preparation (A.7.6)

Document transformations: cleaning, deduplication, redaction, chunking,
embedding model and version, filters, augmentation. Re-running a
preparation pipeline must produce a reproducible artifact or have its
non-determinism documented.

## 8. Personal data

If a system processes personal data:

1. Run the AIIA in [`../templates/ai-impact-assessment.md`](../templates/ai-impact-assessment.md)
   with the "Personal data" section completed.
2. Run or reference an applicable DPIA (GDPR Art. 35) if scope warrants.
3. Apply minimization, retention, and access controls per the
   engagement agreement.

## 9. Retention & deletion

- Client engagement data: deleted within **30 days** of engagement close
  unless contract specifies otherwise.
- Public data: indefinite, with annual relevance review.
- Logs containing user inputs: max retention **90 days** by default;
  override per system.

## 10. Review

Annual; or upon any data-related incident.
