---
title: AI / LLM Product Manager Skills Map and Checklist (for BriefPilot v2 Differentiation)
status: draft
sources_count: 34
sources_count_method: Unique URLs in the sources section (recounted at wrap-up; original value 31)
evidence_note: First-round file. The body does not distinguish [Fact] from [Summary] item by item, and sources do not record individual access dates (all uniformly at the time of writing). Any item marked [Fact] but with no "opened the original page" record in the body should be treated as [Summary · to be verified] before citing (added in the wrap-up revision)
---

# AI / LLM Product Manager Skills Map and Checklist

> **Reading conventions**
> - **[Fact]**: Has a public source, with the URL attached at the end of the document, so you can click through and verify.
> - **[Inference]**: Reasonably derived from multiple facts, but not stated directly by any source.
> - **[Assumption]**: A judgment awaiting validation; do not use it as a conclusion.
> - **(To be verified)**: The source is a secondhand account or content behind a paywall, and only part of it was seen.
>
> This document answers three questions: (1) Where exactly does an AI PM differ from a traditional PM, and by how much; (2) Which "specialized skills" a qualified AI PM must master, and why these; (3) How to turn these skills into a checklist and 10 must-ask questions that can be used directly to review BriefPilot v2's differentiation plan.

---

## 0. One-Sentence Conclusion (Start Here)

**[Inference]** Synthesizing Hamel Husain, Aman Khan, Marily Nika, the official guidance from Anthropic/OpenAI/Google, and an analysis of 54 domestic JDs, the increment of an AI PM over a traditional PM boils down to just one thing: **the product's core behavior is probabilistic and fallible, and the ways it fails cannot be predicted**. Almost all "specialized skills" derive from this single fact:

| Because the model makes mistakes, the PM must… | Corresponding skill |
|---|---|
| First define "what counts as correct", and keep measuring it | Evaluation (evals), error analysis |
| Let users know when to trust and when to check | Trust calibration, grounding/citations, confidence design |
| Make errors discoverable, correctable, and bounded in cost | Human-in-the-loop, progressive automation, reversibility |
| Define behavior precisely in natural language | Prompt / context as product spec |
| Make trade-offs among quality, cost, and latency | Model selection, routing, unit economics |
| Judge the distance between a demo and a product | The "march of nines", failure-mode identification |
| Answer "why you, and not the model vendor" | Moat: workflow embedding, proprietary data, eval assets, distribution |

**Direct implication for BriefPilot v2 [Inference]**: If the differentiation plan cannot use "eval set + error analysis + user correction data" to prove that it is more accurate and more trustworthy than Feishu Minutes/Otter/Fireflies in some **narrow scenario**, then in an AI PM interviewer's eyes it is just a "wrapper". The evidence for differentiation must be **measurable**, not a feature list.

---

## 1. How AI PMs Differ from Traditional PMs: A Summary of Public Views

### 1.1 Overseas Views

