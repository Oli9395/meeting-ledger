---
title: Competitive Analysis, Market Research, PRD, and Demo/MVP Validation Methods — A Collection of Execution-Layer Skills and Templates
status: draft
sources_count: 62
evidence_note: First-round file. The body does not label each item as [Fact] or [Summary], and sources do not each record an access date (all are treated as at the time of writing). Any item labeled [Fact] whose body has no record of "opened the original page" should be treated as [Summary · to be verified] before being cited (note added in the closing revision).
---

# Competitive Analysis, Market Research, PRD, and Demo/MVP Validation Methods (Template Collection)

> **What problem this file solves**: In this round of BriefPilot v2, we have to answer the question a client or interviewer will ask: "Feishu Minutes, Otter, and Fireflies all already turn meetings into tasks, so why build this?" You can't answer that with talk alone. It takes a reproducible method. First, use competitive analysis to lay out as evidence what others have and haven't done. Then use user research to find the "small spot" of unmet need. Then use a PRD to write that need up as something acceptable and testable. Finally, use a demo or experiment to show that it holds. This file organizes the methods needed at each step into **ready-to-use templates**, each with a "how to use it in this project" note.
>
> **Labeling conventions**:
> - **[Fact]**: Has a source URL, and the original page was opened and checked, or multiple sources agree.
> - **[Inference]**: Reasonably derived from facts, but no source says it directly.
> - **[Assumption]**: A judgment about BriefPilot that still needs to be validated by later research.
> - **To be verified**: The source is secondary, behind a paywall, or a vendor blog, or multiple sources contradict each other.

---

## 0. First, why do things in this order

A common failure path is to decide first "I'm going to build a meeting assistant for research labs" and then look for material to prove it's right. This is **confirmation bias**, and an interviewer can spot it at a glance. The correct order is **risk-driven**:

