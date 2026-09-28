# Nexora AI — Hackathon Demo Guide

> *"Without memory, this is an audit. With memory, it becomes an optimization agent."*

This guide walks through the live demonstration of **Nexora AI** — an AI Visibility & Citation Optimization Agent powered by **Hindsight** persistent memory.

---

## 🎯 What the Demo Proves

Traditional SEO auditors are stateless: every audit begins from zero, forgets past fixes, repeats obsolete recommendations, and cannot detect regressions.

Nexora AI solves this by turning auditing into a **continuous learning loop**:
1. It **remembers** previous audits, findings, and recommendations.
2. It tracks **fixes confirmed by the website owner**.
3. It **verifies** whether implemented fixes actually resolved the underlying barrier upon re-audit.
4. It **detects regressions** when previously fixed defects reappear.
5. It uses historical experience to **prioritize the next highest-leverage action**.

---

## ⚡ Quick Demo Execution

Run the complete multi-cycle demonstration with a single command:

```bash
python nexora.py demo
```

This runs three simulated audit cycles against `example.com`:

```
======================================================================
NEXORA AI — AI VISIBILITY & CITATION OPTIMIZATION AGENT
Hackathon Demo: Persistent Memory & Learning Across Audit Cycles
Target Site: example.com | Memory Bank: site_example_com
======================================================================
```

---

## 📖 The 5-Step Demo Storyline

### Step 1: The Baseline Audit (Audit #1)
The agent checks Hindsight for prior knowledge of `example.com`. Finding none, it executes the multi-skill audit engine to establish a baseline:

* **AI Discoverability Score:** `51/100`
* **Defects Detected (4):**
  - `CA-AI-RETRIEVAL-BLOCKED` *(Critical)*: robots.txt blocks AI search fetchers (OAI-SearchBot, Claude-SearchBot).
  - `SD-NO-ORGANIZATION` *(High)*: Missing Organization JSON-LD with entity anchors.
  - `DC-DUPLICATE-TITLE-OR-DESCRIPTION` *(High)*: Title duplicates splitting authority across URLs.
  - `AQ-NO-QUESTION-CONTENT` *(Medium)*: No question-shaped content for assistant quote matching.
* **Hindsight Action:** The baseline snapshot is retained into memory bank `site_example_com`.

### Step 2: The User Implements Fixes
The website owner resolves the top two foundational barriers and logs them with the agent:

```bash
python nexora.py record-fix https://example.com --fix CA-AI-RETRIEVAL-BLOCKED --notes "Allowed AI retrieval bots in robots.txt"
python nexora.py record-fix https://example.com --fix SD-NO-ORGANIZATION --notes "Added Organization schema with sameAs Wikidata anchors"
```

* **Hindsight Action:** User-confirmed implementation events are stored distinctly from observed state, creating an expectation for verification on future audits.

### Step 3: Re-Audit & Impact Measurement (Audit #2)
The user triggers a re-audit. The agent recalls historical snapshots and user implementation events before analyzing the site:

```bash
python nexora.py audit https://example.com --out ./audit_cycle2
```

* **Score Jump:** `51 → 72` (**+21 points! 🟢**)
* **Verified Resolved:**
  - ✅ `CA-AI-RETRIEVAL-BLOCKED` (Confirmed & Verified)
  - ✅ `SD-NO-ORGANIZATION` (Confirmed & Verified)
* **Persistent Issues:**
  - ⏳ `DC-DUPLICATE-TITLE-OR-DESCRIPTION` (Present in 2 consecutive cycles)
  - ⏳ `AQ-NO-QUESTION-CONTENT` (Present in 2 consecutive cycles)

### Step 4: The Agent Reasons Over Memory
**Judge's Question:** *"Why is canonicalization the next priority?"*

**Nexora AI's Memory-Driven Answer:**
> *"Prioritize `DC-DUPLICATE-TITLE-OR-DESCRIPTION`: It has remained unresolved across 2 audit cycles, while 2 foundational defects (crawl access and Organization schema) were successfully resolved, resulting in a +21 point gain. Resolving canonicalization now unifies ranking signals onto authoritative URLs."*

This demonstrates true learning: recommendations are not static check lists, but dynamically adapt based on historical outcomes and persistence debt.

### Step 5: Regression Detection (Audit #3)
Later, a developer accidentally overwrites `robots.txt` during a deployment. Nexora AI audits the site again:

* **Score Movement:** `72 → 60` (**-12 points! 🔴**)
* **Regression Alert:**
  - 🚨 `CA-AI-RETRIEVAL-BLOCKED` [REGRESSION]
  - *History: Previously resolved in Audit #2, but has returned in Audit #3.*
* **Elevated Priority:**
  - *"Urgent Priority: Address regression in `CA-AI-RETRIEVAL-BLOCKED`. This defect was previously resolved but has returned, threatening prior citation gains."*

---

## 🔍 Interactive CLI Verification

You can inspect the longitudinal memory of any site at any time:

```bash
# View complete historical memory timeline
python nexora.py history https://example.com

# Compare any two audit report directories
python nexora.py compare --audit1 ./audit_cycle1 --audit2 ./audit_cycle2
```