**Marily Nika (formerly Google/Meta, Lenny's Podcast, 2023-02-05)**
- **[Fact]** Her core claim is "every Product Manager will be an AI Product Manager in the future"; the episode covers: PMs should learn a bit of coding, how to collaborate with data scientists, **when not to use AI**, how much data AI needs, and build vs. buy. Source: [Lenny's Podcast page](https://www.lennysnewsletter.com/p/ai-and-product-management-marily).
- **[Fact] (secondhand, to be verified)** In an O'Reilly interview she proposed three AI PM archetypes: AI Builder PM (builds models/platforms), AI Experience PM (designs new experiences on top of models), and AI-Enhanced PM (uses AI to enhance traditional PM work). The original O'Reilly page returned a 403 and could not be opened; this taxonomy comes only from search snippets and the description on her book page. Source: [search results roundup](https://www.oreilly.com/radar/?p=17225) (to be verified).
- **[Fact] (secondhand)** A third-party write-up says Nika believes AI PM interviews test the ability to "handle uncertainty" rather than prompt tricks or model trivia. Source: [antoinebuteau.com write-up](https://www.antoinebuteau.com/lessons-from-marily-nika/) (not the original text; be cautious).

**Aman Khan (Head of Product at Arize AI, Lenny's Podcast, 2024-11-14)**
- **[Fact]** He divides AI PMs into three types: **AI Platform PM** (builds tools for AI engineers), **AI Product PM** (builds products with AI at their core), and **AI-powered PM** (uses AI tools to improve their own work). Source: [Becoming an AI PM](https://www.lennysnewsletter.com/p/becoming-an-ai-pm-aman-khan).
- **[Fact]** Key points from the same episode: focus on customer problems rather than chasing trendy AI features; "the right interface is not necessarily a chat box"; **avoid full automation and keep users involved in the experience** (he uses the Betty Crocker cake mix analogy, "let the user add an egg themselves", meaning users need a sense of participation/ownership).
- **[Fact]** In 2025-04 he published "Beyond vibe checks: A PM's complete guide to evals" in Lenny's Newsletter. Its core sentence: "Evals are how you measure the quality and effectiveness of your AI system", and it argues that **writing good evals is becoming the defining skill of AI PMs**. The article uses the example of a travel-planning agent that books San Diego instead of San Francisco to show that evals could have caught this error before launch. Source: [Beyond vibe checks](https://www.lennysnewsletter.com/p/beyond-vibe-checks-a-pms-complete) (workflow section behind a paywall).

**Hamel Husain (independent ML consultant, has served 30+ companies)**
- **[Fact]** In "Your AI Product Needs Evals" (2024-03-29): failing LLM products mostly fail because they **have not built an evaluation system**; success depends on iteration speed, and iteration requires three capabilities: evaluating quality, debugging problems, and changing the system. Many teams only do the third, so they are "stuck at demo quality". Source: [hamel.dev/evals](https://hamel.dev/blog/posts/evals/).
- **[Fact]** He advocates having a "domain expert" rather than an engineer do the labeling and error analysis; PMs/domain experts catch "product failures", while engineers catch "technical failures" (wrong retrieval, wrong tool calls). Source: [Evals FAQ](https://hamel.dev/blog/posts/evals-faq/).

**Aakash Gupta (Product Growth, 2025-10-30)**
- **[Fact]** He argues that the "AI product sense" interview adds three layers on top of traditional product sense: **model considerations** (can a model support this solution? does it need a research breakthrough or only an application-layer change?), **AI safety and ethics**, and **AI-specific metrics** (e.g., how to measure hallucination rate, how to weigh model performance against user satisfaction). Source: [Master the AI Product Sense Interview](https://www.news.aakashg.com/p/ai-product-sense-interview) (framework implementation section behind a paywall).
- **[Fact] (author's personal opinion)** He claims that AI product sense matters more than technical interviews at most top AI companies, and that "Google eliminated the PM technical interview". This is the author's claim and is **not officially confirmed**.
### 1.2 Domestic Perspectives (JDs and Interview Reports)

**"Deep Dive into 54 JDs from Leading Companies: 6 Key Findings" (Everyone Is a Product Manager, 2026-01-17)**
- **[Fact]** The survey covered 54 JDs from 14 companies. Key findings:
  - General PM capabilities remain the foundation (full-lifecycle management, requirements insight, cross-functional drive, data-driven decision-making, executive communication).
  - AI PM roles are becoming "Agent-ized": ByteDance's consumer-facing AI PM requires **prompt engineering, knowledge bases, workflows, and Agent systems**; Meituan requires **prompts, RAG, and Agent evaluation standards**; Tencent Yuanbao's strategy PM requires **RAG, Tools, and Memory**; Alibaba requires intent recognition, response generation, and capability invocation.
  - **Evaluation has become a standalone role**: Tencent has a "Large Model Evaluation PM" and a "Next-Generation AI Experiment Evaluation System PM", and Microsoft has an "AI Safety Evaluation PM".
  - Capabilities fall into three tiers: foundational (LLM principles and limits) → intermediate (RAG, Function Calling, fine-tuning) → expert (Multi-Agent, Memory, MCP).
  - Examples of baseline metrics in an evaluation system: diagnostic accuracy, **suggestion adoption rate**, and improvement in customer outcomes.
  - Priority for project experience: first choice is "has led the full lifecycle of an Agent/LLM application and has a 0→1 launch case".
  - Source: [woshipm 6326220](https://www.woshipm.com/zhichang/6326220.html). Note: the article **does not mention Baidu** and **gives no percentage data**.
- **[Fact]** The visible part of JD&#39;s "LLM Application Product Manager – Digital Employee Self-Evolution and Evaluation" posting requires: **leading the design of evaluation sets, metrics, and scoring mechanisms, and building a complete "evaluation-driven self-evolution" pipeline**; locating root causes from fluctuations in evaluation results and turning them into verifiable product improvement plans. Source: [Mianshima JD page](https://www.mianshima.com/job/9/170798) (the responsibilities section requires login; to be verified).
- **[Fact] (campus-recruitment JD)** Xiaohongshu's AI PM intern JD requires the candidate to explain the **applicable scenarios, pros and cons, and costs** of each of Prompt Engineering / RAG / Agent approaches. Source: [campus recruitment page](https://campus.niuqizp.com/archivejob-vUy5LnNN5.html) (search snippet).

**"Just Finished Interviewing for AI PM at 6 Major Companies: These 7 Questions Appeared 100% of the Time" (Everyone Is a Product Manager, 2025-08-26)**
- **[Fact]** The 7 high-frequency questions: (1) Describe the AI project you led and your role; (2) **How do you decide whether a requirement should be solved with AI**; (3) How do you collaborate with the algorithm team; (4) **What do you do if your AI product hallucinates or produces inappropriate statements**; (5) Design an AI product to solve pain points in a given domain; (6) **The biggest difference between an AI PM and a traditional PM**; (7) Your views on AI industry trends.
- **[Fact]** The author's summary of the difference: "A traditional product manager is a feature designer, whereas an AI product manager is a capability designer"; the points of difference are technical understanding (able to talk with algorithm engineers), data-driven thinking, awareness of ethical risks, and forward-looking insight. Source: [woshipm 6259398](https://www.woshipm.com/zhichang/6259398.html).
- **[Inference]** Note that the reference answer to question (4) is "RAG + disclaimer beforehand, sensitive-word filtering + one-click feedback during, post-incident review afterward" — this is exactly the answer that BriefPilot's "citations + refusal to answer + human confirmation" design can directly benchmark against.

### 1.3 Overseas Interview Questions (aced.io / Exponent Roundup)
- **[Fact] (secondhand roundup; company attribution to be verified)** The page lists: Google, "A user complains that Gemini is confident but wrong — how do you fix it?"; NVIDIA, "How do you measure whether an LLM project is efficient? How do you measure model quality?"; Microsoft, "Design an AI system for evaluating résumés"; OpenAI, "How do you balance speed and safety under executive pressure, and when do you delay a launch?"; Apple, "How do you validate a model? The trade-offs between fine-tuning and synthetic data." Source: [aced.io](https://www.aced.io/blog/ai-product-manager-interview-questions).
- **[Fact]** The answer points the page summarizes: distinguish hallucinations caused at training time from those caused at inference time; mitigate with retrieval grounding, citations, confidence thresholds that hand off to a human, and regression evals; **"better to show uncertainty than to be confidently wrong"**; define "what good looks like" before building; follow the order **prompting → RAG → fine-tuning**.

### 1.4 Summary: What Is the Incremental Part of an AI PM's Role?

**[Inference]** Putting the Chinese and international sources together, the differences can be condensed into four points (ordered by how often they are mentioned):
1. **Evaluation and error analysis** (Husain, Khan, Tencent/JD evaluation roles, Gupta's "AI-specific metrics") — the most frequently mentioned, and already established as a dedicated role.
2. **Judging technical boundaries** (Nika's "when not to use AI", domestic question 2, Gupta's "model considerations", Xiaohongshu JD's "applicable scenarios and costs of each approach").
3. **Risk and trust design** (domestic question 4, Gupta's "safety and ethics", PAIR, Microsoft guidelines).
4. **Defining behavior in natural language (prompt/context)** (Tunguz, ByteDance JD, Anthropic context engineering).

Traditional PM skills (user research, prioritization, cross-functional drive, metrics) are not replaced but are **prerequisites** (the 54-JD survey's "Finding 1").

---

## 2. AI PM Skill Map (7 Domains × Sub-skills × Why)

### Domain A: Evaluation (Evals) and Error Analysis — The Core of the Core

**Why it is a core skill [Inference]**: In traditional software, "correct or not" is determined by test cases and is deterministic. LLM output is probabilistic, so "correct" must first be defined by people and then continuously measured by the system. Who defines "correct"? Husain's answer is the domain expert / PM, not the engineer. So evals are the PM's job, not "something for the technical team".

**A1. Three-level evaluation structure [Fact]** (Husain 2024)
- Level 1, unit tests/assertions: run on every code change, cheap; written by "feature × scenario" (e.g., under a "list lookup" feature: single match / multiple matches / no match), plus generic assertions (e.g., a regex check that no UUID is leaked).
- Level 2, human + model evaluation: run on a cadence, includes debugging.
- Level 3, A/B testing: after major changes, mature products only.
- **"Pass rate is a product decision"**; 100% is not required. Source: [hamel.dev/evals](https://hamel.dev/blog/posts/evals/).

**A2. Error analysis workflow [Fact]** (Husain FAQ + How I AI 2025-10-13)
- Look at the data first, don't build infrastructure first: start with about **100** diverse traces and label the first **30** yourself; continue until you "see no new failure modes".
- After each major change, spend 30 minutes looking at 20–50 outputs.
- After launch, run a cycle every 2–4 weeks, with at least 100 new traces per cycle.
- Label with **binary Pass/Fail plus a written critique**, not a 1–5 score (differences between adjacent scores are subjective and annotators drift toward the middle); to track incremental progress, split into multiple binary sub-checks ("4 of 5 key facts hit").
- Prioritize fixes by **frequency of occurrence**, not intuition.
- Appoint one domain expert as the "benevolent dictator" to set the quality standard; when multiple people annotate, measure agreement with Cohen's Kappa.
- **"The abuse of generic metrics is endemic"**: don't use generic metrics such as helpfulness/coherence as quality metrics; they create false confidence.
- Teams typically spend **60–80%** of development time on error analysis and evaluation, and this is part of development itself.
- **"Evaluation-driven development" (write the evals first, then build the feature) is not recommended**: evals should be written against **observed** errors.
- Sources: [Evals FAQ](https://hamel.dev/blog/posts/evals-faq/), [How I AI episode page](https://www.lennysnewsletter.com/p/evals-error-analysis-and-better-prompts).

**A3. LLM-as-judge (using a model as the judge) [Fact]** (Husain 2024 "Critique Shadowing")
- Steps: find the **principal domain expert** → build a dataset (covering features/scenarios/personas, real + synthetic, starting at about 30 examples) → the expert gives a binary verdict plus a detailed critique → fix the obvious errors first → use the critiques as few-shot examples to iterate the judge prompt until it agrees with the expert → error analysis → build specialized judges only when needed.
- Validation scale: about 100 labeled examples per failure mode (the FAQ says 100–200); below 60 the confidence interval is too wide; data split 10–20% train / 40–45% dev / 40–45% test.
- **Class-imbalance trap**: if the error rate is 5%, a judge that "always says Pass" still has 95% agreement; report TPR/TNR, not raw agreement.
- Honeycomb case: reached >90% expert agreement in 3 iterations.
- Use the strongest model you can afford as the judge (the judge can be slower and more expensive than the production model).
- "Building a judge is really a 'hack' whose purpose is to force everyone to look at the data seriously."
- Source: [hamel.dev/llm-judge](https://hamel.dev/blog/posts/llm-judge/).
- **[Fact]** Academic support: Shankar et al., *Who Validates the Validators?* (arXiv 2404.12272, 2024-04) introduces **criteria drift** — "users need criteria to grade, but grading also helps users define the criteria" — meaning evaluation criteria cannot be fully set before seeing outputs and must be iterated; it also notes that "LLM-generated evaluators inherit all the problems of the LLM being evaluated and need human re-validation". Source: [arXiv](https://arxiv.org/abs/2404.12272).

**A4. Types of evaluation [Fact]** (Khan 2025)
- Human evaluation (thumbs up/down, comments, expert labeling): directly connected to users but sparse, ambiguous, and expensive.
- Code-based evaluation (string/format/executability): cheap and fast, but weak on subjective tasks.
- LLM evaluation: scalable, can give explanations, and **a PM can write the judge prompt directly**; but it needs a labeled set for validation, is probabilistic, and needs a sufficient sample size.
- Common criteria: hallucination (whether the output is faithful to the given context), toxicity/tone, overall correctness, retrieval relevance, summary quality.
- Four elements of a judge prompt: set a role, provide context, define the goal (what success/failure looks like), define terms and labels.
- Source: [Beyond vibe checks](https://www.lennysnewsletter.com/p/beyond-vibe-checks-a-pms-complete).

**A5. Splitting evaluation for RAG and Agents [Fact]** (Husain FAQ)
- RAG splits into two stages: **retrieval** is a search problem, evaluated with Recall@k / Precision@k / MRR; **generation** looks at whether the model uses the context well, evaluated with error analysis + human labels + a validated judge. Tune retrieval first, then generation.
- Agent evaluation has two phases: end-to-end goal achievement (black box) → step-level diagnosis (tool selection, parameter extraction, error handling, context retention, efficiency), using a "transition failure matrix" to find where failures cluster.
- Multi-turn dialogue: first give the whole conversation a Pass/Fail, then locate the **most upstream first failure**; use "N-1 testing" to replay real conversation prefixes.
- **[Fact]** Ragas defines faithfulness as: break the answer into atomic claims and compute the share that the retrieved context supports (example: one of two claims supported = 0.5). Source: [Ragas docs](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/).
- **[Fact]** Google's *Agents Companion* whitepaper (2025, 76 pages) divides Agent evaluation into capability evaluation, **trajectory evaluation** (exact match / in-order match / precision-recall), and **final response evaluation** (autorater + human), and introduces the concept of AgentOps. Source: [marktechpost summary](https://www.marktechpost.com/2025/05/06/google-releases-76-page-whitepaper-on-ai-agents-a-deep-technical-dive-into-agentic-rag-evaluation-frameworks-and-real-world-architectures/) (the original Kaggle page could not be fetched; **to be verified**).

**A6. The economics of run frequency [Fact]**: Husain recommends deciding how often to run evals by three factors — the cost of the eval, whether it is saturated (if everything passes, it yields no new information), and the business value of catching that error; run cheap assertions on every change, run expensive judges before each release, and retire low-value evals.
### Domain B: Grounding, Citations, and Hallucination Handling

**B1. Four product-side approaches to hallucination [Fact]** (Chongchong, woshipm, 2026-03-11)
- Expectation management: disclaimers and confidence display (the "ChatGPT can make mistakes" notice under the ChatGPT input box, the "experimental" label on Google AI Overviews); **limiting the input surface** (preset prompts/dropdowns instead of a blank box); prompts that require hedged wording.
- Source tracing: mandatory citations + anchor jumps (Perplexity-style numbered citations); a **fallback response**, meaning that when retrieval finds nothing or confidence falls below a threshold, the system says plainly that it cannot answer and hands off to a human ("admitting 'I don't know' is a hundred times better than making things up"); process visualization.
- Interaction redesign: ghost text (Copilot-style Tab to accept), atomic operations (accept/regenerate per paragraph), multi-option selection (Midjourney's four images); the core idea is "**AI drafts, humans approve**".
- Complaint loop: **structured thumbs-down** (≤4 category labels: inaccurate / off-topic / outdated / other), and circuit-breaking on high-risk terms.
- Positioning: "The algorithm team is responsible for raising the ceiling of model capability; the product manager is responsible for holding the safety floor."
- Source: [woshipm 6351155](https://www.woshipm.com/ai/6351155.html).

**B2. Engineering guarantees for citations [Fact]** (Anthropic Citations documentation)
- Documents are chunked by sentence (plain text / PDF), or developers can supply custom content blocks to control granularity; the API returns `char_location` / `page_location` / `content_block_location` and `cited_text`.
- The documentation states that "because the API parses citations and extracts `cited_text` directly, **the citation guarantee is a valid pointer into the provided documents**", meaning a citation will not point to a nonexistent location (which is not the same as "the conclusion is correct").
- Limitations: citing images inside a PDF is not supported (scanned documents cannot be cited); it **cannot be used together with structured outputs** (returns a 400).
- Source: [Citations documentation](https://platform.claude.com/docs/en/docs/build-with-claude/citations).
- **[Inference]** Implication for BriefPilot: the design direction in the BriefPilot PRD that "citations must pass server-side allowlist validation" is consistent with this, but "a valid citation ≠ a faithful answer", so faithfulness evaluation is still needed.

**B3. Two root causes of hallucination [Fact]** (aced.io roundup): training-time (the model learned the wrong thing) vs. inference-time (context confusion). The former is addressed by switching models or fine-tuning; the latter by retrieval and context engineering.

### Domain C: Trust Design, Human-AI Collaboration, and Progressive Automation

**C1. Google PAIR *People + AI Guidebook*, Explainability + Trust [Fact]**
- The goal is **trust calibration**: users neither trust blindly nor refuse to use the system; they "rely on it when it is reliable and check it when it is not".
- Three elements of trust: ability, reliability, benevolence; **launch only when you can reach the quality bar you have described to users**.
- "Don't say 'what' without saying 'why' in a high stakes scenario."
- "The best explanation is likely a partial one."
- Test confidence displays before shipping them: numeric scores "assume users understand probability"; when confidence is low, offer multiple alternatives so users can judge for themselves.
- Data sources need three things made clear: scope, reach (personal vs. aggregated), and whether the data can be deleted/reset; **when important data is missing, tell the user**.
- Design for errors: explain in advance what happens when the system is wrong; respond according to severity; let users correct the system; offer a "switch back to manual" option in high-risk scenarios.
- **"Automate more when trust is high, or risk of error is low."** (Increase automation only when trust is high or the cost of error is low.)
- Source: [PAIR chapter](https://pair.withgoogle.com/chapter/explainability-trust/).

**C2. Microsoft *Guidelines for Human-AI Interaction* [Fact]**: Amershi et al., CHI 2019 (Honorable Mention). The 18 guidelines fall into four groups: initially (what the system can do and how well), during interaction, **when wrong**, and over time. They were validated with 49 designers across 20 AI products. Source: [Microsoft Research](https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/) (the page does not list the original text of all 18 guidelines; the specific items are **to be verified**).

**C3. Progressive automation patterns [Fact]** (mostly practitioner blogs; no single academic standard)
- Three supervision modes: **in the loop** (the agent pauses for approval), **on the loop** (a human monitors while the agent runs), **out of the loop** (post-hoc audit).
- Recommended path: start every new behavior in strict in-the-loop mode → once the override rate stays low for a period of time, relax to on-the-loop → eventually autonomy; relax one **action category** at a time, and tighten again when new risks appear.
- Pattern list: classify actions by reversibility, confidence-based routing, **preview before execute**, expiry on timeout, and **"undo" instead of "approve"** (suited to low-risk actions that still need an audit trail).
- Shneiderman: machine autonomy and human control are **two dials**, not one slider, and both can be high at the same time.
- Source: [search roundup (uxdesign.cc, codemia, etc.)](https://uxdesign.cc/the-autonomy-dial-a-pattern-toolkit-for-designing-human-control-over-ai-12bfbe23ca70).
- **[Fact]** OpenAI, *A practical guide to building agents*: human intervention is triggered by **high-risk actions** and by **repeated agent failures**; guardrails are layered (relevance classifier, tool safety assessment, etc.). Source: [maginative summary](https://www.maginative.com/article/how-to-build-ai-agents-a-detailed-practical-guide-from-openai/) (the original PDF is binary and could not be parsed; **to be verified**).
- **[Fact]** Anthropic, *Building effective agents*: an agent can pause at checkpoints to wait for human feedback, and stop conditions (such as a maximum number of iterations) should be set.

**C4. Why "draft + confirm" is not conservative but correct [Inference]**: Khan's "avoid full automation, keep users involved" (Betty Crocker), PAIR's "automate when trust is high or risk is low", the HITL pattern of "start from in-the-loop", and the Chinese hallucination article's "AI drafts, humans approve" are four independent sources pointing to the same conclusion. **But** they also jointly imply a next step: there must be a **measurable relaxation mechanism** (how low must the override rate be before confirmation can be skipped?). BriefPilot S0 has only "confirm" and no path to "automation after trust accumulates"; this is a gap v2 could fill **[Assumption]**.
### Domain D: Prompt / Context as Product Specification

- **[Fact]** Tunguz (2024-10-21): "system prompts are the new PRDs." The leaked Meta AI WhatsApp system prompt is 607 words and reads like a PRD, specifying which data fields to use and how to use them; he calls the best prompts "valuable intellectual property for the next software era." Source: [tomtunguz.com](https://tomtunguz.com/the-prompt-as-prd/).
- **[Fact]** Anthropic, *Effective context engineering for AI agents* (2025-09-29): context engineering is the next step beyond prompt engineering, and the core question is "what configuration of context is most likely to generate the desired behavior." The principle is **"the smallest possible set of high-signal tokens"**; "context must be treated as a finite resource with diminishing marginal returns"; there is **context rot** (the longer the context, the worse the recall); a system prompt should sit at the "right altitude," neither brittle if-else logic nor vague guidance that assumes shared background; **start with a minimal prompt and add instructions where it fails**; a curated set of diverse, canonical examples works better than a long list of edge-case rules; and if a human engineer cannot say which tool to use in a given situation, an agent cannot either. Source: [Anthropic Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
- **[Fact]** Anthropic, *Writing effective tools for agents* (2025-09-11): keep tools few and well-chosen, namespace them by service, return high-signal context (natural-language names rather than IDs), let the agent choose verbosity via `response_format` (a concise response is about 72 tokens vs. 206 for a detailed one), and make error messages give specific, actionable fixes. The evaluation method is "real tasks + verifiable outcomes + reading transcripts + held-out set validation." Source: [Anthropic Engineering](https://www.anthropic.com/engineering/writing-tools-for-agents).
- **[Inference]** Implications for PMs: (1) prompts should be versioned, reviewed, and regression-tested like code; (2) the "spec" shifts from a "feature list" to "behavior definitions + counterexamples + an evaluation set"; (3) PMs must be able to read traces and prompts, or they cannot take part in error analysis. Chinese job postings (ByteDance, Microsoft Language Engineer) already list "Context & Prompt design" as an explicit requirement **[Fact]**.

### Domain E: The Cost / Latency / Quality Triangle

- **[Fact]** Anthropic: agentic systems "often trade latency and cost for better task performance," and for most applications "optimizing single LLM calls with retrieval and in-context examples is usually enough"; the routing pattern example sends easy questions to a small model (Haiku) and hard ones to a larger model (Sonnet). Source: [Building effective agents](https://www.anthropic.com/research/building-effective-agents).
- **[Fact]** OpenAI guide: build a performance baseline with the most capable model first, then swap in cheaper models for specific tasks. Source: same as C3.
- **[Fact] (surveys and blogs)** Routing (pick one model per request) vs. cascading (try models from small to large): when a top-tier model turns out to be needed, a cascade has already paid for multiple calls, and may be worse in latency-sensitive scenarios; "quality estimation" is the key to successful model selection; some system-design material claims that "most LLM products lose not on quality but on unit economics, because they send all traffic to the expensive model by default." FrugalGPT-style "98% savings" is a best case cited by vendors. Sources: [arXiv 2603.04445](https://arxiv.org/pdf/2603.04445), [system-design.space](https://system-design.space/en/chapter/llm-cost-routing) (blog; numbers **to be verified**).
- **[Fact]** A Chinese CSDN article lists "evaluating token cost and response latency" as part of an AI PM's daily work. Source: [CSDN](https://damodev.csdn.net/6aaf80e6e4bab96c93ac4854.html) (the Gartner/IDC figures in it have no cited source; **do not cite them**).
- **[Inference]** A PM's job is not to count tokens but to define the **priorities of the triangle**: which paths must be fast (interactive Q&A), which can be slow but accurate (batch action-item extraction after a meeting), and which errors are costly enough to justify spending more (citation accuracy).

### Domain F: Recognizing AI Product Failure Modes

**F1. Great demo, collapse in production [Fact]**
- Karpathy (Dwarkesh Podcast, 2025-10-17): "There's a very large demo-to-product gap where the demo is very easy, but the product is very hard."; "Every single nine is a constant amount of work." (90% → 99% → 99.9%, each "nine" costs the same amount of work, i.e., the **march of nines**); the gap is especially large where failure is costly (self-driving); he considers this the "**decade of agents**" rather than the "year of agents." Source: [Dwarkesh transcript](https://www.dwarkesh.com/p/andrej-karpathy).
- Husain: teams without an evaluation system get "stuck at demo quality." The symptoms are whack-a-mole bug fixing, relying only on vibe checks, and prompts that keep growing bloated to cover edge cases (the Rechat/Lucy case).

**F2. Most enterprise AI pilots show no return [Fact]**
- MIT NANDA, *The GenAI Divide: State of AI in Business 2025* (reported by Fortune, 2025-08-18): about **95%** of enterprise GenAI pilots produced no measurable P&L impact, while about 5% achieved rapid revenue acceleration; the sample consisted of 150 leader interviews, a survey of 350 employees, and 300 public deployment cases. The root cause is attributed to a "**learning gap**" rather than model quality: general-purpose tools (ChatGPT) work well for individuals but in enterprises "don't learn from or adapt to workflows"; **purchasing specialized vendor tools succeeds about 67% of the time, roughly three times the rate of internal builds**; more than half of budgets go to sales and marketing, but the biggest ROI comes from back-office automation. Source: [Fortune](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/). **Note**: 95% means "no measurable P&L impact," not "does not work technically"; the original report's methodology has not been verified.
- **[Inference]** Implication for BriefPilot: if the product is not embedded in a specific team's workflow and does not learn from its corrections, it lands on the 95% side; a generic positioning such as "small-team knowledge assistant" is exactly the kind of "general-purpose tool that fails in enterprises" that MIT describes.

**F3. "Wrappers" have no moat [Fact] (mostly blog/VC opinion, no authoritative research)**
- A thin wrapper is one whose core functionality depends almost entirely on a third-party model API, with no proprietary logic or deep workflow integration; a thick wrapper has proprietary data pipelines, feedback loops, RAG, deep tool integrations, and custom workflow logic.
- A simple test: **if you remove your layer, does the customer have nothing left?**
- Counterargument: the pejorative "wrapper" assumes no other moat exists.
- Sources: [hatchworks](https://hatchworks.com/blog/gen-ai/ai-wrapper-product-strategy/), [tianpan.co](https://tianpan.co/blog/2026-04-12-the-ai-wrapper-trap-when-your-moat-is-someone-elses-api-call) (opinion, not evidence).

**F4. Missing data flywheel [Fact] (blogs + 1 paper)**
- "A thousand thumbs-down events are worthless until they become labeled, versioned evaluation rows"; **a user correction (the rejection plus the user's rewrite) is worth more than a thousand passive clicks**.
- How to tell "compounding" from "piling up": fix a held-out evaluation set and see whether adding the most recent quarter of data moves the score; if the curve is flat, you are just accumulating.
- NVIDIA's internal NVInfo assistant paper (arXiv 2510.27051): used 1,224 production feedback items (including 495 thumbs-down) to find routing and rewriting failure modes and fine-tune small models (its error classification table is internally inconsistent, so treat the numbers with caution).
- Sources: [stackmatix](https://www.stackmatix.com/blog/data-flywheel), [arXiv 2510.27051](https://arxiv.org/pdf/2510.27051).
### Domain G: Where Moats Come From

**[Inference]** Combining F3/F4 with the MIT report, AI applications have four sources of moat, and **only the last three are something a PM can directly design**:
1. **Distribution**: existing channels (Feishu Minutes lives inside Feishu, Otter lives inside Zoom). Small teams and solo projects essentially have none; this is BriefPilot's weakest dimension.
2. **Workflow embedding**: the product becomes a "mandatory checkpoint" in some process (Cursor inside the IDE, Glean across enterprise tools). The blog argues this is the moat that is "hardest to build and hardest to displace."
3. **Proprietary data + feedback loop**: not chat logs (model vendors see far more of those), but data **tied to decisions, outcomes, user corrections, and approvals**.
4. **Evaluation assets**: the golden dataset and regression cases are "a private asset that compounds over time" (explicitly stated by only one blog source, but consistent with Husain/Shankar's point that "criteria can only be iterated out of the data").

**[Assumption]** For a job-search portfolio project, #1 is out of reach, #2 depends on choosing the right niche scenario, and #3 and #4 are things you **can start accumulating at the demo stage and can show in interviews**. "I have 200 annotated real-scenario cases and an error taxonomy" answers "why you?" better than "I built a meeting-to-tasks feature."

### Domain H: Architectural Judgment in Official Guides (What a PM Needs to Be Able to Read)

- **[Fact]** Anthropic, *Building effective agents* (2024-12-19): distinguishes **workflows** (LLMs and tools orchestrated through predefined code paths) from **agents** (LLMs dynamically direct their own process and tool use). Five workflow patterns: prompt chaining, routing, parallelization (sectioning/voting), orchestrator-workers, evaluator-optimizer. Three principles: simplicity, **transparency (explicitly show the planning steps)**, and careful design of the agent-computer interface. "Start with the simplest solution and add complexity only when needed." Frameworks can obscure prompts and responses and make debugging harder. Two examples that suit agents are customer support (can be priced by resolution rate) and coding (verifiable with tests). Source: [Anthropic](https://www.anthropic.com/research/building-effective-agents).
- **[Fact]** OpenAI guide: three kinds of scenarios suited to agents are complex decision-making (refund approval), rules that are too extensive to maintain (vendor security review), and **processes driven by unstructured data** (insurance claims). Start with a single agent; adopt multi-agent only when complexity demands it (manager pattern / decentralized pattern). Source: same as C3.
- **[Inference]** PM-level judgment: BriefPilot's "minutes → action item drafts" is a classic **workflow** (prompt chaining + programmatic validation), not an agent. Packaging it as an "Agent" would cost points with knowledgeable interviewers. The differentiation should be in "which step of the workflow is more accurate than others'," not in "more autonomy."

---

## 3. AI PM Checklist (Usable Directly to Review Any AI Feature)

> Each item is tagged with its source domain. The criterion for ticking a box is "written evidence exists," not "I think we did it."

**I. Problem and Technical Boundaries**
- [ ] Can this need be solved **without AI**? What does AI add? (Nika, domestic question 2)
- [ ] Can the current model's capabilities support it? Does it rely on existing capabilities or on a research breakthrough? (Gupta, "model considerations")
- [ ] Is this a workflow or an agent? Is it using the simplest architecture? (Anthropic)
- [ ] How costly is failure? That determines how many "nines" are needed. (Karpathy)

**II. Defining "Correct"**
- [ ] Who is the domain expert / final arbiter? A single person or a committee? (Husain)
- [ ] Is there an eval set covering "feature × scenario × persona"? How many cases? Real or synthetic?
- [ ] Are labels binary Pass/Fail plus a critique, or a 1–5 score? (Should be the former.)
- [ ] Have you personally reviewed at least 30 real traces? Are failure modes ranked by frequency?
- [ ] Has the judge's TPR/TNR been validated against human labels? (Not raw agreement rate.)
- [ ] Are you using evals targeted at your own failure modes, or generic metrics like helpfulness?

**III. Grounding and Hallucination**
- [ ] Can every key fact be traced back to a source snippet? Are citations verified server-side, or merely claimed by the model?
- [ ] Does the system refuse to answer when evidence is insufficient? Have the refusal rate and false-refusal rate been measured?
- [ ] Is there a number for faithfulness? (Ragas-style proportion of atomic claims.)
- [ ] Is the input surface open or constrained? (Preset options reduce the hallucination surface.)

**IV. Trust and Human-AI Collaboration**
- [ ] Before first use, does the user know what the system can do and how well it does it? (Microsoft guidelines, first group)
- [ ] When the system errs, can the user notice, correct, and switch back to manual? (PAIR)
- [ ] Do high-risk outputs include "why," not just "what"?
- [ ] Are actions classified by reversibility? Which require approval, and which rely on undo?
- [ ] Is there a **measurable condition for relaxing** from in-the-loop to on-the-loop? (override rate)
- [ ] Has confidence display been user-tested? (PAIR: don't show numbers by default.)

**V. Specification and Maintainability**
- [ ] Are prompts versioned? Do changes go through regression evals?
- [ ] Is the system prompt at the "right altitude"? Was it built up from a minimum, or stuffed with boundary rules from the start?
- [ ] Are tool definitions clear enough that a human engineer can tell at a glance which one to use?

**VI. Cost / Latency / Quality**
- [ ] Which paths must be fast and which can be slow? Which model is used for each?
- [ ] Have unit economics been calculated? Does default traffic go to the most expensive model?

**VII. Moat and Flywheel**
- [ ] If your layer were removed, what would the user be left with?
- [ ] Are user corrections (rejection + the fix) recorded as structured eval rows?
- [ ] On a fixed holdout set, can new data move the score?
- [ ] Which mandatory checkpoint of which specific workflow is being embedded in?
- [ ] Why would existing big-vendor products (Feishu Minutes / Otter / Fireflies) **not** casually build this?

**VIII. Launch and Failure Modes**
- [ ] Has the quality bar that can be communicated to users been met? (PAIR: "ship only when it can be met")
- [ ] Is there structured thumbs-down feedback (≤4 categories) and a circuit breaker for high-risk cases?
- [ ] Is the post-launch error-analysis cadence set? (every 2–4 weeks, ≥100 cases)

---
## 4. 10 AI PM Questions to Ask When Evaluating BriefPilot v2 Differentiation Options

> Each question is followed by "why ask" and "what a qualified answer looks like." These questions are prepared on behalf of the user's client/interviewer, and are also gates the user must pass when choosing a niche (including the "research lab" candidate).

**Q1. Can your differentiation be written as an eval?**
- Why ask: If the differentiation can only be described with adjectives ("understands research better," "more trustworthy"), it can't be measured or proven, and in an interview it can't be distinguished from a wrapper. (Husain, Khan)
- Qualified answer: "On N [type of] meeting minutes, our action item extraction has a Pass rate of X% on three fields — [owner/deadline/evidence sentence] — versus Y% for [Feishu Minutes export/generic LLM]; the gap comes mainly from [failure mode Z]."

**Q2. What are the failure modes of existing products (Feishu Minutes / Otter / Fireflies) in your chosen scenario? How many of their real outputs have you looked at?**
- Why ask: Differentiation must come from **error analysis** of competitors, not a feature comparison table. Husain's methodology applies equally to competitors.
- Qualified answer: A labeled set of 30–100 competitor output samples, ranked by failure frequency; the top three failure modes are v2's direction. **(To do: this round of market research should produce this labeled set)**

**Q3. Who is your "benevolent dictator" — which real person decides "is this action item correct"?**
- Why ask: Without a domain expert, the eval set is just the PM's imagination. In a research lab scenario the expert may be the PI or a project lead; are they willing to label 100 items?
- Qualified answer: A name (or role), a committed amount of labeling time, and a first round of labeled samples.

**Q4. What does one mistake cost in this scenario? How many "nines" are needed?**
- Why ask: Karpathy's demo-to-product gap depends on the cost of failure. A wrong action item in a research lab (missing an experiment deadline) costs something different from an enterprise customer-service bot promising a refund, and that determines the reliability required and the corresponding engineering effort.
- Qualified answer: A quantified or tiered cost of failure + a corresponding "confirm vs. automatic" policy.

**Q5. How does user correction data flow back as eval assets?**
- Why ask: F4 — a thumbs-down is not an asset; a rejection with a correction is. This is the only moat a small project can start accumulating at the demo stage.
- Qualified answer: Every "edit the draft, then confirm" is recorded as an (original output, user correction, source sentence) triple and automatically enters the regression set; a fixed held-out set verifies whether new data actually moves the score.

**Q6. What are the conditions for relaxing from "confirm every item" to "auto-approve low-risk items"?**
- Why ask: C4 — four independent sources all say "human-in-the-loop first," but all also imply a relaxation mechanism; a product that only has "confirm" will be seen as "conservative but with no evolution path."
- Qualified answer: Define override-rate thresholds and observation windows per action category; for low-risk categories, use "undo" instead of "approval."

**Q7. Does your citation "guarantee it points to a real passage" or "guarantee the answer is faithful"? How is each tested?**
- Why ask: B2 — Anthropic Citations guarantees the former but not the latter; interviewers will press for a faithfulness number.
- Qualified answer: Server-side allowlist validation of citation pointers (already designed in S0) + Ragas-style faithfulness evaluation + refusal rate / false-refusal rate.

**Q8. Is this a workflow or an agent? Why not a simpler approach?**
- Why ask: H — Anthropic and OpenAI both say to start with the simplest option; packaging a workflow as an agent loses points.
- Qualified answer: "This is a workflow of prompt chaining + programmatic validation; we evaluated a single call + retrieval approach, whose Pass rate on [field X] was insufficient, so we added a validation step."

**Q9. If you remove your layer, what is left for the user? Why wouldn't a big company just build this?**
- Why ask: F3/G — the wrapper test + distribution disadvantage. A specific follow-up for the research lab assumption: how long would it take Feishu Minutes to add a "research mode"?
- Qualified answer: The moat rests on "a mandatory point in the workflow + a scenario-specific eval set + correction data," along with an explanation of why big companies lack the economic incentive to serve this niche (**evidence needed; it cannot be merely asserted**).

**Q10. What is the budget for cost and latency? Which path can be slow?**
- Why ask: E — interviewers will ask "which model do you use, why, and how much does it cost to process one meeting?"
- Qualified answer: Interactive Q&A takes the fast path, while post-meeting action item extraction takes the slow-but-accurate path (which can use a stronger model/evaluator-optimizer), with an estimated cost range per meeting (**real numbers pending measurement; must not be fabricated**).

**A reminder on the "research lab" candidate niche [Assumption]**: Its strengths are Q3 (experts are close at hand, and dogfooding is possible) and Q5 (correction data is easy to obtain); its risks are Q9 (the market is small, and big companies may not build it because it isn't worth it, rather than because they can't) and Q4 (the cost of failure may be too low, so users don't care about accuracy at all and the differentiation can't be monetized). These two points must be answered with user interviews and competitor error analysis, and cannot be presumed.

---

## 5. Source List

**Primary sources (original pages opened)**
1. Hamel Husain, *Your AI Product Needs Evals*, 2024-03-29 — https://hamel.dev/blog/posts/evals/
2. Hamel Husain, *Creating a LLM-as-a-Judge That Drives Business Results* (Critique Shadowing) — https://hamel.dev/blog/posts/llm-judge/
3. Hamel Husain, *LLM Evals FAQ* — https://hamel.dev/blog/posts/evals-faq/
4. Anthropic, *Building effective agents*, 2024-12-19 — https://www.anthropic.com/research/building-effective-agents
5. Anthropic, *Effective context engineering for AI agents*, 2025-09-29 — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
6. Anthropic, *Writing effective tools for agents*, 2025-09-11 — https://www.anthropic.com/engineering/writing-tools-for-agents
7. Anthropic, *Citations* docs — https://platform.claude.com/docs/en/docs/build-with-claude/citations
8. Google PAIR, *People + AI Guidebook: Explainability + Trust* — https://pair.withgoogle.com/chapter/explainability-trust/
9. Microsoft Research, *Guidelines for Human-AI Interaction* (Amershi et al., CHI 2019) — https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/
10. Shankar et al., *Who Validates the Validators?*, arXiv 2404.12272, 2024-04 — https://arxiv.org/abs/2404.12272
11. Ragas docs *Faithfulness* — https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/
12. Dwarkesh Podcast, *Andrej Karpathy — AGI is still a decade away*, 2025-10-17 — https://www.dwarkesh.com/p/andrej-karpathy
13. Tomasz Tunguz, *The Prompt as PRD*, 2024-10-21 — https://tomtunguz.com/the-prompt-as-prd/
14. Lenny's Newsletter, Aman Khan, *Beyond vibe checks: A PM's complete guide to evals*, 2025-04 (partially paywalled) — https://www.lennysnewsletter.com/p/beyond-vibe-checks-a-pms-complete
15. Lenny's Podcast, *Becoming an AI PM* (Aman Khan), 2024-11-14 — https://www.lennysnewsletter.com/p/becoming-an-ai-pm-aman-khan
16. Lenny's Podcast, *AI and product management* (Marily Nika), 2023-02-05 — https://www.lennysnewsletter.com/p/ai-and-product-management-marily
17. How I AI / Lenny's Newsletter, *Evals, error analysis, and better prompts* (Hamel Husain), 2025-10-13 — https://www.lennysnewsletter.com/p/evals-error-analysis-and-better-prompts
18. Aakash Gupta, *Master the AI Product Sense Interview*, 2025-10-30 (partially paywalled) — https://www.news.aakashg.com/p/ai-product-sense-interview
19. Fortune, *MIT report: 95% of generative AI pilots at companies are failing*, 2025-08-18 — https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/
20. Everyone Is a Product Manager (人人都是产品经理), 辛康在进化, "Want to become / switch to an AI PM? I dug through 54 JDs from top companies — my 6 big findings," 2026-01-17 — https://www.woshipm.com/zhichang/6326220.html
21. Everyone Is a Product Manager (人人都是产品经理), 思艺 Siyi, "Just finished interviewing for AI PM roles at 6 big companies — these 7 questions came up 100% of the time!," 2025-08-26 — https://www.woshipm.com/zhichang/6259398.html
22. Everyone Is a Product Manager (人人都是产品经理), 虫虫, "How should product managers provide a safety net for LLM hallucinations?," 2026-03-11 — https://www.woshipm.com/ai/6351155.html
23. Mianshima (面试马), JD.com "LLM Application Product Manager — Digital Employee Self-Evolution and Evaluation" JD (partially visible) — https://www.mianshima.com/job/9/170798
24. aced.io (formerly Exponent), *AI Product Manager Interview Questions* — https://www.aced.io/blog/ai-product-manager-interview-questions

**Secondary / paraphrased sources (original not opened, or only a summary seen)**
25. Maginative's paraphrase of OpenAI's *A practical guide to building agents* — https://www.maginative.com/article/how-to-build-ai-agents-a-detailed-practical-guide-from-openai/ (original PDF: https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf, binary could not be parsed)
26. MarkTechPost's paraphrase of Google's *Agents Companion* whitepaper, 2025-05-06 — https://www.marktechpost.com/2025/05/06/google-releases-76-page-whitepaper-on-ai-agents-a-deep-technical-dive-into-agentic-rag-evaluation-frameworks-and-real-world-architectures/
27. O'Reilly Radar interview with Marily Nika on three types of AI PM (403; search snippet only) — https://www.oreilly.com/radar/?p=17225
28. uxdesign.cc, *The autonomy dial* (HITL patterns, members-only article, summary only) — https://uxdesign.cc/the-autonomy-dial-a-pattern-toolkit-for-designing-human-control-over-ai-12bfbe23ca70
29. arXiv 2603.04445, *Dynamic Model Routing and Cascading for Efficient LLM Inference: A Survey* — https://arxiv.org/pdf/2603.04445
30. stackmatix, *Data Flywheel* (blog) — https://www.stackmatix.com/blog/data-flywheel ; arXiv 2510.27051 (NVIDIA NVInfo data flywheel paper) — https://arxiv.org/pdf/2510.27051
31. Blogs on AI wrapper moats from hatchworks / tianpan.co — https://hatchworks.com/blog/gen-ai/ai-wrapper-product-strategy/ ; https://tianpan.co/blog/2026-04-12-the-ai-wrapper-trap-when-your-moat-is-someone-elses-api-call

---
## 6. Confidence Notes for This Document

**High confidence (primary sources, original text verified)**
- The evaluation methodology in Domain A (three Husain pieces + the Shankar paper + the visible portion of the Khan article). The numbers (30/100/60/100–200 items, the 10-20/40-45/40-45 split, TPR/TNR, 60–80% of time) all come from the original texts.
- The PAIR principles in Domain C, and the quoted sentences in the original wording.
- The key points and quotations from the three Anthropic pieces in Domains D/H.
- The Citations document limits in Domain B2.
- The Karpathy quotation (from the second half of the Dwarkesh transcript).
- The three domestic woshipm articles and the company/role/keyword table from the 54 JDs.

**Medium confidence (primary but truncated by a paywall, or secondary with a clearly identified source)**
- The "workflow" section of the Khan evals article, the details of Gupta's three-layer framework, and the Lenny/Nika episode (summary only, no transcript).
- The content of the OpenAI guide and the Google Agents Companion comes entirely from secondhand paraphrases.
- The MIT NANDA 95% figure comes from Fortune's reporting; the report's methodology has not been verified.
- For Microsoft's 18 guidelines, only "there are 18, grouped into four categories, CHI 2019" has been verified; the individual items have not.

**Low confidence (blog/vendor opinion, used only as a reference for "industry consensus")**
- Claims about wrappers, data flywheels, and moat ranking in Domains F3/F4/G; "eval assets compound" comes from a single blog source.
- The percentage savings from routing/cascading.
- Gupta's "Google dropped the PM technical interview" and the specific naming of Nika's three prototype types.

**All [Inference] and [Assumption] items in this document** (especially the "one-sentence conclusion" in Section 0, Domain C4, the four types of moats in Domain G, and the reminder to research labs in Section 4) are the author's own synthesized judgments, **not quotations from the sources**, and should be validated in later user interviews and competitor error analysis.

**Research limitations**: The WebSearch quota for this round ran out after about 20 queries, so the following could not be searched further: the full original JD text from the official ByteDance/Alibaba/Tencent/Baidu sites (only third-party aggregations are available); the official OpenAI evals documentation; the original text of Microsoft's 18 guidelines; HCI research on automation bias / overreliance (e.g., Buçinca et al.'s cognitive forcing studies); and the original Sequoia/a16z pieces on AI application moats. These can be filled in during the next round.
