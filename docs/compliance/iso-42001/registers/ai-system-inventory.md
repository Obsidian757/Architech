# AI System & Resource Inventory

```
Owner:        [TBD - AIMS Lead]
Approved by:  [TBD - Managing Member]
Effective:    [TBD]
Last review:  [TBD]
Next review:  [TBD - quarterly]
Coverage:     Clause 7.1 · A.4.2 · A.4.3 · A.4.4 · A.4.5 · A.4.6 · A.10.3
```

The inventory is the source of truth for every in-scope AI system,
every supplier the LLC depends on, and every resource consumed.

## 1. AI systems

| ID | Name / location | Category | Purpose | Criticality | Owner | Model provider(s) | AIIA ref | System card |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SYS-01 | Architech: starter_ai_agents/* | Demo | Educational reference agents | Low | TBD | OpenAI, Anthropic, Google, xAI | TBD | per-app README |
| SYS-02 | Architech: advanced_ai_agents/* | Demo | Educational advanced agents | Low | TBD | mixed | TBD | per-app README |
| SYS-03 | Architech: rag_tutorials/* | Demo | RAG patterns over public corpora | Low | TBD | mixed | TBD | per-app README |
| SYS-04 | Architech: mcp_ai_agents/* | Demo | MCP integration patterns | Low | TBD | mixed | TBD | per-app README |
| SYS-05 | Architech: voice_ai_agents/* | Demo | Voice interface patterns | Low | TBD | mixed | TBD | per-app README |
| SYS-06 | Architech: advanced_llm_apps/* | Demo | Advanced LLM app patterns | Low | TBD | mixed | TBD | per-app README |
| SYS-07 | Architech: ai_agent_framework_crash_course/* | Demo | Framework training material | Low | TBD | mixed | TBD | per-app README |
| SYS-CLT-XX | TBD client system | Production | TBD | TBD | TBD | TBD | TBD | TBD |

> Each Architech subdirectory may later be broken into its own row when
> it graduates from demo to production. Criticality "Low" is justified
> by the systems being user-operated educational demos with no PII, no
> automated decisions, and no LLC-hosted endpoint.

## 2. Suppliers (A.10.3)

| ID | Vendor | Service | Contract / ToS | Risk | DPA? | Last review |
| --- | --- | --- | --- | --- | --- | --- |
| SUP-01 | OpenAI | Foundation model API | Public ToS [TBD link] | Medium | TBD | TBD |
| SUP-02 | Anthropic | Foundation model API | Public ToS [TBD link] | Medium | TBD | TBD |
| SUP-03 | Google | Gemini API | Public ToS [TBD link] | Medium | TBD | TBD |
| SUP-04 | xAI | Grok API | Public ToS [TBD link] | Medium | TBD | TBD |
| SUP-05 | Meta | Llama (open weights, self-hosted) | License [TBD] | Low | N/A | TBD |
| SUP-06 | Alibaba | Qwen (open weights, self-hosted) | License [TBD] | Low | N/A | TBD |
| SUP-07 | TBD | Vector DB (Chroma / Qdrant / Pinecone …) | TBD | TBD | TBD | TBD |
| SUP-08 | TBD | Hosting (Streamlit Cloud / self-host) | TBD | TBD | TBD | TBD |

## 3. Tooling resources (A.4.4)

| Layer | Examples in Architech |
| --- | --- |
| Agent frameworks | agno, LangChain, Phidata variants |
| App UI | Streamlit |
| Vector stores | TBD per app |
| Eval tooling | TBD (gap) |
| CI | GitHub Actions (`.github/workflows/claude.yml`) |
| Source control | Git / GitHub |

## 4. Compute & hosting resources (A.4.5)

| Use | Default boundary |
| --- | --- |
| Demo execution | End-user's machine |
| Client systems | Per engagement; documented in engagement agreement |
| Training | Not performed by LLC (foundation models only) |

## 5. Human resources (A.4.6)

| Role | Named individual | Backup |
| --- | --- | --- |
| Managing Member | TBD | — |
| AIMS Lead | TBD | TBD |
| Engineering | TBD | TBD |
| External advisor (legal/compliance) | TBD | — |

Competence records: see
[`../operations/competence-and-awareness.md`](../operations/competence-and-awareness.md).

## 6. Data resources (A.4.3)

Per-system data sources are documented in each system card under
"Data sources". The default for Architech demos is "public web /
demonstration corpora; no personal data".

## 7. Maintenance

- New systems are added on first commit that introduces them.
- Decommissioned systems retain their row with a "Retired (date)"
  status and link to the closeout AIIA.