1. First list the project's **most important and least evidenced** assumptions (the "assumption map" approach from Product Talk and the book *Testing Business Ideas*: two axes, importance × amount of evidence, with the upper-right corner tested first) [Fact: Product Talk article dated 2023-10-18, citing *Testing Business Ideas*] (https://www.producttalk.org/2021/08/assumption-testing/).
2. For assumptions of the form "existing products already meet this need," use **competitive analysis + review mining** to refute or confirm them (desk research, the lowest cost).
3. For assumptions of the form "target users really have this pain point and are currently solving it with clumsy workarounds," validate with **interviews / switch interviews** (the Mom Test rules keep users from being polite).
4. Only once both kinds of evidence exist should you write the PRD's "problem statement" and "non-goals." Otherwise the PRD is all HYPOTHETICAL (the existing BriefPilot PRD v0.1 is in exactly this state; see the earlier v1 docs (not included), PRD §1.3–§2.1).
5. The demo shows only **the one magic moment that differentiates the product**, not a walkthrough of every feature (a well-known investor essay advises: "don't walk through every feature in screen order; explain the problem first, then how the product solves it") [Fact] (https://paulgraham.com/investors.html).

**[Inference]** For BriefPilot, whether the "research lab" niche holds up depends on whether steps 2 and 3 can produce two kinds of evidence: (a) the reviews, pricing, and feature matrices of mainstream meeting assistants really do leave some specific link in the lab scenario uncovered; (b) lab-member interviews can recount specific, recent events that were handled with clumsy workarounds. If either is missing, don't draw a conclusion.

---

## 1. Competitive analysis: frameworks, templates, sources

### 1.1 Set the purpose first, then choose dimensions (why a template can be "worthless")

A widely cited article on Everyone Is a Product Manager (2019-01-15) points out that competitive reports that fill in a template and pile up information are "like eight-legged essays." The commonly used five-elements-of-user-experience method has two weaknesses: it is **superficial** (it sees the features but not the driving causes behind them) and **lagging** (it can only analyze after the opponent has moved). The author recommends first answering "where is the competitor's core advantage, what are the main influencing factors, and does the analysis focus on differences, competitive relationships, or trends," and only then choosing a method. The report must have a conclusion, and the conclusion has two parts: "a judgment on the competitor" and "feasibility suggestions for ourselves." Subjective judgments should be grounded in facts and verifiable over time, and when unsure, give a range or a likelihood rather than forcing a conclusion [Fact] (https://www.woshipm.com/evaluating/1833499.html).

**How to use it in this project**: Our purpose is very clear: **find unmet needs**, not write a "Feishu Minutes vs Otter comprehensive comparison." So the dimensions should center on each step of the "meeting → task" chain: who does it, how well, and what users complain about, rather than on UI color schemes.

### 1.2 Overview of common frameworks (what each is suited for)

| Framework | What it answers | Suitable stage | Source / credibility |
|---|---|---|---|
| **Feature Matrix** | Who has it / who doesn't / how well it's done | Finding feature gaps | Common practice: our product + 3–5 direct competitors, scored Full/Partial/Missing or ✔/Partial/✘. Looking only at features misses positioning and pricing, which is a recognized pitfall [Fact, multiple sources agree, mostly template/skill pages] |
| **Five elements of user experience** (strategy / scope / structure / skeleton / surface) | Layer-by-layer view of a competitor's positioning → features → interaction → visuals | Product teardown | The mainstream approach in Chinese PM communities, but each layer must be broken down into executable dimensions, and its superficiality/lag should be kept in mind [Fact] (https://www.woshipm.com/user-research/5867375.html, https://www.woshipm.com/evaluating/1833499.html) |
| **Business Model Canvas / Lean Canvas** | How competitors make money and how they defend it | Judging "why don't they do this" | The Lean Canvas replaces 4 boxes of the BMC with Problem / Solution / Key Metrics / **Unfair Advantage** (an advantage that can't easily be copied or bought) [Fact] (https://www.emergn.com/insights/business-model-canvas-lean-canvas/, https://leanspark.leanstack.com/learn/why-lean-canvas-versus-business-model-canvas/) |
| **Pricing comparison** | Value metric, tiers, upgrade triggers | Judging competitors' target customers and our entry price point | Practice: normalize everything to per person per month; record monthly vs annual billing; record the **date** (pricing pages change without notice); check historical Wayback versions; docs and changelogs often hide features available only in higher-tier plans [Fact] (https://cotera.co/articles/how-to-find-competitor-pricing, https://www.getmonetizely.com/articles/how-to-benchmark-your-saas-pricing-against-competitors-a-strategic-guide) |
| **Review Mining** | What existing users hate most | The **most direct source** for the "small spot" of unmet need | See §1.4 |
| **Positioning map (2×2)** | Where the market gaps are | For presentations | The axes must be meaningful (e.g., "self-serve vs sales-driven") rather than "expensive vs cheap" [Fact, template page] |
| **Trend-forecasting timeline** | What competitors will do next | Guarding against "I build it, and a month later they ship it too" | Five steps: collect inflection points / major events → build a timeline → find the persistent driving "causes" → derive effects from causes → observe and verify [Fact] (https://www.woshipm.com/evaluating/1833499.html) |
### 1.3 Desktop Research Source List (Categorized by "What Question It Can Answer")

| Source | What it can answer | How to use it | Caveats |
|---|---|---|---|
| **G2 / Capterra / TrustRadius** | Dissatisfaction among existing users | Filter 1–2 star (or 2–3 star) reviews, read the "What do you dislike" field, code by theme, **copy the original wording rather than summaries**; read at least 10 per competitor [Fact] (https://bigideasdb.com/docs/g2-review-analysis, https://leadhaste.com/prompts/claygent-g2-review-pain-quote-mining) | Many dislike fields are empty or say "nothing to dislike", so the signal is thinner than expected; G2's rating algorithm is controversial [Fact] (https://www.g2.com/products/g2/reviews?page=2) |
| **App Store / Google Play reviews** | Mobile pain points | Low-star filtering + rule-based/manual classification; ratings are only a triage signal, and the original text must be read back [Fact] (https://apify.com/creative_maitake/app-store-review-pain-miner, https://unstar.app/blog/mining-app-reviews-for-product-roadmap) | Meeting assistants are used mainly on desktop/web, so mobile reviews may be skewed |
| **Product Hunt** | New product positioning, follow-up questions from early users | Look at the questions Makers answer and "how are you different from X" | No methodology source found in this round; this is standard practice [Inference] |
| **Reddit / HN** | Real workflow complaints, alternatives | Search "Otter vs Fireflies", "meeting notes lab", "PI meeting notes", etc. | No dedicated Reddit methodology found in this round [Inference] |
| **Zhihu / Xiaohongshu** | Chinese users' usage scenarios and complaints | Xiaohongshu comments can be used for needs mining / pain-point summarization / purchase-concern organization [Fact] (https://smithery.ai/skills/socialdatax/xhs-comment-insights, https://www.fanruan.com/blog/article/738972/) | No Zhihu methodology found in this round; Xiaohongshu users skew toward consumer/lifestyle, so B2B signal is weak |
| **Earnings reports / funding news** | Competitors' strategic focus | For public companies, read the product sections of the 10-K; for private ones, check Crunchbase/ITjuzi | Specific sources not verified in this round [Inference] |
| **Job postings (JDs)** | What competitors will be doing 6–18 months from now | Group by function and watch how counts change over time; a sudden surge in one function is more informative than any single JD [Fact, vendor source] (https://pagecrawl.io/blog/competitor-job-posting-monitoring-hiring-signals, https://go.intervue.io/blog/competitor-hiring-analysis-how-job-postings-reveal-market-strategy) | The "6–18 months ahead" claim comes from monitoring vendors and is **to be verified**; HBR also has an article on the same topic (https://store.hbr.org/product/what-you-can-learn-from-a-competitor-s-job-postings/H09A87) |
| **Competitor help docs / Changelog / pricing pages** | Real feature boundaries | More reliable than marketing pages; the thresholds for higher-tier plans are often stated only in the docs [Fact] (https://cotera.co/articles/how-to-find-competitor-pricing) | Always record the date |

### 1.4 Template A: Competitive Analysis Template (Ready to Copy)

```markdown
# Competitive Analysis: <Scenario> — <Date>

## 0. Purpose of the Analysis (One Sentence)
This analysis should answer: ______ (e.g., in the "meeting → action item → knowledge accumulation" chain, which step do mainstream meeting assistants fail to cover for research lab scenarios?)
Who the readers are and what decisions they will make from this report: ______

## 1. Competitor List and Selection Rationale
| Competitor | Type (direct / indirect / alternative) | Why selected | Data collection date |
(3–5 direct competitors is enough; "alternatives" should include clumsy approaches such as "manual work + Notion/Feishu docs")

## 2. Feature Matrix (Organized Around Chain Steps, Not Around Menus)
| Chain step | Us | Competitor A | Competitor B | Competitor C | Evidence link |
| Recording/transcription | | | | | |
| Speaker identification | | | | | |
| Action item extraction | | | | | |
| Action item confirmation (human gate) | | | | | |
| Action item → task system | | | | | |
| Citation/traceability to source text | | | | | |
| Cross-meeting knowledge Q&A | | | | | |
| Domain terminology / scholarly literature linking | | | | | |
Scoring: Full / Partial / Missing / Unknown (Unknown ≠ Missing; the two must be kept separate)

## 3. Pricing and Value Metric
| Competitor | Free-tier limits | Entry price (normalized to CNY or $ per user per month, billed annually) | Value metric (minutes / seats / number of meetings) | Upgrade trigger | Collection date | Source |

## 4. Review Mining (≥10 Low-Star Reviews per Competitor)
| Competitor | Original quote (verbatim) | Theme code | Occurrences | Source link |
Theme summary: which complaints recur across competitors? (Complaints recurring across competitors = an industry-wide gap and a candidate for differentiation)

## 5. Business Model / Unfair Advantage
One row per competitor: how it makes money, how it defends its position, **why it is unlikely to build the small thing we want to build** (reasons of channel / customer segment / cost structure)

## 6. Timeline of Developments
Major events in the past 12–24 months (launches, acquisitions, pricing changes, JD surges) → infer next steps

## 7. Conclusions (Required)
7.1 Assessment of competitors: ______
7.2 Recommendations for us: ______ (which gaps are worth pursuing, which are not, and why)
7.3 Confidence and unverified items: ______
```

**How to use it in this project**: The rows in Section 2 for "Citation/traceability to source text", "Domain terminology / scholarly literature linking", and "Action item confirmation (human gate)" are selling points that BriefPilot's existing PRD already has; be honest in filling in whether competitors are Full or Partial on these rows, and do not presume Missing. Section 4 is the most important output of this round—**complaints that recur across competitors** are the "small unmet need".

---
## 2. Market Size Estimation: TAM / SAM / SOM

### 2.1 Two Methods and Why to Do Both

- **Top-down**: Slice a third-party report's total category size by proportion. Fast, but prone to inflation, and report definitions often include adjacent categories you don't compete in [Fact] (https://clearbit.com/blog/what-is-total-addressable-market, https://pmtoolkit.ai/how-to/calculate-market-size-tam-sam-som).
- **Bottom-up**: Number of buyers × annual contract value (× frequency). More credible but time-consuming; quality depends on the buyer count and pricing assumptions [Fact] (same as above).
- **Reconciliation**: List the assumptions of both side by side. The gap usually comes from **definition drift** (inconsistent market definitions); adjust the side with the looser definition and record the remaining difference. pmtoolkit explicitly rejects the claim that "within 30% means reliable"; the 20%/30% thresholds are not standard **to be verified** [Fact] (https://pmtoolkit.ai/how-to/calculate-market-size-tam-sam-som).

### 2.2 The Six-Step Method (pmtoolkit) and Common Mistakes [Fact]

1. First define the unit of demand: who the buyer is, the product unit, geography, and annual price (ACV/ARPU).
2. Bottom-up: qualified buyers × ACV (example: 30,000 × $20,000 = $600M).
3. Top-down: total category spend × your segment's share, citing the source and year.
4. Reconcile.
5. TAM→SAM: filter by geography/segment/channel (example: $600M × 50% × 70% = $210M). **Do not subtract competitor share at this stage.**
6. SAM→SOM: a realistic capture rate within a defined period (example: × 2% = $4.2M), then work backward to check whether the required number of customers matches sales capacity.

Common mistakes: assuming 100% penetration for SAM/SOM; applying filters twice; subtracting competitor share at the SAM stage; using unsourced numbers; treating a forecast as a measurement for a new category that has no analyst data.

### 2.3 How to Use This in This Project

**[Inference]** Research labs are a classic segment with "no analyst reports", so top-down is nearly impossible and only **bottom-up** is workable: number of labs (by university/research-institution counting conventions; source still to be found) × annual fee each lab is willing to pay (to be determined through interviews) × penetration rate. In interviews, proactively say "this is a bottom-up estimate; the assumptions are ___; the most uncertain one is willingness to pay". That is far more credible than presenting an inflated TAM. **[Assumption]** The lab budget decision-maker is the PI rather than the members, and the paying unit may be "per lab" rather than "per seat". This is a pricing assumption that must be validated in interviews.

### 2.4 Template B: Research Plan Template

```markdown
# Research Plan: <Topic> — <Date>

## 1. Decision Goal
The decision we will make once this research is done: ______ (e.g., whether to position v2 for research labs)
If the result is A we will ___; if B we will ___ (write this in advance to avoid post-hoc rationalization)

## 2. Hypotheses to Validate (take 3–5 from the top-right of the assumption map)
| ID | Hypothesis | Type (desirability/viability/feasibility/usability/ethical) | Importance | Existing evidence | Validation method |

## 3. Method Mix
- Desk research: source list (§1.3); note which hypothesis each source must answer
- Interviews: n = ___ (see §2.5 on sample size), recruitment channels, screening criteria (must have relevant experience within the last 3 months)
- Survey / single-question poll: only to validate themes that have already emerged, not for discovery
- Task observation: have the user do a "post-meeting wrap-up task" live, and time it

## 4. Interview Guide (Mom Test rules)
- Don't pitch our idea; ask about specific past events; talk less, listen more
- Opening: "The last time you finished a group meeting / project meeting, how did you organize what needed to be done afterward? Walk me through it."
- Follow-ups: What tool did you use at the time? How long did it take? Which step was most annoying? Did you later miss anything? Have you spent money or time looking for a solution to this?
- Switch interview (if the interviewee has changed tools): when did you first feel the old way wasn't working → passive looking → trigger event → active searching → decision → purchase; the four forces: push / pull / anxiety / habit

## 5. Recording and Coding
- Write up notes within 24 hours; tag every finding with respondent_id; code by theme; record the number of respondents supporting each theme
- Evidence strength rule: mentioned independently by ≥3 people = theme; mentioned by 1 person = lead

## 6. Output
findings.md: theme × number of respondents covering it × verbatim quotes × impact on the PRD; hypothesis status (supported / contradicted / mixed)
```

### 2.5 How to Determine Sample Size (and Why)

- **Qualitative interviews / usability testing**: Nielsen's classic model says 5 users uncover about 85% of usability problems (formula N×[1−(1−L)^n], L≈0.31). But that conclusion is for **usability testing**, and each distinct user group should be tested with 3–4 people; for quantitative studies, about 20 people is recommended [Fact] (https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/).
- **PMF survey (Sean Ellis)**: "How would you feel if you could no longer use this product?" A "very disappointed" share of ≥40% is treated as a sign of PMF; respondents must have used the product more than once and be recently active; about 100 responses are needed for stable results, and fewer than 40 only count as preliminary [Fact] (https://www.crv.com/content/product-market-fit-survey).
- **The three Mom Test rules**: talk about the other person's life rather than your idea; ask about specific past events rather than future opinions; talk less, listen more. "Compliments are the fool's gold of customer learning" [Fact, from book reviews and summaries] (https://mtlynch.io/book-reports/the-mom-test/, https://www.shortform.com/blog/what-is-the-mom-test/).
- **Switch interviews (JTBD, Moesta)**: interview only people who have already switched; timeline: first thought → passive looking → event → active looking → event → decision → purchase; record events, not generalizations [Fact] (https://jobstobedone.org/switch-interview/).

**How to use this in this project**: BriefPilot's existing research plan is 6–10 interviews (`docs/research/research-plan.md`, not yet started). For v2 we recommend two groups: **5–6 research lab members** (including 1–2 PIs) plus **3–4 members of non-lab small teams** as a control. Why a control group: if both groups complain about the same things, "research lab" is not a differentiating dimension but merely a channel. The PMF survey does not apply at the Demo stage (there are no real users); don't send one just to look quantitative.

---
## 3. How to Write the PRD

### 3.1 What is most common in mainstream templates

prodmgmt.world surveyed the PRD templates of 15 top teams (Square/Kevin Yien, Figma, Asana, Amazon, Intercom, Shape Up, Uber, Miro, etc.). Based on our own count of the 9 templates we could verify, the section frequencies were: problem statement 8/9, solution 7/9, **non-goals 6/9**, milestones 6/9, success metrics 4/9, FAQ 3/9, sign-off 3/9, open questions/risks 2/9 [Fact; the tally is compiled from this round's fetch of that page's description, and the page itself gives no percentages] (https://www.prodmgmt.world/blog/prd-template-guide).

Several concrete structures worth borrowing [Fact, same source]:
- **Square (Kevin Yien)**: four parts: Problem Alignment (problem, why it matters, customer insights, sign-off) → Solution Alignment (solution, goals, **non-goals**, key flows, prototypes, edge cases, sign-off) → Execution (launch plan, metrics and success criteria, phased rollout) → Appendix (changelog, FAQ, dependencies). Two sign-off gates separate "problem alignment" from "solution alignment".
- **Figma (Yuhki Yamashita)**: the Overview directly includes the problem, goals and success metrics, and non-goals.
- **Asana**: first a Project Brief (problem and opportunity), then a Project Proposal (solution), with a checkpoint in between.
- **Lenny's 1-pager**: Lenny's template roundup lists 9 PRD/1-pager templates (Lenny's own, Square, Asana, Intercom, Product Hunt, SeatGeek, Figma, etc.) [Fact] (https://www.lennysnewsletter.com/p/my-favorite-templates-issue-37). However, his dedicated PRD article (2021-08-31) is paywalled, so **the exact six section headings of Lenny's 1-pager could not be verified this round; to be verified** (https://www.lennysnewsletter.com/p/prds-1-pagers-examples). Third-party descriptions characterize it as "one page, six sections, problem first, including how success will be measured and what is explicitly excluded."

### 3.2 Amazon PR/FAQ (Working Backwards)

The template description published by Colin Bryar (former Bezos chief of staff and co-author of *Working Backwards*) [Fact] (https://docs.superhuman.com/@colin-bryar/working-backwards-how-write-an-amazon-pr-faq):
- Three parts: a **press release** (written as if the product has already launched; the litmus test: "if this text can't convince people to buy, rewrite it"; it must state the customer, the problem, the solution, and why customers would adopt it) + an **external FAQ** (what customers/press would ask) + an **internal FAQ** (longer; the sharp questions from internal stakeholders: risks, challenges, costs).
- The whole is referred to as the "6-page document." The review is a 60-minute meeting: the first 20 minutes are **silent reading in the room** (no pre-reads, so everyone reads the same version), followed by 40 minutes of discussion. "Iterating on the press release is cheaper than iterating on the product," and it usually takes several drafts before approval.
- The finer-grained sections of the press release (headline, subheading, release date, lead paragraph, problem, solution, customer and executive quotes, call to action) come from a secondary summary (https://www.prodmgmt.world/blog/prd-template-guide); Bryar's original does not list them item by item, **to be verified**.

**How to use it in this project**: PR/FAQ fits this round extremely well. **First write a press release for the launch of "BriefPilot for Research Labs."** If we cannot even write the customer quote ourselves, or would not buy it ourselves, then this niche segment does not hold up. The internal FAQ must include the core question: "Feishu Minutes, Otter, and Fireflies already do this, so why build it?" The answer must cite the evidence in §1.

### 3.3 Special sections in an AI product PRD

Multiple practitioner guides agree that an AI PRD needs a separate **evaluation (eval) section**: the decision, scope, target behavior, success metrics, **acceptance thresholds**, test set specification, a golden set (labeled by scenario/risk), and regression rules (which changes require re-running the evals) [Fact, practitioner sources] (https://www.ideaplan.io/blog/how-to-write-ai-product-prd, https://www.institutepm.com/knowledge-hub/ai-prd-template-complex-features). Metrics fall into three layers: model layer + experience layer + business layer. **An acceptable hallucination rate must be written down rather than assumed to be zero**, and "writing evaluation criteria with adjectives instead of numbers" is the most common reason an AI PRD fails engineering review [Fact, same sources]. Hallucination rates drift with the input distribution and with model changes, so they must be measured both offline and online [Fact] (https://braintrust-ao1rtkntn.preview.braintrust.dev/encyclopedia/hallucination). The example thresholds "acceptance rate ≥75%, hallucination rate ≤2%" are illustrative only, not industry benchmarks.

### 3.4 User stories and acceptance criteria

- INVEST: Independent, Negotiable, Valuable, Estimable, Small, Testable [Fact] (https://open-exam-prep.com/study-guides/safe-popm/ch07-user-stories/user-stories-invest).
- Acceptance criteria commonly use Given/When/Then (from Cucumber's Gherkin), though it is not mandatory. Add **negative and edge-case scenarios**; untestable criteria such as "better UX" are a common failure [Fact] (https://www.storypointlab.com/docs/backlog/how-to-write-testable-acceptance-criteria).
- Non-goal phrasing: "We do not solve X (reason)," optionally numbered N1/N2 [Fact] (https://docsio.co/blog/prd-template).
### 3.5 Template C: PRD Skeleton (for v2)

```markdown
# <Product name> PRD v2.0 —— <date>  Status: Draft / Problem-aligned / Solution-aligned / Approved

## 0. One-Page Summary (for someone with 30 seconds)
Users: ___  Problem: ___  What we build: ___  What we don't build: ___  Success metrics: ___  Biggest risk: ___

## 1. Problem Alignment (needs sign-off)
1.1 Target users (specific role + situation; who is the comparison group)
1.2 Problem statement (one paragraph, including the current clumsy workaround; cite the evidence source: respondent_id / review link)
1.3 Why existing solutions fall short (cite the competitor feature matrix + review-mining themes; do not write things like "they are not smart enough")
1.4 Why now / why us (unfair advantage: dogfooding scenario, domain knowledge)
1.5 Assumption list (H1…, each labeled Fact/Inference/Assumption, with the validation experiment ID attached)
— Sign-off: ______

## 2. Solution Alignment (needs sign-off)
2.1 Solution overview (one paragraph) + which single action is the differentiating "magic moment"
2.2 Goals (measurable)
2.3 Non-goals (N1 We will not do ___, because ___)
2.4 Key flows (user stories: As a ___, when ___, I want to ___, so that ___)
2.5 Acceptance criteria (Given/When/Then, including negative and edge cases, including rules like "leave missing fields blank, don't guess")
2.6 AI evaluation section: target behavior, gold-set spec, three-layer metrics, acceptance thresholds (numbers), acceptable hallucination rate, regression rules
2.7 Edge cases and failure modes (refusal to answer, citation check failure, long meetings, multiple speakers)
— Sign-off: ______

## 3. Execution
3.1 Demo/MVP scope (which kind of MVP; see §4)
3.2 Metrics and dashboard (North Star + guardrail metrics)
3.3 Staged rollout / release plan
3.4 Risks and open questions

## 4. Appendix: PR/FAQ (press release + external FAQ + internal FAQ), changelog, dependencies, glossary
```

**How to use it in this project**: The existing PRD v0.1 already has §2.2 "Users we explicitly do not serve" and the §1.4 assumptions table, so the structure does not need to be torn down. What v2 needs to change: in 1.1–1.3, replace HYPOTHETICAL with interview/review evidence; in 2.1, state the single differentiating action explicitly; in 2.6, write the metrics in `docs/evaluation/metrics.md` as acceptance thresholds with numbers; add a PR/FAQ to the appendix.

---

## 4. MVP Types and Demo Design

### 4.1 MVP Type Comparison

| Type | What it tests | When it applies | Cost / pitfalls | Source |
|---|---|---|---|---|
| **Landing page / explainer video** | Whether anyone wants it (value hypothesis) | Nothing built yet; you need to test demand | Clicks / email sign-ups show interest, not willingness to pay | Dropbox tested demand in 2007 with a 3-minute video; the waitlist figure "5,000→75,000" is relayed by multiple secondary sources and the original source was not found **to be verified** (https://www.shortform.com/blog/?p=7911, https://speckyboy.com/successful-minimum-viable-products/) |
| **Fake door / painted door** | Add a fake entry point to an existing product and measure clicks | An existing user base | Ethics: reveal the truth promptly and honestly; never charge for something that does not exist; "<2% is noise" is vendor rule of thumb **to be verified** | (https://amplitude.com/explore/experiment/fake-door-testing, https://www.koji.so/docs/fake-door-testing-guide) |
| **Concierge** | Whether the backend logic/data is useful (no interface; a human serves the user manually) | You need a deep understanding of users and want to verify the data is usable | Labor-intensive, not scalable, results are affected by the personal charm of the person serving | Mind the Product (Amanda White, 2026-03-19): Concierge tests the backend (https://mindtheproduct.com/wizard-of-oz-vs-concierge-testing-behind-the-curtain-or-behind-the-desk/); Netguru (https://www.netguru.com/blog/concierge-testing-versus-wizard-of-oz-prototyping) |
| **Wizard of Oz** | Whether the frontend/interaction is accepted (there is an interface; a human behind the scenes pretends the backend is automated) | The interface is ready but automation is expensive or blocked | The person behind the curtain must be a domain expert, otherwise the feedback is unreliable | Same as above; "I have a screen but no backend" = WoZ |
| **Single-feature MVP** | Whether the core feature itself works | The risk is in technology/quality rather than demand | Easily turns into "small but complete" | Common practice [Inference] |
| **Demo (runnable demonstration)** | Let decision-makers/interviewers see the difference | You need to persuade rather than measure | Demo ≠ validation; it cannot be treated as "validated" evidence | The existing `docs/demo-script.md` already states this honesty principle |

**Selection principle**: Choose the type according to the "riskiest belief", not according to what famous companies have used [Fact] (https://www.launchrock.com/library/expert-advice/mvp).

**How to use it in this project [Inference]**: BriefPilot v2's biggest risk is not "can we extract tasks from meeting minutes" (technically everyone can), but "**does the lab setting have an action that nobody else has built and that users are willing to change their habits for**". So the recommended combination is:
1. **Concierge first (1–2 weeks)**: Take the recordings/minutes of the user's own lab's last 3 group meetings and organize them by hand into the envisioned format (for example, linking action items to the corresponding papers/experiment records), hand them back to the members, and observe whether they use them and whether they edit them. This step requires zero code, and the project owner is right there in the lab (the legitimate advantage of dogfooding).
2. **Build the Demo after Concierge shows a positive signal**: Build only a runnable version of that one magic moment, with everything else mocked.
3. No landing page: the target users are an acquaintance circle, so an email sign-up carries no information.
### 4.2 Demo Design: Showing the Client the Differentiator in 5 Minutes

Principles on which sources agree [Fact]:
- **Say what you do in the first sentence**, and keep the problem setup short; a demo is more effective than a verbal description; organize by "problem → how it's solved" rather than listing features in screen order; assume the network will drop and run a local copy; one person talks while another operates; keep slides under 20 words where possible; use no more than 4–5 numbers, and only about your own product; don't say "we're passionate / the product is great", let the product speak for itself (https://paulgraham.com/investors.html).
- Attention is highest in the first 5 minutes: cut the agenda slide, logo wall, and team introduction; screen every item with three questions: Does the audience find it interesting? Is it critical to the main message? Can it only be said here? Build around one **win-theme** (the single reason the audience should choose you); add a memory hook (https://presalescollective.com/post/how-to-nail-the-first-5-minutes-of-your-product-demo-and-why-it-matters).
- Make the value understandable within 90 seconds; a live demo in a real browser beats a PPT that talks about features (https://www.naoma.ai/blog/first-60-seconds-demo).
- The "magic moment" is a repeatable loop: pain point → live demonstration → proof (metric / artifact / customer's own words) → re-anchoring question, 2–4 minutes per question (this is Demand Curve's framing; the original page returned 404 when fetched, so this comes only from a search snippet and is **to be verified**).
- YC's reminder: Demo Day pitches have become so short that there is almost no demo, and "explaining the product clearly" is the hardest and most valuable preparation [Fact] (https://www.ycombinator.com/blog/guide-to-demo-day-pitches/).

### 4.3 Template D: Demo Script Skeleton (5 Minutes)

```markdown
# Demo script: <product> for <segment> — <date>  provider: mock / real  data: fictional / anonymized real

## 0. Before you start (first line on the cue card)
"The data is ___, the model is ___, and the part of this project that I built on my own is ___." (Honest disclosure; must be said)

## 0:00–0:30  One sentence + the problem
"BriefPilot is ___ (one sentence)."
A concrete incident (not an abstract pain point): "After last Wednesday's group meeting, ___ spent ___ minutes doing ___ and still missed ___."

## 0:30–1:00  Comparison with the status quo (optional, ≤30 seconds)
"With Feishu Minutes/Otter you get this ___ (screenshot / one sentence), and it stops at ___." (Must be verified fact; no disparaging)

## 1:00–3:00  Magic moment (the one differentiating action, run live)
Action: ___ → ___ appears on screen → point out "Notice this: ___" (the differentiating detail)
Proof: a number / a user quote / an artifact
Re-anchor: "When did your lab/team last run into this?"

## 3:00–4:00  Trust and boundaries
Show one refusal to answer / one case of owner=null with no guessing / a citation that can be opened
"It does not do ___ (non-goal), because ___."

## 4:00–5:00  Evidence and next steps
"These are the results from the concierge stage with ___ users and ___ meetings: ___ (≤3 numbers)."
"Next we will validate ___, with a threshold of ___."
Leave one question for the audience.

## Contingency plan
Network down → run locally; model answers wrong → don't hide it, say "the evaluation set has ___ questions of this type, currently ___%"; timeout → switch to mock and say so.
```

**How to use this in the project**: The existing `docs/demo-script.md` is a "feature-tour" type (data import → Q&A → extraction → confirmation), aimed at general small teams. The v2 version should be cut down to "**one magic moment + trust boundaries**", and the competitor comparison in §0:30–1:00 must rest on the verified results of the §1 competitor matrix; do not say "they have no citations" from impression.

---

## 5. Hypothesis Validation Experiment Design

### 5.1 Template Sentence Pattern and Why Thresholds Must Be Set First

A general sentence pattern (multiple sources agree, with slightly different wording) [Fact] (https://featbit.co/release-decision-agent/hypothesis-before-you-build, https://pmtoolkit.ai/learn/experimentation/hypothesis-driven-development, https://thegrowthmind.substack.com/p/growth-experiments-a-simple-framework):

> We believe that making **[change]** for **[specific population]** will lead to **[outcome]**, because **[causal reason]**.
> We will know we are right when **[single primary metric]** reaches **[threshold]** within **[time window]**, and **[guardrail metric]** does not fall below **[threshold]**.

Why the threshold must be set in advance: without a line drawn beforehand, teams declare success whenever the numbers "look good"; use one primary metric and treat the rest as guardrails: if the primary metric wins but retention drops, it is not a win [Fact, same sources]. Torres also says to "draw the line in advance", and to record the hypothesis, audience, test details, criteria, results, and actions; and to **compare multiple options** rather than judging a single one on whether it is "good enough" [Fact] (https://www.producttalk.org/2021/08/assumption-testing/). The fields of the Bland/Strategyzer experiment card: hypothesis, test, metric, success criteria [Fact, secondhand] (https://www.strategyzer.com/library/testing-business-ideas-book-summary).

### 5.2 Template E: Experiment Design Template

```markdown
# Experiment E__: <name> — <date>

## Hypothesis (from the top-right corner of the assumption map)
H__: We believe that making [change] for [population] will [outcome], because [reason].
Type: desirability / viability / feasibility / usability / ethical

## Test type
prototype test / one-question survey / data mining / research spike / concierge / WoZ / controlled timing

## Audience and sample
Who, how many, screening criteria (relevant experience within the last __), recruitment channel

## Metrics and thresholds (fixed in advance)
Primary metric: ___  Success line: ___  Time window: ___
Guardrail metric: ___  Must not fall below: ___
If the primary metric lands in the [gray zone]: ___ (write this in advance)

## Procedure
Steps 1…n (who does what, what is recorded)

## Result → action (committed in advance)
Supports → we will ___
Refutes → we will ___
Mixed/inconclusive → we will ___

## Result log (fill in after execution)
Actual value, comparison with threshold, unexpected findings, next steps
```

**How to use this in the project**: First rewrite the existing H1/H2/H3 in the sentence pattern above (they currently lack a "population" and a "threshold"). v2 adds the most critical one, an **[Assumption]**: H4, "The unmet need of research lab members regarding meeting assistants is ___ (to be filled in from competitor reviews and interviews)", validated through §1.4 review mining (recurring across ≥3 competitors) + §2.4 interviews (≥3 of 6 people independently recounting a specific incident). Both lines must be met before it enters the PRD problem statement.

---
## 6. Portfolio Case Study Writing

### 6.1 Consensus on structure

- General PM portfolio: 3 strong case studies beat 8 thin ones; each case should cover the problem, users, constraints, alternatives, trade-offs, and measurable results [Fact] (https://www.productledalliance.com/product-manager-portfolio-framework/, https://www.joinleland.com/library/a/product-manager-portfolio). This round did not find an article by Lenny himself dedicated to portfolios **(to be verified)**.
- AI PM portfolio (Institute of AI PM guide) [Fact] (https://www.institutepm.com/knowledge-hub/ai-pm-portfolio-guide):
  - Home page: a one-line positioning statement + 3–5 project cards (title, one-line summary, key result, link) + background + contact details; start with Notion, and build a standalone site once you have 3 or more strong pieces.
  - Seven sections per case: **Problem** (one paragraph: who is affected, how severely) → **Why AI** (why not rules / manual work / simple automation) → **Your role** (precise about ownership; use "led" only when you were the DRI) → **Approach** (rationale for model choice, data strategy, trade-offs, stakeholders) → **What you built** (screenshots/links) → **Results** (quantified; label estimates) → **Learnings**.
  - AI-specific elements: model comparison and rationale for the choice (cost/latency/accuracy), data requirements, **evaluation** (precision/recall/human-review disagreement rate), staged rollout (shadow → partial traffic → full), feedback loops, responsible-AI trade-offs.
  - Readable in under 5 minutes; at least one "Tier 1" piece (an end-to-end case study / a working prototype / a product with real metrics).
  - Substitutes for career changers without a shipped product: a working prototype + case study, a PRD for an AI feature that does not exist in an existing product, an AI product teardown of about 1,500 words, an open-source/research contribution, a course capstone.

### 6.2 How to use this in this project

The existing `docs/portfolio-case-study.md` is already divided into sections using three kinds of wording, "fact / assumption / experiment goal", which is the right approach (the Institute guide likewise requires estimates to be labeled). What v2 needs to add are the **Why AI** and **Why this segment** sections. The latter is the written answer to the interviewer's question "why build this at all?", and its answer should directly cite the competitor matrix and the interview theme IDs. **[Inference]** The project owner's lab experience can be written into the case as "why I could see this gap", but only as "firsthand observation + interviews with n peers", not as "this is how the research market generally works".

---

## 7. One-Page Cheat Sheet: This Round's Workflow

| Step | Template to use | Output directory | Completion criteria |
|---|---|---|---|
| 1 Assumption map | §5.2 | 03_positioning | List ≥8 assumptions, mark importance/evidence, pick 3–5 |
| 2 Competitor analysis | Template A | 01_market-research | 3–5 competitors, every cell in the feature matrix has a link + date, ≥10 low-star reviews coded per competitor |
| 3 User research | Template B | 02_user-research | 5–6 people in the lab group + 3–4 in the control group; findings.md has themes × number of people × verbatim quotes |
| 4 Market sizing | §2.2 six steps | 01_market-research | Primarily bottom-up; every number has a source or is labeled "assumption" |
| 5 PR/FAQ + PRD v2 | Template C + §3.2 | 04_prd | Internal FAQ contains an evidence-based answer to "why build this at all?"; evaluation section has numeric thresholds |
| 6 Concierge → Demo | §4.1 + Template D | 05_demo-plan | Run 2–3 concierge meetings first; build the single-magic-moment Demo only after a positive signal |
| 7 Experiments | Template E | 05_demo-plan | Every assumption has a pre-set threshold and "supports / contradicts / mixed → action" |
| 8 Portfolio | §6.1 seven sections | 03_positioning or the earlier v1 docs (not included) | Fact / assumption / estimate wording kept separate |

---

## Source List

**PRD / PR-FAQ**
1. https://www.lennysnewsletter.com/p/my-favorite-templates-issue-37 (Lenny's template collection, free)
2. https://www.lennysnewsletter.com/p/prds-1-pagers-examples (paywalled, only the intro was visible)
3. https://www.prodmgmt.world/blog/prd-template-guide (roundup of 15 PRD templates)
4. https://docs.superhuman.com/@colin-bryar/working-backwards-how-write-an-amazon-pr-faq (Colin Bryar's PR/FAQ template guide; the original coda.io link redirects here)
5. https://productschool.com/blog/product-fundamentals/prfaq
6. https://www.workingbackwards.com/resources (resource index only; template page returns 404)
7. https://docsio.co/blog/prd-template (example of what not to do)
8. https://open-exam-prep.com/study-guides/safe-popm/ch07-user-stories/user-stories-invest
9. https://www.storypointlab.com/docs/backlog/how-to-write-testable-acceptance-criteria
10. https://www.ideaplan.io/blog/how-to-write-ai-product-prd
11. https://www.institutepm.com/knowledge-hub/ai-prd-template-complex-features
12. https://braintrust-ao1rtkntn.preview.braintrust.dev/encyclopedia/hallucination
13. https://uvik.net/blog/ai-prd-template/

**Competitor analysis / desk research**
14. https://www.woshipm.com/evaluating/1833499.html (Ni Cai-Zane, 2019-01-15)
15. https://www.woshipm.com/user-research/5867375.html
16. https://www.woshipm.com/evaluating/271053.html
17. https://bigideasdb.com/docs/g2-review-analysis
18. https://leadhaste.com/prompts/claygent-g2-review-pain-quote-mining
19. https://www.g2.com/products/g2/reviews?page=2
20. https://apify.com/creative_maitake/app-store-review-pain-miner
21. https://unstar.app/blog/mining-app-reviews-for-product-roadmap
22. https://smithery.ai/skills/socialdatax/xhs-comment-insights
23. https://www.fanruan.com/blog/article/738972/
24. https://pagecrawl.io/blog/competitor-job-posting-monitoring-hiring-signals
25. https://go.intervue.io/blog/competitor-hiring-analysis-how-job-postings-reveal-market-strategy
26. https://store.hbr.org/product/what-you-can-learn-from-a-competitor-s-job-postings/H09A87
27. https://cotera.co/articles/how-to-find-competitor-pricing
28. https://www.getmonetizely.com/articles/how-to-benchmark-your-saas-pricing-against-competitors-a-strategic-guide
29. https://www.artisangrowthstrategies.com/md/blog/b2b-saas-pricing-page-analysis-200-top-companies-right-wrong (vendor data, not independently verified)
30. https://www.emergn.com/insights/business-model-canvas-lean-canvas/
31. https://leanspark.leanstack.com/learn/why-lean-canvas-versus-business-model-canvas/
32. https://app.lucid.co/blog/lean-canvas-model

**Market sizing**
33. https://pmtoolkit.ai/how-to/calculate-market-size-tam-sam-som
34. https://clearbit.com/blog/what-is-total-addressable-market

**User research / assumption testing**
35. https://www.producttalk.org/2021/08/assumption-testing/ (fetch returned a page dated 2023-10-18)
36. https://www.strategyzer.com/library/testing-business-ideas-book-summary
37. https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/
38. https://www.crv.com/content/product-market-fit-survey
39. https://mtlynch.io/book-reports/the-mom-test/
40. https://www.shortform.com/blog/what-is-the-mom-test/
41. https://jobstobedone.org/switch-interview/
42. https://featbit.co/release-decision-agent/hypothesis-before-you-build
43. https://pmtoolkit.ai/learn/experimentation/hypothesis-driven-development
44. https://thegrowthmind.substack.com/p/growth-experiments-a-simple-framework

**MVP / Demo**
45. https://mindtheproduct.com/wizard-of-oz-vs-concierge-testing-behind-the-curtain-or-behind-the-desk/ (Amanda White, 2026-03-19)
46. https://www.netguru.com/blog/concierge-testing-versus-wizard-of-oz-prototyping
47. https://openclassrooms.com/en/courses/4544561-learn-about-lean-startup/4703206-discover-the-4-types-of-minimum-viable-product
48. https://echai.ventures/startingup/validate-idea/what-is-a-concierge-or-wizard-of-oz-mvp-and-when-should-i-use-one
49. https://amplitude.com/explore/experiment/fake-door-testing
50. https://www.koji.so/docs/fake-door-testing-guide
51. https://www.shortform.com/blog/?p=7911 (Dropbox video MVP)
52. https://speckyboy.com/successful-minimum-viable-products/
53. https://www.launchrock.com/library/expert-advice/mvp
54. https://paulgraham.com/investors.html
55. https://www.ycombinator.com/blog/guide-to-demo-day-pitches/
56. https://presalescollective.com/post/how-to-nail-the-first-5-minutes-of-your-product-demo-and-why-it-matters
57. https://www.naoma.ai/blog/first-60-seconds-demo
58. https://www.demandcurve.com/lessons/the-show-dont-tell-demo (fetch returned 404; search snippet only)

**Portfolio**
59. https://www.institutepm.com/knowledge-hub/ai-pm-portfolio-guide
60. https://www.institutepm.com/knowledge-hub/best-ai-pm-portfolios
61. https://www.productledalliance.com/product-manager-portfolio-framework/
62. https://www.joinleland.com/library/a/product-manager-portfolio
---

## Note on the Confidence of This Document's Conclusions

- **High confidence (original page opened and verified)**: Bryar PR/FAQ structure and review process; Square/Figma/Asana PRD structure (compiled second-hand via prodmgmt.world, but the descriptions are specific); Torres's five assumption-test types and two axes; Nielsen's 5-user model and its limitations; CRV/Sean Ellis PMF survey and the 40% threshold; Paul Graham's demo rules; Mind the Product's distinction between WoZ and Concierge; pmtoolkit's six-step TAM/SAM/SOM and common mistakes; the methodology of Ni Cai's article "Templates Are Worthless."
- **Medium confidence (multiple secondary sources agree, but the original source was not opened)**: the three Mom Test rules; the JTBD switch-interview timeline and four forces; the four boxes replaced in the Lean Canvas; the practice of mining low-star reviews on G2/Capterra; job postings (JDs) as a forward-looking signal; the "assumption → metric → threshold" sentence pattern; the elements of an AI PRD evaluation section; the seven-section structure of an AI PM portfolio (single source: Institute of AI PM).
- **Low confidence / needs verification**: the exact six sections of Lenny's 1-pager (paywalled); the paragraph-by-paragraph breakdown of the Amazon press release; Dropbox "5,000→75,000"; JDs leading by 6–18 months; fake door "<2% is noise"; the 20%/30% thresholds for TAM reconciliation; "three-tier pricing converts 14% higher"; Demand Curve's magic-moment loop (page returns 404).
- **Coverage gaps (search quota was exhausted this round, so these could not be followed up)**: authoritative sources for Chinese PRD templates; methodology for using Zhihu as a research channel; methodology for using Product Hunt reviews for research; specific ways to use Chinese data sources such as iResearch, 36Kr, and IT Juzi; academic sources for the "saturation" sample size in qualitative interviews; Lenny's own articles on portfolios. All of these are marked [Inference] or needs verification in the text; we recommend searching for them in the next round.
- **All "how to use this in our project" paragraphs are [Inference] or [Assumption]**: they are suggestions for applying the methods to BriefPilot, not research conclusions. In particular, whether the "research lab" segment holds up is something this document does not, and should not, answer.
