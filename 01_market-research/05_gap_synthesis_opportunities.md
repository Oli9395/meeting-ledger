---
title: "Market Research 05 — Cross-File Gap Synthesis and Differentiation Opportunity List (Gap Synthesis)"
status: draft (revised in place, Round 2, following review 06)
sources_count: 83
---

# Market Research 05: Cross-File Gap Synthesis — Everyone Has Built It, So What Small Piece Is Left?

> **Reading notes**
> - This document is a **secondary synthesis**, not new primary research. The input is the 13 research files in this directory (`00_pm-skills/01–05`, `01_market-research/01–04`, `02_user-research/01–04`), all read in full, plus the 75 candidate gaps submitted by the individual research agents.
> - Labeling rules are the same as in the rest of the project: **[Fact]** has a source URL; **[Inference]** is derived from multiple facts without direct evidence; **[Assumption]** awaits interviews or experiments; **to be verified** means the source is secondhand, a search snippet only, or contradictory.
> - Each conclusion is followed by its **evidence source files** (abbreviations in the table below). Key facts also carry the original URL, so you can skip the intermediate files and check directly.
> - **Only 1 item was newly verified this round**: Fellow's official action items page (opened with WebFetch). The plan also called for checking Otter's pre-meeting briefs, Zoom AI Companion's cross-meeting tracking, and others, but the whole round's shared WebSearch quota (200 queries) was exhausted, so these could not be run. They are listed in §6 Open Questions.
> - All scores are the researcher's judgment based on current evidence, **not measurements**, and are used only for ranking.
> - **Round 2 revision note **: This document was revised in place per `06_research_integrity_review.md` §1, §6, and §9 P0-4, covering K3, K5, K8, K11, K12, G3–G6, G17, G20, and the differentiation wording of Options B and C. Overturned claims are kept as ~~strikethrough~~ with "(correction: …)" next to them. A new label, **[Summary]** = only a search snippet was seen and the original page was not opened; it is no longer grouped with [Fact]. All changes are listed in the "Revision Log (Round 2)" at the end.

| Abbreviation | File |
|---|---|
| **M1** | `01_market-research/01_competitors_china_feishu_minutes.md` |
| **M2** | `01_market-research/02_competitors_global_otter_fireflies_granola.md` |
| **M3** | `01_market-research/03_competitors_research_lab_tools.md` |
| **M4** | `01_market-research/04_user_complaints_unmet_needs.md` |
| **U1** | `02_user-research/01_segment_academic_labs.md` |
| **U2** | `02_user-research/02_segment_other_candidates.md` |
| **U3** | `02_user-research/03_research_commitment_tracking_specifics.md` |
| **U4** | `02_user-research/04_cross_cutting_constraints.md` |
| **S1–S5** | `00_pm-skills/01–05` (PM fundamentals, product discovery, differentiated positioning, AI PM, competitor/PRD/demo methods) |

---

## 0. Conclusions First (Answer First, Then the Reasoning)

