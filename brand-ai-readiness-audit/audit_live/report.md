# AI-readiness audit — allbirds.com

*2026-09-26T06:38:22Z · ecommerce site · 5 pages sampled*

**No hard blockers; the largest problem is F-001: Product markup is missing required properties**

| | |
|---|---|
| AI discoverability score | **39/100** |
| On-site engagement score | **80/100** |
| Findings | 13 (0 critical, 3 high, 6 medium, 4 low) |

## Findings

### F-001 · HIGH — Product markup is missing required properties

- **Category:** discoverability · **Confidence:** high · **Source check:** `SD-INCOMPLETE-PRODUCT`
- **Evidence:** 108 Product node(s) lack name, offers. Example: https://www.allbirds.com/products/mens-wool-runners (missing name, offers).
- **Why it matters:** An incomplete node is often treated as invalid and dropped, which is worse than having no markup: the page appears marked up while providing nothing extractable.
- **Fix (low effort, high priority):** Populate name, offers on every Product node.
- **Verify:** Validate a page of each template and confirm zero required-property errors.
- **Affected:** https://www.allbirds.com/products/mens-wool-runners

### F-002 · HIGH — The site links to no independent profile that could corroborate it

- **Category:** discoverability · **Confidence:** high · **Source check:** `CF-NO-OFFSITE-ANCHORS`
- **Evidence:** 60 external links found across 5 pages, none pointing to an identity or review source (Wikipedia/Wikidata, LinkedIn company page, Crunchbase, GitHub, G2, Trustpilot, Google Maps, a registry).
- **Why it matters:** A claim that appears in exactly one place on the internet is fragile. Machines weight a fact by how many independent sources repeat it, so a brand described only by its own website has nothing reinforcing what it says about itself.
- **Fix (medium effort, high priority):** Create and link the brand's authoritative profiles — at minimum a LinkedIn company page, a Google Business Profile if there is a physical location, an industry directory or review listing, and a Wikidata item — then reference them from sameAs.
- **How:** This is the on-site half of the signal only. The off-site protocol in references/offsite-protocol.md checks whether those profiles exist, are current, and agree with the site.
- **Affected:** https://allbirds.com/

### F-003 · HIGH — No Organization node identifies the brand

- **Category:** discoverability · **Confidence:** high · **Source check:** `SD-NO-ORGANIZATION`
- **Evidence:** 162 JSON-LD node(s) across 5 crawled pages declare types (aggregaterating, brand, offer, product, productgroup), but none is an Organization or LocalBusiness.
- **Why it matters:** Page-level types describe individual pages. Only an Organization node says who publishes them, which is what links every page to one brand entity.
- **Fix (medium effort, high priority):** Add an Organization node to the site-wide template with name, url, logo, description and sameAs.
- **Affected:** https://allbirds.com/

### F-004 · MEDIUM — Several render-blocking scripts sit in the document head

- **Category:** engagement · **Confidence:** high · **Source check:** `EN-RENDER-BLOCKING`
- **Evidence:** Median of 16 scripts per page load synchronously without async or defer.
- **Why it matters:** Each synchronous script pauses parsing, so the visitor stares at a blank screen while code they did not ask for downloads and executes.
- **Fix (low effort, medium priority):** Add defer (or async where order does not matter) to every script that is not needed for first paint.
- **Affected:** https://allbirds.com/, https://www.allbirds.com/agents.md, https://www.allbirds.com/products/mens-wool-runners, https://www.allbirds.com/products/mens-wool-runners-natural-white, https://www.allbirds.com/products/womens-wool-runners-natural-black

### F-005 · MEDIUM — Deep pages carry no BreadcrumbList markup

