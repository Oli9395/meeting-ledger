---
title: "Competitive Research 02: In-Depth Competitive Analysis of International Meeting AI Assistants (Otter / Fireflies / Granola / Gong and 15+ Others)"
status: draft (Round 2 revised in place per review 06)
sources_count: 81
sources_count_method: number of unique URLs in the sources section (recounted at close-out; original value 66)
---

# Competitive Research 02: In-Depth Competitive Analysis of International Meeting AI Assistants

> Labeling conventions: **[Fact]** has a source, with URL; **[Inference]** a judgment derived from facts, which may be wrong; **[Assumption]** a proposition awaiting validation, which requires user research or experiments; **To be verified** means sources contradict each other, only secondhand accounts exist, or the original page could not be opened.
> Unless otherwise noted, all pricing information reflects the figures on official pricing pages **accessed at the time of writing**. Any price given by a third-party site is always labeled "third-party".

---

## 0. One-Line Conclusion (Answer First, Then the Reasoning)

1. **[Fact] "Meeting → summary → action items" is already standard in the international market, and in most cases it is free.** All 15 products can output action items, and the platform vendors (Zoom, Microsoft, Google) bundle it directly into their plans. So "we can also extract tasks from meetings" **cannot** serve as differentiation (evidence in §2 and §3).
2. **[Fact] Even "human confirmation before sending" is not unique to BriefPilot.** The tl;dv website states that it drafts follow-up emails and next-step tasks "for review before sending"; Notion's summaries carry citations that link back to the original transcript; Teams Copilot's answers also carry citations (§3.4, §3.11, §3.9). The "citations + human confirmation" in the BriefPilot PRD counts as differentiation only if it is done **more deeply in a specific scenario**; these two forms alone are not enough.
3. **[Fact + Inference] The dominant industry direction is "more automatic": agents that write to the CRM automatically, create tasks automatically, and attend meetings for you.** Examples include ZoomMate, Otter's Sales/SDR Agent, Read's "Ada" digital twin, and Read's claim that it can "summarize even when no one attends". At the same time, backlash against recording consent and bots joining meetings is turning into litigation: Otter was hit with a class action in 2025-08, and Fireflies with a BIPA voiceprint lawsuit in 2025-12. **[Inference]** The tension between "more automatic" and "more trustworthy and controllable" is the most visible structural gap in this red ocean.
4. **[Fact] Granola broke out through its interaction paradigm, not its feature list.** It does not send a bot into the meeting; instead it lets "your own notes" act as the prompt, and it targets people such as VCs and founders, who have high meeting density, high willingness to pay, and spread the product among each other. Its valuation rose from $250 million (2025-05) to $1.5 billion (2026-03). **[Fact] Gong took the vertical route**: the sales scenario has a clear outcome signal ("deal won or not") and a budget-holding buyer in the CRO, and it grew to over $300 million in ARR. The shared lesson of the two cases for BriefPilot is: **differentiation must come either from the interaction paradigm (who leads, how the product joins) or from scenario depth (outcome signal + budget holder + domain workflow); adding a single feature point is not enough** (§4, §5).
5. **[Inference] International products share six common weaknesses.**
   - ① None publishes the accuracy of its action-item extraction (precision, recall, owner attribution);
   - ② Local or offline deployment is nearly nonexistent, and "no bot" does not mean "not in the cloud";
   - ③ The burden of consent is shifted onto the user;
   - ④ Support for cross-organization meetings is weak; for example, Teams Copilot is unavailable in meetings hosted by an external organization;
   - ⑤ ~~The integration ecosystem is centered on sales CRMs, and engineering and research tools (e.g., GitHub Issues) did not appear in the pages crawled in this round;~~ (Corrected: this does not hold. Fellow syncs bidirectionally with GitHub; Granola connects to GitHub, Linear, Jira, and Asana via Zapier; Circleback, Read, and Otter offer MCP or Claude integration. The Fellow and Granola integration pages had not been crawled at the time. Sources: https://fellow.ai/integrations/github , https://www.granola.ai/integrations , accessed at the time of writing. Only research tools such as W&B, Overleaf, and Zotero remain unseen.)
   - ⑥ Multilingual and mixed Chinese-English capabilities degrade under an "English first" approach; for example, Notion's speaker labeling supports only English, and Krisp's local transcription supports only English. (Added at the time of writing: Chinese is **not** among Krisp's 16 supported languages; Google Meet "Take notes for me" has no Chinese among its supported languages and states "Multiple languages spoken in the same meeting aren't currently supported"; Teams Facilitator's AI notes "only support meetings where a single language is spoken". Sources: https://krisp.ai/pricing/ , https://support.google.com/meet/answer/14754931 , https://learn.microsoft.com/en-us/microsoftteams/facilitator-teams , accessed at the time of writing.)

   **Clearly overlooked groups**: cross-institution research labs, teams in regulated or air-gapped environments, small teams in Asia that mix Chinese and English, and small non-sales engineering teams (§7, §8).
6. **[Fact] There is a new competitor to watch: Littlebird.** It targets graduate students directly, with the selling points of "tracking your commitments to your advisor", pre-meeting briefs, and recording without a bot, at a student price of $15 per month. This shows that "research commitment tracking" is not uncontested territory. ~~However, it is a **personal** assistant, not a **lab- or team-level** tool (§3.17).~~ (Corrected: the Littlebird pricing page has a **Team plan, from $17 per seat per month (billed annually)**, which includes "Admin controls and team usage analytics" and "Shared projects and routine templates", https://littlebird.ai/pricing , accessed at the time of writing. The accurate statement is: **it has a team billing tier, but the commitment-tracking routine remains personal in perspective**: "tuned to yours, the things you said you'd do"; tracking what others owe you has to be specified separately in the prompt, and the page describes no shared team commitment ledger, https://littlebird.ai/routines/promise-tracker . See §3.17.)
7. **[Fact, added at the time of writing] This document originally missed two direct rivals: Fellow and Microsoft Teams Facilitator.** Fellow brings unfinished action items into pre-meeting prep, supports multiple owners and reassignment, and syncs bidirectionally with GitHub; Facilitator offers Planner task tracking (public preview) and mobile capture of in-person discussions, but supports only a single language and does not support external meetings or 1:1 chats. See the new §3.18 and §3.19 and the new rows in the matrix.

---
## 1. Research Scope, Method, and Limitations

- **Subjects**: the 15 products required by the brief (Otter.ai, Fireflies.ai, Fathom, tl;dv, Granola, Read.ai, Circleback, Zoom AI Companion, Microsoft Teams Copilot, Google Gemini in Meet, Notion AI Meeting Notes, Krisp, Supernormal, Avoma, Gong), plus two related subjects found during research: Littlebird (graduate-student scenario) and anarlog (formerly Hyprnote, an open-source local solution).
- **Method**: I prioritized **official pricing pages, product pages, and help documentation**. Funding and revenue figures were cross-checked against TechCrunch, Tech.eu, and Sacra. User complaints come from Trustpilot, Microsoft Tech Community, university IT notices, and law-firm blogs.
- **Limitations (must be stated honestly)**:
  1. **The original Reddit, G2, and Capterra pages could not be opened directly**: Reddit rejected the scraping tool, and G2 and Capterra returned 403. Every quote in this document labeled "Reddit/G2/Capterra" **comes from search snippets or aggregator-site retellings and is secondhand material**; each one is marked "secondhand".
  2. **This session's search quota has been used up** (shared cap of 200). As a result, **public complaints about Zoom AI Companion, Teams Copilot, Gemini, Avoma, and Supernormal were not specifically collected**. These are marked "not collected" in the relevant entries, and nothing has been fabricated. If needed, they can be filled in with a separate search in the next round.
  3. Claims on vendor websites, such as accuracy and user counts, are **vendor self-reported** and have not been independently verified.

---

## 2. Market Landscape: Four Types of Players

| Category | Representatives | How it joins meetings | Business logic | Meaning for BriefPilot |
|---|---|---|---|---|
| A. Standalone notetakers that join via bot | Otter, Fireflies, Fathom, tl;dv, Read, Avoma | After calendar authorization, a bot joins automatically (most have since added a desktop no-bot mode) | Free tier for acquisition → per-seat pricing → sold to sales teams via CRM integrations | The main battlefield for "meeting to tasks"; already highly homogeneous |
| B. No-bot, enhanced personal notes | Granola, Circleback desktop, Krisp, Supernormal, Notion, Littlebird | Captures local device audio; no bot appears in the meeting | Experience-driven; individuals adopt first, then it spreads to teams | Proves that the "interaction paradigm" itself can be a differentiator |
| C. Built into the platform | Zoom AI Companion, Teams Copilot, Gemini in Meet | Native capability | Bundled into plans; marginal price close to 0 | Pushes the price of basic summaries and action items to the floor; standalone tools must go "deeper" to survive |
| D. Vertical specialists | Gong (sales revenue intelligence), Avoma (sales-leaning) | Bot joins | Sold to business owners with budget (CROs); high contract value | A model of successful verticalization (§5) |

**[Inference]** Category A is being squeezed from below by Category C, because free bundled platform capabilities can already cover "basic summary + action items". Category A is therefore moving upmarket into agents, CRM automation, and sales coaching, increasingly resembling Category D. Category B takes a different path, competing on user experience and social cost. **[Inference] None of these three paths has gone deep in scenarios that are high-sensitivity, cross-organizational, non-sales, and multilingual.** This is the starting point for Sections 7 and 8.

---

## 3. Product-by-Product Analysis

> Each product is laid out with the same fields: positioning and target users, core features, pricing, distinguishing traits, complaints, how action items are extracted and how reliable that is, task integrations, privacy and compliance, and on-premises deployment.

### 3.1 Otter.ai

- **Positioning and target users** [Fact]: The website describes itself as "Meeting AI that turns talk into action" and calls itself "the world's only Conversational Knowledge Engine". The target audiences listed are sales (including SDRs), education, media, recruiting, and enterprise. Source: https://otter.ai/
- **Core features** [Fact]:
  - Recording works on desktop (including a no-bot mode), mobile, and in the browser;
  - Pre-meeting briefs that bring in "previous discussions, action items, and updates";
  - Otter AI Chat can answer questions across meetings and across apps;
  - Live-Assist real-time prompts;
  - Channels for grouping by team or project;
  - An MCP Server that can connect to ChatGPT and Claude.

  Source: same as above.
- **Pricing (official page accessed at the time of writing)** [Fact]:

  | Plan | Price | Main limits |
  |---|---|---|
  | Basic | Free | 300 minutes per month, 30 minutes per session, 3 file imports for life |
  | Pro | $16.99 monthly / $8.33 annual (the page also shows a promotional price marked with an asterisk) | 1,200 minutes per month, 90 minutes per session |
  | Business | $30 monthly / $19.99 annual | Unlimited meetings, 4 hours per session |
  | Enterprise | Custom | SSO and SCIM require at least 100 users; HIPAA is an Enterprise add-on |

  Source: https://otter.ai/pricing
- **Distinguishing traits** [Inference]: Otter started as a "recording and transcription" product and is the established player most aggressively transforming into a "knowledge engine + sales agent"; the Enterprise tier comes with a Sales Notetaker and an SDR Agent.
- **Public complaints**:
  - [Fact] The Carleton College IT blog (2026-03-26) recorded one instructor's experience: Otter "joined their Google Meet without being invited, without asking permission", and the person only learned of it upon receiving the transcript email Otter sent. The author commented: "the default settings, at least to me, prioritize convenience over consent", and "an unanticipated email of a recording can erode the trust that makes those conversations possible". The author also notes being **unable to fully reproduce** the situation. Source: https://www.carleton.edu/ai/blog/an-uninvited-guest-what-you-should-know-about-otter-ais-notetaker/
  - [Fact] Trustpilot has 826 reviews with a TrustScore of 4.4, of which 26% are 1-star. One 4-star review (Ezra Simons, 2026-08-13) says: "there is a sales feature that pulls your team onto a paid plan sort of in the background". Source: https://www.trustpilot.com/review/otter.ai
  - [Secondhand] Aggregator sites relayed a 2024 Reddit user's remark calling Otter "basically malware", on the grounds that it joins other people's meetings and then invites all attendees to sign up. The original post could not be opened, so this is **to be verified**. The retellings are cited in search snippets from https://char.com/blog/otter-ai-review and https://vantaige.io/ai-tool/otter-ai
  - [Fact] **Class action**: On 2025-08-15, Justin Brewer sued Otter in the U.S. District Court for the Northern District of California, alleging that Otter Notetaker records without the consent of participants (including non-Otter users) and uses the recordings to train models. The complaint states that once a host connects a calendar, the Notetaker can join **without any participant's affirmative consent**. Otter's response is that it "only records when a user starts it", and that its terms require users to obtain permission themselves. As of this writing, the status of the case is **to be verified**. Sources: https://www.npr.org/2025/08/15/g-s1-83087/otter-ai-transcription-class-action-lawsuit ; https://www.storyboard18.com/digital/otter-ai-sued-for-allegedly-recording-private-conversations-without-consent-79130.htm
  - [Fact] The University of Waterloo's internal wiki has a dedicated page titled "Stop Otter.ai from joining meetings and sharing transcripts". Source: https://uwaterloo.atlassian.net/wiki/spaces/HEALTHHELP/pages/44600164869/Stop+Otter.ai+from+joining+meetings+and+sharing+transcripts
- **Action item extraction** [Fact]: The website claims it "Captures and assigns next steps automatically"; the pricing page lists a takeaways panel where action items can be assigned. **[Fact] No public action-item accuracy figure for Otter was found.**
- **Task integrations** [Fact]: The website lists Slack, Notion, Jira, Asana, Salesforce, and HubSpot. The pricing page shows that the Pro tier already includes Salesforce, HubSpot (subject to user limits), and Zapier.
- **Privacy and compliance**:
  - [Fact] HIPAA is an Enterprise add-on. The website homepage lists no specific certifications, saying only "built with the security, governance, and compliance controls enterprises expect".
  - [Secondhand] Several sources say Otter by default emails the transcript to everyone on the invite list; the current default is **to be verified**.
- **On-premises deployment** [Fact]: No on-premises or offline deployment option appeared in the official pages scraped this round.
### 3.2 Fireflies.ai

- **Positioning and target users** [Fact]: Describes itself as "The #1 AI Assistant For Your Meetings," covering meetings, email, Slack, and 100+ tools. The website claims "75% of Fortune 500" use it (vendor's own claim). Industries covered include sales, recruiting, engineering, healthcare, education (FERPA), VC, and others. Source: https://fireflies.ai/
- **Core features** [Fact]:
  - Real-time notes, multilingual mode (100+ languages, with automatic detection);
  - AskFred Q&A, sentiment analysis, "transcript-only / summary-only" modes;
  - Automatic task creation after meetings.

  Sources: https://fireflies.ai/ ; https://fireflies.ai/pricing
- **Pricing** [Fact]: The official pricing page  **does not show any amounts**. It lists only four tiers: Free, Pro, Business, and Enterprise. Enterprise includes private storage, SSO, SCIM, audit logs, and custom retention periods. Source: https://fireflies.ai/pricing
  - [Third-party, to be verified] Pro is about $10/seat/month (billed annually) or $18 (billed monthly); Business is about $19 (annual) or $29 (monthly); Enterprise is about $39 (annual). The Pro tier reportedly includes only 20 AI credits per month. Sources: https://sonix.ai/resources/fireflies-ai-pricing/ ; https://www.outdoo.ai/blog/fireflies-ai-pricing
- **Public complaints**:
  - [Fact] On the Microsoft Tech Community, an administrator wrote: "We've removed your app permissions from all users, but your bot keeps trying to join meetings." Another user said: "It stopped as soon as I unsubscribed in the fireflies website." Source: https://techcommunity.microsoft.com/discussions/microsoft-365/fireflies-ai-note-taker-robot-keeps-popping-up/1571150
  - [Fact] Trustpilot has 882 reviews with a 4.5 rating. A 1-star review (Rutger Jönåker, 2026-10-30) wrote: "Several email categories were already checked and greyed out, making it impossible to change them." The same reviewer also wrote: "A company that cannot respect a simple 'NO' has absolutely no business asking for access". Source: https://www.trustpilot.com/review/fireflies.ai
  - [Fact] On the Zoom community, a user asked "How to block bots like firefliesai notetaker". Source: https://community.zoom.com/t5/Zoom-Meetings/How-to-block-bots-like-firefliesai-notetaker/m-p/210098
  - [Fact] **BIPA voiceprint lawsuit**: Plaintiff Katelin Cruz, case no. 3:25-cv-03399, filed 2025-12-18, alleging that Fireflies' speaker recognition feature generates voiceprints without written notice and consent. According to secondary reports, a second similar lawsuit was filed in 2026-03, **to be verified**. Sources: https://www.dataprivacyandsecurityinsider.com/2025/12/lawsuit-alleges-fireflies-ai-corp-illegally-collects-biometric-data-from-virtual-meetings/ ; https://www.workplaceprivacyreport.com/wp-content/uploads/sites/938/2026/04/Fireflies.ai-Complaint-1.pdf ; https://www.illinoislawyernow.com/2026/02/employers-beware-uptick-in-bipa-lawsuits-targeting-ai-note-taking-software/
- **Action item extraction** [Fact]: The AI summary includes action items; the website says it can "Create tasks automatically after every meeting". **This is "auto-create," not "create after confirmation."** No accuracy data was found in this round.
- **Task integrations** [Fact]: The website mentions only generic "project management integrations" and does not name Asana, Jira, or Linear; the pricing page shows "App and CRM integrations" starting from the Pro tier.
- **Privacy and compliance** [Fact]:
  - Certifications: SOC 2 Type II, ISO 42001, GDPR;
  - HIPAA BAA and FERPA DSA require Enterprise plus private storage;
  - States that "data is never used for AI training".
- **On-premises deployment** [Fact]: Enterprise "Private Storage" is "Dedicated cloud storage", **not on-premises deployment**.
### 3.3 Fathom

- **Positioning** [Inference]: The free tier is extremely generous and is used to acquire users; revenue comes from charging teams and sales organizations (CRM field sync, deal views, coaching scores).
- **Pricing (official)** [Fact]:

  | Plan | Price (per user per month) | Main contents |
  |---|---|---|
  | Free | Free | Unlimited recording and transcription; bot-free capture is a beta feature on Mac |
  | Premium | $20 monthly / $16 annual | |
  | Team | $19 monthly / $15 annual | Minimum 2 seats |
  | Business | $34 monthly / $25 annual | CRM field sync, AI scorecards |
  | Enterprise | Contact sales | |

  All paid plans come with a 90-day guarantee. Source: https://www.fathom.ai/pricing
  - [Third-party] One source says the free tier's advanced AI summaries are limited to 5 per month. Source: https://sonix.ai/resources/fathom-pricing/
- **Core features** [Fact]:
  - Integrations: Claude, ChatGPT, Zapier/Make, Slack, HubSpot, Salesforce, Asana, and a public API (with MCP support);
  - Ask Fathom can answer questions across calls.

  Same source as above.
- **Public complaints** [Secondary: G2/Capterra search snippets; original pages returned 403]:
  - The G2 aggregate page lists 329 cons in the "meeting report accuracy" category;
  - A Capterra review says "sometimes takeaways weren't accurate" and "does not get names correct all the time"; the latter directly affects who an action item gets assigned to;
  - A G2 review also says "don't blindly trust the summaries".

  Sources: https://www.g2.com/products/fathom-video ; https://www.capterra.com/p/276054/Fathom/reviews/?page=8 (**original text for both still to be verified**)
- **Action item extraction** [Fact]: The Premium and Team tiers offer AI action items; the free tier is marked "Limited use" in the comparison table. **Reliability** [Secondary]: Users rate it well overall, but name recognition and assignment make mistakes, so human review is needed.
- **Task integrations** [Fact]: Asana, HubSpot, Salesforce; CRM sync is limited to 3 users per domain (the page does not make clear which plans this applies to).
- **Privacy and compliance** [Fact]: The Enterprise tier provides SSO, SCIM, custom retention periods, and a HIPAA BAA; see trust.fathom.video for details.
- **On-premises deployment** [Fact]: None found.

### 3.4 tl;dv

- **Positioning and target users** [Fact]: The website describes it as an AI notetaker for team collaboration, its tagline reads "No bot required", and it claims more than 2 million users. Primary users are sales, product management, marketing, and customer success teams. Source: https://tldv.io/
- **Core features** [Fact]:
  - Customizable summary formats, including sales frameworks such as MEDDIC;
  - **Cross-meeting reports**: aggregate trends and feature requests across multiple meetings, delivered by email on a schedule;
  - Sales coaching;
  - Transcription and translation in 30+ languages;
  - **Drafts follow-up emails and next-step tasks "for review before sending"**.
- **Pricing (official, EUR)** [Fact]: Free €0; Pro €29 monthly / €18 annual; Business €39 monthly / €29 annual. Source: https://tldv.io/pricing/
- **Distinguishing points** [Fact]:
  - Data is hosted in the EU, and private AI hosting is available on request;
  - Claims data is "never used to train AI", and works with Anthropic to provide generative AI;
  - The website still displays an "EU US Privacy Shield" badge. That framework was invalidated by the EU Court of Justice in 2020, so **what this badge means is still to be verified**.
- **Public complaints**: **Not collected this round** (search quota limit).
- **Action item extraction** [Fact]: After extracting action items, it **drafts tasks for human review**. By design this is the closest match to BriefPilot's "takes effect only after confirmation", and **BriefPilot can no longer claim this as unique**.
- **On-premises deployment** [Fact]: The website mentions "private AI hosting available on request". Whether this includes customer-run data centers (on-prem) is **still to be verified**.

### 3.5 Granola (detailed analysis in §4)

- **Positioning and target users** [Fact]: An "AI notepad". Users jot down key points themselves during the meeting, Granola transcribes in the background, and AI fleshes out the notes afterward. The CEO says: "Granola's secret? It augments you, rather than replaces you." The October 2024 Series A blog post says more than half of users hold leadership roles, and partners at Benchmark, Sequoia, Accel, and USV use it to listen to pitches. Source: https://granola.ai/blog/series-a
- **Pricing (official)** [Fact]:

  | Plan | Price (per user per month) | Main contents |
  |---|---|---|
  | Basic | $0 | Only 30 days of meeting history retained |
  | Business | $14 | Unlimited history; cross-meeting AI chat; pre-meeting briefs; follow-up emails; integrations with Notion, Zapier, HubSpot, Attio, Affinity; MCP and API |
  | Enterprise | $35 | SSO (50+ users), SCIM, HIPAA workspace, audit API, Salesforce; training disabled by default |

  Source: https://www.granola.ai/pricing
- **Public complaints**:
  - [Secondary] The Verge reportedly reported in April 2026 that Granola note links were by default "viewable by anyone with the link", and that non-Enterprise users participated in model training by default (unless they opted out manually). This round only found a Chinese-language repost (aitoolly, 2026-04-02 or 04-03); **the original The Verge article was not read and is still to be verified**. Granola's security page currently says "Notes are private by default"; its sharing settings documentation lets admins set the default to public link, company-only, or off. Sources: https://aitoolly.com/zh/ai-news/article/2026-04-03-granola-privacy-alert-ai-notes-viewable-via-link-and-used-for-training-by-default ; https://www.granola.ai/security ; https://www.granola.ai/docs/docs/FAQs/sharing-controls
  - [Fact + Secondary] **Audio is not retained, so there is no playback.** Granola's security page states "Granola doesn't store the audio from meetings". Several reviews point out that in a dispute you cannot listen back to check; however, most of these reviews come from competitors' blogs and have a bias. Sources: https://www.granola.ai/security ; https://tldv.io/ko/blog/granola-review/ ; https://www.meetjamie.ai/en/blog/granola-review
  - [Secondary] Speaker identification is weaker on Windows and in the Zoom web client (from HappyScribe, a transcription vendor with a conflict of interest). Source: https://www.happyscribe.com/nl/blog/granola-ai-review
  - [Secondary] From 2024 to early 2026, the local cache `cache-v3.json` was plaintext and third-party tools read it directly; version 7.427.0 in July 2026 closed off this route. Source: https://superframeworks.com/articles/granola-encrypted-local-notes (**to be verified**)
  - [Fact] Granola has officially published several security post-mortems, including a TestFlight build leaking an AssemblyAI API key and a desktop vulnerability reported on 2026-06-23. Sources: https://docs.granola.ai/help-center/policies/security-reports/post-mortem-assembly-ai-api-key-exposure ; https://docs.granola.ai/help-center/policies/security-contributions/desktop-app-navigation-vulnerability
- **Action item extraction** [Fact + to be verified]: The selling point is "augmenting the notes you write", and the Business tier provides follow-up emails. **This round did not verify, on official pages, any specific mechanism for "automatically assigning action items to someone"; still to be verified.**
- **Task integrations** [Fact]: Notion, Zapier, HubSpot, Attio, Affinity, Slack, plus MCP and API. The official pricing page **does not list Asana, Jira, or Linear**. ~~(Implication: no engineering-tool integrations)~~ (Corrected at the time of writing: the pricing page indeed does not list them, but the **integrations page** lists Asana, ClickUp, **GitHub**, Jira, Linear, Monday.com, and Trello under Project management, all "via Zapier"; Claude, ChatGPT, Cursor, and others connect through the "Granola MCP connector". Source: https://www.granola.ai/integrations , accessed at the time of writing.)
- **Privacy and compliance** [Fact]:
  - Capture: no bot on any plan; uses device audio;
  - Consent: a consent message can be sent automatically at the start of a meeting; Enterprise can enforce an organization-wide prompt (marked as a pilot, i.e., a trial feature); the official recommendation is to obtain consent before transcribing others;
  - Certification: SOC 2 Type 2 (obtained 2025-07);
  - Cloud pipeline: transcription uses Deepgram and Assembly, summarization uses OpenAI and Anthropic, and data is stored on AWS in the US.

  Sources: https://www.granola.ai/pricing ; https://www.granola.ai/security
- **On-premises deployment** [Fact]: None. Both transcription and summarization go through the cloud; **"no bot" ≠ "not in the cloud"**.
### 3.6 Read.ai

- **Positioning** [Fact]: Its tagline is "Meetings In, Decisions Out." It describes itself as "independent and platform-agnostic" and claims "millions" of users. It puts meetings, email, and Slack content into a single search context; it has a digital twin called "Ada"; and it also claims that "an AI agent can summarize meetings even when no one attends." Source: https://www.read.ai/
- **Pricing (official)** [Fact]:

  | Plan | Price (per user per month) | Main contents |
  |---|---|---|
  | Free | Free | 5 meetings per month |
  | Pro | $19.75 monthly / $15 annual | |
  | Enterprise | $29.75 monthly / $22.50 annual | Minimum 5 seats |
  | Enterprise+ | $39.75 monthly / $29.75 annual | HIPAA, SAML, SCIM, custom retention period |

  Source: https://www.read.ai/plans-pricing
- **Public complaints** [Fact]:
  - An information security bulletin from Cumbria Fire and Rescue Service in the UK asks staff to remove unauthorized bots such as Otter and Read.ai from meetings. Source: https://www.cumbriafire.gov.uk/sites/default/files/2025-10/28799%20CFRS%20Information%20Security%20Month%2025%20Newsletter%205%20v3.pdf
  - An IT notice from UW-Madison also lists read.ai among "uninvited bots." Source: https://kb.wisc.edu/helpdesk/149383
- **Action item extraction** [Fact]: Ask Read can answer questions about "decisions, owners, and open items" with citations; action items can be routed to the tools a team already uses.
- **Task integrations** [Fact]: Jira, Confluence, Notion, Asana, **Linear**, HubSpot, Salesforce, Zapier, webhooks.
- **On-premises deployment** [Fact]: Not seen.

### 3.7 Circleback

- **Positioning** [Fact]: The website describes it as "AI-powered notes, action items, automations, and search," backed by YC. Source: https://circleback.ai/
- **Pricing (official)** [Fact]:

  | Plan | Price (per user per month) | Main contents |
  |---|---|---|
  | Free | $0 | Unlimited meetings, but only 30 days of history retained |
  | Pro | $15 | All integration automations |
  | Business | $25 | Custom retention period |
  | Enterprise | $35 | SSO, SCIM, HIPAA |

  All tiers include API, MCP, and CLI. Source: https://circleback.ai/pricing
- **Features** [Fact]:
  - Desktop app (Mac and Windows) with no bot; also supports in-person meetings and mobile;
  - **Incorporates slides, dashboards, and documents from shared screens into the notes**;
  - Supports 100+ languages;
  - States that it does not train models on customer data.
- **Action item extraction** [Fact]: Action items are "Captured, assigned, and organized." The website cites Garry Tan's comment "action and todos tracking is the best in class." **Note that Garry Tan is the CEO of YC, and Circleback is a YC-backed company, so there is a conflict of interest.** There is also a quote from the Runway CEO: "It gives me a sense of safety that I won't drop things I owe people."
- **Task integrations** [Fact]: Linear, Asana, Notion, HubSpot, Salesforce, Attio, Slack, Zapier, Make, webhooks. The website does not mention Jira.
- **Public complaints**: **Not collected in this round.**
- **On-premises deployment** [Fact]: Not seen.

### 3.8 Zoom AI Companion (including ZoomMate)

- **Positioning** [Fact]: AI Companion is included with paid Zoom Workplace plans at no extra charge. Version 3.0, released on 2025-12-15, added agentic workflows and was opened to free users and to standalone purchase (note: "opened to free users" is supported by a TechCrunch headline, while the "agentic workflows" details come only from the press release [Summary]). Sources: https://investors.zoom.us/news-releases/news-release-details/zoom-launches-ai-companion-30-agentic-workflows-transforming (summary; original returned 403); https://techcrunch.com/2025/12/15/zoom-brings-its-ai-assistant-to-the-web-with-access-to-free-users/
- **Current website ** [Fact]: The page now promotes **ZoomMate**.
  - Free Basic tier: 3 meeting summaries per month, 20 AI queries, 10 workflow runs;
  - Paid tier: unlimited notes, 2,200 AI credits per user per month;
  - After a meeting it can automatically update Salesforce, write follow-up emails, and draft presentations;
  - Connects to Salesforce, Jira, Google Drive, OneDrive;
  - My Notes supports Zoom, in-person, mobile, and third-party meeting platforms.

  Source: https://www.zoom.com/en/ai-assistant/
- **Pricing** [Third-party, to be verified]: ZoomMate launched on 2026-06-01, starting at $20 per user per month; the standalone AI Companion is about $10 per month. Source: https://www.laxis.com/blog/zoom-ai-companion/ ; the text captured from the official website contains no price figures.
- **Action item extraction** ~~[Fact]~~ **[Summary · to be verified]**: 3.0 provides a template library used to "capture action items and track cross-meeting projects." (correction: this sentence appears only in the search snippet of the investor press release, whose original returned 403; the official AI assistant page does not contain it, and instead says "ZoomMate project agent to track progress, share updates, and manage tasks," with My Notes covering in-person meetings and a Jira integration. Source https://www.zoom.com/en/products/ai-assistant/ , 06 V10, accessed at the time of writing. The general direction holds; the original sentence remains to be verified.)
- **Public complaints**: **Not collected in this round.**
- **On-premises deployment**: Not seen.
### 3.9 Microsoft Teams Copilot (meeting recap)

- **Features** [Fact]:
  - Summarizes key points and "who said what", and **suggests action items**;
  - Q&A is available both during and after the meeting, and **answers cite their sources**;
  - Participants who join more than 5 minutes late can get a catch-up summary.

  Source: https://support.microsoft.com/en-us/office/use-copilot-in-microsoft-teams-meetings-0bf9dd3c-96f7-44e2-8bb8-790bedf066b1
- **Key limitations** [Fact]:
  - Post-meeting use requires transcription to be turned on;
  - **"Copilot doesn't work in meetings hosted outside the participant's organization"**;
  - In a meeting series, once a later session is transcribed, the conversation history of the earlier session is lost;
  - When a transcript is deleted, the Copilot history is deleted with it;
  - Intelligent recap requires Teams Premium or a Copilot license.

  Source: same as above.
- **Pricing** [Third-party, to be verified]: Copilot Business (under 300 users) is listed at $21 per user per month (billed annually), with a promotional price of $18; the Enterprise edition is $30 per month and must be paired with a base license. Sources: https://www.stmicro.net/blog/microsoft-365-copilot-business-july-2026/ ; https://copilot-experts.com/microsoft-copilot-pricing-guide/
- **Compliance significance** [Fact]: The meeting etiquette guidance of Derbyshire County Council in the UK approves only Copilot and stipulates that external notetakers "must not be invited or permitted". Source: https://staff.derbyshire.gov.uk/site-elements/documents/information-security/meeting-etiquette-for-ai-notetakers.pdf
- **[Inference]** For organizations already in the M365 ecosystem, Copilot's "compliant by default" availability is itself a moat; but cross-organization meetings are precisely its blind spot.
- **(Added at the time of writing) [Fact]** Microsoft also has a meeting agent, **Facilitator**, with "Task tracking integration with Planner" (public preview), so the claim that "Teams only suggests action items and does not track them" is outdated; see the newly added §3.19.
- **Public complaints**: **not collected in this round**.

### 3.10 Google Gemini in Meet (Take notes for me)

- **Features** [Fact]: Transcribes the meeting, generates a summary with key action items, saves it as a Google Doc, and emails the summary to the user; when the feature is on, **all participants are notified**; only "select languages" (a subset of languages) are supported. Source: https://blog.google/products-and-platforms/products/workspace/take-notes-for-me/ (2026-06-29)
- **In-person meetings** [Fact]: Starting 2026-08-13, an in-person "Take notes with me" mode is supported, available on Business Standard and Plus, Enterprise Standard and Plus, Google AI Pro and Ultra, Frontline Plus, and AI Pro for Education, and it reuses the existing Meet note-management settings. The official post **does not say whether action items are labeled with an owner**. Source: https://workspaceupdates.googleblog.com/2026/08/take-notes-with-me-for-in-person-meetings-is-now-available.html
- **Language limitations** [Fact, added at the time of writing]: The supported languages listed on the help page are English, French, German, Italian, Japanese, Korean, Portuguese, and Spanish, **with no Chinese**; "This feature supports one language at a time. Multiple languages spoken in the same meeting aren't currently supported." Source: https://support.google.com/meet/answer/14754931 (accessed at the time of writing)
- **[Inference]** Google already covers "in-person meetings + automatic minutes" and also offers this feature for the education edition. But the minutes are just a Doc, with **no task closed loop**: no confirmation and no overdue tracking.
- **Public complaints**: **not collected in this round**.

### 3.11 Notion AI Meeting Notes

- **Features** [Fact]:
  - Capture: the desktop app captures microphone and system audio, while browser and mobile use only the microphone (suitable for in-person meetings);
  - Languages: 16 are supported, including Chinese and English; **speaker labeling is English only**;
  - Summaries: highlights key points and action items, with **citation links back to the original transcript**;
  - Pre-meeting notes are incorporated into the summary;
  - Notes are stored in a meetings database, and follow-up tasks can be created through skills;
  - Up to 10 hours per person per day; **offline is not supported**.

  Source: https://www.notion.com/help/ai-meeting-notes
- **Consent mechanism (the most complete among comparable products)** [Fact]:
  - The consent message can be copied and pasted into the chat;
  - The consent statement can be **announced by voice** through the speaker, and can also be set to play automatically;
  - Workspace Owners can **enforce** consent;
  - The Google Meet plugin pins a chat message and shows a recording indicator.

  Source: same as above.
- **Audio retention** [Fact]: The temporary local copy on desktop is deleted after successful processing or within 24 hours; audio that failed to upload is kept on the server for up to 3 days.
- **Pricing** [Fact + third-party]: Requires a Business or Enterprise plan (official help page). [Third-party] Business is $20 per person per month billed annually, or $24 billed monthly. Source: https://www.layer3labs.io/guides/notion-ai-meeting-notes
- **[Inference]** Notion is the big-vendor product closest to BriefPilot on the path of "minutes → structured task database"; its citation backlinks and consent mechanism **already cover part of the "with citations" selling point in the BriefPilot PRD**.
- **Public complaints** [Secondhand]: Some reviews say accuracy and translation are unstable for non-English meetings. Source: https://www.eesel.ai/blog/notion-ai-meeting-notes (to be verified)
### 3.12 Krisp

- **Positioning** [Fact]: Describes itself as "a complete Voice AI layer for your meetings," combining noise cancellation, accent conversion, and AI notes. Source: https://krisp.ai/ai-meeting-assistant/
- **Pricing (official)** [Fact]:

  | Plan | Price (per user per month) | Main contents |
  |---|---|---|
  | Free trial | 7 days | |
  | Core | $16 monthly / $8 annual | |
  | Advanced | $30 monthly / $15 annual | |
  | Enterprise | Custom | **"Private Transcription & Recordings (On-device)"**, selectable data center location |

  The page also contradicts itself: the FAQ says it is HIPAA certified, but the comparison table lists HIPAA only under the Enterprise tier. Source: https://krisp.ai/pricing/
- **On-premises / local deployment** [Fact]: The official site says it "supports on-device English transcription," with **the other 15 languages processed on servers**; it also says "No voice data visible to Krisp servers" (vendor's own claim). **This is the only mainstream vendor found in this round that offers on-device transcription (English)**. (Re-checked at the time of writing: the original sentence is on https://krisp.ai/ai-meeting-assistant/, not the pricing page; the pricing page lists On-device only under Enterprise. Neither page lists **Chinese** among its languages; the feature section also says "17 languages," which is inconsistent with the FAQ's "English + 15." accessed at the time of writing.)
- **Action item extraction** [Fact]: Extracts action items and "automatically assigns next steps."
- **Task integrations** [Fact]: Asana, Jira, monday.com, Salesforce, HubSpot, Pipedrive, Slack, Zapier.
- **Public complaints**: **Not collected in this round**.

### 3.13 Supernormal

- **Positioning change** [Fact]: On 2026-01-29, a co-founder posted on Indie Hackers announcing consolidation under the Supernormal brand and a shift toward "AI workspace + agents," using agents to generate documents, emails, presentations, and spreadsheets. The help center says it is "no longer just for meeting notes," and meeting notes have been moved to the left panel. Sources: https://www.indiehackers.com/post/were-consolidating-under-supernormal-and-building-an-ai-agent-da9d62dc4f ; https://help.supernormal.com/en/articles/7207888-what-s-new-with-supernormal
- **Pricing** [Fact]: The official pricing page  **shows $0 for every tier, which is likely a display error**; billing is credit-based, and the page says "No per seat pricing"; it claims GDPR, HIPAA, and SOC 2 compliance. [Third-party] The Team tier is $20 per month, **to be verified**. Sources: https://www.supernormal.com/pricing ; https://toolquestor.com/tool/supernormal
- **[Inference] Implication**: A "pure meeting notes" company that was once valued fairly highly chose to pivot, which suggests that **standalone pricing power in the pure-notes segment is declining**; these companies are moving toward "meetings as context → producing work output."
- **Public complaints**: **Not collected in this round**.

### 3.14 Avoma

- **Positioning** [Fact]: A meeting assistant for revenue teams. Billed per "recorder" seat, with **viewers free**. Source: https://www.avoma.com/pricing
- **Pricing (official)** [Fact]:
  - Startup: $19 annual / $29 monthly;
  - Organization: the page shows two conflicting prices ($24 and $29 annual, $39 monthly), **to be verified**;
  - Enterprise: $39 annual, minimum 10 seats;
  - Add-on modules: Conversation Intelligence at $29 per seat per month, Revenue Intelligence at $29 per seat per month (both annual prices).
- **Action item extraction** [Fact]: All tiers include action items, and notes are written automatically into CRM records.
- **[Inference]** Avoma's pricing structure is "basic notes are cheap, sales intelligence costs extra." This supports the view that **what commands a high price is never the notes themselves, but vertical-specific analysis**.
- **Public complaints and how it joins meetings**: **Not collected in this round; how it joins meetings is to be verified**.

### 3.15 Gong (vertical benchmark; detailed analysis in §5)

- **Positioning** [Fact]: Started out positioned as "pair programming for sales teams," and in 2019 named the "revenue intelligence" category itself, targeting CROs. Source: https://sacra.com/c/gong
- **Pricing** [Third-party: Sacra estimate]: About $1,360 to $1,600 per user per year, plus a $5,000 annual platform fee.
- **Scale** [Fact]: As of 2025-03, ARR exceeded $300 million, with about 4,500 enterprise customers. Source: https://techcrunch.com/2025/03/05/revenue-prediction-startup-gong-surpasses-300m-arr-indicating-potential-ipo-path
- **Public complaints**: **Not collected in this round**.
### 3.16 Supplementary subject: anarlog (formerly Hyprnote)

- [Fact] An open-source AI meeting notepad. The community edition is MIT-licensed, with about 9.7k GitHub stars. It captures device audio and does not send a bot; sessions are stored in local SQLite. **Transcription can run locally on a Mac, and summarization can connect to local models such as Ollama or LM Studio**; cloud features are optional. The team has now moved on to Char. Source: https://github.com/fastrepl/hyprnote
- **[Inference]** The "fully local" need is already being met by the open-source community, but these projects are positioned as **personal** tools, with no team collaboration or task closure.

### 3.17 Supplementary subject: Littlebird (graduate-student scenario, highly relevant to this project)

- [Fact] The official graduate-student page states:
  - Bot-free recording of **advisor meetings**, producing summaries with action items;
  - **Tracks your commitments to your advisor**, e.g. "revised outline due on…";
  - Every Monday it lists your commitments to your advisor, deadlines found in email, and upcoming meetings;
  - Pre-meeting briefs gather "commitments, open feedback, what you've read";
  - Remembers papers you have viewed on your screen;
  - Students subscribing to Plus with a .edu email pay $15 per month, with the first two months free;
  - Has passed a SOC 2 Type II audit;
  - The page reminds users to follow school policies and to inform others.

  Source: https://littlebird.ai/for/graduate-students
- **[Fact, added at the time of writing]** Pricing page: the Team plan is from $17 per seat per month (billed annually), and includes "Admin controls and team usage analytics" and "Shared projects and routine templates"; student Plus is $15/month (billed monthly), first two months free, covering up to four years; Plus includes "Littlebird MCP". Source: https://littlebird.ai/pricing (accessed at the time of writing)
- **[Fact, added at the time of writing]** Promise-tracker routine: compares commitments against actual outcomes ("the email that went out, the document that shipped, the message that never did"). The sample report is divided into Kept / In progress / Needs a note; "Vague maybes are left alone unless you ask for them"; by default it is "tuned to yours", and tracking what others owe you must be specified in the prompt. Source: https://littlebird.ai/routines/promise-tracker (accessed at the time of writing)
- **[Inference] Impact on BriefPilot**: "Research commitment tracking" is **already being done by someone else, and it is bot-free with student pricing**. However, Littlebird's commitment tracking has a **personal perspective** (what I owe my advisor) ~~, and it is a personal tool~~ (corrected at the time of writing: it has a Team billing tier and shared projects; the page simply does not describe a team-shared commitment ledger). It does not address (as far as the opened pages show):
  - A lab- or team-level shared **commitment ledger** (whether Team-plan shared projects cover commitments remains to be verified by trial);
  - The PI's view of "who owes what";
  - Cross-institution collaboration;
  - Mixed Chinese-English speech;
  - Local handling of unpublished data.

  These differences need to be validated in user research (see §8).

### 3.18 Supplementary subject (added in Round 2): Fellow

> Review 06, §3 pointed out that Fellow is the most direct competitor to options B and C, but the original text did not analyze it. This section covers only the two official pages opened in this round, and **has not been tested hands-on**.

- **Carrying items across meetings** [Fact]: "It also tracks whether items are still open and resurfaces them before the next relevant meeting"; "Pre-meeting briefs remind every attendee of the follow up items from previous conversations".
- **Assignment** [Fact]: "assign action items to specific attendees either during or after the meeting"; items can be reassigned and edited; "supports multiple assignees on a single action item". **The page does not mention the assignee confirming or accepting.**
- **Status** [Fact]: The page only shows "mark them complete" and "still open".
- **Accuracy** [Fact]: It only says "human-level accuracy", with no figures or method.
- **GitHub integration** [Fact]: Two-way sync. Fellow → GitHub: "every new action item assigned in a meeting instantly opens an issue in a specified GitHub repository"; GitHub → Fellow: "a newly created or updated issue appears as an action item in the related Fellow note"; "any addition or status change moves across systems in real time". **This sync is implemented via Zapier** (the page says Zapier continuously monitors both services).
- Sources: https://fellow.ai/features/action-items ; https://fellow.ai/integrations/github (both accessed at the time of writing)
- **[Inference] Impact on BriefPilot**: "Carrying items across meetings + multiple owners + engineering-tool sync" are all already done by someone else; what remains is "the assignee claiming the item themselves" (not seen on the pages) and "research-outcome semantics" (not seen on the pages). Pricing, the 1:1 template, and MCP capabilities were not verified in this round.
### 3.19 Additional Subject (added in Round 2): Microsoft Teams Facilitator

- **Capabilities** [Fact]: Generally available features include collaborative live notes, Q&A over meeting content, a timeline, Word document generation, and "Mobile capture of ad-hoc discussions and action items". "Task tracking integration with Planner" is in public preview. A Microsoft Copilot license is required.
- **Limitations** [Fact]: "Facilitator isn't supported in 1:1 chats, group chats, or external chats and meetings". When turned on, the user must choose the meeting language: "The language selected must match the spoken language during the meeting, or notes aren't generated". "AI-generated notes for meetings only support meetings where a single language is spoken. If multiple languages are spoken during the meeting, notes are only taken for the portions of the meeting that are spoken in the selected meeting language."
- Source: https://learn.microsoft.com/en-us/microsoftteams/facilitator-teams (page ms.date 2026-08-13, accessed at the time of writing)
- **[Inference] Implication for BriefPilot**: The claim "Teams only suggests, it doesn't track" is outdated. However, the official documentation confirms two limitations, "single language only" and "no support for external meetings", which work in favor of mixed Chinese-English meetings (Option D) and cross-institution use (G18).

---

## 4. Special Analysis A: How Granola Broke Out of a Red Ocean

### 4.1 Factual Timeline

| Date | Event | Source |
|---|---|---|
| 2024-05 | Launched its AI notepad, with the pitch of "no meeting bots" | https://techcrunch.com/2024/05/22/granola-debuts-an-ai-notepad-for-meetings |
| 2024-10 | $20M Series A (Spark). Weekly active users were 6x the level at launch; "Half of the people who try Granola still use it 10 weeks later, doing an average of 6 meetings a week" | https://granola.ai/blog/series-a |
| 2025-05 | $43M Series B at a $250M valuation (NFDG), $67M raised in total; launched shared folders and cross-meeting Q&A; usage had grown roughly 10% per week since launch, driven mainly by word of mouth among VCs and founders | https://techcrunch.com/2025/05/14/ai-note-taking-app-granola-raises-43m-at-250m-valuation-launches-collaborative-features |
| 2026-03-25 | $125M Series C at a $1.5B valuation (led by Index, with Kleiner participating), roughly $188M raised in total; launched a public API and an enterprise API; the CEO said enterprises use it "not only to capture their notes, but also to capture their context" | https://tech.eu/2026/03/25/granola-raises-125m-at-1-5bn-valuation/ |
| 2026-04 | Reported that links are "visible by default and used for training by default" (secondhand, to be verified) | §3.5 |

### 4.2 Why It Broke Out (Point by Point)

1. **It solves a "social cost" problem, not a "missing feature" problem.** [Fact] Between 2025 and 2026, university IT departments (UW-Madison, Carleton, Waterloo) and UK public-sector bodies (Cumbria, Derbyshire) published a wave of guidance on how to remove notetaker bots from meetings. UW-Madison wrote: "Most hosts are unaware if an attendee integrated an AI assistant bot with their account". It also admitted that domain-blocking settings are "not consistently blocking recently configured third-party AI assistant bots". Source: https://kb.wisc.edu/helpdesk/149383
   **[Inference]** For VCs and founders, bringing a bot to a meeting with a portfolio company or a customer is seen as unprofessional or even offensive. Granola brought that cost down to zero. What users get is not "one more feature" but "one less awkward moment".
2. **It puts the human back in the loop, and the notes a person writes are the best prompt.** [Fact] The CEO said: "Writing is thinking, and your tools should support your thinking, not replace it." And: "if you think your judgment is valuable, you should not outsource that judgment to AI". Source: https://granola.ai/blog/series-a
   **[Inference]** The few words a user jots down during a meeting tell the model "this matters here", so the summary is more relevant than a summary of the full transcript. This shares its roots with BriefPilot's "human confirmation" philosophy. The difference is that Granola places the human's involvement **during the meeting**, at very low cost, rather than in an after-the-fact approval step.
3. **It picked the right seed users: high meeting density, high willingness to pay, strong word of mouth.** [Fact] More than half of its users hold leadership roles, VC partners use it to take notes on pitches, and growth comes mainly from word of mouth among VCs and founders. Notes that are shared can be opened, and queried with AI, even by non-users, which is itself a viral mechanism. Sources: same as above, plus TechCrunch 2025-05.
   **[Inference]** A VC sits through 6 to 10 meetings a day. If a product feels good to them, it gets recommended to every company in their portfolio.
4. **Narrow and deep product principles.** [Fact, secondhand Korean paraphrase] The CEO has described four principles:
   - Don't solve problems that will soon disappear, such as context length in long meetings;
   - In the early stage, give a small number of users the most expensive model;
   - "Context is king";
   - Go narrow and deep, with differentiation coming from UX details such as notification flow, automatic meeting detection, and echo cancellation.

   Source: https://news.hada.io/topic?id=20660 (original at https://www.commits.world/p/how-to-build-a-truly-useful-ai-product, not opened directly)
5. **Timing.** [Inference] By 2024, LLM summarization quality was good enough that the experience of "filling in the notes afterward" could reliably reach a usable level. Using the same paradigm two years earlier would most likely not have worked.
### 4.3 Granola's Costs and Risks (Also Facts)

- **It does not retain audio**, so when there is a dispute there is no original audio to replay (§3.5).
- **"No bot" ≠ "not in the cloud"**: transcription uses Deepgram and Assembly, summarization uses OpenAI and Anthropic, and data is stored on AWS in the US (§3.5).
- **Consent becomes "invisible"**: without a bot, other participants do not know you are transcribing. Granola can only compensate with "automatically sent consent messages" and an Enterprise pilot feature (§3.5). **[Inference]** From a legal standpoint, this simply shifts responsibility for consent more completely onto the user.
- **Controversy over privacy defaults** (secondhand, to be verified).

### 4.4 Implications for BriefPilot

- **[Inference] Implication 1**: Differentiation can lie in the **interaction paradigm**, for example who leads, how the tool joins the meeting, and at which step a person intervenes, and not only in a single feature. BriefPilot's current "post-meeting human confirmation" happens after the meeting as a separate step, which puts more burden on the user than Granola's in-meeting note-taking. **[Assumption]** If this were changed to "tap one button during or after the meeting to mark 'this is my commitment / this is tentative', and then let the AI fill in the fields", the cost of confirmation might fall and adoption might rise. This needs prototype testing.
- **[Inference] Implication 2**: The seed population should be a group with **high meeting density and members who spread the word to each other**. Lab members have weekly group meetings, 1:1s, and cross-group collaborations, and people under the same advisor, in the same department, or in the same field recommend tools to each other. **[Assumption]** Labs may have a word-of-mouth structure similar to the "VC circle", but with a much weaker willingness to pay (see §5.3).
- **[Inference] Implication 3**: The gaps Granola leaves are precisely: **local processing, traceable evidence (audio or quotes), and visible consent**. These three matter especially for "research meetings that contain unpublished data" (see file 03, §6 for details).

---

## 5. Special Analysis B: Why Going Vertical Worked for Gong

### 5.1 Facts

- **Origins**: Founded in 2015 (per Sacra; TechCrunch says 2016, so **the two sources disagree**). It was originally positioned as "pair programming for sales teams", giving salespeople call replay for peer coaching. In 2019 it named itself "revenue intelligence" and targeted the CRO as the buyer. Source: https://sacra.com/c/gong
- **Scale**:
  - In 2025-03, ARR exceeded $300M with about 4,500 enterprise customers (Canva, Google, LinkedIn, Square, and others), and the CEO described the company as "close to profitable". Source: https://techcrunch.com/2025/03/05/revenue-prediction-startup-gong-surpasses-300m-arr-indicating-potential-ipo-path
  - Sacra estimates ARR of about $500M in 2026-05. Source: https://sacra.com/c/gong
- **Valuation**: $7.25B in 2021 (Series E); about $4.5B in a secondary-market transaction in 2025-11. Sources as above, plus https://www.builtinsf.com/articles/gong-raises-250m-series-e-sales-software-unicorn-hiring
- **Moat and threats**:
  - Moat: Gong positions itself as the repository for all of a company's customer calls, and layers deal boards, coaching, call scoring, and forecasting on top;
  - Threat 1: "Gongification", as HubSpot, Apollo, Outreach, Clari, and others have built in call recording and analytics;
  - Threat 2: APIs such as Recall.ai, Deepgram, and AssemblyAI have turned recording and transcription into infrastructure;
  - Threat 3: Zoom launched Zoom for Sales & Revenue to compete head-on.
  - Sales teams broadly laid off staff in 2022 to 2023, and growth at per-seat-priced Gong slowed as a result.

  Source: https://sacra.com/c/gong

### 5.2 Why Going Vertical Worked (reasoned step by step, all [Inference])

1. **There is a clear outcome signal.** A sales conversation ultimately leads to "deal won or lost" and a deal amount. Gong can link "what was said" to "what happened", and learn "high-win-rate talk tracks" from it. Meeting notes thus turn from "records" into "prediction and coaching". **This is a data loop that general-purpose note-taking tools do not have.**
2. **There is a buyer who holds the budget.** The CRO is accountable for revenue and is willing to pay about $1,400 or more per person per year, plus a platform fee, to "raise win rate by a few points". General-purpose note-taking tools can only charge $10 to $20 per person per month.
3. **There is a system of record to write into.** The CRM is the sales team's system of record, and Gong's outputs (next steps, risks, field updates) can be written straight into it, creating workflow lock-in.
4. **The domain workflow goes far beyond the notes themselves.** Coaching, scorecards, forecasting, and deal risk are each a module that can be charged for separately. Avoma, which sells conversation intelligence and revenue intelligence as add-on modules at $29 per seat per month, follows the same logic (§3.14).
5. **The cautionary lesson**: once recording itself is commoditized, the only value left is the "domain analysis" layer; and the per-seat model takes a hit when customers lay off staff.

### 5.3 Implications for BriefPilot

- **[Inference]** For verticalization to succeed, it needs **three elements: an outcome signal + a budget holder + a domain workflow**. Below, this framework is applied to "research labs", scoring each element honestly:

| Element | Sales (Gong) | Research labs (BriefPilot candidate) | Assessment |
|---|---|---|---|
| Outcome signal | Deal won, deal amount; clear and short-cycle | Whether experiments finish, progress on papers and submissions, whether deadlines are met; long cycle, weak signal, hard to quantify | [Inference] Weaker than sales, but "whether commitments are fulfilled on time" can serve as a **short-cycle proxy signal** |
| Budget holder | CRO, ample budget | PI or project grant; limited budget, slow procurement; individual students have low willingness to pay (Littlebird charges students $15 per month) | [Inference] Clearly weak. Commercially this may only suit a "entry point or portfolio piece", and not necessarily a market that can be funded on its own |
| Domain workflow | CRM, coaching, forecasting | Group meeting → experiment tasks → literature and code (GitHub) → submission; tracking reviewer comments; cross-institution collaboration | [Inference] Exists, and general-purpose tools do not cover it (file 03, §6) |
| Compliance specifics | Call-recording regulations | Unpublished data, ethics review (IRB), university data policies, cross-border | [Inference] A source of differentiation (local or private deployment) |

- **[Assumption, to be validated]** The value of "labs" as BriefPilot's **first segment** lies mainly in **being able to dogfood, having real needs, and supporting a portfolio narrative**, and not in market size. If a commercial story is needed, it can be abstracted as **"small knowledge-work teams with high sensitivity, long cycles, and cross-organization work"**, which would put consulting, law firms, medical research, and hardware R&D teams in the same category. This point needs to be weighed in a later positioning document.

---
## 6. Feature Matrix

> Legend: ✓ present (with source); ◐ partial or limited; ✗ not seen or explicitly absent; ? not verified. "Not seen" means it did not appear on the official pages fetched in this round; it does not mean the feature is definitely absent.

| Product | How it joins meetings | Action item extraction | Draft first, human confirms before execution | Asana/Jira/Linear | Cross-meeting Q&A | Citations linking back to source | Local/offline | Consent tooling | Entry paid price (annual billing, per user per month) |
|---|---|---|---|---|---|---|---|---|---|
| Otter | bot + bot-free desktop app | ✓ auto-assigned | ? | ✓ Jira/Asana | ✓ | ? | ✗ | ◐ (default sharing is controversial) | $8.33 (Pro) |
| Fireflies | bot + desktop app | ✓ auto-creates tasks | ✗ (auto-created) | ◐ generic wording | ✓ AskFred | ? | ✗ (dedicated cloud) | ◐ recording is visible | about $10 (third-party) |
| Fathom | bot + bot-free (Mac beta) | ✓ | ? | ✓ Asana | ✓ | ? | ✗ | ? | $16 (Premium) |
| tl;dv | bot / claims no bot needed | ✓ | **✓ drafts for review** | ? | ✓ cross-meeting reports | ? | ◐ private AI hosting (on request) | ? | €18 (Pro) |
| Granola | **no bot** | ◐ enhanced notes | ? | ~~✗ (Notion/Zapier)~~ ◐ connects to Asana/Jira/Linear/**GitHub** via Zapier; has MCP (corrected at the time of writing, https://www.granola.ai/integrations ) | ✓ (Business) | ? | ✗ (cloud) | ✓ automatic consent message | $14 (Business, monthly billing only) |
| Read.ai | bot + desktop/mobile apps | ✓ routed to tools | ? | ✓ includes Linear | ✓ includes email/Slack | ✓ citations | ✗ | ◐ visible on joining | $15 (Pro) |
| Circleback | bot + bot-free | ✓ assigned | ? | ✓ Linear/Asana | ✓ | ? | ✗ | ? | $15 (Pro) |
| Zoom AI Companion/ZoomMate | native | ✓ templates | ? | ✓ Jira | ✓ | ? | ✗ | ? | included in paid plans; ZoomMate about $20 (third-party) |
| Teams Copilot | native | ✓ suggestions | ◐ "suggests" only (Copilot recap; see the Facilitator row below) | ? | ✓ | ✓ citations | ✗; **not available in meetings hosted by external organizations** | ◐ organizer toggle | about $21 to $30 (third-party) |
| Gemini in Meet | native + in-person | ✓ | ✗ | ✗ (only generates a Doc) | ? | ? | ✗ | ✓ notifies all participants | included in Business Standard and above |
| Notion AI Notes | no bot (device audio) | ✓ | ◐ skills create tasks | ◐ Notion databases | ✓ | **✓ links back to transcript** | ✗ (explicitly no offline support) | **✓ spoken announcement, can be enforced** | about $20 (Business, third-party) |
| Krisp | no bot (default) | ✓ auto-assigned | ? | ✓ Asana/Jira/monday | ✓ AI chat | ? | **◐ on-device transcription for English**; on-device for Enterprise | ? | $8 (Core) |
| Supernormal | bot-free desktop app | ? | ? | ? | ? | ? | ✗ | ? | to be verified (credit-based billing) |
| Avoma | ? | ✓ | ? | ◐ CRM | ? | ? | ✗ | ? | $19 (Startup) |
| Gong | bot | ✓ (sales next steps) | ? | ◐ CRM | ✓ | ? | ✗ | ? | about $113 to $133, plus a platform fee (third-party) |
| Littlebird | no bot | ✓ includes **commitment tracking** (Kept / In progress / Needs a note; skips vague commitments; individual perspective) | ? | ? | ✓ | ? | ✗ (cloud, SOC 2) | ◐ reminds users to notify participants | Student $15 (monthly); ~~individual only~~ **Team from $17/seat (annual billing), includes shared projects and admin controls** (corrected at the time of writing, https://littlebird.ai/pricing ) |
| **Fellow** (added at the time of writing) | ? | ✓ assign, reassign, multiple owners; carries unfinished items into the next meeting's prep | ? (no assignee confirmation seen on the page) | ✓ **two-way GitHub sync** (via Zapier) | ? | ? | ? | ? | not verified |
| **Teams Facilitator** (added at the time of writing) | native (meeting agent) | ✓ includes in-person capture on mobile | ? | ◐ Planner task tracking (public preview) | ✓ Q&A on meeting content | ? | ✗; **does not support external meetings or 1:1s**; **AI notes support only a single language** | ? | requires a Copilot license |
| anarlog (open source) | no bot | ? | ? | ? | ? | ? | **✓ fully local, optional** | ? | free (MIT community edition) |

**How to read the matrix [Inference]**:

- The "Action item extraction" column is almost entirely ✓, which shows it is table stakes.
- The "Local/offline" column is almost entirely ✗; only Krisp offers partial support and the open-source anarlog offers full support. It is the emptiest column.
- For "Draft first, human confirms", only tl;dv clearly does it; Teams only reaches the "suggestion" level.
- "Citations linking back to source" is clearly supported by three products (Notion, Teams, Read), so **BriefPilot is not unique here**.
- (Added at the time of writing) The "Asana/Jira/Linear" column is now mostly ✓ or ◐, and GitHub has also appeared (Fellow, Granola), so **integrations are no longer an empty column**.
- **Among the pages fetched in this round, no product combines "local or private processing + citations + human confirmation + a team task pool + mixed Chinese-English speech"**. This combination is a testable differentiation hypothesis, but the "combination" itself is easy for large vendors to fill in, so it holds up only when paired with a narrower target scenario.

---
## 7. Common Weaknesses of International Products

| # | Weakness | Evidence | Type |
|---|---|---|---|
| 1 | **None publishes the quality of its action item extraction**, including precision, recall, and the accuracy of owners and due dates | Among the 15 official sites and pricing pages crawled in this round, none publishes action item accuracy; user reviews repeatedly mention "inaccurate key points" and "misrecognized names" (Fathom, secondhand) | [Fact: not found] + [Inference] |
| 2 | **"Automation first," with no confirmation step** | Fireflies says "Create tasks automatically," Krisp says "automatically assigns," ZoomMate updates Salesforce automatically, and Read claims it can summarize "even when no one attends" | [Fact] |
| 3 | **The consent burden is shifted onto users, and bots get banned by institutions** | The Otter lawsuit and its response; the Fireflies BIPA lawsuit; bans or guidance at UW-Madison, Carleton, Waterloo, Cumbria, and Derbyshire | [Fact] |
| 4 | **"No bot" ≠ "local"; local or offline deployment is nearly nonexistent** | Granola runs in the cloud; Notion does not support offline use; Fireflies' "private storage" is a dedicated cloud; only Krisp offers on-device English transcription, along with the open-source anarlog | [Fact] |
| 5 | **Weak support for cross-organization meetings** | Teams Copilot is unavailable in meetings hosted by an external organization; Gemini only works for meetings it hosts itself | [Fact] |
| 6 | ~~**The integration ecosystem centers on sales CRM**~~ **Paid-tier integrations are mostly CRM, but engineering tool integrations already exist** (corrected at the time of writing) | Almost every product puts Salesforce/HubSpot on a paid tier (Otter, Fathom, Granola, Read, Circleback, Krisp); ~~in the pages crawled this round, **GitHub Issues does not appear** (Read and Circleback support Linear)~~ (corrected at the time of writing: Fellow syncs bidirectionally with GitHub; Granola connects to GitHub, Linear, and Jira via Zapier; Circleback, Read, and Otter have MCP or Claude integrations, https://fellow.ai/integrations/github , https://www.granola.ai/integrations , https://circleback.ai/integrations , https://www.read.ai/integrations , https://otter.ai/integrations , accessed at the time of writing) | ~~[Fact: within the scope observed]~~ [Fact] The weakness does not hold; W&B, Overleaf, and Zotero not seen |
| 7 | **Multilingual support is "English first"** | Notion's speaker labeling supports only English; Krisp's on-device transcription supports only English (and the supported languages do not include Chinese); Gemini says only "select languages" (added at the time of writing: the help page lists 8 languages, none of them Chinese, and mixed languages within one meeting are not supported); **Teams Facilitator AI notes support only a single language** (added at the time of writing); no vendor has published an evaluation of mixed Chinese-English speech (file 03 already cites vendor blogs from Gladia and Avoma) | [Fact] + [Inference] |
| 8 | **Notes and tasks are disconnected, and overdue tracking is missing** | Gemini produces only a Doc; most products stop at "push to an external task tool." Only the pre-meeting briefs of Otter and Granola, and the commitment list of Littlebird, **carry the last meeting's commitments into the next one** (added at the time of writing: **Fellow**'s pre-meeting brief also brings back unfinished items; **Teams Facilitator** has a Planner task tracking preview. The "only" claim was too narrow) | [Fact] + [Inference] |
| 9 | **The free tier is choked by history limits, and pricing is per seat** | Granola's and Circleback's free tiers keep only 30 days of history; Read's free tier allows 5 sessions per month; Otter's free tier limits each session to 30 minutes | [Fact] |

---

## 8. Clearly Overlooked User Segments

> All of the following are **[Inference]**, some with supporting facts, and need to be validated through user research.

1. **Cross-institution research labs or project groups**
   - Why they are overlooked:
     - Their meetings are in person, at a whiteboard, plus cross-institution Zoom, so the cross-organization limits of built-in platform tools (Teams) are a poor fit;
     - Their content includes unpublished data, and cloud processing with training turned on by default is unsettling (the Granola controversy, the Otter lawsuit);
     - Individual students have low willingness to pay, and PI procurement is slow;
     - Their integration needs are GitHub, Overleaf, and reference tools, not CRM.
   - Current state: Littlebird ~~covers only the **individual graduate student** layer~~ has commitment tracking from an individual's perspective, but a Team plan already exists (corrected at the time of writing, https://littlebird.ai/pricing ); the layer of "shared lab commitment pool + PI view + cross-institution" has **no dedicated product found in this round** (Fabric, mentioned in file 03, needs further verification).
2. **Small teams in regulated or air-gapped environments** (medical research, legal, defense, hardware R&D)
   - The only options are Krisp Enterprise's on-device transcription and open-source solutions; the big vendors tie HIPAA to the Enterprise tier, usually with a threshold of 50 to 100 people (Otter requires 100 people to enable SSO, Granola requires 50).
3. **Small Chinese-English mixed-speech teams in Asia** (for example, Singapore)
   - Speaker labeling, local transcription, and summary quality are all "English first"; no vendor has published an evaluation of mixed Chinese-English speech.
4. **Small non-sales engineering or product teams**
   - Integrations and paid tiers are designed around CRM; ~~GitHub Issues does not appear;~~ (corrected at the time of writing: Fellow and Granola already connect to GitHub) products still lack structured support for **semantic matching** from "technical discussion → issue" (which existing issue a decision maps to) [Inference].
5. **Public-sector and university staff working in environments where bots are banned**
   - Derbyshire allows only Copilot; university IT departments are actively purging bots. These people can only use built-in platform tools or take notes by hand.

---
## 9. Direct Recommendations for BriefPilot (for the Positioning and PRD Stages)

> All items are [Inference] or [Assumption] and need validation through user research and prototyping.

1. **Stop pitching "meeting-to-task," "citations," and "human confirmation" as standalone selling points.** Competitors already do each of them (tl;dv, Notion, Teams, Read). The pitch should be: **in [a specific segment], because of [constraint X], these capabilities in existing products break down, and here is how we make them usable again.**
2. **Candidate differentiation bundle (assumption)**:
   - "**Local or private processing** + **commitment cards with citations** + **low-cost in-meeting annotation** + **cross-meeting commitment tracking and overdue reminders** + **mixed Chinese-English speech**";
   - Validate first in "cross-institution research labs," then generalize to "small knowledge-work teams that are high-sensitivity, long-cycle, and cross-organizational."
3. **Turn "evaluability" into a weapon**: publish BriefPilot's own action-item precision, recall, and owner-attribution accuracy on synthetic data. This directly addresses weakness 1, no competitor has published metrics of this kind, and it makes the most convincing story in interviews.
4. **Make the consent mechanism more "visible" than Granola's and Notion's**, for example a one-click consent notice generated before the meeting, and a label on the minutes saying "these minutes were produced with everyone's informed consent." This is both a compliance requirement and a trust-level differentiator.
5. **Face Littlebird head-on**: state explicitly in the positioning document "how we differ from Littlebird," namely ~~team vs. individual~~ **a team-shared commitment ledger and personal commitment lists** (corrected at the time of writing: Littlebird already has a Team plan, so the distinction can no longer be "team vs. individual"), the PI perspective, local processing, and mixed Chinese-English speech. Do not pretend nobody works in this space. Likewise, write down "how we differ from Fellow" (added at the time of writing).

---

## 10. Uncovered Items and Next Steps

- **Not collected**: Verbatim user complaints for Zoom, Teams Copilot, Gemini, Avoma, Supernormal, Krisp, Circleback, and tl;dv (search quota exhausted). The original posts on Reddit r/productivity and r/PhD were also not retrieved.
- **To be verified**:
  - The original The Verge article on Granola;
  - The latest developments in the Otter and Fireflies lawsuits;
  - Official pricing for Fireflies, Notion, Microsoft, and ZoomMate;
  - How Avoma joins meetings;
  - Granola's action-item mechanism;
  - The year Gong was founded (2015 or 2016);
  - tl;dv's "Privacy Shield" badge.
- **(Added at the time of writing) Still to be verified**: Fellow's pricing, 1:1 templates, and MCP; whether Littlebird Team's shared projects share commitments; details of Planner tracking in Teams Facilitator; the source of the Zoom "track cross-meeting projects" original phrasing.
- **Suggested next step**: in the "user complaint mining" document, collect the verbatim quotes from Reddit, G2, and Capterra in one pass, opening the pages manually in a browser if necessary.

---

## Source List

**Official product, pricing, and help pages (accessed at the time of writing)**
1. Otter pricing — https://otter.ai/pricing
2. Otter website — https://otter.ai/
3. Fireflies pricing — https://fireflies.ai/pricing
4. Fireflies website — https://fireflies.ai/
5. Fathom pricing — https://www.fathom.ai/pricing
6. tl;dv pricing — https://tldv.io/pricing/
7. tl;dv website — https://tldv.io/
8. Granola pricing — https://www.granola.ai/pricing
9. Granola security page — https://www.granola.ai/security
10. Granola sharing settings — https://www.granola.ai/docs/docs/FAQs/sharing-controls
11. Granola Series A blog (2024-10-23) — https://granola.ai/blog/series-a
12. Granola security post-mortem (API key) — https://docs.granola.ai/help-center/policies/security-reports/post-mortem-assembly-ai-api-key-exposure
13. Granola desktop app vulnerability — https://docs.granola.ai/help-center/policies/security-contributions/desktop-app-navigation-vulnerability
14. Read.ai pricing — https://www.read.ai/plans-pricing
15. Read.ai website — https://www.read.ai/
16. Circleback pricing — https://circleback.ai/pricing
17. Circleback website — https://circleback.ai/
18. Zoom AI assistant / ZoomMate — https://www.zoom.com/en/ai-assistant/
19. Zoom AI Companion 3.0 press release — https://investors.zoom.us/news-releases/news-release-details/zoom-launches-ai-companion-30-agentic-workflows-transforming
20. Microsoft: Use Copilot in Teams meetings — https://support.microsoft.com/en-us/office/use-copilot-in-microsoft-teams-meetings-0bf9dd3c-96f7-44e2-8bb8-790bedf066b1
21. Google blog: Take notes for me (2026-06-29) — https://blog.google/products-and-platforms/products/workspace/take-notes-for-me/
22. Google Workspace Updates: in-person meeting notes (2026-08-13) — https://workspaceupdates.googleblog.com/2026/08/take-notes-with-me-for-in-person-meetings-is-now-available.html
23. Notion AI Meeting Notes help page — https://www.notion.com/help/ai-meeting-notes
24. Krisp pricing — https://krisp.ai/pricing/
25. Krisp AI meeting assistant — https://krisp.ai/ai-meeting-assistant/
26. Supernormal pricing — https://www.supernormal.com/pricing
27. Supernormal help center: What's new — https://help.supernormal.com/en/articles/7207888-what-s-new-with-supernormal
28. Supernormal pivot post (Indie Hackers, 2026-01-29) — https://www.indiehackers.com/post/were-consolidating-under-supernormal-and-building-an-ai-agent-da9d62dc4f
29. Avoma pricing — https://www.avoma.com/pricing
30. Littlebird graduate students page — https://littlebird.ai/for/graduate-students
31. anarlog (formerly Hyprnote) GitHub — https://github.com/fastrepl/hyprnote
32. Char — https://char.com/

**Added in Round 2 revision (accessed at the time of writing, opened directly via WebFetch)**
59. Fellow Action Items — https://fellow.ai/features/action-items
60. Fellow × GitHub — https://fellow.ai/integrations/github
61. Granola Integrations — https://www.granola.ai/integrations
62. Littlebird Pricing — https://littlebird.ai/pricing
63. Littlebird Promise Tracker — https://littlebird.ai/routines/promise-tracker
64. Microsoft Learn: Facilitator in Teams — https://learn.microsoft.com/en-us/microsoftteams/facilitator-teams
65. Google Meet "Take notes for me" help page — https://support.google.com/meet/answer/14754931
66. Zoom AI assistant product page (cited from 06 V10) — https://www.zoom.com/en/products/ai-assistant/ ; Circleback / Read / Otter Integrations (cited from 06 V2) — https://circleback.ai/integrations ; https://www.read.ai/integrations ; https://otter.ai/integrations

**Funding, revenue, and media**
33. TechCrunch: Granola launch (2024-05) — https://techcrunch.com/2024/05/22/granola-debuts-an-ai-notepad-for-meetings
34. TechCrunch: Granola Series B (2025-05) — https://techcrunch.com/2025/05/14/ai-note-taking-app-granola-raises-43m-at-250m-valuation-launches-collaborative-features
35. Tech.eu: Granola Series C (2026-03-25) — https://tech.eu/2026/03/25/granola-raises-125m-at-1-5bn-valuation/
36. GeekNews: Granola CEO's product principles (Korean-language paraphrase) — https://news.hada.io/topic?id=20660
37. Sacra: Gong — https://sacra.com/c/gong
38. TechCrunch: Gong ARR surpasses $300M (2025-03) — https://techcrunch.com/2025/03/05/revenue-prediction-startup-gong-surpasses-300m-arr-indicating-potential-ipo-path
39. Built In SF: Gong Series E — https://www.builtinsf.com/articles/gong-raises-250m-series-e-sales-software-unicorn-hiring
40. TechCrunch: Zoom opens its AI assistant to free users (2025-12) — https://techcrunch.com/2025/12/15/zoom-brings-its-ai-assistant-to-the-web-with-access-to-free-users/

**Privacy, litigation, and institutional policy**
41. NPR: Otter class-action lawsuit — https://www.npr.org/2025/08/15/g-s1-83087/otter-ai-transcription-class-action-lawsuit
42. Storyboard18: Otter lawsuit — https://www.storyboard18.com/digital/otter-ai-sued-for-allegedly-recording-private-conversations-without-consent-79130.htm
43. Data Privacy & Security Insider: Fireflies BIPA lawsuit — https://www.dataprivacyandsecurityinsider.com/2025/12/lawsuit-alleges-fireflies-ai-corp-illegally-collects-biometric-data-from-virtual-meetings/
44. Fireflies complaint PDF — https://www.workplaceprivacyreport.com/wp-content/uploads/sites/938/2026/04/Fireflies.ai-Complaint-1.pdf
45. Illinois Lawyer Now: rise in BIPA lawsuits — https://www.illinoislawyernow.com/2026/02/employers-beware-uptick-in-bipa-lawsuits-targeting-ai-note-taking-software/
46. UW-Madison: third-party AI assistant bots — https://kb.wisc.edu/helpdesk/149383
47. Carleton College: the uninvited Otter — https://www.carleton.edu/ai/blog/an-uninvited-guest-what-you-should-know-about-otter-ais-notetaker/
48. University of Waterloo: stopping Otter — https://uwaterloo.atlassian.net/wiki/spaces/HEALTHHELP/pages/44600164869/Stop+Otter.ai+from+joining+meetings+and+sharing+transcripts
49. Cumbria Fire and Rescue Service information security newsletter — https://www.cumbriafire.gov.uk/sites/default/files/2025-10/28799%20CFRS%20Information%20Security%20Month%2025%20Newsletter%205%20v3.pdf
50. Derbyshire County Council: meeting etiquette for AI notetakers — https://staff.derbyshire.gov.uk/site-elements/documents/information-security/meeting-etiquette-for-ai-notetakers.pdf
51. AIToolly: Granola privacy report (reprint of The Verge, secondary source) — https://aitoolly.com/zh/ai-news/article/2026-04-03-granola-privacy-alert-ai-notes-viewable-via-link-and-used-for-training-by-default
**User Reviews and Community**
52. Trustpilot: Otter — https://www.trustpilot.com/review/otter.ai
53. Trustpilot: Fireflies — https://www.trustpilot.com/review/fireflies.ai
54. Microsoft Tech Community: Fireflies bot keeps popping up — https://techcommunity.microsoft.com/discussions/microsoft-365/fireflies-ai-note-taker-robot-keeps-popping-up/1571150
55. Zoom Community: Blocking bots such as Fireflies — https://community.zoom.com/t5/Zoom-Meetings/How-to-block-bots-like-firefliesai-notetaker/m-p/210098
56. G2 / Capterra: Fathom (secondhand; original page returned 403) — https://www.g2.com/products/fathom-video ; https://www.capterra.com/p/276054/Fathom/reviews/?page=8

**Third-Party Pricing and Reviews (for cross-checking; all labeled "third-party")**
57. Sonix: Fireflies pricing — https://sonix.ai/resources/fireflies-ai-pricing/ ; Sonix: Fathom pricing — https://sonix.ai/resources/fathom-pricing/ ; Outdoo: Fireflies pricing — https://www.outdoo.ai/blog/fireflies-ai-pricing ; Laxis: Zoom AI Companion — https://www.laxis.com/blog/zoom-ai-companion/ ; STMicro: Copilot Business — https://www.stmicro.net/blog/microsoft-365-copilot-business-july-2026/ ; Copilot Experts: pricing guide — https://copilot-experts.com/microsoft-copilot-pricing-guide/ ; Layer3 Labs: Notion AI meeting notes — https://www.layer3labs.io/guides/notion-ai-meeting-notes ; eesel: Notion AI meeting notes — https://www.eesel.ai/blog/notion-ai-meeting-notes ; ToolQuestor: Supernormal — https://toolquestor.com/tool/supernormal
58. Competitor reviews of Granola (biased by their own positioning): tl;dv — https://tldv.io/ko/blog/granola-review/ ; Jamie — https://www.meetjamie.ai/en/blog/granola-review ; HappyScribe — https://www.happyscribe.com/nl/blog/granola-ai-review ; Superframeworks: local cache — https://superframeworks.com/articles/granola-encrypted-local-notes

---

## Confidence in This Document's Conclusions

- **High confidence** (fetched directly from official pages):
  - Pricing: Otter, Fathom, tl;dv, Granola, Read, Circleback, Krisp, Avoma;
  - Features and compliance notes: Teams Copilot's cross-organization limits, Notion's consent mechanism and language coverage, which Gemini editions are eligible, Granola's cloud pipeline and no-audio-retention policy, Littlebird's graduate-student features, anarlog's local capabilities;
  - Funding facts: Granola's Series A, B and C (cross-checked across TechCrunch, Tech.eu and the official blog); Gong's ARR as of 2025-03 (TechCrunch).
- **Medium confidence**:
  - The existence and allegations of the Otter and Fireflies lawsuits (reported consistently by multiple media outlets and law firms), but the latest developments are unknown;
  - Announcements by institutions banning bots (the original text can be checked, but it represents only individual institutions);
  - Sacra's ARR and pricing estimates for Gong (research-firm estimates).
- **Low confidence or needs verification**:
  - All Reddit, G2 and Capterra quotes labeled "secondhand" (the original pages could not be opened);
  - The Verge's report on Granola's default settings (only a repost was readable);
  - Pricing from third-party sites (Fireflies, Microsoft, ZoomMate, Notion, Supernormal);
  - The claim that Granola keeps a plaintext local cache;
  - Competitor blogs' criticisms of Granola (biased by their own positioning).
- **Main risks in the inference-type conclusions**:
  - "Local or offline deployment is almost nonexistent" is based only on the official pages fetched in this round, and may miss small and mid-sized vendors;
  - "Labs have weak budgets" lacks support from first-hand interviews;
  - "No competitor has the full differentiating combination" will become outdated as competitors iterate, and needs a quarterly review.
- **(Added at the time of writing) Two erroneous premises in the original text**: "GitHub Issues does not appear" and "Littlebird only does personal use" both arose because the integrations page and pricing page had not been fetched at the time. The lesson: a claim that "a feature is absent" must state **which pages were opened**; otherwise it can only be written as "not verified".

---
## Revision Log (Round 2)

> Based on `01_market-research/06_research_integrity_review.md` §0, §1 (V1–V3, V6, V9–V12), §3, §6 (C4, C8, C9), §9 P0-4. At the time of writing, the following were re-opened with WebFetch and rechecked: Fellow (2 pages), Granola Integrations, Littlebird (2 pages), Teams Facilitator, the Google Meet help page, and Krisp (2 pages). Statements that were overturned are kept with strikethrough.

| # | Location | Change | Basis |
|---|---|---|---|
| 1 | frontmatter | status marked as revised; sources_count 58 → 66 | 06 §7 |
| 2 | §0 item 5 ⑤ | "GitHub Issues does not appear" struck through, changed to "only W&B/Overleaf/Zotero remain unseen" | 06 V1, V2, C9 |
| 3 | §0 item 5 ⑥ | Added: Krisp has no Chinese, Gemini has no Chinese and does not support multiple languages in the same meeting, Facilitator is single-language | 06 V9, V11, V12 |
| 4 | §0 item 6 | "Littlebird is a personal assistant" struck through, changed to "has a Team billing tier; commitment tracking is still from an individual's perspective" | 06 V3, C4 |
| 5 | §0 new item 7 | Points out that Fellow and Teams Facilitator were missed | 06 §3 |
| 6 | §3.5 Granola task integrations | Added the integrations page: GitHub, Linear, Jira, and Asana are all via Zapier, plus a Granola MCP connector | 06 V1 |
| 7 | §3.8 Zoom | "track cross-meeting projects" changed from [Fact] to [Summary · to be verified]; added the official-site ZoomMate project agent; added a note to the one-line 3.0 positioning | 06 V10 |
| 8 | §3.9 Teams Copilot | Added Facilitator guidance | 06 V11 |
| 9 | §3.10 Gemini | Added the language list (no Chinese) and the lack of support for multiple languages in the same meeting | 06 V12; rechecked this round |
| 10 | §3.12 Krisp | Noted that on-device English transcription comes from the AI Meeting Assistant page; added no Chinese and the 17 vs 16 language-count inconsistency | 06 V9, C8; rechecked this round (the original statement **holds**, only its source is not the pricing page) |
| 11 | §3.17 Littlebird | Added the Team plan, student pricing details, the three states of commitment tracking, and "tuned to yours"; "personal tool" struck through | 06 V3–V5 |
| 12 | New §3.18 Fellow | Cross-meeting carry-over, assignment, multiple owners, two-way GitHub sync (via Zapier), no assignee confirmation seen | 06 §3, V1, V6 |
| 13 | New §3.19 Teams Facilitator | Planner tracking (preview), mobile capture; does not support external meetings or 1:1s; single-language | 06 §3, V11 |
| 14 | §6 feature matrix | Granola integrations cell changed to ◐ including GitHub; Littlebird pricing adds Team, action items adds the three states; added two rows for Fellow and Teams Facilitator; note added to Teams Copilot; one more point added to "How to read it" | 06 §9 P0-4 |
| 15 | §7 #6, #7, #8 | #6 struck through and re-judged; #7 adds Gemini and Facilitator; #8 adds Fellow and Facilitator | 06 V1, V11, V12 |
| 16 | §8 #1, #4 | Littlebird "covers individuals only" struck through; "GitHub Issues does not appear" struck through | 06 V1, V3 |
| 17 | §9 item 5 | The differentiation "team vs individual" changed to "team-shared commitment ledger vs personal commitment list", with a requirement to spell out the difference from Fellow | 06 V3 |
| 18 | §10, sources, credibility notes | Added items to be verified, sources 59–66 (all marked accessed at the time of writing), and an explanation of how the erroneous premises arose | — |

**Not changed, left for later**: Fellow's pricing and 1:1 template have not been verified, so the Fellow cells in several matrix columns remain "?"; the cells for the other 15 products were not rechecked one by one.
