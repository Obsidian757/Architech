# Model / System Card — Template

```
System ID:    [TBD - from ai-system-inventory.md]
Version:      [TBD]
Owner:        [TBD]
Approved by:  [TBD - AIMS Lead]
Effective:    [TBD]
Last review:  [TBD]
Next review:  [TBD]
Coverage:     A.8.2 · A.6.2.7 · A.6.2.3 · A.9.4
```

> **Usage.** Copy alongside the system's source (e.g., next to its
> `README.md` in the relevant Architech subdirectory or client repo).
> The system card is the *external-facing* documentation; pair with
> the *internal* AIIA.

## 1. Purpose & intended use

- **What it does (one paragraph):** TBD
- **Intended use:** TBD
- **Out of scope use:** TBD
- **Foreseeable misuse:** TBD
- **Audience:** TBD

## 2. Architecture

- **Inputs:** TBD
- **Model(s):** provider + name + version. TBD
- **Tools / external calls:** TBD
- **Outputs:** TBD
- **Hosting:** TBD

A simple text diagram is sufficient:

```
input → [preprocess] → [model: provider/name vX.Y] → [postprocess] → output
                              ↘ [tool: name] ↗
```

## 3. Data sources

| Source | Origin | License | Sensitivity | Notes |
| --- | --- | --- | --- | --- |
| TBD | TBD | TBD | Public / Internal / Confidential / PII | TBD |

## 4. Evaluation

- **Eval scenarios:** TBD
- **Eval dataset(s):** TBD (size, source, license)
- **Metrics & results:** TBD
- **Known limitations:** TBD

## 5. Known risks & mitigations

Cross-reference [`../registers/risk-register.md`](../registers/risk-register.md)
risk IDs that apply, plus system-specific risks.

| Risk | Mitigation | Owner |
| --- | --- | --- |
| TBD | TBD | TBD |

## 6. Use-time monitoring

- **What is logged:** TBD
- **Retention:** TBD
- **Alerts:** TBD
- **Human-in-the-loop points:** TBD

## 7. Incident & feedback channel

Report concerns or incidents to **[TBD email or form URL]** per the
LLC's [AI Policy](../policies/ai-policy.md) § 8.

## 8. Provenance & change history

| Date | Version | Author | Summary |
| --- | --- | --- | --- |
| TBD | 0.1 | TBD | Initial card |

## 9. Approval

```
Approved by: [TBD]   Role: AIMS Lead
Date:        [TBD]
```
