# Third-Party and Customer Relationships Policy

```
Owner:        [TBD - AIMS Lead]
Approved by:  [TBD - Managing Member]
Effective:    [TBD]
Last review:  [TBD]
Next review:  [TBD - annual]
Coverage:     A.10.2 · A.10.3 · A.10.4
```

## 1. Purpose

Define how 12th House AI, LLC manages AI-relevant relationships across
the AI value chain — upstream (suppliers) and downstream (customers).

## 2. Value chain & allocation of responsibilities (A.10.2)

```
Foundation model provider  →   12th House AI, LLC   →   Client / End-user
   (OpenAI, Anthropic,         (Architech demos +        (consumes outputs
    Google, xAI, Meta,          client systems)           or operates system)
    Alibaba, …)
```

A RACI for each major activity is maintained in
[`../operations/roles-responsibilities.md`](../operations/roles-responsibilities.md)
§ "Value-chain RACI". As a minimum:

- **Model behavior & training data** → upstream provider (R), LLC (C),
  client (I).
- **System integration & deployment** → LLC (R/A), client (C).
- **Use-time monitoring** → client where they operate the system; LLC
  where the LLC hosts.
- **End-user disclosure** → whoever interfaces with the end user.

## 3. Suppliers (A.10.3)

### 3.1 Approved supplier list

Maintained in [`../registers/ai-system-inventory.md`](../registers/ai-system-inventory.md)
§ "Suppliers". Each entry records:

- Vendor name & contact.
- Service used (model API, hosting, vector DB, framework).
- Contract / ToS / DPA reference & expiry.
- Risk classification (Low / Medium / High).
- Date of last review.

### 3.2 Onboarding checks

Before relying on a new supplier:

1. Review terms of service for training-on-customer-data clauses;
   opt out where possible.
2. Confirm certifications (SOC 2, ISO 27001, ISO 42001 if available).
3. Document allocation of responsibilities in the value-chain RACI.
4. Add to inventory.

### 3.3 Ongoing oversight

- Annual review of supplier list.
- Re-assess on any supplier security incident, policy change, or
  breach disclosure.

## 4. Customers (A.10.4)

### 4.1 Pre-engagement

Each client engagement records:

- Intended use of the AI system.
- Data flows and classifications.
- AIIA reference.
- Disclosures the client must make to their end-users.

### 4.2 Engagement contract minimums

The standard engagement template (TBD) includes:

- LLC's AI policy by reference.
- Allocation of responsibilities per value-chain RACI.
- Incident notification SLA.
- Data deletion at engagement close.
- Audit-cooperation clause.

### 4.3 Post-engagement

- Final AIIA snapshot delivered.
- Client retains ownership of their data; LLC retains aggregated
  learnings only.

## 5. Outbound IP

The Architech repository is published under the MIT license (see
`/LICENSE`). Forks and derivative works carry that license; the LLC
makes no AI-specific warranty for demo code.

## 6. Review

Annual; or upon onboarding/offboarding any High-risk supplier or
material customer.
