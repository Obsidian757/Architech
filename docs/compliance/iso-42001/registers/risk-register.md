# AI Risk Register

```
Owner:        [TBD - AIMS Lead]
Approved by:  [TBD - Managing Member]
Effective:    [TBD]
Last review:  [TBD]
Next review:  [TBD - quarterly]
Coverage:     Clause 6.1 · 8.2 · 8.3 · A.5
```

## Methodology

- **Likelihood:** 1 (Rare) — 5 (Almost certain).
- **Impact:** 1 (Negligible) — 5 (Severe).
- **Inherent risk** = Likelihood × Impact (pre-control).
- **Residual risk** = Likelihood × Impact (post-control).
- **Treatment:** Mitigate · Transfer · Avoid · Accept.

Reviewed at least quarterly and after any High/Critical incident or
material change. Risk source categories follow ISO/IEC 23894 and ISO/IEC
42001 Annex C.

## Risk taxonomy (seed list — refine per system)

| ID | Risk source | Risk description (default) | Inh. L | Inh. I | Inh. | Treatment | Controls referenced | Res. L | Res. I | Res. | Owner |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R-01 | Model hallucination | LLM output is plausibly wrong, misleading user or client | 4 | 3 | 12 | Mitigate | A.6.2.4 V&V; AUP § disclose AI use; system card limits | 3 | 2 | 6 | AIMS Lead |
| R-02 | Prompt injection | Adversarial input subverts system instructions / tools | 4 | 3 | 12 | Mitigate | A.6.2.4; tool-call allowlists; output filters | 3 | 2 | 6 | AIMS Lead |
| R-03 | Data leakage to model provider | Confidential data sent to third-party API without DPA | 3 | 4 | 12 | Mitigate | Data policy § 4; supplier DPAs | 1 | 4 | 4 | AIMS Lead |
| R-04 | Bias / discrimination | System produces outputs that disadvantage a protected group | 3 | 4 | 12 | Mitigate | A.5 AIIA; eval set diversity | 2 | 3 | 6 | AIMS Lead |
| R-05 | Foundation-model deprecation | Provider sunsets a model used by an LLC system | 4 | 2 | 8 | Mitigate | Multi-provider abstraction; change control | 3 | 2 | 6 | AIMS Lead |
| R-06 | Supplier ToS change | Model provider changes terms (e.g., training on data) | 3 | 3 | 9 | Mitigate | A.10.3 supplier review cadence | 2 | 2 | 4 | AIMS Lead |
| R-07 | IP / copyright | Output infringes third-party IP | 3 | 3 | 9 | Mitigate | Provider IP indemnity check; client disclaimer | 2 | 2 | 4 | AIMS Lead |
| R-08 | Personal-data misuse | PII processed without lawful basis | 2 | 5 | 10 | Avoid | Data policy § 8; DPIA where applicable | 1 | 5 | 5 | AIMS Lead |
| R-09 | Regulatory non-compliance | EU AI Act / US state law obligations missed | 3 | 4 | 12 | Mitigate | Annual regulatory scan in management review | 2 | 3 | 6 | AIMS Lead |
| R-10 | Reputational damage | Public incident with an Architech demo | 2 | 3 | 6 | Mitigate | A.8.3 reporting; incident runbook | 1 | 3 | 3 | AIMS Lead |
| R-11 | Over-reliance | User treats AI output as authoritative | 3 | 3 | 9 | Mitigate | AUP § review outputs; UI disclaimers | 2 | 2 | 4 | AIMS Lead |
| R-12 | Cost overrun | Token/API spend exceeds budget on a demo or client system | 3 | 2 | 6 | Mitigate | Rate limits; budget alerts | 2 | 2 | 4 | AIMS Lead |
| R-13 | Drift | Behavior changes after provider model update | 3 | 3 | 9 | Mitigate | Eval reruns on model update; pinned versions | 2 | 2 | 4 | AIMS Lead |
| R-14 | Insecure tool use by agent | Agent invokes a tool with unintended consequences | 3 | 4 | 12 | Mitigate | Tool allowlist; sandboxing; human-in-loop | 2 | 3 | 6 | AIMS Lead |
| R-15 | Loss of human oversight | No named owner for an in-scope system | 2 | 4 | 8 | Avoid | Inventory mandates owner field | 1 | 4 | 4 | AIMS Lead |

## Per-system addenda

Each in-scope system attaches a per-system risk addendum at
`registers/risk-system-<id>.md` capturing risks that are not covered by
the taxonomy above, or that have a different inherent/residual rating
for that system.

## Acceptance criteria

- Residual risk ≤ **6** is accepted with periodic review.
- Residual risk **7–12** requires a documented treatment plan with a
  named owner and target date.
- Residual risk **> 12** is not accepted; system cannot operate until
  reduced.