1. **[Fact] None of the following can be treated as a selling point any more**: meeting → action items (20+ products have it, including Feishu, DingTalk, Tencent Meeting, Otter, and Fireflies); citations or provenance (Feishu, iFlytek, Notion, Teams, and Read have it); human confirmation before publishing (tl;dv "for review before sending"; Feishu's "AI action items" and "formal tasks" are already two separate layers); no bot (Granola, Notion, Circleback, and others); no training on user data (Fireflies, Feishu, Granola Enterprise); local transcription (Krisp English, anarlog, Meetily). Evidence in M1 §0, M2 §0/§6, U4 §4.
2. **[Fact, newly verified this round] "Cross-meeting commitment tracking" is not an empty space either.** Fellow's website states that before each recurring meeting it will "surface outstanding action items from previous sessions" and that it "tracks whether items are still open and resurfaces them before the next relevant meeting" (https://fellow.ai/features/action-items , opened at the time of writing). In addition, Otter's and Granola's pre-meeting briefs bring back action items from the last meeting (M2 §3.1/§3.5), Littlebird has personal commitment tracking (M2 §3.17, U2 §2.14), Procore automatically carries over leftover items (U2 §2.10), and Zoom AI Companion 3.0 offers "track cross-meeting projects" (M2 §3.8; note added at the time of writing: this quote comes only from a search snippet of a press release, so it is relabeled [Summary·to be verified]; the official site says "ZoomMate project agent to track progress", 06 V10). Also (added at the time of writing), Feishu's "Meeting Digest" aggregates action items from "the smart minutes of the last week" (https://www.feishu.cn/content/article/7577317993749269689 ), so the Chinese vendors are no longer an entirely blank row either. **The "cross-meeting commitment status tracking" row marked ○ throughout in the M1 feature matrix holds only for Chinese vendors and cannot be generalized to the whole market.** M4 said at the time "Fellow to be verified"; we can now conclude that someone has already built it.
3. **[Inference] What is still open is the three-layer semantics "after the commitment", not "whether there is tracking".** Existing products track ~~**binary status** (open/done)~~ **mostly binary status** (correction: Littlebird's commitment tracking already has three states, Kept / In progress / Needs a note, and checks against "the email that went out, the document that shipped"; Fellow syncs issue status bidirectionally with GitHub via Zapier. Sources: https://littlebird.ai/routines/promise-tracker , https://fellow.ai/integrations/github , accessed at the time of writing) and **unilateral assignment** (by the AI or the host). Three things have not been done thoroughly:
   - **Verifiable**: every commitment can be traced back to the original sentence, speaker, and timestamp within 3 seconds; anything without support is not output; missing fields are not guessed (M4 categories A/C, M1 §9).
   - **Claimed**: the named person confirms, reschedules, or declines it themselves, rather than the AI or the PM claiming it on their behalf (M4 category D).
   - **With an outcome**: on completion, fill in "what the result was and where the evidence is", not just tick a box (U3 §3.2, U2 §4 Top 2). (correction: the generic version of "with an outcome" is already partly covered by Littlebird's evidence comparison. The remaining room lies only in **research-outcome semantics** (supported / refuted / inconclusive / abandoned / superseded, [Assumption·to be validated]) and **experiment-artifact evidence** (W&B run, config, data version); see K5, G5.)
4. **[Inference] The gaps with the strongest evidence are horizontal (everyone needs them) but are also the easiest for large vendors to fill; the gaps with weaker evidence are niche-scenario ones (research, client–vendor, mixed Chinese–English) that large vendors are structurally unlikely to address.** This is the core trade-off of this round. The five combination options in §4 unfold along this tension line: from a pure feature play (a horizontal "verifiable commitment layer") to a pure user play (doctoral-student/advisor 1-on-1s), with several hybrids in between.
5. **[Inference] "Publicly reproducible action item evaluation" is the proof mechanism shared by all options.** Among the 24 products covered by M1 and M2, none publishes precision, recall, or owner accuracy for action item extraction. This is not itself a user pain point (users want "something they dare to trust", not "metrics to look at"), but it turns any differentiation claim into a **measurable gap** (S4 Q1/Q2). It is also the hardest part of the interview narrative to rebut.
6. **[Assumption] Recommended order for the next round of validation**: first run an error analysis of competitors' real outputs, using 30–100 synthetic group-meeting and requirements-meeting samples through Feishu Minutes, Tongyi Tingwu, and Otter (S4 Q2, M1 §10.6); at the same time run a 2-week diary study to measure "commitment frequency × 48-hour miss rate" (S2 §3.4). These two efforts decide which combination in §4 survives. **Until they are complete, every ranking in this document is only an "order worth validating first", not a conclusion.**

---
## 1. Method: How We Merged and Scored

### 1.1 Merge Rules
- The 75 candidate gaps were clustered by "**the job the user is trying to get done**", not by feature name. For example, "cross-meeting commitment ledger", "automatic review at the next meeting", and "advisor 1-on-1 open items" were first grouped into one family, then split by semantic depth (binary tracking and outcome backfill are two different things).
- Pure methodology items (such as "the internal FAQ in a PR/FAQ must answer why we are still doing this" and "compress the demo into one magic moment") do not enter the requirements list. They go into §5 (how to prove it).
- **Internal capabilities or moats** such as "user corrections flow back into the evaluation set" and "progressive automation" are labeled separately as "moat-type" and placed at the end of the list, because they are not needs users can perceive.

### 1.2 Scoring Rules (four dimensions multiplied, maximum 625)
| Dimension | 1 point | 3 points | 5 points |
|---|---|---|---|
| **E Evidence strength** | Inference only, or a single vendor source | 2–3 independent sources, or indirect evidence from policies/guidelines | ≥3 independent first-hand sources, with direct quotes or official documentation |
| **P User pain** | Minor annoyance | Requires rework or manual fallback | Causes real losses, lawsuits, or abandonment, or is mandated by policy |
| **U Uncovered degree** | Mainstream products have largely solved it | Partly done by some products | No product in this round's search scope does it |
| **D Demo feasibility** | Requires real data from multiple parties or strict compliance access | Needs synthetic data plus a small amount of real material | Doable in 2–4 weeks with text input and the existing S0 architecture |

**Why multiply instead of using a weighted sum**: If any one dimension is close to 0 (for example, no evidence at all, or already fully done by competitors), the opportunity should not rank near the top. Multiplication exposes such a weak spot; a weighted sum would mask it. The cost is greater sensitivity to scoring error on any single dimension, so score differences within 30 points should be treated as the same tier.

---

## 2. Summary Table of Competitors' "Common Shortcomings" (China + international + research tools, three lists merged and de-duplicated)

> Legend: **Yes** = public evidence exists; **Partial** = limited, or claims conflict; **Not seen** = did not appear in the pages crawled this round (≠ confirmed absent).

| # | Common shortcoming | Products that have it / partly do it | Products where not seen | Evidence (file + original URL) | Assessment |
|---|---|---|---|---|---|
| K1 | **No public disclosure of action-item extraction quality** (precision, recall, owner and due-date accuracy) | None (only vendor self-reported transcription accuracy, e.g., DingTalk claims 97–98%) | Feishu, Tencent, DingTalk, iFlytek, Tongyi Tingwu, Notion, WPS, Huawei, Xiaomi, Otter, Fireflies, Fathom, tl;dv, Granola, Read, Circleback, Zoom, Teams, Gemini, Krisp, and others, 24 products in total | M1 §8–§9 (https://www.leiphone.com/category/CorporateServices/laMyPOOWyk7FzjEa.html ); M2 §7 #1 | **[Fact: not found in search]**, the whole row is blank; confidence medium ("not published" ≠ "does not exist") |
| K2 | **Silently fills in a missing owner or due date** instead of leaving it blank for confirmation | Feishu: when missing, "users can add it manually" (partial) | DingTalk, in hands-on testing, defaults to assigning the meeting organizer; Tencent Meeting action items do not name an owner (summary, to be verified); others not stated | M1 §4.2 (https://www.woshipm.com/share/6269848.html ); Weibo article https://weibo.com/2/detail/comos:niwmapc3412577 ; M4 category C | **[Fact]** Only one hands-on test, of DingTalk; "big vendors tend to fill every field" is an [Inference] |
| K3 | **Does not distinguish commitment strength** (firm commitment / suggestion / under discussion / assumption) | ~~None~~ **Partial: Littlebird's commitment tracking captures only explicit commitments ("I'll send", "we'll decide"); "Vague maybes are left alone unless you ask for them"** (correction: originally written as "None") | ~~All~~ Not seen in other products (DingTalk generates action items directly from "conclusions") | M1 §9 #3; U1 §5; U3 §2.2; 06 V5 (https://littlebird.ai/routines/promise-tracker , accessed at the time of writing) | ~~**[Inference]** No counter-evidence, but no direct search either~~ **[Fact]** A basic binary version of "explicit commitment vs. vague statement" already exists; **[Inference]** multi-level strength (suggestion / under discussion / assumption) plus publicly evaluable tiering is still not seen within the search scope |
| K4 | **Assigned by AI or the host; the named person does not claim it** | Teams only "suggests"; tl;dv has the sender review | Fireflies "Create tasks automatically"; Krisp "automatically assigns"; Otter "assigns next steps automatically" | M2 §3.1/§3.2/§3.12/§7 #2; M4 C3–C4, D1–D5 (https://collab365.com/library/microsoft-365-productivity/teams-meeting-recaps-create-notes-but-actions-stil-IrSTUa ) | **[Fact]** Automation-first is the official wording; "lack of self-claiming by the person" is an [Inference] |
| K5 | ~~**Task completion is only a binary state, with no outcome or evidence recorded**~~ **Task completion is mostly binary; generic evidence comparison has appeared, but research-outcome semantics and experimental evidence are not seen** (correction) | Littlebird checks whether the email or document has been sent (partial); **added at the time of writing: outputs three states, Kept / In progress / Needs a note, comparing against "the email that went out, the document that shipped, the message that never did"**; **Fellow syncs bidirectionally with GitHub via Zapier, "any addition or status change moves across systems in real time"** | Feishu action items sync only completion status; Fellow's action-items page says only "mark them complete" and "tracks whether items are still open"; ELNs have no meeting object | U3 §1, §3.2 (Feishu https://www.feishu.cn/content/article/7602953888668339380 ); U2 §2.14 (https://littlebird.ai/routines/promise-tracker ); Fellow https://fellow.ai/features/action-items ; Fellow × GitHub https://fellow.ai/integrations/github (all accessed at the time of writing); 06 V4 | **[Fact]** "Only binary, no evidence" has been weakened; **[Inference]** research needs five values (supported / refuted / inconclusive / abandoned / superseded), with evidence linked to a W&B run/config/data version; this remains an [Inference] (U3 self-assessment) |
| K6 | **Cross-meeting commitment tracking** (bringing last meeting's commitments back before the next meeting) | **Yes**: Fellow (carries unfinished items into recurring meetings), Otter and Granola pre-meeting briefs, Littlebird (personal), Procore (construction), Zoom 3.0 templates (claimed); partial: Feishu "Meeting Express", Tingwu multi-file Q&A | Chinese vendors: none seen; Gemini produces only a single Doc | M1 §8; M2 §3.1/§3.5/§3.8/§7 #8; U2 §2.10; **Fellow verified this round** | **[Fact] Not a blank space.** International products already cover the binary version; the remaining gap is only "team-level + outcome backfill + evidence links" |
| K7 | **Citations reach only the "key point" or "answer" level**, not "each commitment → original sentence + speaker + timestamp" | Yes: Feishu key points with timestamps, iFlytek minutes traceability, Notion hover citations, Teams/Read answers with citations; partial: Tencent's claims conflict | Otter, Fireflies, Fathom, Granola, Circleback not seen | M1 §2.2 (https://www.feishu.cn/content/article/7577317993749269689 ), §5; M2 §6; M4 category A | **[Fact]** Traceability is becoming standard; whether "per-commitment, sentence-level" is already achieved is **to be tested hands-on** |
| K8 | **Local or offline processing is almost nonexistent**; "no bot" ≠ "not in the cloud" | Partial: Krisp (on-device transcription in English only; verified at the time of writing: "supports on-device English transcription", see https://krisp.ai/ai-meeting-assistant/ ; the pricing page lists "Private Transcription & Recordings (On-device)" only under Enterprise; **Chinese is not among the 16 supported languages**, https://krisp.ai/pricing/ ); yes: anarlog, Meetily (open source, personal tools) | Otter, Fireflies (dedicated cloud), Granola (cloud pipeline), Notion (explicitly no offline support), Feishu and other Chinese vendors | M2 §7 #4 (https://www.granola.ai/security ; https://krisp.ai/pricing/ ); U4 §4, §6 (https://github.com/Zackriya-Solutions/meeting-minutes ) | **[Fact]** Commercial products leave a gap; open source has it, but open source only goes as far as "transcription + summary" |
| K9 | **Consent burden shifted to the user**, with no "participant control" (decline, do not record, redact before sending) | Partial: Notion (voice announcement, can be enforced), Gemini (notifies all participants), Granola (automatic consent message, must be enabled manually) | Off-the-record segments and pre-send redaction: none seen | M2 §3.11, §4.3; M4 category B, W6/W7; U4 §3.2 (Granola complaint https://ppc.land/granola-sued-for-recording-meetings-without-consent-to-train-ai-models/ ) | **[Fact]** The problem is strong (two class actions, bans at multiple schools); the value of the solution is an [Assumption] |
| K10 | **Ecosystem lock-in / unusable across organizations** | Tingwu and iFlytek are independent of IM (but have no action-item loop) | Teams Copilot is unavailable in meetings hosted by an external organization; Feishu external recordings do not trigger voiceprint recognition (summary); Tencent's AI depends on Tencent Meeting | M1 §9 #5; M2 §3.9 (https://support.microsoft.com/en-us/office/use-copilot-in-microsoft-teams-meetings-0bf9dd3c-96f7-44e2-8bb8-790bedf066b1 ) | **[Fact]** |
| K11 | ~~**Integrations center on sales CRM**, with no GitHub Issues, W&B, Overleaf, or Zotero~~ **Engineering-tool integrations (GitHub, Linear, Jira) are no longer a gap; W&B, Overleaf, and Zotero are still not seen** (correction) | Partial: Read and Circleback support Linear; Otter and Zoom support Jira; **yes (added at the time of writing): Fellow syncs bidirectionally with GitHub (via Zapier; an action item newly assigned in a meeting "instantly opens an issue in a specified GitHub repository"); Granola connects to GitHub, Linear, Jira, and Asana via Zapier; Circleback, Read, Otter, and Granola offer MCP or Claude integration** | ~~None of the pricing pages crawled this round lists GitHub Issues~~ W&B, Overleaf, Zotero: not seen within the search scope | M2 §7 #6; M3 §7; U3 §4; 06 V1, V2 (https://fellow.ai/integrations/github ; https://www.granola.ai/integrations ; https://circleback.ai/integrations ; https://www.read.ai/integrations ; https://otter.ai/integrations , all accessed at the time of writing) | ~~**[Fact: within the scope seen]**~~ **[Fact]** GitHub integration already exists; **[Inference]** once MCP becomes common, "integration" itself is not a moat, only an expected feature |
| K12 | **Mixed Chinese-English speech and terminology are "English-first"**, and glossaries are not productized | Partial: Feishu transcribes in the original language, iFlytek handles mixed Chinese/English/Cantonese, AssemblyAI natively supports English-Mandarin switching as of 2026-08, Granola lists Mandarin | Notion speaker labeling supports English only; Krisp local mode supports English only (and Chinese is not among its supported languages); **Gemini in Meet has no Chinese among its supported languages, and "Multiple languages spoken in the same meeting aren't currently supported"; Teams Facilitator AI notes "only support meetings where a single language is spoken"** (added at the time of writing); Deepgram's switching does not include Mandarin; Huawei supports Mandarin only; ~~no product does the glossary → correction → recall-rate chain~~ (correction: Feishu already has "enterprise information recognition", which can recognize "rare characters in colleagues' names and project names"; the original "no product does this" wrote "not verified" as "does not exist"; a **project-level glossary + public term-recall rate** is still not seen within the search scope) | M1 §9 #6; M2 §7 #7; U4 §2.1–§2.2 (https://arxiv.org/html/2502.18913 ; https://assemblyai.com/blog/universal-3-5-pro-code-switching-contextual-prompting ); 06 V8, V9, V11–V13 (https://support.google.com/meet/answer/14754931 ; https://learn.microsoft.com/en-us/microsoftteams/facilitator-teams ; https://www.feishu.cn/content/article/7577317993749269689 , all accessed at the time of writing) | **[Fact]** "Mixed-language support" is being filled in (Feishu recognizes by original language), and international platform products (Gemini, Teams Facilitator) officially acknowledge single-language limits; ~~"term recall rate" is a gap~~ **[Fact: not seen within the search scope]** a public "project-level term-recall rate" |
| K13 | **Research tools have no "meeting" object; meeting tools have no "research object"** | Fabric academic labs (marketing page, no case studies); Research Lab Hub (rating 0); LabRAT (personal project) | ELNs (eLabFTW, SciNote, LabArchives, Labguru, Benchling) have no meeting object; meeting tools have no objects such as hypotheses, experiments, or success criteria | M3 §3–§4 (https://fabric.so/teams/academic-labs ); U3 §2.2 | **[Fact + Inference]** |
| K14 | **Outputs a full summary per single meeting**, without slicing by person or by project | Partial: tl;dv cross-meeting reports, configurable templates | Per-person push of "you have N commitments": not seen; organizing by project across meetings: no mainstream product seen emphasizing this | M4 category H, category I (https://news.ycombinator.com/item?id=48823024 ; https://news.ycombinator.com/item?id=44725306 ) | **[Inference]** Evidence is medium |
**How to read this table [Inference]**
- Only **K1 (public quality)**, ~~**K3 (commitment strength)**~~ (corrected at the time of writing: Littlebird already skips vague commitments, so K3 is downgraded to "partial"), and the sub-items under K9 and K12 (off-the-record, topic-level terminology recall) are entirely blank. These items are either a "means of proof" or need user research to confirm their value.
- **K6 is the most important correction this document makes to earlier files**. We can no longer say "nobody does cross-meeting tracking"; we have to say "some tools track status, but nobody tracks **outcomes and evidence**, and nobody lets **the person named** claim an item."
- K8, K9, and K12 are cross-cutting constraints; none of them is a moat on its own (the overall judgment in U4), but they stack up in the niche of "mixed Chinese-English + highly sensitive + offline."
- **(Added at the time of writing) K11 is overturned, and K5 and K3 are weakened.** The pattern: gaps of the "does the feature exist" kind get filled quickly, while "constraint" gaps (multilingual, cross-organization, local, consent) are instead confirmed by official documentation (06 §1 summary).

---

## 3. Merged Table of Unmet Needs (21 items after deduplication, ranked by E×P×U×D)

### 3.1 Ranking Overview

| Rank | ID | Opportunity (one sentence) | Type | E | P | U | D | Score | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | G1 | Public, reproducible action-item extraction benchmark + competitor error analysis | Feature (means of proof) | 4 | 3 | 5 | 5 | **300** | Medium-high |
| 2 | G2 | Every commitment verifiable within 3 seconds: original sentence + speaker + timestamp; no output without evidence | Feature | 5 | 5 | 2 | 5 | **250** | High (need) / Medium (differentiation) |
| 3 | G3 | Don't guess missing fields + commitment-strength tiers | Feature | 3 | 4 | 4 | 5 | **240** | Medium |
| 4 | G4 | The named person claims the item themselves (confirm, reschedule, decline) | Feature | 3 | 4 | 4 | 4 | **192** | Medium |
| ~~4~~ about 11 (after correction) | G5 | Commitment → outcome → evidence loop (five-value outcome + run/commit/log links) | Feature (research or R&D semantics) | 3 | 4 | ~~4~~ 3 | 4 | ~~**192**~~ **144** | Medium (corrected at the time of writing: Fellow's GitHub sync and Littlebird's evidence comparison each cover half, so U is lowered; see §3.2 G5) |
| 4 | G6 | Two-way commitment ledger for advisor 1:1s + advisor confirmation gate | User | 3 | 4 | 4 | 4 | **192** | Medium |
| 4 | G7 | Consent first: pre-recording notice, off-the-record segments, redaction before sending | Feature | 4 | 4 | 3 | 4 | **192** | Medium (problem) / Low (solution) |
| 4 | G8 | Mixed Chinese-English error correction driven by a topic glossary + terminology recall rate | Feature | 4 | 3 | 4 | 4 | **192** | Medium |
| 9 | G9 | Research object model: hypotheses, experiments, success criteria, advisor suggestions, reviewer comments | Both | 3 | 3 | 5 | 4 | **180** | Medium-low |
| 9 | G10 | Embed into existing weekly-report slots: draft "done / issues / plan" from this week's meetings | User | 4 | 3 | 3 | 5 | **180** | Medium-high |
| 11 | G11 | Cross-meeting commitment tracking (binary version) | Feature | 4 | 4 | 2 | 5 | **160** | High (need) / **Low (differentiation)** |
| 12 | G12 | Sourced, refusable decision-retrieval Q&A (rationale quotes original words only) | Feature | 3 | 3 | 3 | 5 | **135** | Medium |
| 12 | G13 | Text-first / non-audio input (post-meeting Markdown, whiteboard photos, phone transcripts) | Feature | 3 | 3 | 3 | 5 | **135** | Medium |
| 12 | G14 | Few and accurate, pushed per person (decisions / my commitments / open questions) | Feature (experience) | 3 | 3 | 3 | 5 | **135** | Medium |
| 15 | G15 | Client-vendor requirements meetings: requirements baseline diff + counterparty confirmation sheet | User + Feature | 2 | 4 | 4 | 4 | **128** | Medium-low |
| 16 | G16 | Open-source communities: write meeting decisions back to existing issues/PRs, confirmed by maintainers | User + Feature | 3 | 2 | 4 | 5 | **120** | Medium |
| 17 | G17 | PI-wide commitment board (who is blocked, who is overdue, what I owe whom) | User | 3 | 4 | 3 | 3 | **108** | Medium-low (corrected at the time of writing: the evidence claim "Littlebird only does individuals" does not hold, but its commitment tracking is still an individual view, so U stays at 3; see §3.2 G17) |
| 17 | G18 | Cross-ecosystem, cross-organization, low lock-in (multi-platform meetings + offline) | Both | 4 | 3 | 3 | 3 | **108** | Medium |
| 19 | G19 | Data never leaves the device (local ASR + local LLM) | Both | 4 | 3 | 2 | 4 | **96** | Medium |
| ~~20~~ 21 (after correction) | G20 | Organize by topic + Markdown/Obsidian/GitHub export and integration | Feature | 3 | 2 | ~~3~~ 2 | 5 | ~~**90**~~ **60** | Low (corrected at the time of writing: GitHub integration is already covered by Fellow and Granola, so U is lowered) |
| 21 | G21 | [Moat category] User corrections fed back into the benchmark set + progressive automation | Feature (internal) | 2 | 2 | 4 | 5 | **80** | Medium-low |

**Why the ranking looks like this [Inference]**: The top three (G1–G3) have strong evidence and cheap demos, but they are all **horizontal features** that large vendors can follow. About half of the fourth tier consists of **niche semantics** (G5, G6, G8); their U scores are high because large vendors structurally don't do them, but their E scores are low because first-hand user evidence is lacking. G11 has high pain and strong evidence, but because Fellow and others already cover it, it drops to 11th. This shows that "the need is real" and "it can be differentiated" are two different things.

**(Corrected at the time of writing)** Per the checks in 06 V1 and V4, G5's U is lowered from 4 to 3 (144 points, landing around 11th), and G20's U is lowered from 3 to 2 (60 points, landing last). In the table, only these two rows have annotated rank cells; the ranks of the other rows were not reshuffled, to avoid breaking references from earlier files. **The fourth tier now contains only four items: G4, G6, G7, and G8.** In addition, G3's U=4 may be too high (Littlebird already makes an explicit / vague distinction); the score is left unchanged this round and handed to `03_positioning` for review.
### 3.2 Item-by-Item Notes

> Each item follows the same structure: opportunity description → type → evidence (source file + original URL) → counterarguments (why it might be a false need, or why big vendors could ship it quickly) → confidence. The source agent IDs after each heading indicate which candidate gaps were merged into it.

#### G1 Public, reproducible action-item extraction evaluation + competitor error analysis (from comp-china, comp-global, skills-ai-pm ×2, skills-pm-core, user-multilingual-offline)
- **Opportunity**: On the same set of 30–100 synthetic or anonymized meeting samples, report field-level metrics: owner accuracy, due-date accuracy, "no-guess-on-missing rate", fabrication rate (people or dates that do not appear in the source), and terminology recall. Run Feishu Minutes, Tongyi Tingwu, and Otter on the same samples, rank by failure-mode frequency, and phrase the differentiation as "In scenario X, we reach a Pass rate of a% on field Y, versus b% for the comparison."
- **Type**: Feature differentiation (more precisely, a **proof mechanism** and a trust selling point).
- **Evidence**:
  - [Fact] Of 24 products, none publishes action-item quality (M1 §8, last two rows; M2 §7 #1).
  - [Fact] Husain argues that differentiation comes from error analysis, and that priorities should be ranked by failure frequency (https://hamel.dev/blog/posts/evals-faq/ , S4 §2 A2).
  - [Fact] Major Chinese vendors already have dedicated "LLM evaluation PM" roles (https://www.woshipm.com/zhichang/6326220.html , S4 §1.2).
  - [Fact] There is no mixed Chinese-English benchmark that covers commercial meeting products (U4 §2.1).
- **Counterarguments**:
  1. Users will not switch tools just because metrics exist; metrics impress interviewers and procurement teams, not end users.
  2. Big vendors can publish an evaluation blog at any time; also, building one's own evaluation set invites the suspicion of being both player and referee, so the samples and labeling rules must be made public.
  3. The representativeness of synthetic samples will be questioned.
- **Confidence**: Medium-high ("nobody has published this" is a search-based conclusion; "valuable" mainly refers to value for the portfolio and interviews).

#### G2 Every commitment verifiable within 3 seconds (from comp-complaints #1, skills-positioning, skills-discovery, comp-china)
- **Opportunity**: Every decision or commitment comes with the original sentence excerpt, the speaker, and a timestamp (a paragraph anchor for text input); one click lets the user check it; items without supporting evidence are not output (continuing S0's citation allowlist and refusal principle).
- **Type**: Feature differentiation.
- **Evidence**:
  - [Fact] HN users say tools of this kind "plausibly mishear the parts that matter most", with examples of clinical information being dropped outright and statements attributed to people who never said them (https://news.ycombinator.com/item?id=48823024 , M4 A1–A3).
  - [Fact] Zoom AI Companion's summary missed the workshop's conclusions (https://www.writingclearscience.com.au/ai-meeting-summary/ ).
  - [Fact] M4 gave this category the highest score, 60.
- **Counterarguments**:
  1. **This is already becoming a basic (Kano) feature**: Feishu offers "precise action-item recognition with source-text tracing", iFlytek has "minutes tracing", and Notion has hover citations (M1 §0 item 2). The remaining gap may be only "granularity" and "refusal to answer", which a big vendor could close in one iteration.
  2. Users say they want verification, but may not actually click through (M4 category H, "nobody reads the minutes").
- **Confidence**: High on the need; **medium** as a differentiator. On its own it is not enough to answer "why build this anyway".

#### G3 No guessing on missing fields + commitment-strength tiers (from comp-china ×2, skills-ai-pm "restricted-input exposure", user-academic-lab soft commitments)
- **Opportunity**: When the owner or due date is not clearly stated, explicitly mark it "to be confirmed" and do not fill in a default; label each item with a strength level (firm commitment / suggestion / under discussion / hypothesis), so that "should we try swapping the backbone?" does not become an action item.
- **Type**: Feature differentiation.
- **Evidence**:
  - [Fact] In a hands-on test, DingTalk "automatically assigned the task to the meeting organizer by default" (https://www.woshipm.com/share/6269848.html ).
  - [Fact] A Weibo article points out that AI "fills in" owners and nonexistent dates (https://weibo.com/2/detail/comos:niwmapc3412577 ).
  - [Fact] PAIR: "Don't say 'what' without saying 'why' in a high stakes scenario" (https://pair.withgoogle.com/chapter/explainability-trust/ ).
  - [Inference] Soft commitments make up a high share of research discussions (U1 §5, U3 §2.2).
  - **[Fact, added at the time of writing]** Littlebird's promise tracking only captures explicit commitments; "Vague maybes are left alone unless you ask for them" (https://littlebird.ai/routines/promise-tracker , accessed at the time of writing). So G3 can only claim "multi-level strength tiers + evaluability", and **cannot claim "nobody does this"** (06 V5).
- **Counterarguments**:
  1. The DingTalk evidence is a single article, dated 2025-09, and may have been fixed since (M1 credibility table).
  2. Strength tiering depends on model judgment; one misclassification can drop a real commitment, so recall must be evaluated.
  3. Adding a "to be confirmed" tag is very cheap for a big vendor.
  4. Users may find too many "to be confirmed" items annoying, which adds burden instead.
- **Confidence**: Medium.

#### G4 Self-claiming by the named person (from comp-complaints #2, comp-global "low-cost in-meeting tagging")
- **Opportunity**: After the meeting, push a "you have N commitments" notice to each person who was named; they can confirm, reschedule, or decline; only after confirmation does an item become a formal task. In offline single-microphone scenarios, "self-claiming" replaces voiceprint recognition and sidesteps the speaker diarization problem.
- **Type**: Feature differentiation (also an interaction-paradigm difference, similar to Granola putting the human back in the loop).
- **Evidence**:
  - ~~[Fact]~~ **[Summary, to be verified]** Teams training materials position recap action items as "suggestions, not authoritative assignments" (M4 C4, search summary, to be verified). (Corrected at the time of writing: this item comes only from a search summary, so it is relabeled [Summary]; it may also be outdated, since Microsoft Teams Facilitator already offers "Task tracking integration with Planner" (public preview) and "Mobile capture of ad-hoc discussions and action items", https://learn.microsoft.com/en-us/microsoftteams/facilitator-teams , accessed at the time of writing.)
  - **[Fact, added at the time of writing]** Fellow's action-items page says "assign action items to specific attendees either during or after the meeting", and supports reassignment and multiple owners, **but does not mention the assignee confirming or accepting** (https://fellow.ai/features/action-items , accessed at the time of writing). G4 is still not seen on Fellow's page, but only one vendor has been checked (06 V6).
  - [Fact] Some people report "I have Teams recaps but still do not know who owns the actions" (Collab365, M4 C3).
  - [Fact] In a 7-person team, at least 1/3 of AI action items were untouched three weeks later (https://www.lilachbullock.com/ai-meeting-notes-accountability-small-teams/ , **a personal estimate, not a statistic**).
  - [Inference] The underlying mechanism is diffusion of responsibility (M4 category D).
- **Counterarguments**:
  1. It requires **every attendee** to be in the system, which creates cold-start and network-effect problems; a single-person demo can hardly show the real effect.
  2. Named people may find it annoying and not click, which would lower the completion rate.
  3. Fellow already supports "assigning during or after the meeting, and reassigning", which is only one step short of "claiming".
- **Confidence**: Medium.
#### G5 Commitment → Result → Evidence Loop (from user-research-commitments F1, comp-research-tools, user-other-segments hardware, comp-research-tools GitHub)
- **Opportunity**: Before the next meeting, list the "commitments awaiting a result," and require a five-value result (supported / refuted / inconclusive / not run / superseded) plus one evidence link (W&B run, commit, config, test log), rather than just a checkmark. The enhanced version automatically looks for matching evidence in test logs or Git (U2 Top 2).
- **Type**: Feature differentiation (fine-grained semantics), naturally tied to research or R&D teams.
- **Evidence**:
  - [Fact] MIT's Cahoy advising policy requires "reviewing these items at subsequent meetings" (https://aeroastro.mit.edu/wp-content/uploads/2022/03/AdvisingPhilosophy.Cahoy_.2019.pdf ).
  - [Fact] Imperial's supervision agenda opens with "progress since the last meeting" (M3 source 37).
  - [Fact] A Duke case says the biggest obstacle is "members don't update and need continuous supervision" (https://pmc.ncbi.nlm.nih.gov/articles/PMC12401938 ).
  - [Fact] Feishu action items only sync a binary status (U3 §1).
  - ~~[Fact] Fellow only tracks open/closed (verified this round).~~ (Corrected at the time of writing: The Fellow action-items page itself does only say "mark them complete" and "tracks whether items are still open", but Fellow syncs **bidirectionally** with GitHub via Zapier: "Updates made in Fellow will reflect in GitHub automatically", so engineering teams' status already flows back automatically. Sources: https://fellow.ai/features/action-items , https://fellow.ai/integrations/github , accessed at the time of writing.)
  - **[Fact, added at the time of writing]** Littlebird's promise tracking already compares commitments against actual outcomes ("the email that went out, the document that shipped, the message that never did"), and outputs Kept / In progress / Needs a note (https://littlebird.ai/routines/promise-tracker , accessed at the time of writing).
  - **[Inference, added at the time of writing]** So G5's uniqueness is reduced to two points: ① **the five-value research result** ([Assumption · to be validated], see U3 self-assessment); ② **the evidence source is experiment artifacts** (W&B runs, configs, data versions), rather than email, documents, or GitHub issue status.
- **Objections**:
  0. **(Added at the time of writing) Fellow's GitHub sync and Littlebird's evidence comparison each already cover half of the job: "status flowing back" and "evidence comparison"**; Zoom's website lists "ZoomMate project agent to track progress, share updates, and manage tasks" (https://www.zoom.com/en/products/ai-assistant/ , 06 V10), so the window is narrowing.
  1. The "five-value result" is derived from the data model (U3 self-assessment [Inference]); whether students are willing to spend 30 seconds filling it in is unvalidated (U3 H-A).
  2. Computational labs may feel "it's all in W&B, and I remember it myself" (H-B failure signal).
  3. Fabric claims to have a decision log; adding a result field would bring it close.
- **Confidence**: ~~Medium~~ Medium-low (corrected at the time of writing: U lowered from 4 to 3).

#### G6 Advisor 1:1 Two-Way Commitment Ledger + Advisor Confirmation Gate (from user-academic-lab, user-research-commitments advisor confirmation gate)
- **Opportunity**: Record commitments from both student and advisor ("I'll open dataset access for you"); the student drafts, and once the advisor confirms with one click it becomes the agreed record; before the next 1:1, automatically show "unresolved items from last time + the original wording."
- **Type**: User differentiation (most of the features already exist in Fellow and Littlebird; the difference lies in "for whom" and "which institutional process it embeds into").
- **Evidence**:
  - ~~[Fact]~~ **[Summary · to be verified]** The UW CS PhD handbook says "if your advisor can't remember what was discussed at the last meeting, don't be upset" (search snippet). (Corrected at the time of writing: the original page 301-redirects to internal.cs.washington.edu, which requires login; it still could not be opened this round, so it cannot be quoted as original wording.)
  - ~~[Fact]~~ **[Summary · to be verified]** UK supervision record systems (Haplo, LJMU eDoc) are all "student writes, advisor confirms" (U3 §6.2, partly from search snippets). (Corrected at the time of writing: the Haplo page now 301-redirects to the Cayuse help center home page, the LJMU PDF returns 404, and the Wolverhampton PDF came back empty this round; none of the three can be opened. The main basis for Option B, "embed into existing institutional processes," is therefore all [Summary], 06 W8.)
  - [Fact] Newcastle and Liverpool require students to keep supervision records (U1 §3.4).
  - [Fact] A student who wrote in was repeatedly subjected to the advisor changing their mind (https://softacademia.substack.com/p/dear-bewildered-and-burnt-out ).
  - [Fact] The Supervisor Meeting Brief plugin has only 3 users (U1 §12).
- **Objections**:
  1. **There is no direct evidence for "advisor commitments to the student"** (U1 self-assessment).
  2. Whether advisors are willing to confirm every week is the biggest risk (U3 H-C).
  3. Littlebird's student price of $15/month already offers a personal version, **and it has a Team plan (from $17 per seat per month, including shared projects and admin controls, https://littlebird.ai/pricing , accessed at the time of writing)**; Fellow's 1:1 template could do this with small tweaks.
  4. Students' willingness to pay is low (M3 §8, payment score 2).
- **Confidence**: Medium.
#### G7 Consent-first (from comp-complaints consent-first, comp-global, user-multilingual-offline)
- **Opportunity**: A pre-recording notice that shows who has consented; an in-meeting "don't record this part" control; every attendee can redact before the minutes go out; audio is deleted immediately, and only the confirmed text is kept.
- **Type**: Feature differentiation.
- **Evidence**:
  - [Fact] Otter faces a class action (https://www.npr.org/2025/08/15/g-s1-83087/otter-ai-transcription-class-action-lawsuit ).
  - [Fact] Granola faces a class action, case no. 3:26-cv-07926-EMC (https://ppc.land/granola-sued-for-recording-meetings-without-consent-to-train-ai-models/ ).
  - [Fact] Fireflies faces a BIPA lawsuit (M2 §3.2).
  - [Fact] In a survey of 500 people, only 34.7% of those who had encountered an AI note-taker said they were "always asked for consent" (commissioned by a law firm, which has a stake in the outcome; https://krdo.com/stacker-business-economy/2026/07/16/ai-notetakers-have-sat-in-on-1-in-3-us-workers-meetings-but-only-a-third-say-they-were-asked-first/ ).
  - [Fact] UCSD, Waterloo, UW-Madison and others restrict or ban bots (U1 §6.3, U2 §1.2).
  - [Fact] HN user rcost300 says the issue is "discretion" (M4 category L).
- **Counterarguments**:
  1. The problem is strong, but **the value of the solution is unvalidated**: users may simply want "don't record," not a consent workflow to manage.
  2. Notion already has a voice announcement and mandatory consent, so adding off-the-record is a minor feature.
  3. Under the text-first route (G13), the consent problem itself shrinks, and the two may substitute for each other.
- **Confidence**: Problem medium-high, solution low.

#### G8 Project glossary-driven correction of mixed Chinese-English speech + term recall rate (from comp-china, user-multilingual-offline ×2, comp-complaints, user-academic-lab)
- **Opportunity**: Automatically generate a glossary from BibTeX, paper titles, READMEs, and last week's minutes, and use it for ASR hotwords and post-processing correction ("RT two" → "RT-2"); report term recall rate; terms in action items can be clicked through to their source.
- **Type**: Feature differentiation.
- **Evidence**:
  - [Fact] On CS-Dialogue, the WER for English segments is 15.57%–32.02%, and the lowest Chinese CER is 3.70% (https://arxiv.org/html/2502.18913 ).
  - [Fact] Fun-ASR hotword recall exceeds 0.97 (vendor self-reported, https://arxiv.org/html/2509.12508v3 ).
  - ~~[Fact]~~ **[Summary]** Feishu users fix misrecognitions by writing their own replacement rules (U4 §2.2, summary).
  - **[Fact, added at the time of writing]** Feishu states that "in discussions mixing Chinese and English, the transcript can recognize each in its original language," and offers "enterprise information recognition" ("rare characters in colleagues' names, project names, etc. can also be recognized"); the page does not mention hotwords or a glossary (https://www.feishu.cn/content/article/7577317993749269689 , accessed at the time of writing). So G8 must be framed as "project-level glossary + public recall rate," not "nobody is doing terminology."
  - [Fact] Hands-on testing of DingTalk found "English abbreviations are inaccurate" (M1 §4.2).
- **Counterarguments**:
  1. **There is no first-hand complaint from any Chinese-speaking user** (M4 category J, U4 self-assessment).
  2. AssemblyAI and Granola added mixed-language support in 2026, so ASR progress may close the window quickly.
  3. Feishu already has post-meeting keyword replacement, so adding a "glossary import" would not be hard.
  4. If we go with text-first input, the ASR problem does not exist, and this opportunity disappears with it.
- **Confidence**: Medium.

#### G9 Research object model (from comp-research-tools research schema, user-research-commitments hypothesis ledger, reviewer-comment mapping, comp-china research templates)
- **Opportunity**: Make hypotheses, experiment commitments, success criteria, decisions (including rejected options), advisor suggestions, and reviewer comments first-class objects, linked by "tests" and "based on" relations (U3 §9.1 object model).
- **Type**: User + feature (the object model means only research users need it).
- **Evidence**:
  - [Fact] Inie et al., C&C'22, list "hypotheses" as one of four types of research ideas (https://researcher.itu.dk/en/publications/how-researchers-manage-ideas/ ).
  - [Fact] GoTranscript's lab-minutes template has the fields "experiment ID / hypothesis / result / interpretation / next-step success criteria" (M3 §3).
  - [Fact] Feishu's official meeting-type templates include no research category (M1 §2.5).
- **Counterarguments**:
  1. The more objects there are, the less willing students are to maintain them; in the Duke case even monday.com needed ongoing supervision.
  2. The "hypothesis ledger," "reviewer-comment mapping," and "decision-conflict alerts" have no direct user evidence (in the U3 confidence table, F3/F5/F6 are medium or low).
  3. It could easily turn into an ELN that nobody uses.
- **Confidence**: Medium-low.

#### G10 Embedding into existing weekly-report slots (from user-academic-lab)
- **Opportunity**: Draft a one-page "done / problems / plan" weekly report from this week's meetings and logs, replacing an existing painful chore rather than introducing a new process.
- **Type**: User differentiation.
- **Evidence**:
  - [Fact] A lab at China Agricultural University requires a one-page weekly report "before 8 a.m. every Monday," and two consecutive missed weeks result in a public notice of criticism (https://fdl.cau.edu.cn/col/col41806/index.html ).
  - [Fact] The Beheshti group requires a one-page report each week (https://data-science-group.github.io/weekly-report.html ).
  - [Fact] Fischer Lab and Whitaker Lab also have weekly-report requirements (U1 §4.2, M3 §2.1).
- **Counterarguments**:
  1. General-purpose LLMs (ChatGPT, Doubao) can write a weekly report from pasted minutes, so "embedding into the slot" does not need a dedicated product.
  2. Fabric's main selling point is the PI weekly digest.
  3. Report quality depends on whether the input is complete; if a meeting was not recorded, there is nothing to draft from.
- **Confidence**: Medium-high (the demand has institutional evidence); degree of differentiation medium-low.
#### G11 Cross-meeting commitment tracking (binary version) (from comp-china, comp-global, comp-complaints, skills-discovery)
- **Opportunity**: At the start of a recurring meeting series, automatically list the completion status of commitments from the previous meeting.
- **Type**: Feature.
- **Evidence**:
  - [Fact] Lilach suggests spending 90 seconds at the start of a meeting on a recap (M4 D3).
  - [Fact] The third-party tool lark-retro is filling this gap in Feishu (https://www.v2ex.com/t/1209427 ).
- **Counterarguments**: **Already covered by Fellow, Otter, Granola pre-meeting briefs, and Littlebird** (verified this round + M2). Whether Chinese vendors cover it still needs hands-on testing of Feishu's "Meeting Express" (会议速递) and Tongyi Tingwu's multi-file Q&A (M1 credibility table).
- **Confidence**: Demand is high; as a differentiator it is **low**. We keep it because it is the infrastructure for G5 and G6, and no longer treat it as a standalone selling point.

#### G12 Decision-recall Q&A with sources and the ability to decline to answer (from user-research-commitments F2, skills-positioning relationship map)
- **Opportunity**: Ask "why did we choose 8 for the action chunk", and get back the decision, the verbatim excerpt, the results it relied on, and the experiment link; rationales cite only verbatim quotes, and if there is no record the answer is "no record found".
- **Type**: Feature.
- **Evidence**:
  - [Fact] Liu et al. (CHI 2020) found that many decisions are made implicitly, and warned about hindsight bias (https://ar5iv.arxiv.org/html/1910.13602 ).
  - ~~[Fact]~~ **[Summary · to be verified]** The design-rationale literature indicates that rationales raised in meetings get lost (U3 §5.1, search summary).
- **Counterarguments**:
  1. Fabric already claims "answers are recorded by the time reviewers ask about methods" (marketing copy, https://fabric.so/teams/academic-labs ).
  2. MangoApps and Circleback have decision logs (U2 §2.12).
  3. Recall frequency may be very low, a few times per paper (U3 H-D).
- **Confidence**: Medium.

#### G13 Text-first / non-recording input (from comp-research-tools, user-multilingual-offline C7, skills-positioning bot-free)
- **Opportunity**: The main pipeline does not depend on recordings. It accepts Markdown bullet points written within 10 minutes after the meeting, OCR of whiteboard photos, and transcripts from a phone; audio is optional, local, and deleted immediately.
- **Type**: Feature (interaction paradigm).
- **Evidence**:
  - [Fact] Fireflies' own blog admits that separating speakers is harder when an in-person meeting shares a single microphone (M3 §6).
  - [Fact] Gerstein uses Rocketbook plus OCR to handle whiteboards (Nature 2021, https://www.nature.com/articles/d41586-021-01752-y ).
  - [Fact] Transcription of spoken formulas is poor (https://arxiv.org/html/2508.03542v1 ).
  - [Fact] A student on GradCafe says "recordings have to be screened afterward, 30–60 minutes" (U1 §3.1).
- **Counterarguments**:
  1. Students may not take notes at group meetings at all, in which case there is no input (U4 §5 [Assumption]).
  2. Feishu and Otter both support file upload, so "can upload text" is not a differentiator.
  3. Text input is information-sparse; "who / when" is often missing, which makes extraction harder (U4 §5 table).
- **Confidence**: Medium.

#### G14 Fewer, more accurate items, pushed per person (from comp-complaints #4)
- **Opportunity**: By default, output only three columns, "Decisions / My commitments / Open questions", split by person; the full transcript is demoted to an attachment.
- **Type**: Feature (experience differentiation, Linear-style subtraction).
- **Evidence**:
  - [Fact] HN user smartmic says "nobody will ever read those notes" (M4 H1).
  - [Fact] One article says "archives are for auditing" (https://programminginsider.com/why-ai-note-taker-summaries-go-unread-and-what-fixes-it/ ).
  - The Cotera and Laxis figures are vendor self-reported and **cannot be trusted**.
- **Counterarguments**: Every vendor supports configurable templates; this is more a default-setting choice than a capability difference, and it is easy to copy.
- **Confidence**: Medium.

#### G15 Client–vendor requirements baseline diff + counterparty confirmation sheet (from user-other-segments Top 1)
- **Opportunity**: Using the contract, SOW, or PRD as the baseline, mark each item as added, modified, deleted, or out of scope, noting who proposed it, who verbally agreed, and the verbatim quote; generate a confirmation sheet for the client, and only after confirmation does an item enter the new baseline.
- **Type**: User + feature.
- **Evidence**:
  - [Fact] Procore separates internal and external tasks and carries over leftover items only in the construction industry (https://www.procore.com/ai/agents/meeting-minutes-publisher ).
  - [Fact] Best practices for change control require linking changes to meetings (https://monolith.law/en/it/howto-manage-change-in-system-development ).
  - [Fact] ScopeGuard-type tools look only at Slack and email, and their maturity is uncertain (U2 §2.12).
  - [Inference] Search did not find any requirement-level diff product.
- **Counterarguments**:
  1. Pain-point evidence consists mainly of experience articles, with no large sample (U2 self-rates it "medium").
  2. Chinese B2B delivery tools (Zentao, PingCode, Teambition) have not been checked.
  3. Clients may not be willing to click confirm (U2 H2).
  4. Feishu Docs plus Bitable could in theory be assembled into this, so the moat is narrow.
  5. The project owner lacks real source material.
- **Confidence**: Medium-low.
#### G16 Open-source communities: write meeting decisions back to existing issues/PRs (from user-other-segments Top 3)
- **Opportunity**: Match each meeting decision to a specific issue or PR, generate a comment draft with timestamped references, and submit it after a maintainer confirms; build a gold-label evaluation set from public recordings, minutes, and issue history.
- **Type**: User + feature; its more important role is as an **evaluation venue**.
- **Evidence**:
  - [Fact] OpenSSF TAC issue #532 raised this need and is still open with no replies (https://github.com/ossf/tac/issues/532 ).
  - [Fact] Kubernetes requires SIGs to publish recordings and minutes (https://github.com/kubernetes/community/blob/master/events/community-meeting.md ).
- **Counterarguments**:
  1. Only one issue demonstrates the need; maintainers feel little pain, and willingness to pay is close to 0.
  2. Communities dislike AI automatically writing issues.
  3. What it can prove is "evaluation capability," not "someone wants this."
- **Confidence**: Medium (high as an evaluation venue, low as a market segment).

#### G17 PI-wide commitment board (from user-academic-lab, comp-global team-level)
- **Opportunity**: Every Monday, a one-page view of "who delivered, who is overdue, what I owe whom," with no need to hold another meeting.
- **Type**: User.
- **Evidence**:
  - [Fact] In Nature 2021, PI Bahlai said long-term goals "keep falling through the cracks" (M3 §2.1).
  - [Fact] The Prograds author said advisors often don't know which stage their students have reached (U1 §3.4).
  - ~~[Fact] Littlebird only does individuals (M2 §3.17).~~ (Corrected at the time of writing: the Littlebird pricing page has a Team plan, "from $17 per seat per month", including "Admin controls and team usage analytics" and "Shared projects and routine templates", https://littlebird.ai/pricing , accessed at the time of writing. However, its commitment-tracking routine is still "tuned to yours, the things you said you'd do"; tracking what others owe you has to be specified separately in the prompt, and the page does not describe a team-level commitment ledger, https://littlebird.ai/routines/promise-tracker .)
  - **[Inference, added at the time of writing]** So the differentiation for G17 is not "team edition vs. personal edition" but "**a team-shared commitment ledger** (who owes whom, cross-person dependencies) vs. each person's own commitment list."
- **Counterarguments**:
  1. It only works if the whole group uses it, so the cold-start problem is severe.
  2. Students may not want their advisor to see their full list (M3 §5 [Assumption]).
  3. Fabric's marketing already emphasizes this.
- **Confidence**: Medium-low.

#### G18 Cross-ecosystem, cross-organization, low lock-in (from comp-china, comp-global cross-organization)
- **Opportunity**: Serve teams without a unified IM, whose meetings are spread across Zoom, Tencent Meeting, Teams, and in person, and whose participants may come from different institutions.
- **Type**: Both.
- **Evidence**:
  - [Fact] Teams Copilot "doesn't work in meetings hosted outside the participant's organization" (M2 §3.9).
  - [Fact] A comparative review says Feishu is not suitable for people who don't use Feishu, and Tencent's tool is not suitable for teams using Zoom/Teams (https://aixiaobailab.com/ai-meeting-notes-tools/ ).
- **Counterarguments**: Otter, Fireflies, and Read already claim to be "platform-agnostic"; only platform-built-in tools have this weakness.
- **Confidence**: Medium.

#### G19 Data never leaves the device (from comp-global, user-research-commitments F8, user-multilingual-offline, user-academic-lab compliance)
- **Opportunity**: Local ASR (SenseVoice, Paraformer, whisper.cpp) plus a local LLM (Ollama qwen3 8B/14B), so raw meeting text does not leave the machine by default.
- **Type**: Both.
- **Evidence**:
  - [Fact] In the OUP 2024 survey, only 8% trusted AI companies not to misuse research data (https://www.timeshighereducation.com/news/use-ai-research-widespread-distrust-still-high-oup ).
  - [Fact] In the Wiley 2025 survey, privacy concerns rose to 58% (U3 §7).
  - [Fact] The user's M1 Max/32GB machine can run 8–14B models (U4 §0).
- **Counterarguments**:
  1. Meetily (32.4k stars) and anarlog already occupy the "local recording" mindshare (U4 §6).
  2. Researchers use ChatGPT anyway (U3 H-E failure signal).
  3. There is no public evaluation of local LLM extraction quality.
- **Confidence**: Medium. **Position it as a foundation or entry requirement, not a selling point** (U4 and U2 agree).

#### G20 Organize by project + Markdown/Obsidian/GitHub export (from comp-complaints, comp-global GitHub, comp-research-tools)
- **Opportunity**: Make the project, not the meeting, the top-level object; allow commitments to be pushed to GitHub Issues; export to the user's own knowledge base.
- **Type**: Feature.
- **Evidence**:
  - [Fact] HN user kpen11 said "getting data in has consistently been the point of failure," and crashabr wanted to add project tags to transcripts (M4 category I).
  - [Fact] The Whitaker, Durrant, and COMET labs use Git and Markdown to manage projects (M3 §2.1).
  - **[Fact, added at the time of writing]** Fellow syncs bidirectionally with GitHub (via Zapier, https://fellow.ai/integrations/github ); Granola lists GitHub, Linear, Jira, and Asana via Zapier and has a Granola MCP connector (https://www.granola.ai/integrations ); both accessed at the time of writing.
- **Counterarguments**: Integrations are an "expected" feature; adding them doesn't delight anyone, and big vendors and Zapier can fill the gap. **(Added at the time of writing) This has already happened: GitHub push is not a differentiator, and only "organize by project" and "export to Markdown/Obsidian" remain partial gaps; users can also assemble their own setup with "meeting-tool MCP + Claude Code + GitHub MCP."**
- **Confidence**: ~~Medium-low~~ Low (corrected at the time of writing: U lowered from 3 to 2).
#### G21 [Moat] User-correction feedback evaluation + progressive automation (from skills-ai-pm ×2, skills-pm-core evals)
- **Opportunity**: Every time a user edits a draft and then confirms, record it as an (original output, user correction, source sentence) triple and add it to the regression set. Define override-rate thresholds per action category, so that low-risk categories move from "approval" down to "undo".
- **Type**: Feature (internal capability, not directly perceptible to users).
- **Evidence**:
  - [Fact] PAIR: "Automate more when trust is high, or risk of error is low".
  - [Fact] MIT NANDA attributes enterprise pilot failures to "not learning from the workflow" (https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/ ).
  - The data-flywheel claim comes mainly from blogs (S4 F4).
- **Counterarguments**: Big companies have far more data than a small project; at the demo stage the volume of correction data is too small to form a moat, so it can only showcase the "mechanism".
- **Confidence**: Medium-low (as a moat); medium-high as an interview narrative.

### 3.3 Candidate gaps that were merged or downgraded rather than listed separately (and why)
- **"Process-contribution evidence" for student project teams**: Willingness to pay is 0, and there is an ethical risk of students monitoring each other (U2 §2.6) → used only as an interview pool.
- **Lab-bundled pricing gap**: No competitor pricing page was verified; this is a pure assumption (S5 §2.3) → moved to the §6 open questions.
- **Using notes to back-correct the transcript**: No product was found doing this, but the evidence is very weak (U4 §5) → treated as an implementation detail of G8.
- **Low-cost in-meeting annotation (Granola paradigm)**: Merged into the interaction form of G4 (claiming).
- **Decision-conflict alerts**: Derived only from the data model (U3 F6) → merged into G9 as a long-term item.
- **PR/FAQ, demo structure, control-group design, diary study**: These are methods and go into §5.

---

## 4. Candidate "differentiation combinations" (6 options)

> Each option = one target segment + 1–2 sharp differentiators + a one-line positioning statement (written along April Dunford's logic chain: competitive alternatives → unique attributes → provable value → customers who care most → market category, S3 §1) + a one-sentence answer to "others already do this, so why are you still building it?"
> The options are deliberately different from one another: A is **pure feature** differentiation (no segment restriction); B is **pure user** differentiation (the features are largely off-the-shelf); C–F are hybrid options for different segments.

### Option A [Pure feature differentiation] "A verifiable, claimed commitment layer"
- **Target segment**: Not limited to any industry; any team of 5–20 people that makes decisions in meetings and often argues afterward about "who promised that".
- **Sharp differentiators**:
  - **G2 + G3**: Every commitment carries the original sentence, speaker, timestamp, and a strength label; missing fields are explicitly marked "to be confirmed";
  - **G4**: A commitment becomes a task only after the named person claims it.
  - Use the public evaluation from **G1** to prove "our fabrication rate and mis-assignment rate are lower than Feishu Minutes and Otter".
- **Positioning statement (Dunford)**: For teams that already use Feishu Minutes or Otter but still have to check the recording line by line to find out "who exactly promised what", BriefPilot is a "meeting commitment verification layer": it does not guess owners, every commitment can be traced back to the original sentence in 3 seconds, and the person concerned claims it themselves, so the mis-assignment and fabrication rates in the public evaluation can be checked.
- **"Others already do this, so why are you still building it?"**: "They solve 'generation'; I solve 'dare to trust it, and someone owns it'. I tested them on the same samples: their mis-assignment rate on the owner field is X%, ours is Y%." (X and Y depend on actual G1 measurements; **no numbers can be quoted now**.)
- **Why big companies may not build it / risks**:
  - On the favorable side is weak counter-positioning: big companies' product philosophy is "the more automation the better" (official statements from Fireflies, Krisp, and ZoomMate), and actively showing "leave blank" and "refuse to answer" would weaken their "fully automatic" selling point (S3 §4.2, [Inference]).
  - **But this is the easiest of the six options to copy**: every differentiator is a small feature. Without a segment scenario to support it, it falls into what S3 §8.5 calls "feature differentiation alone is the most fragile".

### Option B [Pure user differentiation] "A 1-on-1 ledger for PhD students and their advisors"
- **Target segment**: PhD and master's students who hold weekly or biweekly 1-on-1s with their advisors (first at the target university and Singapore universities), with advisors as the secondary users.
- **Sharp differentiators**: The features largely reuse existing capabilities (summary, action items, next-meeting recap, which Fellow and Littlebird both have); the difference lies entirely in "who it is built for":
  - **G6**: Two-way commitments (what the advisor owes the student is also recorded) + a "student drafts → advisor confirms" consensus record, which matches already-institutionalized processes such as UK supervision records (note: the evidence on UK supervision systems is currently all [Summary · to be verified]; see G6);
  - **G10**: One-click export to the supervision record and weekly report formats required by the university or lab.
- **Positioning statement (Dunford)**: For PhD students who piece together "what my advisor asked me to do last time" from WeChat chat history and notebooks, BriefPilot is a "supervision meeting record assistant": like Fellow, it brings back unfinished items before the next meeting, but it is designed only for the student–advisor relationship. The advisor's commitments are recorded too, a record counts as consensus only after the advisor confirms it, and it directly generates the supervision record the university requires.
- **"Others already do this, so why are you still building it?"**: ~~"Fellow is for managers and their direct reports in 1-on-1s, and Littlebird only records what students owe their advisors; what I build is the supervision record that universities already require to be kept and that advisors confirm, just with its cost reduced to 1 minute."~~ (correction: "Littlebird only records what students owe their advisors" is inaccurate. Littlebird has a Team plan, and its commitment tracking can also be prompted to track "what others owe you"; see https://littlebird.ai/pricing and https://littlebird.ai/routines/promise-tracker. Fellow can also bring back unfinished items before the next meeting and supports multiple owners.)
  **Corrected differentiating statement [Inference]**: "Fellow and Littlebird can both bring back what was left undone last time before a meeting, and Littlebird also has a team edition; but what they record is 'one person's own list', and Fellow's action-item page does not say that the assignee confirms. What I build is **a supervision record confirmed jointly by student and advisor**: the student drafts it, it becomes consensus only after the advisor confirms, what the advisor owes the student is on it too, and its format matches the supervision records that universities require to be kept." (The UK evidence for "universities require it to be kept" is currently [Summary · to be verified]; before external use it must be replaced with a page that can actually be opened or with the target university's local regulations.)
- **Why big companies may not build it / risks**:
  - On the favorable side: the market is small and fragmented and not on big companies' roadmaps (S3 §0 insight 2), and it requires understanding universities' supervision systems.
  - **Risk**: whether advisors are willing to confirm (U3 H-C); students' willingness to pay is weak; Fellow or Littlebird could get close just by shipping a template (addendum: Littlebird already has a Team plan and shared projects, so the cost of approximating this is lower than originally estimated). Pure user differentiation has to be defended by "understanding this group better", and it only holds if 6 or more users who say they would be "very disappointed to lose it" are secured within 4 weeks (S2 §2.7).
### Option C [User + Feature, preferred for dogfooding] "The commitment–result–evidence chain for computational research groups"
- **Target segment**: Computational labs in CS, robotics, and VLA (the project owner's own group is the seed), whose toolchain is GitHub, W&B, Overleaf, and Zotero.
- **Sharp differentiators**:
  - **G5**: Every commitment must be backfilled with a five-value result and a run/commit link. Before the next group meeting, the tool automatically lists "awaiting backfill" and "done, but conditions differ from the commitment";
  - **G12**: Decision-retrospective Q&A, where the rationale cites only verbatim quotes, and the tool declines to answer if nothing was recorded.
  - Input follows **G13**, text first (post-meeting Markdown), fully reusing S0's RAG, citation verification, and confirmation gate.
- **Positioning statement (Dunford)**: For computational research groups whose experiment records are scattered across W&B, Git, and oral reports at group meetings, and who cannot explain "why we set it up this way back then" when writing a paper, BriefPilot is a "group-meeting decision and experiment-commitment record layer": ~~meeting tools only tick off tasks~~ meeting tools can tick off tasks and sync status to GitHub issues, and personal assistants can check emails and documents to judge whether a commitment was fulfilled (corrected at the time of writing: Fellow has two-way sync with GitHub, and Littlebird has Kept / In progress / Needs a note evidence comparison, https://fellow.ai/integrations/github , https://littlebird.ai/routines/promise-tracker ), but none of them records the **research semantics of experiment results**. BriefPilot requires every experiment commitment to be backfilled with a result (supported / refuted / uncertain / abandoned / superseded) and run and config links, and it can answer "why did we choose this setting?" with verbatim quotes.
- **"Others already do this, so why build it?"**: "Feishu Minutes delivers tasks with checkboxes. In research, 'done' carries no meaning; 'ran it, refuted hypothesis H2, so dropped method A' is the information. Right now that chain exists only in next week's oral report, and then it gets lost again."
  **(Differentiation line added at the time of writing [Inference])**: If an interviewer asks, "Fellow can already sync with GitHub and Littlebird can already compare evidence," the answer should land on two points: "What they feed back is an issue's open/closed state, or whether an email was sent. What I want is whether this run supported or refuted hypothesis H2, and the evidence is the W&B run and config, not an issue's status. I don't treat 'integration' itself as a selling point; anyone can connect things with MCP." (The "five-value result" itself is still [Assumption, to be validated], 06 W10.)
- **Why big vendors may not build it / risks**:
  - Favorable: It requires changing the object model (hypothesis, result, evidence), which cannot be fixed by adding a template (U3 §1), so general-purpose meeting products have little incentive.
  - **Risks**: Fabric is ~~the only~~ one of the explicit benchmarks and already claims a decision log (added at the time of writing: Fellow's two-way GitHub sync and Littlebird's evidence comparison are also partial benchmarks); willingness to pay is low (M3 §8, 2 points), so it is better framed as a portfolio piece than as a business; the author is the target user, which creates a self-projection bias (U1 §14).
  - Expansion path (bowling pin): It can extend to U2's "hardware/robotics R&D teams" (reconciling experiment commitments made in meetings ↔ test logs), which supports a paid-product story.

### Option D [Constraint-driven] "A terminology-accurate commitment assistant for teams that mix Chinese and English"
- **Target segment**: Small technical and research teams of Chinese speakers in Singapore and overseas, who speak in "Chinese sentence frames + English terms" (not limited to labs; also startup engineering teams).
- **Sharp differentiators**:
  - **G8**: Automatically builds a glossary from team materials (README, papers, BibTeX, last week's minutes), used for hotwords and post-processing correction, and publicly reports "terminology recall";
  - **G19**: Local execution as the foundation.
- **Positioning statement (Dunford)**: For Chinese-speaking technical teams who sprinkle English terms into their speech and find that Feishu Minutes or Otter keeps mishearing model names and abbreviations, BriefPilot is a "terminology-accurate meeting commitment assistant": it learns your terminology from your own documents, runs recognition on your own machine, and reports the recall of your terms, rather than vaguely saying "supports mixed Chinese-English."
- **"Others already do this, so why build it?"**: "Everyone says they support mixed Chinese-English, but nobody reports accuracy on your team's terminology. In public benchmarks the error rate on English segments is 15%–32%, and the most critical nouns in action items are precisely those English words."
- **Why big vendors may not build it / risks**:
  - Favorable: Big vendors optimize general WER and will not maintain a glossary and recall evaluation for every small team ([Inference]).
  - **Risks**: There are no first-hand Chinese-language complaints (M4 category J, 24 points and marked "to be validated"); ASR vendors catch up quickly (AssemblyAI 2026-08); if users actually use text input, this selling point disappears.

### Option E [User + Feature, responding to the client] "A requirement-change ledger for the vendor side"
- **Target segment**: Vendor-side PMs at outsourcing firms, agencies, and B2B delivery teams, in the scenario of holding repeated requirements meetings with the same client.
- **Sharp differentiators**:
  - **G15**: Cross-meeting requirement diff against an SOW or PRD baseline, flagging additions, modifications, and out-of-scope items;
  - **Cross-organization version of G4**: Generates a client confirmation sheet, and only after the client confirms does an item enter the new baseline.
- **Positioning statement (Dunford)**: For vendor-side PMs who get requirements added bit by bit by the client through WeChat voice messages and meeting minutes, and afterward cannot say "who promised that verbally," BriefPilot is a "requirement baseline change ledger": meeting tools only tell you what was said in a single meeting, while it tells you how far this series of meetings has drifted the contract baseline, with every item carrying verbatim quotes and client confirmation.
- **"Others already do this, so why build it?"**: "The unit for Feishu and Otter is 'one meeting,' while the unit for scope creep is 'a series of meetings + one contract.' Procore has already validated this need in the construction industry, but there is no corresponding product for software outsourcing yet."
- **Why big vendors may not build it / risks**:
  - Favorable: Cross-tenant confirmation and document-version baselines go beyond the boundary of a meeting product (U2 §4, [Inference]).
  - **Risks**: The weakest evidence (E=2); Chinese project-management SaaS has not been checked; the project owner lacks real material, so dogfooding does not hold; Feishu Docs plus Bitable could be used to piece it together.
### Option F [Evaluation-driven] "Open-source community meetings → issue write-back" (as an evaluation testbed, not the commercial main line)
- **Target segment**: Maintainers of open-source communities with public recordings and minutes, such as Kubernetes SIGs and OpenSSF working groups.
- **Sharp differentiators**:
  - **G16**: Match decisions to existing issues/PRs and generate comment drafts with timestamped citations; nothing is submitted until the maintainer confirms.
  - **G1**: Build gold labels from public data and report "decision → issue matching accuracy" and "erroneous write-back rate".
- **Positioning statement (Dunford)**: For maintainers who finish a SIG meeting and still have to copy decisions by hand under a dozen issues, BriefPilot is a "meeting-decision write-back assistant": existing automation only covers the pre-meeting agenda, while it matches post-meeting decisions to specific issues and submits only after you confirm, and its accuracy on public data is reproducible.
- **"Others have already built this, so why are you building it?"**: "Someone raised this need in OpenSSF and it has gone unanswered to this day; and this is the only scenario where AI quality can be proven with real public data. Others' claims are marketing, while my numbers are reproducible."
- **Risks**: Willingness to pay is 0 and the pain is weak; communities dislike AI-written issues. **Its real value is to provide credible evaluation evidence for Option A or C**, rather than to stand on its own.

### 4.7 Side-by-side comparison of the six options [Inference]

| Option | Type | Evidence strength | Speed of being copied by big vendors | Dogfooding | Business story | Biggest single-point risk |
|---|---|---|---|---|---|---|
| A Verifiable commitment layer | Pure feature | **High** | **Fast** | Medium | Medium | Only a feature, no segment to anchor it |
| B PhD student 1:1 | Pure user | Medium | Medium | **High** | Low | Advisors unwilling to confirm (H-C) |
| C Computational research group | User + feature | Medium | **Slow** | **Highest** | Low (can extend to hardware R&D) | Students don't backfill results (H-A) |
| D Mixed Chinese-English team | Constraint-driven | Medium-low | Medium | High | Medium | No first-hand Chinese pain points |
| E Vendor-side requirements ledger | User + feature | Low | Slow | **Low** | **High** | Weakest evidence, can't get material |
| F Open-source issue write-back | Evaluation-driven | Medium | Slow | Medium | None | Nobody wants it |

**[Inference] A possible combination play** (to be handed to `03_positioning` for review, not a conclusion):
- Use **C as the wedge**: it can be dogfooded, and big vendors copy it slowly.
- Make **A's three differentiators the trust foundation of C**, proven through G1 evaluation.
- Use **F's public data to give A a reproducible evaluation**.
- B and D serve as fallbacks if C's validation fails.
- E is reconsidered only after ≥3 interviews with real vendor-side PMs.

---

## 5. How to prove it (method-type gaps that do not enter the requirements list)

| Source | Key point | Specific requirement for the next round |
|---|---|---|
| skills-research-methods, S5 §3.2 | The PR/FAQ internal FAQ must directly answer "Feishu Minutes, Otter, and Fireflies already do this, so why build it?"; being unable to write a convincing customer quote is itself a signal that the segment does not hold | `03_positioning/pr-faq.md` comes before the PRD |
| skills-research-methods, S5 §4.2 | Compress the demo into "one magic moment + trust boundary"; the competitor comparison section may use only verified features | The competitor comparison **must not** again say "they have no cross-meeting tracking" (see K6 correction) |
| skills-ai-pm, S4 Q2 | Define direction through error analysis of competitors' real outputs, not feature comparison tables | This is the execution version of G1, §6 Q1 |
| skills-research-methods, S5 §2.5 | A control group of 3–4 non-lab people is needed; otherwise we cannot tell whether "labs are a differentiated segment" or "labs are just one channel" | Add a control group to the interview plan |
| skills-discovery, S2 §3.4 | A diary study measures "frequency × 48-hour omission rate", a first-hand number that neither competitors nor interviewers have | 3–5 people, for 2 weeks |
| skills-pm-core, S1 §3.1 | Differentiators must land in the Kano delighter category; turning meetings into tasks is already a basic need | Run the Kano paired-question method on G2–G6 |

---

## 6. Open questions (judgments where evidence is still insufficient and the next round must validate)

| # | Open question | Why it matters | Items / options affected | Suggested validation method |
|---|---|---|---|---|
| Q1 | What exactly are the action-item **failure modes** of Feishu Minutes, Tongyi Tingwu, and Otter on real group meetings (mixed Chinese-English, soft commitments, offline), and what share does each account for? | All differentiation claims currently rest on "public descriptions"; **not a single real competitor output has been seen** | G1–G3, G8, all options | 3–5 synthetic group meetings, run through each product, 30–100 manual annotations (M1 §10.6, U4 §8.2) |
| Q2 | To what extent do Fellow, Otter, and Granola bring the previous action items back before a meeting? Is it limited to a single person, to the same meeting series, or to binary status only? | Determines the U scores for G5 and G6; also determines whether Option B still holds | G5, G6, G11, Options B/C | Trial accounts; test recurring meetings hands-on |
| Q3 | How many times per week do lab members "fail to remember the advisor's specific request from last time"? What share of commitments is recorded within 48 hours? | The evidence so far is all policies and guidelines ("required to record"), with no frequency data | G6, G10, G11, Options B/C | Diary study (S2 §3.4); U1 H1 |
| Q4 | Are advisors willing to spend under 5 minutes each week confirming? Are students willing to spend 30 seconds backfilling results and links? | The make-or-break line for Options B and C | G5, G6, G17 | Concept tests with 2–3 PIs; backfill rate over 4 weeks of dogfooding (U3 H-A, H-C; failure line is 50%) |
| Q5 | Is "advisor commitments to students" a real pain? Are students unwilling to let the PI see the full list? | The key to separating Option B from Fellow and Littlebird, but currently **zero direct evidence** | G6, G17 | Ask about specific past events in interviews (Mom Test) |
| Q6 | Real complaints from Chinese-speaking users about Feishu Minutes and Tingwu handling mixed Chinese-English and terminology | Neither M4 nor U4 obtained a single piece of Chinese UGC (Zhihu and Xiaohongshu returned 403) | G8, Option D | Project owner browses manually and adds 10–20 entries; compute the share of English tokens in self-recorded samples |
| Q7 | Original posts on Reddit r/PhD, r/GradSchool, and r/AskAcademia | All student-side sentiment evidence is indirect | Options B, C | Search manually for "advisor doesn't remember" and "lab meeting notes" |
| Q8 | The target university's specific IT policy on AI meeting transcription and third-party cloud tools; the attitude of the target university's lab members toward recording | Determines whether G7 and G19 are a "threshold" or a "preference" (U3 H-E) | G7, G13, G19 | Check the target university's IT and research integrity/ethics office policies; interviews |
| Q9 | Does Fabric academic labs have real customers? ~~Does Littlebird have a team plan?~~ (Answered at the time of writing: yes, Team from $17 per seat per month, https://littlebird.ai/pricing ; still to answer is whether Team shares a commitment ledger) | These two are the most direct competitors of Options B and C, and so far there are only marketing pages | Options B, C | Sign up for trials; search for customer case studies |
| Q10 | Can the model reliably recognize commitment strength (explicit / suggested / under discussion)? Do human annotators agree with each other? | Feasibility of G3; if humans do not agree with each other (low Cohen's Kappa), it should not be built as a product feature | G3 | Two annotators label 20 samples |
| Q11 | Quality of local 8B/14B models at extracting Chinese and mixed Chinese-English action items | Feasibility of Option D and G19; there is currently no public evaluation | G19, Option D | Test on a local M1 Max (U4 §9 next step 1) |
| Q12 | Frequency of vendor-side PMs' "verbal change disputes"; whether Chinese project-management SaaS (Zentao, PingCode, Teambition) has requirement-level diff | Option E has the weakest evidence | G15, Option E | Interview 5 vendor-side PMs; supplement the competitor check |
| Q13 | Unit of payment: do labs pay "per person" or "per group"? What is the threshold? | The business story for all research options; no competitor pricing has been verified yet | Options B, C | Interview PIs about their reimbursement process (U1 H6) |
| Q14 | Facts that still contradict each other between M1 and M2: whether Tencent Meeting action items can be traced back to the source (the comparative reviews contradict each other); Granola's default sharing and training settings (only a The Verge repost); the direction of the numbers on supervision time and satisfaction in Nature 2025 | If written into the PRD or interview script, errors would be caught | K2, K7, K9 | Open the original pages and check item by item |
| Q15 | What does Zoom AI Companion 3.0's "track cross-meeting projects" actually mean? | May once again narrow G5's white space | G5, G11 | This round's search quota ran out; follow up next round. (Partially answered at the time of writing: the official AI assistant page does not contain this exact sentence, which came only from a search snippet of an investor press release [Summary · to be verified]; the page does say "ZoomMate project agent to track progress, share updates, and manage tasks", https://www.zoom.com/en/products/ai-assistant/ , see 06 V10) |

---
## 7. Contradictions Between Earlier Documents and How This Document Handles Them

| Contradiction | Document A says | Document B says | How this document handles it |
|---|---|---|---|
| Whether cross-meeting commitment tracking is an open gap | M1: all 9 Chinese products have ○ across the whole row | M2: Otter and Granola pre-meeting briefs bring back action items; U2: Littlebird, Procore; this round: Fellow | **Treat it as "already done by others (binary version)"**; M1's conclusion holds only within the Chinese market |
| Whether "citations" are a selling point | S3 §1.5 lists "server-side citation validation" as a unique attribute | M1 §0, M2 §0: citations are becoming standard | Citations are **not** a unique attribute; what can be claimed is "per-commitment, sentence-level grounding + no output without evidence" (G2), and this must be tested |
| Whether "human confirmation" is a selling point | Core design of the S0 PRD | M2: tl;dv already offers "for review before sending"; M1: WPS officially also advocates "pending review" | Confirmation **itself** is not a differentiator; the difference lies in **who confirms** (the person involved, or the advisor; G4, G6) and **what they see when confirming** (evidence, strength) |
| Status of privacy and localization | U3: local-first is the **entry threshold** for research use | U2, U4: can only be a supporting feature, cannot stand alone | The two do not conflict: it is a threshold, not a selling point (G19 ranks low, but every research solution must satisfy it) |
| Scoring for academic labs | M3: paid score 2, suitable for a portfolio | U2 §3.2: rough-scored 3.80, higher than other segments | Both acknowledge "high portfolio value, low commercial value"; this document labels the commercial story of the research solution as "low" |

---

## Source List

**Newly verified this round **
1. Fellow Action Items feature page — https://fellow.ai/features/action-items

**Newly verified in the Round 2 revision (accessed at the time of writing, opened directly via WebFetch)**
73. Fellow × GitHub — https://fellow.ai/integrations/github
74. Granola Integrations — https://www.granola.ai/integrations
75. Littlebird Pricing — https://littlebird.ai/pricing
76. Littlebird Promise Tracker (reopened) — https://littlebird.ai/routines/promise-tracker
77. Microsoft Learn: Facilitator in Teams — https://learn.microsoft.com/en-us/microsoftteams/facilitator-teams
78. Google Meet "Take notes for me" help page — https://support.google.com/meet/answer/14754931
79. Krisp AI Meeting Assistant — https://krisp.ai/ai-meeting-assistant/
80. Feishu intelligent meeting minutes (reopened) — https://www.feishu.cn/content/article/7577317993749269689
81. Circleback / Read / Otter Integrations (cited from 06 V2) — https://circleback.ai/integrations ; https://www.read.ai/integrations ; https://otter.ai/integrations
82. Zoom AI Assistant product page (cited from 06 V10) — https://www.zoom.com/en/products/ai-assistant/
83. Still could not be opened this round (to be verified): UW CS handbook (301 redirect to an internal domain requiring login); Haplo (301 redirect to the Cayuse help center home page); Wolverhampton supervision record PDF (fetch returned empty)

**Chinese competitors (cited from M1)**
2. Feishu intelligent meeting minutes — https://www.feishu.cn/content/article/7577317993749269689
3. Feishu AI action item breakdown — https://www.feishu.cn/content/article/7600354912756681687
4. Feishu meeting summary and action item export (cited from U3) — https://www.feishu.cn/content/article/7602953888668339380
5. DingTalk AI Tingji 55-minute hands-on test — https://www.woshipm.com/share/6269848.html
6. Leiphone: DingTalk Tingji accuracy — https://www.leiphone.com/category/CorporateServices/laMyPOOWyk7FzjEa.html
7. China.com: iFlytek Tingjian minutes traceability — https://m.tech.china.com/hea/articles/20251106/202511061760505.html
8. Weibo article: AI doesn't invent tasks and owners — https://weibo.com/2/detail/comos:niwmapc3412577
9. V2EX: lark-retro — https://www.v2ex.com/t/1209427
10. AI Xiaobai Lab comparative review — https://aixiaobailab.com/ai-meeting-notes-tools/
11. Juejin: mixed Chinese-English speech and glossaries — https://juejin.cn/post/7696662898145345587

**International competitors (cited from M2)**
12. Otter website — https://otter.ai/
13. Fireflies website — https://fireflies.ai/
14. tl;dv website — https://tldv.io/
15. Granola security page — https://www.granola.ai/security
16. Notion AI Meeting Notes — https://www.notion.com/help/ai-meeting-notes
17. Microsoft: Copilot in Teams meetings — https://support.microsoft.com/en-us/office/use-copilot-in-microsoft-teams-meetings-0bf9dd3c-96f7-44e2-8bb8-790bedf066b1
18. Google: Take notes for me — https://blog.google/products-and-platforms/products/workspace/take-notes-for-me/
19. Zoom AI Assistant / ZoomMate — https://www.zoom.com/en/ai-assistant/
20. Krisp pricing — https://krisp.ai/pricing/
21. Littlebird graduate students page — https://littlebird.ai/for/graduate-students
22. Littlebird Promise Tracker — https://littlebird.ai/routines/promise-tracker
23. anarlog (formerly Hyprnote) — https://github.com/fastrepl/hyprnote
24. Meetily — https://github.com/Zackriya-Solutions/meeting-minutes
25. Granola Series A blog — https://granola.ai/blog/series-a
26. Sacra: Gong — https://sacra.com/c/gong

**Research tools and labs (cited from M3, U1, U3)**
27. Fabric for Academic Labs — https://fabric.so/teams/academic-labs
28. Nature 2021 lab digital tools — https://www.nature.com/articles/d41586-021-01752-y
29. Duke JACMP 2025 (PMC12401938) — https://pmc.ncbi.nlm.nih.gov/articles/PMC12401938
30. Durrant Lab project management — https://durrantlab.pitt.edu/durrant-lab-project-management-system/
31. COMET Lab GitHub Projects — https://comet.luddy.indianapolis.iu.edu/cmt23s/training/comet-lab-project-management-with-github/
32. GoTranscript lab meeting minutes template — https://gotranscript.com/en/blog/lab-meeting-minutes-template-decisions-actions-experiments-copy-paste
33. Kanza et al. 2017 — https://link.springer.com/article/10.1186/s13321-017-0221-3
34. MIT Cahoy advising policy — https://aeroastro.mit.edu/wp-content/uploads/2022/03/AdvisingPhilosophy.Cahoy_.2019.pdf
35. Imperial supervision agenda advice — https://t4awstest.cc.ic.ac.uk/media/imperial-college/administration-and-support-services/staff-development/public/pfdc/Download-C.4.9---Advice-sheet---Effective-PhD-supervision-meeting-agendas.pdf
36. UW CS PhD handbook (search snippet; retried at the time of writing, still requires login, to be verified) — https://www.cs.washington.edu/academics/phd/handbook/advising-guide/building-a-relationship
37. GradCafe: note-taking during advisor meetings — https://forum.thegradcafe.com/topic/108546-note-taking-during-advisor-meetings
38. China Agricultural University Functional Dairy Lab rules — https://fdl.cau.edu.cn/col/col41806/index.html
39. Beheshti group weekly report — https://data-science-group.github.io/weekly-report.html
40. Supervisor Meeting Brief — https://chromeboard.com/extension/supervisor-meeting-brief-fmibimgfmoaogdajeoeedledhejppgll
41. Haplo PhD Manager (search snippet; retried at the time of writing, 301 redirect to the Cayuse home page, to be verified) — https://support.haplo.com/phd-manager/user-guidance/supervision-meetings
42. Soft Academia — https://softacademia.substack.com/p/dear-bewildered-and-burnt-out
43. Liu, Althoff, Heer, CHI 2020 — https://ar5iv.arxiv.org/html/1910.13602
44. Inie et al., C&C 2022 — https://researcher.itu.dk/en/publications/how-researchers-manage-ideas/
45. Wiley ExplanAItions 2025 — https://newsroom.wiley.com/press-releases/press-release-details/2025/AI-Adoption-Jumps-to-84-Among-Researchers-as-Expectations-Undergo-Significant-Reality-Check/default.aspx
46. THE report on OUP survey — https://www.timeshighereducation.com/news/use-ai-research-widespread-distrust-still-high-oup
47. Gautam et al., FAccT'26 — https://arxiv.org/pdf/2604.23136
48. UCSD AI guidelines — https://privacy.ucsd.edu/ai-guidelines/
49. Speech-to-LaTeX — https://arxiv.org/html/2508.03542v1

**Complaints, lawsuits, and compliance (cited from M4, U2, U4)**
50. HN: Leave your AI note-taker at home — https://news.ycombinator.com/item?id=48823024
51. HN: Otter bot recording without consent — https://news.ycombinator.com/item?id=32751071
52. HN: Launch HN Hyprnote — https://news.ycombinator.com/item?id=44725306
53. Zoom AI Companion summary error evaluation — https://www.writingclearscience.com.au/ai-meeting-summary/
54. Lilach Bullock: AI minutes and accountability — https://www.lilachbullock.com/ai-meeting-notes-accountability-small-teams/
55. Collab365: Teams recap action items — https://collab365.com/library/microsoft-365-productivity/teams-meeting-recaps-create-notes-but-actions-stil-IrSTUa
56. Programming Insider — https://programminginsider.com/why-ai-note-taker-summaries-go-unread-and-what-fixes-it/
57. NPR: Otter class action — https://www.npr.org/2025/08/15/g-s1-83087/otter-ai-transcription-class-action-lawsuit
58. PPC Land: Granola class action — https://ppc.land/granola-sued-for-recording-meetings-without-consent-to-train-ai-models/
59. Kolmogorov Law survey (KRDO repost) — https://krdo.com/stacker-business-economy/2026/07/16/ai-notetakers-have-sat-in-on-1-in-3-us-workers-meetings-but-only-a-third-say-they-were-asked-first/
60. UW-Madison third-party bots — https://kb.wisc.edu/helpdesk/149383
61. University of Waterloo bot guidelines — https://uwaterloo.ca/information-systems-technology/about/policies-standards-and-guidelines/artificial-intelligence-ai/meeting-bots-ai-transcription-tools-guidelines
**Other segments (cited from U2)**
62. Procore Meeting Minutes Publisher — https://www.procore.com/ai/agents/meeting-minutes-publisher
63. Procore Meetings — https://www.procore.com/en-ca/project-management/meetings
64. OpenSSF TAC issue #532 — https://github.com/ossf/tac/issues/532
65. Kubernetes community meeting description — https://github.com/kubernetes/community/blob/master/events/community-meeting.md
66. Monolith law firm: managing change in system development — https://monolith.law/en/it/howto-manage-change-in-system-development

**Multilingual and localization (cited from U4)**
67. CS-Dialogue — https://arxiv.org/html/2502.18913
68. Fun-ASR technical report — https://arxiv.org/html/2509.12508v3
69. AssemblyAI Universal-3.5 Pro — https://assemblyai.com/blog/universal-3-5-pro-code-switching-contextual-prompting

**Methodology (cited from S1–S5)**
70. Hamel Husain, Evals FAQ — https://hamel.dev/blog/posts/evals-faq/
71. Google PAIR Explainability + Trust — https://pair.withgoogle.com/chapter/explainability-trust/
72. a16z, Avoiding Death on the Yellow Brick Road — https://a16z.com/avoiding-death-on-the-yellow-brick-road/ ; MIT NANDA (Fortune) — https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/

---

## Confidence in this document's conclusions

| Conclusion | Confidence | Rationale |
|---|---|---|
| "Meeting-to-action-item, with citations, human confirmation, no bot, no training" are no longer differentiators | **High** | Primary official pages in M1 and M2 corroborate each other |
| "Cross-meeting commitment tracking (binary version)" has already been built | **High** | This round opened Fellow's official page; M2 recorded Otter and Granola pre-meeting briefs; U2 opened the original Littlebird source |
| No vendor publishes action-item quality (K1) | **Medium** | This means "not found among the 24 products searched," not an exhaustive check |
| G2–G4 (verifiable, no guessing, claiming) are real needs | **Medium-high** | Multiple sources: HN, Trustpilot, blogs, lawsuits; but complaint channels skew toward English-language and technical communities, and toward negative sentiment |
| G2–G4 can constitute differentiation | **Medium-low** | All are features that can be copied quickly; Q1's competitor error analysis is needed to quantify the gap |
| G5, G6, G9 (research semantics) are uncovered gaps | ~~**Medium**~~ **Medium-low** (revised at the time of writing: G5's "status feedback" and "evidence comparison" are each half-covered by Fellow and Littlebird; G6's institutional basis is entirely [Summary]) | "No product models hypotheses and results" is a search conclusion based on verified pages; "users need it" rests mainly on indirect evidence from policies and guidelines, lacking frequency and sentiment evidence |
| G8 (Chinese-English terminology) is a strong pain point | **Low to medium** | The academic figures are credible, but there is no first-hand complaint from any Chinese-speaking user |
| Specific scores and rankings in the scoring table | **Low to medium** | Subjective scoring by the researcher; multiplying four dimensions amplifies single-dimension error; gaps within 30 count as the same tier |
| Positioning statements and "one-sentence answers" for the six options in §4 | **Assumption** | All pending PR/FAQ review and user interview validation; sentences containing X/Y numbers **must not be used externally before G1 is measured** |
| Quoted verbatim text | **Medium** | All cited from earlier files, which note that some come from scraping-tool summaries; each must be opened and checked before external use |

**Most important reminder**: What this synthesis can strongly support is two things: first, **what is no longer a differentiator** (including the newly added "cross-meeting tracking" this round); second, **the room for differentiation lies in the semantic layer "after the commitment"** (verifiable, claimed, with outcomes). It **cannot** support "research labs are the answer." The research options (B, C) rank first because they can be dogfooded and large vendors will be slow to copy them, not because the evidence is stronger. Option A, which has the strongest evidence, is precisely the easiest to copy. The next round's competitor error analysis (Q1) and diary study (Q3) are the only ways to break this deadlock.

---

## Revision log (Round 2)

> Based on `01_market-research/06_research_integrity_review.md` §1 (V1–V14), §2 (W1, W7, W8, W10), §6 (C8–C10), §9 P0-4, and the following pages were re-opened with WebFetch for verification: Fellow × GitHub, Fellow Action Items, Granola Integrations, Littlebird Pricing, Littlebird Promise Tracker, Teams Facilitator, Google Meet help page, Krisp Pricing, Krisp AI Meeting Assistant, Feishu AI Meeting Minutes. Parts of the original text that were overturned are kept with strikethrough.

| # | Location | Change | Basis |
|---|---|---|---|
| 1 | frontmatter, reading notes | Status marked as revised; sources_count 72 → 83; added explanation of the [Summary] tag | 06 §7 |
| 2 | §0 item 3 | Added strikethrough to "binary state"; added Littlebird's three states and Fellow's GitHub sync; added "the general version is already partially covered" to the "with outcomes" item | 06 V1, V4 |
| 3 | K3 | Changed "None / all" to "Partial: Littlebird skips vague maybes"; changed the judgment from [Inference] to [Fact]+[Inference] | 06 V5 |
| 4 | K5 | Changed the title to "mostly binary"; added Littlebird's three-state evidence comparison and Fellow's two-way GitHub sync | 06 V4, V6 |
| 5 | K8 | Added the source for Krisp's on-device English transcription (AI Meeting Assistant page); added "supported languages do not include Chinese" | 06 V9, C8; re-verified this round |
| 6 | K11 | Added strikethrough to the entire claim; changed to "GitHub/Linear/Jira integrations exist; W&B/Overleaf/Zotero not found" | 06 V1, V2, C9 |
| 7 | K12 | Added strikethrough to "no product does glossary chaining"; added Feishu's enterprise information recognition, the single-language limits of Gemini and Facilitator, and Krisp's lack of Chinese | 06 V8–V13, C10 |
| 8 | §2 how to read | K3 no longer counts as a "fully blank row"; added correction notes for K11/K5/K3 | Same as above |
| 9 | §3.1 ranking table | G5's U 4 → 3 (192 → 144); G20's U 3 → 2 (90 → 60); added a note to G17 without changing its score; added a correction paragraph | 06 V1, V3, V4 |
| 10 | G3 | Added evidence that Littlebird skips vague commitments | 06 V5 |
| 11 | G4 | Changed the Teams "suggestions" item from [Fact] to [Summary·pending verification] and noted it may be superseded by Facilitator Planner tracking; added that the Fellow page shows no "assignee confirmation" | 06 W7, V6, V11 |
| 12 | G5 | Added strikethrough to "Fellow only tracks open/closed"; added GitHub sync, Littlebird evidence comparison, and the ZoomMate project agent; confidence Medium → Medium-low | 06 V1, V4, V10, W10 |
| 13 | G6 | Changed the UW CS and UK supervision system items from [Fact] to [Summary·pending verification] (neither original page would open); added the Littlebird Team plan to the counterarguments | 06 W1, W8, C1 |
| 14 | G8 | Changed the Feishu replacement rules item from [Fact] to [Summary]; added Feishu enterprise information recognition | 06 V13 |
| 15 | G12 | Changed the design-rationale literature item from [Fact] to [Summary·pending verification] | 06 §7 |
| 16 | G17 | Added strikethrough to "Littlebird is personal-only"; added the Team plan and "tuned to yours"; changed the differentiation to "team-shared commitment ledger" | 06 V3, C4 |
| 17 | G20 | Added evidence of the Fellow and Granola GitHub integrations; confidence Medium-low → Low | 06 V1 |
| 18 | Option B | Added strikethrough to the original "one-sentence answer" and provided a corrected differentiation statement; noted in the G6 citation that the UK evidence is [Summary]; added Littlebird Team to the risks | 06 V3, W8 |
| 19 | Option C | Added strikethrough to the positioning statement "meeting tools only tick off tasks" and rewrote it; added a differentiation statement for when Fellow/Littlebird are raised; changed "the only benchmark" in the risks to "one of the benchmarks" | 06 V1, V4 |
| 20 | §6 Q9, Q15 | Q9 marked as answered (Littlebird has a Team plan); Q15 partially answered | 06 V3, V10 |
| 20b | §0 item 2 | Marked Zoom's "track cross-meeting projects" as [Summary·pending verification]; added Feishu's "meeting express" | 06 V10, V13 |
| 21 | Source list | Added 73–83 (Round 2 verification, all marked with access date at the time of writing); UW CS and Haplo marked as still unopenable on retry | — |
| 22 | Confidence table | G5/G6/G9 row changed from "Medium" to "Medium-low" | Same as above |

**Not changed, left for later**: the evidence grades of K2 (a single DingTalk test) and K7 (Tencent traceability contradiction); the scores of the other G items were not re-ranked; items such as "[Fact] DingTalk test" that are cited from M1 were not re-opened against their original pages one by one this round.
