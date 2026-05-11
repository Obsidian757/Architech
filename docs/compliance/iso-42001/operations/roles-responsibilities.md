# Roles, Responsibilities & Authorities

```
Owner:        [TBD - AIMS Lead]
Approved by:  [TBD - Managing Member]
Effective:    [TBD]
Last review:  [TBD]
Next review:  [TBD - annual]
Coverage:     Clause 5.1 · 5.3 · A.3.2 · A.3.3
```

## Top management

**Managing Member, 12th House AI, LLC** — accountable for the AIMS.
Owns: AI policy approval, resourcing, management review chair,
incident escalation receiver.

## AIMS Lead

The single point of responsibility for running the AIMS day-to-day.
For a small LLC, this may be the Managing Member wearing the AIMS hat
or a delegate. The role must be **named** and **single-threaded**.

Owns:

- This documentation set.
- SoA maintenance.
- Risk register and AIIA process.
- Internal audit scheduling.
- Triage of concerns reported via the channel in
  [`../policies/ai-policy.md`](../policies/ai-policy.md) § 8.

## Engineering

Responsible for the SDLC of in-scope systems per
[`../policies/ai-sdlc-procedure.md`](../policies/ai-sdlc-procedure.md).

## External advisor (optional)

Legal / compliance counsel engaged on demand for regulatory questions
and audit prep. Not part of the AIMS chain of command.

## RACI — AIMS activities

R = Responsible · A = Accountable · C = Consulted · I = Informed

| Activity | Managing Member | AIMS Lead | Engineering | Advisor |
| --- | --- | --- | --- | --- |
| Approve AI policy | A | R | C | C |
| Maintain SoA | A | R | C | C |
| Run AI risk assessment | A | R | C | C |
| Run AIIA on new system | A | R | C | C |
| Approve high-risk system go-live | A | R | C | C |
| Implement controls in code | I | A | R | — |
| Supplier review | A | R | I | C |
| Internal audit | I | R | I | C |
| Management review | A/R (chair) | R | C | C |
| Incident triage & disclosure | A | R | C | C |

## Value-chain RACI (A.10.2)

| Activity | Model provider | 12th House AI, LLC | Client |
| --- | --- | --- | --- |
| Model training | R/A | I | I |
| Provider-side safety filters | R/A | I | I |
| System design & integration | I | R/A | C |
| Use-time monitoring (LLC-hosted) | I | R/A | I |
| Use-time monitoring (client-hosted) | I | C | R/A |
| End-user disclosure | I | C | R/A |
| Personal-data handling | I | C/R per engagement | A |
| Incident reporting upstream | C | R | I |
| Incident reporting downstream (end-users) | I | C | R/A |

## Separation of duties

Where the LLC's headcount permits, the person approving an AIIA or
SoA change is not the same person who implemented the change. Where
headcount does not permit (small team), the management review acts as
the compensating control.

## Reporting concerns (A.3.3)

Anyone may report concerns confidentially via **[TBD email / form]**.
The AIMS Lead acknowledges within 2 business days and protects the
reporter from retaliation per LLC employment terms.