- **Category:** both · **Confidence:** high · **Source check:** `SD-NO-BREADCRUMBS`
- **Evidence:** 3 crawled pages are three or more levels deep (e.g. https://www.allbirds.com/products/mens-wool-runners) and no BreadcrumbList node was found.
- **Why it matters:** Breadcrumbs tell a machine where a page sits in the site and tell a visitor arriving from an AI answer what the surrounding context is. Assistants send people to deep pages, not homepages, so this is the cheapest fix that helps both extraction and orientation.
- **Fix (low effort, medium priority):** Add BreadcrumbList markup, and render matching visible breadcrumbs, on every page below the top level.
- **Affected:** https://www.allbirds.com/products/mens-wool-runners, https://www.allbirds.com/products/mens-wool-runners-natural-white, https://www.allbirds.com/products/womens-wool-runners-natural-black

### F-006 · MEDIUM — JSON-LD blocks omit @context

- **Category:** discoverability · **Confidence:** high · **Source check:** `SD-NO-CONTEXT`
- **Evidence:** 3 page(s) have a JSON-LD block with no @context, e.g. https://www.allbirds.com/products/mens-wool-runners.
- **Why it matters:** Without @context the types are undefined names rather than schema.org terms, and the whole block is ignored.
- **Fix (low effort, medium priority):** Add "@context": "https://schema.org" to the top of each block.
- **Affected:** https://www.allbirds.com/products/mens-wool-runners, https://www.allbirds.com/products/mens-wool-runners-natural-white, https://www.allbirds.com/products/womens-wool-runners-natural-black

### F-007 · MEDIUM — Pages are heavy before any media is counted

- **Category:** engagement · **Confidence:** high · **Source check:** `EN-PAGE-WEIGHT`
- **Evidence:** Median HTML document is 738 KB with 26 external scripts and 16 render-blocking scripts per page, across 5 pages. (HTML and resource counts only; images and fonts are additional.)
- **Why it matters:** Cited traffic skews mobile and impatient — the visitor did not choose this site, an assistant suggested it. Every second before the answer appears is spent on a page they have no prior commitment to.
- **Fix (medium effort, medium priority):** Cut third-party scripts to the ones with a named owner and a measured purpose, defer everything non-critical, and split oversized HTML documents.
- **How:** Audit tag-manager containers first; they are usually where script count grows without anyone deciding it should.
- **Verify:** Re-measure document size and script count after the cull.
- **Affected:** https://www.allbirds.com/products/womens-wool-runners-natural-black, https://www.allbirds.com/products/mens-wool-runners-natural-white, https://www.allbirds.com/products/mens-wool-runners

### F-008 · MEDIUM — Two or more URLs carry near-identical body text

- **Category:** discoverability · **Confidence:** medium · **Source check:** `DC-NEAR-DUPLICATE-PAGES`
- **Evidence:** 3 page pair(s) share 85%+ word-stem overlap, e.g. https://www.allbirds.com/products/mens-wool-runners and https://www.allbirds.com/products/mens-wool-runners-natural-white (100% overlap), with no canonical relating them.
- **Why it matters:** Two URLs with the same content compete against each other for the same query, splitting the corroboration and link signal that would otherwise accumulate on one page — the opposite of what makes a page citable.
- **Fix (low effort, medium priority):** Pick one canonical URL per distinct piece of content and either rel=canonical or 301-redirect the others to it; if both must stay live (e.g. two locales), differentiate them or declare hreflang instead.
- **Affected:** https://www.allbirds.com/products/mens-wool-runners, https://www.allbirds.com/products/mens-wool-runners-natural-white

### F-009 · MEDIUM — No registered business or charity identity is disclosed anywhere

- **Category:** both · **Confidence:** medium · **Source check:** `TL-NO-BUSINESS-IDENTITY-DISCLOSED`
- **Evidence:** No company registration number, VAT/tax ID, registered address or charity registration was found in text across 5 crawled pages.
- **Why it matters:** For a site that takes payment or donations, this disclosure is what lets a buyer or donor verify who they are actually dealing with. Its absence is a concrete, checkable legitimacy gap distinct from general off-site corroboration.
- **Fix (low effort, medium priority):** Disclose the legal entity name, registration number and registered address (or charity registration number) in the footer or an About/Legal page.
- **Affected:** https://allbirds.com/

### F-010 · LOW — Basic accessibility attributes are missing

- **Category:** both · **Confidence:** high · **Source check:** `EN-ACCESSIBILITY-BASELINE`
- **Evidence:** 4 form field(s) have no label, aria-label or id to bind a label to (across 5 crawled pages).
- **Why it matters:** These attributes are what both assistive technology and text extractors rely on to know what an element is. Missing them excludes real users and leaves machine readers guessing at the same time.
- **Fix (low effort, low priority):** Fix the mechanical basics: a lang attribute on <html>, a bound label for every form field, and text or an aria-label on every link.
- **How:** This is a floor, not an accessibility audit: passing these checks does not make the site conformant, but failing them guarantees it is not.
- **Affected:** https://allbirds.com/, https://www.allbirds.com/agents.md, https://www.allbirds.com/products/mens-wool-runners, https://www.allbirds.com/products/mens-wool-runners-natural-white, https://www.allbirds.com/products/womens-wool-runners-natural-black

### F-011 · LOW — Pages declare several competing H1 headings

- **Category:** discoverability · **Confidence:** high · **Source check:** `RX-MULTIPLE-H1`
- **Evidence:** 3 pages have more than two <h1> elements, e.g. https://www.allbirds.com/products/mens-wool-runners has 3.
- **Why it matters:** Several H1s leave no single statement of the page's subject, so the extracted topic is diluted.
- **Fix (low effort, low priority):** Keep one H1 per page and demote the rest to H2/H3 in reading order.
- **Affected:** https://www.allbirds.com/products/mens-wool-runners, https://www.allbirds.com/products/mens-wool-runners-natural-white, https://www.allbirds.com/products/womens-wool-runners-natural-black

### F-012 · LOW — No WebSite node declares the site's name

- **Category:** discoverability · **Confidence:** high · **Source check:** `SD-NO-WEBSITE-NODE`
- **Evidence:** Structured data present but no WebSite node found across 5 pages.
- **Why it matters:** The WebSite node is what supplies the site's display name and links the domain to the brand entity, rather than leaving it inferred from the URL.
- **Fix (low effort, low priority):** Add a WebSite node with name, url and (if the site has search) a potentialAction/SearchAction.
- **Affected:** https://allbirds.com/

### F-013 · LOW — Internal links point at URLs that redirect instead of the final URL

- **Category:** discoverability · **Confidence:** high · **Source check:** `SA-INTERNAL-LINKS-TO-REDIRECTING-URLS`
- **Evidence:** 9 internal link(s) target a URL that redirects during this crawl, e.g. https://www.allbirds.com/products/mens-wool-runners links to https://www.allbirds.com/.
- **Why it matters:** Every redirect hop is a request some fetchers do not follow and latency all of them pay. Internal links are entirely within the site's control, so this is pure waste rather than an unavoidable consequence of an external change.
- **Fix (medium effort, low priority):** Update internal links to point directly at the final destination URL.
- **Affected:** https://www.allbirds.com/

## Fix in this order

**Navigable** — A crawler that got in must also be able to find the site's other pages; a dead end or an orphaned URL is invisible even though the entry point works.

- `F-013` (low, medium effort) Update internal links to point directly at the final destination URL.

**Readable** — The facts must exist in the served HTML, as text.

- `F-011` (low, low effort) Keep one H1 per page and demote the rest to H2/H3 in reading order.

**Unambiguous** — The page must state what it is and who the brand is, explicitly.

- `F-001` (high, low effort) Populate name, offers on every Product node.
- `F-003` (high, medium effort) Add an Organization node to the site-wide template with name, url, logo, description and sameAs.
- `F-005` (medium, low effort) Add BreadcrumbList markup, and render matching visible breadcrumbs, on every page below the top level.
- `F-006` (medium, low effort) Add "@context": "https://schema.org" to the top of each block.
- `F-012` (low, low effort) Add a WebSite node with name, url and (if the site has search) a potentialAction/SearchAction.

**Corroborated** — The facts must be current and repeated by independent sources.

- `F-002` (high, medium effort) Create and link the brand's authoritative profiles — at minimum a LinkedIn company page, a Google Business Profile if there is a physical location, an industry directory or review listing, and a Wikidata item — then reference them from sameAs.

**Trustworthy** — Corroboration shows independent sources repeat the facts; trust signals show the facts come from an identifiable, accountable source in the first place.

- `F-009` (medium, low effort) Disclose the legal entity name, registration number and registered address (or charity registration number) in the footer or an About/Legal page.

**Not diluted** — Even a corroborated, trustworthy fact can be split across near-duplicate URLs so that none of them accumulates enough weight to be the one cited.

- `F-008` (medium, low effort) Pick one canonical URL per distinct piece of content and either rel=canonical or 301-redirect the others to it; if both must stay live (e.g. two locales), differentiate them or declare hreflang instead.

**Worth staying for** — The visitor the citation delivers must find the answer and a reason to continue.

- `F-004` (medium, low effort) Add defer (or async where order does not matter) to every script that is not needed for first paint.
- `F-007` (medium, medium effort) Cut third-party scripts to the ones with a named owner and a measured purpose, defer everything non-critical, and split oversized HTML documents.
- `F-010` (low, low effort) Fix the mechanical basics: a lang attribute on <html>, a bound label for every form field, and text or an aria-label on every link.

## Worth doing even with no defect found

**Publish an answer-shaped FAQ on the questions sales actually gets**  
Collect the questions prospects ask, publish each as a heading with a direct two-sentence answer immediately beneath it, and mark the block up as FAQPage. Question-shaped headings with short literal answers are the structure assistants quote most readily, because they match the shape of what was asked.

**Keep one canonical description and use it verbatim everywhere**  
Write one sentence — '<brand> is a <category> that <does what> for <whom>' — and use it unchanged in the meta description, the Organization schema, the About page, and every third-party profile. Repetition across independent sources is what makes a description the one a model returns.

**Give each important question its own URL**  
One page per question the brand should own, titled as the question, answering it in the first paragraph. A page that answers one thing precisely gets cited for it; a page that covers ten things gets cited for none.

**Mark up availability, shipping and returns, not just price**  
Add availability, shippingDetails and hasMerchantReturnPolicy to Offer nodes. 'Is it in stock, when does it arrive, can I send it back' are the questions that decide a purchase, and they are the ones assistants are asked to compare across retailers.

**Publish specifications as text tables on every product page**  
A real HTML table of dimensions, materials, compatibility and model numbers makes the product matchable against a specific query. Specification sheets in images or PDFs cannot be compared against anything.

**Publish one original, dated, methodologically-stated data asset a year in the brand's domain — a benchmark, a survey of its customers, a pricing or market breakdown — with a stable URL and reusable figures.**  
Corroboration cannot be bought, but it can be earned: original numbers get quoted and linked by other sites, and those independent repetitions are exactly the signal that makes a brand's facts trusted and repeated back.

## What this audit could not check
- No headless browser was available (playwright not installed), so JavaScript-render gaps were inferred from the served HTML. Findings that depend on rendering are marked confidence 'medium'.
- Off-site corroboration (independent sources, entity collisions, what assistants currently say about the brand) was not verified with live search; only the on-site half of those signals was assessed.
- 5 page(s) were crawled (1×home, 1×other, 3×product). Findings describe the sampled pages; a finding reported on a sample of one template usually applies to every page built from it.

## Checks deliberately not fired

These were evaluated and found not to apply — recorded so the report can be trusted to have looked.

- `CA-AI-TRAINING-BLOCKED` — no training-crawler blocks present in robots.txt
- `CA-EDGE-BOT-BLOCK` — a self-identifying non-browser request received the same status as a browser request
- `CA-CANONICAL-MISSING` — every crawled page declares a canonical
- `CA-SLOW-RESPONSES` — median response time 616 ms is within budget
- `RX-CLIENT-RENDERED-SHELL` — served HTML already contains substantial text on every page
- `RX-NO-QUOTABLE-DEFINITION` — homepage states the organisation's category in extractable text
- `SD-CONTRADICTS-PAGE` — no price or name mismatches detected between markup and page text
- `SD-FAQ-OPPORTUNITY` — no page carries three or more question-shaped headings
- `CF-NAME-AMBIGUITY-RISK` — distinctive name or registry-grade identity links already present
- `EN-NO-ARRIVAL-ORIENTATION` — interior pages carry breadcrumbs or name the brand up front
- `EN-NO-VIEWPORT-META` — all pages declare a viewport
- `SA-DEAD-END-PAGES` — 3 of 4 interior pages carry onward links
- `SA-ORPHAN-SITEMAP-URLS` — sitemap declares 499 URLs against only 5 crawled pages — too large a gap for a shallow sample to reliably judge orphaning; a fuller crawl (--max-pages) is needed to check this
- `SA-PAGES-MISSING-FROM-SITEMAP` — crawled pages are declared in the sitemap
- `AQ-NO-QUESTION-CONTENT` — 4 page(s) carry question-shaped headings or FAQ/HowTo structured data exists
- `AQ-THIN-ANSWER-PAGE` — pages with question-shaped headings carry a substantive amount of text per question
- `AQ-NO-COMPARISON-CONTENT` — comparison-shaped content already exists
- `AQ-NO-OBJECTION-HANDLING` — objection-handling content (refunds, guarantees, security) already exists
- `TL-NO-HSTS` — HSTS is present
- `TL-NO-AUTHOR-BYLINE` — fewer than 2 article/blog pages were crawled
- `TL-NO-LEGAL-PAGES-LINKED` — a privacy/terms/legal link or page was found
- `DC-DUPLICATE-TITLE-OR-DESCRIPTION` — no two distinct, non-canonicalised URLs share an identical title
- `DC-PARAM-VARIANT-NOT-CANONICALIZED` — no crawled URL carried query parameters
- `LP-NAP-INCONSISTENT` — site classified as ecommerce, not local_business; NAP and map checks assume a physical, address-bound business
- `LP-HOURS-NOT-IN-SCHEMA` — site classified as ecommerce, not local_business; NAP and map checks assume a physical, address-bound business
- `LP-NO-MAP-EMBED-OR-LINK` — site classified as ecommerce, not local_business; NAP and map checks assume a physical, address-bound business