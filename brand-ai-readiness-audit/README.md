# Nexora AI — AI Visibility & Citation Optimization Agent

> *"This is not a one-shot SEO auditor. Nexora AI remembers what happened to a website across audit cycles and uses that historical experience to improve future recommendations."*

Nexora AI is an autonomous **AI Visibility & Citation Optimization Agent** built for the modern AI search ecosystem (ChatGPT Search, Perplexity, Google Gemini, Claude). It audits websites for factors that prevent AI assistants from discovering, reading, trusting, and citing them, while utilizing **Hindsight** as a persistent memory and reasoning layer to track changes, measure the outcome of fixes, identify regressions, and learn what works over time.

Read-only. Nexora AI never modifies live websites.

```bash
# Run an AI visibility audit with longitudinal memory tracking
python nexora.py audit https://example.com --out ./audit
# → Generates audit/report.json & audit/report.md with historical comparison
```

---

## 1. The Problem: The Stateless Auditor Trap

Traditional SEO tools and website auditors are **stateless**. Every audit begins from a blank slate:
- They forget that you fixed a robots.txt restriction last week.
- They cannot tell if an issue has persisted through five consecutive sprints or appeared five minutes ago.
- If a deployment accidentally reverts a structured data template, they treat it as an ordinary finding rather than a **critical regression**.
- They provide the exact same generic advice regardless of what actually moved the needle in prior cycles.

**Appearing in an AI answer is a strict dependency chain:**

```
reached  →  led around  →  read  →  understood  →  answerable  →
believed  →  trusted  →  not diluted  →  locally consistent  →  worth staying for
```

When website owners implement recommendations, they need an agent that remembers their history, verifies whether changes worked, measures score movement, and determines what to prioritize next based on longitudinal evidence.

---

## 2. The Solution: Persistent Memory with Hindsight

Nexora AI integrates **Hindsight** as its durable memory layer, enabling a continuous optimization loop:

```
        AUDIT (10 Modular Skills)
                   ↓
               FINDINGS
                   ↓
            RECOMMENDATIONS
                   ↓
         USER IMPLEMENTS FIX
                   ↓
               RE-AUDIT
                   ↓
          COMPARE (Longitudinal Diff)
                   ↓
            MEASURE OUTCOME
                   ↓
       STORE LEARNING IN HINDSIGHT (Retain)
                   ↓
   USE MEMORY IN NEXT RECOMMENDATION (Recall & Reflect)
                   ↓
              NEXT AUDIT
```

Hindsight is **not treated as simple document storage**. It directly alters agent reasoning through three core operations:

1. **RETAIN:** Ingests structured audit snapshots, user implementation events, score movements, and outcome observations into a domain-specific memory bank (e.g. `site_example_com`).
2. **RECALL:** Before initiating a re-audit, retrieves previous findings, recommendations, and logged fixes to set expectations and identify targets for verification.
3. **REFLECT:** Synthesizes higher-level reasoning over accumulated history to answer: *What changed? What worked? What remains unresolved? What regressed? What is the next highest-leverage action?*

---

## 3. High-Level Architecture

Nexora AI combines a deterministic, evidence-driven audit backbone with a longitudinal memory and reasoning system:

```
                    USER / DEVELOPER
                           │
                           ▼
                    Website URL
                           │
                           ▼
               Nexora Orchestrator
                           │
          ┌────────────────┴────────────────┐
          │                                 │
          ▼                                 ▼
   Memory Agent (Recall)             Audit Engine
   (Hindsight Memory Bank)           (Single Crawl & Extract)
          │                                 │
          │                   ┌─────────────┴─────────────┐
          │                   ▼                           ▼
          │             Crawl Access               Structured Data
          │             Render Engine              Answer Coverage
          │             Architecture               Engagement...
          │                   │                           │
          │                   └─────────────┬─────────────┘
          │                                 │
          └────────────────┬────────────────┘
                           │
                           ▼
                Historical Comparison
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
   Resolved Issues  Persistent Debt    Regressions
          │                │                │
          └────────────────┼────────────────┘
                           │
                           ▼
                    Impact Analysis
               (Non-causal Correlation)
                           │
                           ▼
             Memory-Aware Recommendations
               (Prioritize Chronic Debt)
                           │
                           ▼
                Augmented Final Report
               (report.json & report.md)
                           │
                           ▼
             Retain Outcome in Hindsight ───► Future Audits
```

---

## 4. The Preserved Multi-Skill Audit Engine

Nexora AI preserves 100% of the proven, read-only multi-skill audit engine:

| Skill | Stage | The Question It Answers |
|---|---|---|
| **`audit-orchestrator`** | 0 | Coordinates the crawl, profiles the domain, executes skills concurrently, and composes findings. |
| `crawl-access-audit` | 1 | **Can an agent reach the page?** robots.txt policy for AI bots, edge bot blocking, sitemaps, redirect chains, latency. |
| `render-extractability-audit` | 2 | **Can a machine read it?** Client-side JavaScript render gaps, app shells, iframes, facts locked in images, single quotable definitions. |
| `structured-data-audit` | 3 | **Does it declare what it is?** JSON-LD presence, valid Schema.org types, Organization entity anchors, sameAs authority links. |
| `corroboration-freshness-audit` | 4 | **Is it current and corroborated?** Staleness, undated content, expired claims, off-site identity profiles. |
| `engagement-audit` | 5 | **Does the visitor stay?** Deep-page orientation, mobile readiness, interrupting overlays, page weight, accessibility baseline. |
| `site-architecture-audit` | 6 | **Can a crawler find the rest of the site?** Dead-end pages, orphan sitemap URLs, internal links to redirecting URLs. |
| `answer-coverage-audit` | 7 | **Does an answer actually exist?** Question-shaped headings, direct answers, comparison tables, objection handling. |
| `trust-legitimacy-audit` | 8 | **Are facts accountable?** HSTS enforcement, author bylines, linked privacy/terms pages, disclosed business registration. |
| `duplicate-canonicalization-audit` | 9 | **Is authority diluted?** Duplicate titles across distinct URLs, near-duplicate body text, uncanonicalized parameters. |
| `local-presence-audit` | 10 | **For local businesses, is it consistent?** Name, address, phone (NAP) consistency, opening hours in schema, map links. |

### Core Audit Principles Preserved:
- **Evidence-driven:** Every finding includes exact observed numbers, HTTP status codes, or quoted HTML strings.
- **Zero false positives:** Checks are strictly gated on the site profile (e.g., an ecommerce store is never checked for local business hours).
- **Read-only & safe:** GET requests only, respects robots.txt, 1-second politeness delays, denylists on sensitive endpoints (cart, login, checkout).

---

## 5. What Hindsight Adds: Longitudinal Intelligence

### A. Stable Website Identity
URLs are normalized (`https://www.example.com/` and `http://example.com` map to domain `example.com`), creating a durable Hindsight memory bank (`site_example_com`).

### B. Accurate Longitudinal Categorization
Upon re-audit, Nexora AI deterministically categorizes every finding:
1. **Resolved Issues:** Detected in prior audit, no longer present on the sampled pages.
2. **Persistent Issues:** Present in prior audit and still present now. Tracks consecutive cycle counts (e.g. *Present across 3 cycles*).
3. **New Issues:** Freshly introduced defects not present previously.
4. **Regressions:** Issues that were resolved in an earlier audit but have now reappeared.
5. **Score & Metric Deltas:** AI Discoverability and Engagement score deltas (`+21`, `-12`).

### C. Non-Causal Impact Analysis
The agent correlates resolved issues with score improvements without making unsupported causal leaps:
- *"Following confirmed user implementation, the resolution of 'robots.txt blocks AI' (CA-AI-RETRIEVAL-BLOCKED) coincided with an increase of 21 points in AI Discoverability (51 → 72)."*

### D. Memory-Aware Recommendations
Recommendations dynamically adapt based on historical memory:
- **Chronic Debt Elevation:** If an issue like canonical duplication has remained unresolved across multiple audits while foundational issues were resolved, the agent elevates its priority:
  > *"Prioritize `DC-DUPLICATE-TITLE-OR-DESCRIPTION`: It has remained unresolved across 2 audit cycles, while foundational crawlability issues were fixed. Resolving canonicalization now unifies citation weight."*
- **Regression Alerts:** Regressed findings receive urgent priority to protect prior gains.
- **Implementation Verification:** Distinguishes between user-confirmed fixes and observed outcomes. If a user logged a fix but the defect is still detected, the agent flags an implementation discrepancy.

---

## 6. Installation & Setup

### Prerequisites
- Python 3.10+ (Standard library only for core engine; `hindsight-client` for persistent memory)

### Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/aditya/cite-trail-ai-agent.git
cd cite-trail-ai-agent

# Install Hindsight client
pip install hindsight-client
```

### Environment Configuration
Copy the sample environment file:

```bash
cp .env.example .env
```

Configure your `.env` file:
```ini
# Option 1: Managed Hindsight Cloud
HINDSIGHT_BASE_URL=https://api.hindsight.vectorize.io
HINDSIGHT_API_KEY=your_api_key_here

# Option 2: Self-hosted Hindsight (Docker)
# HINDSIGHT_BASE_URL=http://localhost:8888
```

> **Note on Graceful Degradation:** If Hindsight credentials are not set or the server is temporarily offline, Nexora AI automatically operates using a local structured snapshot cache in `.nexora/`. Audits and comparisons continue to function with zero data loss.

---

## 7. CLI Usage

### 1. Run an AI Visibility Audit
```bash
python nexora.py audit https://example.com --out ./audit
```
*Options:* `--max-pages 30`, `--delay 1.0`, `--budget 210`, `--render auto|off`, `--no-history`, `--quiet`.

### 2. View Longitudinal History & Reflection
Inspect all past audits, score trajectories, and Hindsight reflections for a domain:
```bash
python nexora.py history https://example.com
```

### 3. Record a User-Confirmed Fix
Log that your engineering team deployed a fix for a specific finding:
```bash
python nexora.py record-fix https://example.com \
    --fix CA-AI-RETRIEVAL-BLOCKED \
    --notes "Allowed OAI-SearchBot and Claude-SearchBot in robots.txt"
```

### 4. Compare Two Existing Audits
Directly compare two audit report directories without re-crawling:
```bash
python nexora.py compare --audit1 ./audit_cycle1 --audit2 ./audit_cycle2
```

### 5. Run the Interactive Hackathon Demo
Experience the full 3-cycle learning, resolution, and regression workflow in seconds:
```bash
python nexora.py demo
```

---

## 8. Backward Compatibility

Nexora AI maintains 100% backward compatibility with the original orchestrator CLI:

```bash
python skills/audit-orchestrator/scripts/run_audit.py https://example.com --out ./audit
```

Existing pipelines and scripts run without modification. The orchestrator automatically enriches reports with `historical_context` while preserving all original keys in `report.json` and `report.md`.

---

## 9. Testing & Quality Assurance

Nexora AI includes comprehensive unit and integration tests covering all critical scenarios:

```bash
# Run structural marketplace & script compilation checks
python tests/validate-marketplace.py

# Run the 27-defect seeded fixture site self-test
python tests/run_selftest.py

# Run Nexora AI scenario test suite (Scenarios A through G)
python -m unittest tests/test_nexora.py
```

### Tested Scenarios:
- **Scenario A:** First audit baseline (no prior history, no fabricated diffs).
- **Scenario B:** Resolved issue detection and evidence retirement.
- **Scenario C:** Persistent issue recurrence tracking across consecutive cycles.
- **Scenario D:** Newly introduced defect detection.
- **Scenario E:** Regression detection across a 3-audit sequence.
- **Scenario F:** Numeric score delta calculation with non-causal language.
- **Scenario G:** Distinct tracking of user-confirmed implementations vs observed crawler evidence.

---

## 10. Repository Structure

```
cite-trail-ai-agent/
├── marketplace.json              # Agent skill marketplace manifest
├── README.md                     # Comprehensive project documentation
├── DEMO.md                       # Hackathon live showcase guide
├── LICENSE                       # MIT License
├── nexora.py                  # Primary Nexora AI CLI entrypoint
├── .env.example                  # Environment configuration template
│
├── nexora/                    # Nexora AI Longitudinal Intelligence Package
│   ├── identity.py               # Domain normalization and Hindsight bank_id derivation
│   ├── models.py                 # Snapshots, comparison models, and event schemas
│   ├── orchestrator.py           # Master workflow orchestrator
│   ├── demo.py                   # Multi-cycle interactive hackathon demonstration
│   ├── memory/                   # Hindsight persistent memory layer
│   │   ├── hindsight_client.py   # Official hindsight-client wrapper & offline cache
│   │   └── agent.py              # MemoryAgent: pre-audit recall & post-audit retain
│   ├── analysis/                 # Longitudinal comparison engine
│   │   ├── comparison.py         # ComparisonAgent: diffing, resolved, persistent, regressions
│   │   └── impact.py             # ImpactAnalyzer: score correlations & learned patterns
│   ├── recommendations/          # Memory-aware recommendation engine
│   │   └── agent.py              # RecommendationAgent: priority adaptation
│   └── reporting/                # Report serializers
│       └── historical_report.py  # Markdown generator with longitudinal scoreboard
│
├── skills/                       # 11 Modular Audit Skills
│   ├── audit-orchestrator/       # Entrypoint skill (crawl, profile, compose)
│   ├── crawl-access-audit/       # Stage 1: Bot accessibility & robots.txt
│   ├── render-extractability-audit/ # Stage 2: JS rendering & fact extraction
│   ├── structured-data-audit/    # Stage 3: Schema.org JSON-LD & entity anchors
│   ├── corroboration-freshness-audit/ # Stage 4: Freshness & off-site corroboration
│   ├── engagement-audit/         # Stage 5: Deep-page orientation & UX
│   ├── site-architecture-audit/  # Stage 6: Link graphs & orphaned URLs
│   ├── answer-coverage-audit/    # Stage 7: Question headings & direct answers
│   ├── trust-legitimacy-audit/   # Stage 8: Authorship & legal disclosures
│   ├── duplicate-canonicalization-audit/ # Stage 9: Canonical tags & content dilution
│   └── local-presence-audit/     # Stage 10: Local business NAP & hours
│
└── tests/                        # Verification & Test Suites
    ├── fixture-site/             # Broken fixture site with 27 seeded defects
    ├── run_selftest.py           # Cross-platform runner asserting 27/27 defect detection
    ├── test_nexora.py         # Scenario unit tests (Scenarios A through G)
    └── validate-marketplace.py   # Manifest and skill frontmatter validation
```

---

## 11. Safety & Ethical Commitments

- **Read-Only:** Nexora AI never executes write operations, modifies DNS, submits forms, or interacts with authenticated surfaces.
- **Polite Crawling:** Maximum 1 request per second, strictly honors `Crawl-delay` up to 5s, caps crawling depth, and denylists administrative and transaction paths.
- **Evidence Over Inference:** Historical memory provides context, not proof. If current crawl evidence shows a defect is resolved, current evidence immediately overrides past memory.
