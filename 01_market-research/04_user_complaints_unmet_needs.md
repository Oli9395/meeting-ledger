---
title: Market Research 04 — User Complaint Evidence Base and Top 10 Unmet Needs for Meeting AI / Meeting-to-Task Products
status: draft
sources_count: 45
sources_count_method: Number of unique URLs in the sources section (recalculated at wrap-up; original value 44)
evidence_note: First-round file. The body does not label each item individually as [Fact] or [Summary], and sources do not record per-item access dates (all are taken to be at the time of writing). Any item labeled [Fact] whose body has no "opened the original page" record should be treated as [Summary · to be verified] before it is cited (added in the wrap-up revision)
---

# Market Research 04: Mining User Complaints — What Do Meeting AI Products Actually Fail to Deliver?

> **Reading notes**
> - Labeling rules: **[Fact]** means sourced and verifiable; **[Inference]** means reasonably derived from several facts but with no direct evidence; **[Assumption]** means to be validated, requiring interviews or experiments.
> - **How quotes were obtained must be stated up front**: verbatim quotes are English sentences extracted from the original pages with a web-scraping tool and kept essentially as written, but the scraping tool applies a layer of summarization first. **Before any public use, open the link and check the wording word for word.** Where only a search snippet was obtained and the original page was not opened, the quote is marked "(search snippet, to be verified)".
> - **Hard limits on coverage (must be disclosed honestly)**:
>   1. **Reddit was inaccessible.** reddit.com blocks the crawler used for this research; both search and fetch were refused, so subreddits named in the task brief such as r/productivity, r/PhD and r/GradSchool have **no first-hand quotes**. Reddit-related content is secondhand only (a third-party blog saying "Reddit users complain that…") and is labeled separately.
>   2. **The original G2 and Capterra pages returned 403**; only a few statistics and fragments from search snippets were obtained.
>   3. **Coverage of original posts in Chinese-language communities is thin.** No genuine complaint posts were found on Zhihu, Xiaohongshu, V2EX or Bilibili comments; the search results were almost entirely Feishu official-site promotional pieces and aggregated reviews. This round of research also hit the **search quota limit** midway (shared by all parallel agents), so the supplementary Chinese-language searches were not completed.
>   4. As a result, the first-hand evidence in this document comes mainly from **Hacker News threads, low-star Trustpilot reviews, the Zoom community, independent blogs, and lawsuit coverage**. This population skews English-speaking, technical and workplace-oriented, and **cannot directly represent Chinese users or research users**.

---

## 0. Conclusions first (then the reasoning)

1. **[Fact] The most concentrated and most intense complaints are not "can't extract action items" but "can't trust it" and "no consent"**:
   - **Can't trust it**: summaries miss key content, misattribute statements (putting words in the mouth of someone who never said them), and fabricate things that never happened. Doctors, educators and engineers all gave concrete examples on HN.
   - **No consent**: bots join meetings automatically, share the notes with all attendees by default, and still join after the user has unsubscribed. Otter (August 2025) and Granola (July 30, 2026) have each been hit with a class-action lawsuit.
2. **[Fact] "Nobody reads the notes" and "nobody claims the tasks" are high-frequency topics in the 2026 blogosphere** (Laxis, Lilach Bullock, Programming Insider, Collab365). One consultant estimates that of the AI-generated action items from her team's last 10 meetings, **at least one third were still untouched three weeks later**. This is a personal estimate, not statistical data.
3. **[Inference] Mainstream products have largely solved "generation" but not "closing the loop."** Existing products can already turn meetings into transcripts, summaries and action-item lists, but they fall short on three things:
   - letting people **verify generated content at low cost**;
   - letting the person concerned **confirm and claim** a task;
   - **reviewing at the next meeting** whether commitments were fulfilled.
   The "solutions" offered by multiple independent sources are all manual processes (a 60-second recap at the end of the meeting, moving items into the task system within 24 hours, going over the previous meeting's action items at the start of the next one), which suggests the product layer is still a gap or is poorly done.
4. **[Inference] The most valuable differentiation direction for BriefPilot is an "evidence-backed commitment ledger"**: every decision or commitment is attached to the original quote and a timestamp, the person concerned confirms or disowns it with one click, and it is reviewed automatically at the next meeting. This direction addresses three kinds of complaints at once: can't trust it, nobody claims tasks, nobody reads the notes. It also fits naturally with BriefPilot's existing "citation + human confirmation" design.
5. **[Assumption] Distinguishing speakers in offline or hybrid meetings, mixed Chinese-English speech, and research jargon are amplifiers specific to research lab scenarios.** But the public complaint evidence collected this round gives only moderate or weak support for these points, and first-hand Chinese-language evidence is especially lacking; they need to be validated through interviews in 02_user-research.
6. **[Fact] Counter-evidence exists too**: Fireflies has a rating of about 4.7–4.8 on G2 (search snippet, to be verified), and Otter shows 4.4 (826 reviews) on Trustpilot Canada. Many users find these products "good enough." Complaint channels are naturally skewed negative, and are further amplified by billing problems.

---

## 1. Research Method

| Channel | Plan | Actual | Notes |
|---|---|---|---|
| Reddit (6 subreddits) | Search + original posts | **Failed** (site blocks crawlers) | Only secondhand accounts obtained |
| Hacker News | Search Otter/Fireflies/Granola/meeting notes | **Succeeded**, opened 10 threads | Main source of first-hand quotes |
| G2 / Capterra 1–3 stars | Original pages | **403**, search snippets only | Statistics to be verified |
| Trustpilot | Supplementary low-star reviews | **Succeeded**, including Otter 1/2-star, Fireflies 1-star, Granola | Skews toward billing and customer support |
| Zoom community, Microsoft-related | AI Companion, Teams recap | Partial success | Zoom community pages truncated for length |
| Independent blogs, lawsuit coverage | "Why nobody reads meeting notes," lawsuits | Succeeded | Vendor blogs distinguished from neutral blogs |
| Zhihu, Xiaohongshu, V2EX, Bilibili | Chinese-language complaints | **Largely failed** | Found only one 2022 piece from Sspai and several promotional articles |
| App Store / Google Play | Low-star reviews | Not obtained directly | Only one Trustpilot review about Android |

**Scoring method**: each category of complaint is scored on three dimensions, with **total score = frequency × intensity × unresolved degree**, out of a maximum of 75.
- **Frequency F (1–5)**: how many times it appears across different sources and different users.
- **Intensity I (1–5)**: how severe the consequences are. 1 is a minor annoyance, 3 requires extra rework, 5 causes actual harm, subscription cancellation or a lawsuit.
- **Unresolved degree U (1–3)**: 1 means mainstream products have largely fixed it; 2 means partially fixed or avoidable through settings; 3 means it is still widespread.

The scoring itself is an **[Inference]**, with the basis written under "Why this score" for each category. The sample size is small, so the scores are used only for ranking and do not indicate precision.

---
## 2. Complaint Evidence Library (by Category)

### A. Summary Hallucination, Misattribution, and Missed Key Content — F4 × I5 × U3 = **60**

**Why it scores this way**:
- **Frequency**: Recurs across HN, independent blogs, and reviews.
- **Intensity**: In medical, education, and workplace settings, erroneous minutes get forwarded as fact. One user called these tools "downright dangerous" outright.
- **Unfixed degree**: Zoom's own documentation says the tool "may provide incorrect, inaccurate, or misleading answers," and every vendor hands the responsibility for checking to the user.

| # | Quote | Source / Date |
|---|---|---|
| A1 | "they capture all the smalltalk perfectly, but tend to plausibly mishear the parts that matter most." (Small talk is recorded word for word, but the most critical parts are misheard in a way that sounds plausible.) | HN user bad_username, "Re: I'm Begging You to Leave Your AI Note-Taker at Home" thread, around mid-2026 https://news.ycombinator.com/item?id=48823024 |
| A2 | "Except they straight up drop important clinical information." (The user's partner is a doctor; the tool simply omits clinical information, and after checking item by item it saves no time at all.) | HN user girvo, same thread |
| A3 | "These things are downright dangerous." (A summary attributed statements to someone who never said them.) | HN user adamddev1, same thread |
| A4 | "I did not talk about project objectives." / "It completely left out the workshop conclusion and follow-up instructions." | Dr Marina Hurley's review of a Zoom AI Companion summary of a 90-minute workshop, 2025-10-28 https://www.writingclearscience.com.au/ai-meeting-summary/ |
| A5 | "It's like asking someone for a quick recap of a meeting, and they tell you what snacks were on the table." | Ask HN "Are there any LLM summary features that don't suck?", 2024-11-23 https://news.ycombinator.com/item?id=42223144 |
| A6 | One user said Copilot's summaries of meetings they presented misunderstood their remarks in some important way "more than half the time"; another said important context was "turned into super generic statements." | HN search snippets (specific posts to be verified) |
| A7 | (An outline generated by Otter) "filled with AI generated questions that I absolutely did not need answered" | HN user arcticfox, 2022-09-07 https://news.ycombinator.com/item?id=32751071 |

**[Inference] Pattern**: Hallucination is not evenly distributed. **The more critical and the less repeated a piece of information is, the more likely it is to be lost**, for example conclusions, numbers, and decisions mentioned only once. A possible cause is that the model treats "frequency of occurrence" as "importance." The vendor Wispr's blog makes a similar argument: the model spreads its attention evenly across the whole meeting, so the sentence that settled a decision reads with the same weight as scheduling small talk (vendor view, https://wisprflow.ai/notetaker/why-ai-meeting-summaries-miss-what-mattered). This is exactly the value of **"attach the verbatim quote and timestamp to every conclusion"**: readers don't need to re-listen to the whole recording, and can verify an item in 3 seconds.

---

### B. Privacy, Consent, and Bots Auto-Joining Meetings — F5 × I5 × U2 = **50**

**Why it scores this way**:
- **Frequency**: Highest. One HN thread has 612 upvotes and 176 comments, plus two class-action lawsuits, dedicated articles from security vendors, and multiple Zoom community posts.
- **Intensity**: Highest, involving leaks of confidential meetings and legal risk.
- **Unfixed degree**: Vendors already offer settings to turn off auto-join, so this is scored 2. But "no-bot" approaches like Granola's turn the problem into "other people don't know they're being recorded," and a new risk arises.

| # | Quote or fact | Source / Date |
|---|---|---|
| B1 | Otter Assistant automatically joined two confidential meetings and recorded them even though the user had turned the setting off, then sent an inaccurate AI outline to all attendees. The original poster said: "I feel completely abused in this situation." | HN "Tell HN: Otter.ai bot recording meetings without consent", 2022-09-07, 612 upvotes / 176 comments https://news.ycombinator.com/item?id=32751071 |
| B2 | "they share conversations with everyone in the meeting by DEFAULT"; "HIS Otter bot will join my work meetings that he is not even invited to." | Same thread, users xyos, latetomato |
| B3 | "Even if you've canceled your subscription or stopped using the app, Otter can keep showing up" | Bitdefender, Cristina Popov, 2025-11-14 https://www.bitdefender.com/en-us/blog/hotforsecurity/otter-ai-keeps-joining-your-meetings-uninvited-heres-how-to-make-it-stop |
| B4 | "Notetaker stayed in meeting after I left - major privacy issue"; "The auto-join settings are also buried and hard to find." | Trustpilot 1 star, Alex Guillen, 2026-06-04 https://www.trustpilot.com/review/otter.ai?stars=1 |
| B5 | "IT PREVENTS ME FROM LOGGING IN IF I DON'T GIVE IT ACCESS TO MY ENTIRE GOOGLE CALENDAR?" | Trustpilot Fireflies 1 star, 2026-08-27 https://www.trustpilot.com/review/fireflies.ai?stars=1 |
| B6 | "Granola was automatically making each of my notes folders public to the entire organization." | HN user eawgewag, 2025-07-30 https://news.ycombinator.com/item?id=44736878 |
| B7 | **[Fact] Lawsuit 1**: Otter was hit with a class action (Brewer, August 2025, N.D. Cal., later styled In re Otter.AI Privacy Litigation), alleging that Notetaker joined and recorded meetings without the consent of other participants. These are allegations, not judgments. | Secondary reports (search snippets, to be verified) https://www.sally.io/blog/otter-ai-class-action-lawsuit ; https://incidentdatabase.ai/entities/justin-brewer/ |
| B8 | **[Fact] Lawsuit 2**: *Chamberlain v. Granola* (Case No. 3:26-cv-07926-EMC, N.D. Cal., filed 2026-07-30). Four main allegations: others are not notified by default; two prompt features must each be turned on manually; the Free and Business plans train models on data by default; and shared links can be set to public. As of the report's publication, Granola had not responded publicly. | PPC Land, 2026-08-01 https://ppc.land/granola-sued-for-recording-meetings-without-consent-to-train-ai-models/ |

**[Inference] Implications for differentiation**:
- Privacy is already the "second track" within a red ocean. Local-first, no-bot products such as Hyprnote/Char, Meetily, and MacWhisper are all playing this card (https://news.ycombinator.com/item?id=44725306). Differentiating on "local processing" alone is **not distinctive enough**.
- What remains truly unmet is **"consent first"**: all participants are informed, can decline on the spot to be recorded, and can decide which remarks stay out of the minutes.
- For research settings, this bears directly on IRB compliance. NYU's guidance explicitly requires researchers to follow IRB rules and names Otter as automatically recording meetings (https://guides.nyu.edu/ai-tools/transcription).

---
### C. Action item extraction is inaccurate: vague, missed, wrong owner —— F4 × I4 × U3 = **48**

**Why it was scored this way**:
- **Frequency**: Recurs across review sites and independent reviews.
- **Intensity**: Once the owner is wrong, the task is assigned to the wrong person.
- **Unfixed degree**: Microsoft's own training materials position the action items in a recap as "suggestions" and require confirming them with the people involved first.

| # | Quote or fact | Source / date |
|---|---|---|
| C1 | Otter "rarely captured the real 'next steps' or key takeaways"; users still have to manually review everything | Capterra review (search snippet, to be verified) https://www.capterra.com/p/202799/Otter/reviews |
| C2 | Misattributed speakers cascade into tasks being assigned to the wrong people; especially noticeable in meetings with more than 10 participants, crosstalk, and phone-bridge audio | eesel review, 2026-10-05 (competitor vendor blog) https://www.eesel.ai/blog/otter-ai-reviews ; NeuronFeed review (search snippet) https://neuronfeed.com/reviews/otter-ai-review |
| C3 | "I have Teams recaps but still do not know who owns the actions"; "yet leaves ownership, due dates and destination unconfirmed." | Collab365, 2026-08-25 https://collab365.com/library/microsoft-365-productivity/teams-meeting-recaps-create-notes-but-actions-stil-IrSTUa |
| C4 | Action items generated by the recap are "suggestions inferred from what was said, not authoritative assignments"; any item that looks like a commitment should first be confirmed with the person named | Azure certification exam prep guide (search snippet, to be verified) https://open-exam-prep.com/study-guides/azure-ab-730/meetings-collaboration-personalization/meeting-recap-catchup |
| C5 | "the summary in the android app does not show the actions!" (action items are not visible on mobile) | Trustpilot Otter 2-star review, Jim Barron, 2026-02-14 https://www.trustpilot.com/review/otter.ai?stars=2 |

**[Inference]**:
- The "extraction" step itself is no longer a differentiator. Every vendor can produce a list, and the original BriefPilot PRD's design of "leave missing fields blank rather than guess" is already a response to C1–C4.
- The differentiator lies in what happens **after extraction**: when the owner or due date is missing, the product should proactively flag it rather than guess, and the person named should be able to **confirm or reject**.

---

### D. Tasks go unclaimed and have no follow-up —— F3 × I5 × U3 = **45**

**Why it was scored this way**:
- **Frequency**: Medium; it comes mainly from independent blogs in 2026, with few original user posts.
- **Intensity**: High; this kind of problem directly leads to delivery failures.
- **Unfixed degree**: The solutions offered by the sources are all manual rituals; none mentions a product that has already solved it.

| # | Quote | Source / date |
|---|---|---|
| D1 | "I thought it was in the notes somewhere, I assumed someone would follow up." / "The founder thought the ops manager had it." | Lilach Bullock, case of a 7-person marketing agency, 2026 https://www.lilachbullock.com/ai-meeting-notes-accountability-small-teams/ |
| D2 | "It did nothing to make anyone feel responsible for it" | Same as above |
| D3 | "at least a third would be untouched, sitting exactly where the AI left them, in a summary nobody reopened." | Same as above (the author's personal estimate, not a statistic) |
| D4 | "An action without a date is a preference. The date is what makes it show up in something." | Programming Insider, Marc Berman, 2026-09-08 https://programminginsider.com/why-ai-note-taker-summaries-go-unread-and-what-fixes-it/ |
| D5 | "Coordinators must run a manual verification step to move items into the system of record." | Collab365, 2026-08-25 (same as C3) |

**[Inference] Explanation of the mechanism**: This is **diffusion of responsibility**. AI meeting notes make "writing it down" costless, but "writing it down" used to be a social signal of public commitment. Lilach's original text also says that automated notes make individuals "feel less personally on the hook" (feeling that the matter is no longer something they must personally carry). So simply pushing tasks into Asana is not enough; **an action where the person involved claims the task in their own words or with their own hands is needed**. BriefPilot's "human confirmation" can be upgraded from "the PM confirms the draft" to "the owner personally claims the task."

---
### E. Pricing, Billing, and Quotas — F5 × I3 × U3 = **45** (low differentiating value for BriefPilot)

| # | Quote | Source / Date |
|---|---|---|
| E1 | "Fireflies attempted to charge my card 10+ times over two weeks without any prior notice" | Trustpilot, Fireflies 1-star, 2026-06-01 |
| E2 | "will auto-upgrade you to use more AI credits and will charge your account silently" | Same as above, 2026-05-14 |
| E3 | "Max 30 minute recording on free plan - NOT STATED ANYWHERE CLEARLY!" | Trustpilot, Otter 2-star, 2026-09-11 |
| E4 | "Software works, but constantly run out of minutes." | Trustpilot, Otter 2-star, 2025-12-29 |

**[Fact] Pricing check**: Otter's current pricing on its website is as follows (https://otter.ai/pricing , retrieved at the time of writing):

| Plan | Price | Monthly transcription quota | Per-meeting limit |
|---|---|---|---|
| Basic | Free | 300 minutes | 30 minutes |
| Pro | $16.99/month (annual billing works out to $8.33/month) | 1,200 minutes | 90 minutes |
| Business | $30/month (annual billing $19.99/month) | Unlimited | 4 hours |

A 1-hour group meeting exceeds the free plan's per-meeting limit. eesel also mentions that users perceive "shrinkflation", i.e., fewer minutes for the same price.

**[Inference]**: Billing complaints are the most numerous, but this is a business-model problem, **not a feature-differentiation opportunity**. However, the fact that "research group meetings usually run 60–120 minutes and students have low willingness to pay" will affect how the demo is deployed. Consider local Whisper or on-demand upload rather than a cloud service billed per minute.

---

### F. Transcription Accuracy and Speaker Identification — F5 × I4 × U2 = **40**

| # | Quote | Source / Date |
|---|---|---|
| F1 | "the inability to tell who said what is a show stopper." | HN user ljosa, 2025-07-30 https://news.ycombinator.com/item?id=44725306 |
| F2 | "Transcription accuracy poor with >1 speaker, overlap, painful edits to clean up." | Trustpilot, Otter 1-star, 2026-05-29 |
| F3 | "Otter has consistently failed to capture or transcribe 32% of the material." | Trustpilot, Otter 2-star, 2026-06-20 (user-reported figure, unverified) |
| F4 | "It writes 'START' where the recording clearly says 'STOP.'" | Trustpilot, Otter 1-star, 2026-08-06 |
| F5 | G2's comparison page lists Fireflies' top cons as "AI Inaccuracy" (39 reviews) and "Meeting Management" (32 reviews) | G2 (search snippet, to be verified) https://www.g2.com/compare/fireflies-ai-vs-supernormal |

**[Inference]**: The underlying ASR keeps improving, so the unfixed score is 2. But **speaker identification remains weak in single-microphone, multi-speaker, in-person scenarios**; see category G. This is a technically heavy "hard nut to crack," and as a PM portfolio demo it **should not be tackled head-on**. A better approach is to sidestep it: let owners claim action items themselves, instead of relying on AI to guess who said what.

---

### G. No Support for In-Person or Hybrid Meetings (Single Microphone, Multiple People) — F3 × I4 × U2 = **24**

| # | Quote | Source / Date |
|---|---|---|
| G1 | "it becomes completely useless when holding meetings in a hybrid fashion." (a meeting room sharing a single microphone) | HN user marcofiset, 2025-07-29 https://news.ycombinator.com/item?id=44725306 |
| G2 | Note-taking tools are "skewed towards one-person summary" and struggle in multi-person in-person scenarios | HN user nashashmi, same as above |
| G3 | "Speaker recognition can be a bit sketchy for multiple speakers on a single recording device." | tl;dv's Otter review (competitor vendor, search snippet) https://tldv.io/blog/otter-ai-review/ |
| G4 | **[Fact]** The Granola complaint alleges it can also record in-person conversations, raising a new issue: "it is harder for others to know they are being recorded in person" | PPC Land, 2026-08-01 (same as B8) |

**[Inference]**: Research group meetings, whiteboard discussions, and advisor one-on-ones are often held in person or in hybrid format, as already discussed in document 03. Such scenarios hit both category F (poor identification) and category B (consent issues). The combination of **"in-person meetings + owner self-claiming"** may be more feasible than "in-person meetings + better speaker identification." This point is an **[Assumption]**, pending validation.

---
### H. Nobody reads the notes, information overload — F4 × I3 × U3 = **36**

| # | Quote | Source / date |
|---|---|---|
| H1 | "The most absurde thing is that nobody will ever read those notes, transcripts anyhow." | HN user smartmic, around mid-2026 https://news.ycombinator.com/item?id=48823024 |
| H2 | "We're using AI to summarize meetings nobody wanted to attend. Then nobody reads the summaries." (a saying quoted in the article as circulating widely) | Laxis, 2026-05-11 (vendor blog) https://www.laxis.com/blog/ai-meeting-summary-fatigue-2026/ |
| H3 | If nobody reads the notes, "in my experience almost nobody does" | Lilach Bullock (search snippet) https://www.lilachbullock.com/ai-meeting-notes-worse-listeners/ |
| H4 | "A summary saved to a folder is an archive, and archives are for auditing." | Programming Insider, 2026-09-08 |
| H5 | Would rather get "three accurate one-line takeaways" than "several pages of AI slop" | HN comment (search snippet, to be verified) |
| H6 | Vendor self-reported: generic summaries are opened about 0.3 times per person; after switching to targeted extraction, about 2.7 clicks per summary | Cotera (vendor self-reported, unverified) https://cotera.co/articles/ai-meeting-summary-tool |

**[Inference] Two side effects**:
- Laxis relays a "study circulating in 2026": teams that use instant summaries actually send 15% more follow-up clarification emails after meetings. The study is **unnamed and unlinked, and cannot be relied on**; it can only serve as a lead for a hypothesis.
- Laxis also observes that "people stop asking questions in the meeting, because there's a recap anyway."

**Opportunity**: Output should be **shorter, more accurate, and pushed per person**. "You have 2 commitments in this meeting" is more likely to get opened than "a 3-page summary of the whole meeting."

---

### I. Can't integrate with one's own notes and knowledge base — F3 × I3 × U2 = **18**

| # | Quote | Source / date |
|---|---|---|
| I1 | "getting data in has consistently been the point of failure." (importing meeting notes into a personal knowledge base always fails) | HN user kpen11, 2025-07-29 https://news.ycombinator.com/item?id=44725306 |
| I2 | "Granola are cracking down on their auth." (after Granola tightened authentication, a user's Obsidian sync plugin stopped working) | HN user tomelliot, around mid-2026 https://news.ycombinator.com/item?id=48936123 |
| I3 | "I'd love to be able to add project tags to transcripts." | HN user crashabr, 2025-07-30 https://news.ycombinator.com/item?id=44725306 |
| I4 | Wants to take notes live during a meeting and have them automatically aligned with the recording and transcript afterward (an Avoma co-founder replied that this is already supported) | HN user futureshock, 2021-06-29 https://news.ycombinator.com/item?id=27679122 |
| I5 | When connecting Obsidian via MCP, "defeats the offline transcription thing" (undermines the original point of offline transcription) | HN user marshalla, same as I2 |

**[Inference]**:
- Granola's selling point is "your notes + AI filling in the gaps," and Avoma also claims to support aligning notes with transcripts, so the unfixed score is 2.
- The remaining gaps are **"organizing across meetings by project or topic"** and **"exporting to the user's own knowledge base (Obsidian, Zotero, etc.)"**. This matters especially for research users: a single topic runs for months and spans dozens of group meetings.

---

### J. Multilingual and mixed Chinese-English speech — F2 × I4 × U3 = **24** (first-hand Chinese-language evidence missing)

| # | Quote or fact | Source / date |
|---|---|---|
| J1 | "the Japanese scripts lacked sufficient detail" | Trustpilot Otter 1-star, 2026-09-23 |
| J2 | "It doesnt even have Chinese" | Trustpilot Otter 2-star, 2025-07-11. **Note: Otter's current pricing page already lists Chinese**, so this may have been fixed, but its performance on mixed Chinese-English speech is unknown (to be verified) |
| J3 | **[Fact, academic]** A 2026 arXiv paper identifies three kinds of failure when large audio models handle Chinese-English code-switching: dropping one of the languages, turning transcription into translation, and hallucination | arXiv 2605.23975 https://arxiv.org/pdf/2605.23975 |
| J4 | **[Fact, academic]** A medRxiv heuristic evaluation tested an AI documentation tool for clinical settings (not Otter): at Mandarin–English switch points, dropped words were frequent | medRxiv (search snippet, to be verified) |
| J5 | Recall.ai's documentation states that some ASR vendors require candidate languages to be specified in advance, and few vendors natively support code-switching | https://docs.recall.ai/v1.10/docs/multilingual-transcription (search snippet) |

**[Inference]**:
- English-speaking user communities barely discuss mixed Chinese-English speech; this is **sample bias** and does not show that the problem doesn't exist. For labs like those in Singapore and at the target university, where the language is "mostly English, with some Mandarin and technical terms mixed in," this may be a strong need.
- However, this round **did not obtain any original posts from Chinese-speaking users** showing that "Feishu Minutes and Tongyi Tingwu handle mixed Chinese-English poorly." Feishu's official site claims 98% accuracy for Chinese transcription (https://www.feishu.cn/content/article/7600354990053559227 ), which is the vendor's own claim.
- So this item can only be treated as an **[Assumption]**, handed to 02_user-research/中英夹杂与隐私约束 for validation.

---
### K. Domain Terms, Proper Nouns, and Numbers Going Wrong — F3 × I3 × U2 = **18**

- A Bilibili tool roundup tutorial warns that in the output of Tongyi Tingwu and Tencent Meeting, "key numbers and proper nouns still should be manually rechecked" (https://www.bilibili.com/read/cv50268644, search snippet).
- NYU's guide warns that AI transcription can "add text that was not part of the source audio, mis-attribute text to speaker" (https://guides.nyu.edu/ai-tools/transcription).
- An HN comment says even a good tool is only "roughly equivalent to a human note-taker who knows the domain terminology" (search snippet, to be verified).

**[Inference]**: In research meetings, model names (VLA, RT-2, π0 and the like), dataset names, and hyperparameter numbers are exactly the content most likely to be wrong, and the most costly when wrong. **A user-defined glossary + highlighting numbers and proper nouns for review** is a low-cost, high-perceived-value feature.

---

### L. Social Cost: The Awkwardness of a Bot Joining the Meeting — F4 × I3 × U2 = **24**

- "users hate the bot and it takes up too much visibility on many of these calls." HN user theodorewiles, 2025-07-29 (https://news.ycombinator.com/item?id=44725306)
- A G2 reviewer says other participants wonder "who is this extra participant" (search snippet, to be verified).
- HN user rcost300: "The issue is discretion - something that nearly all humans have, and no AI model has an ounce of." A human secretary proactively leaves out sensitive tangents (https://news.ycombinator.com/item?id=48823024).
- HN user jerlam: shared notes that participants can see and approve on the spot work better, because AI minutes are often compiled long after the meeting (same source).

**[Inference]**: rcost300 and jerlam point to the same unmet need: **"consensus on the spot"**, meaning the minutes are seen and approved by participants before the meeting ends, plus **"discretion"**, meaning the ability to mark a segment as not to be recorded. This is also the direction in which "human confirmation" can be moved earlier in the flow.

---

### M. Can't Find "What Was Decided Last Week" (Cross-Meeting Retrieval) — F2 × I3 × U1.5 ≈ **9**

- **[Fact]** Direct original user complaint posts are rare. Vendor marketing, on the other hand, covers this point heavily, for example Fabric's semantic search, MangoApps' decision extraction, and Fabric's weekly decision digest (https://fabric.so/use-cases/meeting-notes; https://www.mangoapps.com/apps/ai-notepad).
- The Vibe blog quotes Laxis as saying: "70% of meeting decisions are forgotten within 24 hours when post-meeting notes are not shared." This is **a vendor claim relayed second-hand and unverified; do not cite it**.
- HN has a counter-view: if the full transcript is searchable, what value is left in a summary (search snippet).

**[Inference]**: "Cross-meeting search" is already a standard vendor selling point, so **on its own it is a weak differentiator**. But if the retrieval target is narrowed from "all transcripts" to **"confirmed decisions and commitments"**, and combined with category D, it becomes a **"commitment ledger"**. It answers the question "who promised what last time, and did they do it", which is more specific than "search for what was said last week".

---

### N. Export, Integration, and Sync Problems — F2 × I2 × U2 = **8**

- Fireflies summaries do not update after the user manually edits the transcript (Capterra, search snippet, to be verified).
- Otter's Android app cannot show action items (see C5).
- In 2022, Feishu Minutes had no folder system yet, and Feishu Docs could not directly parse Minutes links (Sspai, Zhang Lixing, 2022-01-14, https://sspai.com/post/70960; **content is older and may have since been updated**).
- Granola tightened authentication, which broke third-party sync (see I2).

---

### O. Research Compliance and Data Localization (IRB) — F2 × I4 × U2 = **16**

- NYU requires researchers who use AI transcription to comply with IRB rules (https://guides.nyu.edu/ai-tools/transcription).
- An opinion article argues that if the research protocol states that recordings stay on an encrypted laptop, uploading audio to the cloud for transcription may constitute a protocol deviation (yaps.ai, opinion piece, search snippet).
- HN user joos3 thinks hosted solutions "don't really make sense" and prefers local recording; _trampeltier thinks keeping recordings on the device is less unsettling (https://news.ycombinator.com/item?id=44725306; https://news.ycombinator.com/item?id=48823024).

---

## 3. Summary Scoring Table

| Rank | Category | F | I | U | Total | Main evidence sources | Relevance to BriefPilot |
|---|---|---|---|---|---|---|---|
| 1 | A Hallucination, misattribution, missed key points | 4 | 5 | 3 | 60 | HN×4, Zoom review | **High** (the citation mechanism fits directly) |
| 2 | B Privacy, consent, auto-join | 5 | 5 | 2 | 50 | HN post with 612 upvotes, two lawsuits, Trustpilot | Medium (red ocean, but there is room for "consent first") |
| 3 | C Inaccurate action item extraction, wrong owner | 4 | 4 | 3 | 48 | Collab365, Capterra, eesel | **High** |
| 4 | D Nobody claims items, no follow-up | 3 | 5 | 3 | 45 | Lilach, Programming Insider, Collab365 | **High** (core differentiator) |
| 4 | E Pricing, billing | 5 | 3 | 3 | 45 | Trustpilot (many) | Low (business issue) |
| 6 | F Transcription, speaker identification | 5 | 4 | 2 | 40 | HN, Trustpilot, G2 | Medium (technically heavy, better to sidestep) |
| 7 | H Nobody reads them, information overload | 4 | 3 | 3 | 36 | HN, Laxis, Lilach | High |
| 8 | G In-person and hybrid meetings | 3 | 4 | 2 | 24 | HN×2, complaint filings | Medium-high (amplified in research settings) |
| 8 | J Mixed Chinese-English speech | 2 | 4 | 3 | 24 | arXiv, Trustpilot (no Chinese UGC) | Medium-high (**to be verified**) |
| 8 | L Social cost of bots, discretion | 4 | 3 | 2 | 24 | HN×3 | Medium |
| 11 | I Integration with personal notes | 3 | 3 | 2 | 18 | HN×5 | Medium-high (research is organized by project) |
| 11 | K Terminology, numbers | 3 | 3 | 2 | 18 | Bilibili, NYU | High (low-cost feature) |
| 13 | O Research compliance | 2 | 4 | 2 | 16 | NYU, HN | Medium (research setting) |
| 14 | M Finding decisions across meetings | 2 | 3 | 1.5 | 9 | Mostly vendor marketing | Medium (valuable only when merged with D) |
| 15 | N Export, integration | 2 | 2 | 2 | 8 | Scattered | Low |

---
## 4. Recurring "I wish it could… but no product does it"

The table below distills the wishes from the original quotes. The column "Does an existing product claim to do this?" is filled in honestly, so that things already done are not mistaken for gaps.

| # | Wish (quote or paraphrase) | Source | Does an existing product claim to do this? |
|---|---|---|---|
| W1 | Take notes live during the meeting, then align them with the recording and transcript afterward | futureshock, 2021 | Avoma and Granola claim to support it → **largely met** |
| W2 | Tag transcripts with a "project label" and organize them across meetings by project | crashabr, 2025 | No mainstream product was seen highlighting this (to be verified) |
| W3 | Fully local, background daemon, CLI-first | tomelliot, 2026 | Partly met by Hyprnote/Char and Meetily |
| W4 | During the meeting, have an LLM suggest "what question to ask right now" | ashishact, 2025 | Some sales tools do this (to be verified) |
| W5 | After local processing, still sync to one's own knowledge base | marshalla, tomelliot | **Gap**: local processing and integrations conflict with each other |
| W6 | Minutes that participants can see and approve on the spot | jerlam, 2026 | **Gap**: every product generates minutes only after the meeting |
| W7 | Discretion like a human secretary, proactively leaving out sensitive side remarks | rcost300, 2026 | **Gap** |
| W8 | Every action item has an owner and a date, and shows up in the owner's workflow | Programming Insider, Collab365 | Partly met (integrations exist, but owners are not confirmed) |
| W9 | Not several pages of summary, just "three accurate key points" | HN (search summary) | Partly met (configurable templates) |

---

## 5. Top 10 Unmet Needs (Ranking Table)

Ranking basis: the scores from Section 3, multiplied by an adjustment for "BriefPilot feasibility and differentiation." "Evidence strength" is determined by the following criteria:
- **Strong**: ≥3 independent primary sources, with verbatim quotes;
- **Medium**: 2–3 sources, or mainly independent blogs;
- **Weak**: only a single source, vendor sources, or indirect academic evidence.

| Rank | Unmet need | Evidence strength | Key evidence | Why existing products don't meet it [Inference] | Possible product opportunity (BriefPilot) |
|---|---|---|---|---|---|
| 1 | **Low-cost verifiable minutes**: every decision or commitment can be traced back to the original words in 3 seconds | Strong | A1–A7, K | Products output "fluent summaries"; citations often don't reach the sentence level; the burden of checking is pushed onto the user | Attach an **original quote snippet + timestamp + speaker** to every decision or commitment, playable with one click; output nothing that has no supporting evidence (following BriefPilot's refusal-to-answer principle) |
| 2 | **Owners claim items themselves**, rather than being assigned by AI | Medium-strong | C3, C4, D1–D5 | Products default to "generated means done"; claiming requires another person to take action, which is hard to automate and hard to use in marketing | After the meeting, push "you have N commitments" to each person named, with options to **confirm, reschedule, or decline**; only after confirmation does an item become a formal task |
| 3 | **Automatic review of last meeting's commitments at the next meeting** | Medium | D3 (1/3 untouched), Lilach's suggestion of a "90-second review at the start" | Products treat a single meeting as the unit and have no state at the "meeting series" level | A "commitment ledger": at the start of a meeting series (e.g., a weekly group meeting), automatically generate a "status of last meeting's commitments" list |
| 4 | **Few and accurate, pushed per person**, not a full summary | Medium-strong | H1–H6, W9 | Full summaries are easy to build and easy to show off; personalized slices require an identity and permission model | By default output only three columns, "decisions / commitments / open questions," split by person; the full transcript is demoted to an attachment |
| 5 | **Consent first**: everyone is informed, can refuse, and can mark "do not record" | Strong (problem) / Weak (solution) | B1–B8, L, W7 | Bot-free approaches buy "others don't know"; bot-based approaches carry a social cost. Neither gives participants control | Consent card at the start; an in-meeting "don't record this part" marker; a chance for participants to redact before the minutes are sent |
| 6 | **Consensus on the spot**: confirm the minutes before the meeting ends | Weak-medium | W6 (jerlam), rcost300 | The mainstream architecture is post-meeting batch processing | In the last 3 minutes of the meeting, show a draft of "decisions and commitments from this session" and confirm it verbally on the spot (can be merged with #2) |
| 7 | **In-person or hybrid meetings, multiple people on a single microphone** | Medium | G1–G4, F1 | Approaches that rely on platform audio tracks or bots are inherently weak in this scenario, and speaker identification is a hard technical problem | Sidestep identification: after an in-person meeting, let participants claim "which items are mine," replacing voiceprint recognition with social confirmation **[Assumption]** |
| 8 | **Glossary and number checking** (research and technical settings) | Medium | K, J3 | General-purpose products target business English; custom vocabulary features have not been verified | One glossary per research topic (imported from papers, Zotero, or a README); numbers and proper nouns are highlighted for checking (pending) |
| 9 | **Organize across meetings by research topic or project, and export to one's own knowledge base** | Medium | I1–I5, W2, W5 | Products treat the "meeting" rather than the "topic" as the first-class object; closed ecosystems (e.g., Granola tightening authentication) | A topic view, with Markdown and Obsidian-friendly export; connected to BriefPilot's "knowledge Q&A with citations" |
| 10 | **Mixed Chinese-English speech and local compliance** (the target university, Singapore labs) | Weak (UGC) / Medium (academic) | J1–J5, O | Chinese-English code-switching is a recognized hard problem for ASR; the IRB places constraints on cloud third parties | Allow connecting a user-chosen ASR, or use local Whisper; first **measure** commitment-extraction recall under mixed Chinese-English speech in the demo, rather than promising results **[Assumption]** |

**[Inference] The common thread of the Top 10**: put together, items 1, 2, 3, 4, and 6 form **"commitments that are evidenced, claimed, and reviewed."** This is consistent with BriefPilot's existing direction of "citations + don't guess when information is missing + human confirmation," and the differentiation can be stated as:

> Other products help you **generate** meeting minutes; BriefPilot helps the team **fulfill** the commitments made in the meeting, and every one of them can be traced back to the original words.

Items 7–10 are **amplifiers for the research-lab segment**, used to answer "why start with labs." But their evidence is currently weak, and they must wait for 02_user-research to fill the gaps.

---
## 6. Draft Direct Responses to Client or Interviewer Questions [Inference]

> "Feishu Minutes and Otter both already turn meetings into tasks. Why build this?"

1. **They "convert" tasks; they don't get them "fulfilled."** The most concentrated complaints in public posts are that summaries can't be trusted (Category A, 60 points) and that tasks have no one to claim them (Category D, 45 points). Even Microsoft's own training materials say the action items in a recap are only "suggestions" that should be confirmed with the people involved first (C4).
2. **The widespread use of manual workflows shows the product layer is empty.** Several independent sources offer the same fix: manual rituals such as "recap at the end of the meeting, move items over within 24 hours, review at the start of the next meeting" (D1–D5).
3. **The entry point is a dogfooding scenario.** Research group meetings are held in person or in hybrid format, mix Chinese and English, and are dense with jargon, and most commitments are soft ones like "I'll try X next week." Mainstream products are weak on all of these (Categories G, J, K). I am in this scenario myself, so I can validate quickly.
4. **Honest boundaries.** Many products already address privacy and localization, so these are not my main selling points. I don't build my own ASR or speaker recognition; I work around them instead.

---

## 7. Gaps and Next Steps

1. **First-hand Reddit evidence**: the project owner needs to search r/PhD, r/GradSchool, r/academia, and r/productivity manually in a browser. Suggested keywords: "lab meeting notes", "Otter action items", "advisor meeting follow up". Excerpt 10–20 posts and add them to this document.
2. **Chinese UGC**: manually search Zhihu, Xiaohongshu, V2EX, and Bilibili comments for "飞书妙记 不准" (Feishu Minutes inaccurate), "通义听悟 中英" (Tongyi Tingwu Chinese-English), "组会 纪要 AI" (group meeting minutes AI), and "腾讯会议 AI 纪要 待办" (Tencent Meeting AI minutes action items). The search quota ran out this round, so this was not completed.
3. **Original G2 / Capterra pages**: open them manually and verify statistics such as Fireflies "AI Inaccuracy 39".
4. **Low-rated App Store / Google Play reviews**: not covered.
5. **Turn the Top 10 into interview questions**: hand these to 02_user-research and validate #2, #3, #7, and #10 with 3–5 members of labs at the target university.

---

## Source List

**Hacker News (first-hand)**
1. Tell HN: Otter.ai bot recording meetings without consent (2022-09-07) https://news.ycombinator.com/item?id=32751071
2. Launch HN: Hyprnote (YC S25) (2025-07-29/30) https://news.ycombinator.com/item?id=44725306
3. HN comment by eawgewag (2025-07-30) https://news.ycombinator.com/item?id=44736878
4. Ask HN: Best meeting transcription daemon for macOS? (around mid-2026) https://news.ycombinator.com/item?id=48936123
5. Re: I'm Begging You to Leave Your AI Note-Taker at Home (around mid-2026) https://news.ycombinator.com/item?id=48823024
6. Original post at firesphere.dev https://firesphere.dev/articles/yes-actually-i-do-fucking-mind
7. Ask HN: Are there any LLM summary features that don't suck? (2024-11-23) https://news.ycombinator.com/item?id=42223144
8. HN comment by futureshock (2021-06-29) https://news.ycombinator.com/item?id=27679122
9. Show HN: Turn messy meeting notes into actionable tasks (2025-06-24) https://news.ycombinator.com/item?id=44368806
10. Open-source granola (2025-06-13) https://news.ycombinator.com/item?id=44271745

**Review sites**
11. Trustpilot Otter 1-star https://www.trustpilot.com/review/otter.ai?stars=1
12. Trustpilot Otter 2-star https://www.trustpilot.com/review/otter.ai?stars=2
13. Trustpilot Otter (Canada site overview) https://ca.trustpilot.com/review/otter.ai?page=1
14. Trustpilot Fireflies 1-star https://www.trustpilot.com/review/fireflies.ai?stars=1
15. Trustpilot Granola https://www.trustpilot.com/review/granola.ai
16. G2 Fireflies vs Supernormal (search snippet) https://www.g2.com/compare/fireflies-ai-vs-supernormal
17. Capterra Otter (search snippet) https://www.capterra.com/p/202799/Otter/reviews

**Zoom / Microsoft**
18. Writing Clear Science: Zoom AI Companion summary errors (2025-10-28) https://www.writingclearscience.com.au/ai-meeting-summary/
19. Zoom Community: Meeting Summary Issues (search snippet) https://community.zoom.com/ai-companion-21/meeting-summary-issues-shorter-and-no-longer-accurate-75447
20. Zoom Community: Can't disconnect Otter.ai (search snippet) https://community.zoom.com/t5/Marketplace/Can-t-disconnect-Otter-ai/m-p/120902
21. Collab365: Teams recaps still lose action items (2026-08-25) https://collab365.com/library/microsoft-365-productivity/teams-meeting-recaps-create-notes-but-actions-stil-IrSTUa
22. Open Exam Prep: Meeting Recap (search snippet) https://open-exam-prep.com/study-guides/azure-ab-730/meetings-collaboration-personalization/meeting-recap-catchup
23. Microsoft Support: Use Copilot in Teams meetings https://support.microsoft.com/en-us/office/use-copilot-in-microsoft-teams-meetings-0bf9dd3c-96f7-44e2-8bb8-790bedf066b1

**Independent and vendor blogs**
24. Lilach Bullock: AI meeting notes accountability (2026) https://www.lilachbullock.com/ai-meeting-notes-accountability-small-teams/
25. Lilach Bullock: AI meeting notes worse listeners (search snippet) https://www.lilachbullock.com/ai-meeting-notes-worse-listeners/
26. Laxis: AI meeting summary fatigue (2026-05-11, vendor) https://www.laxis.com/blog/ai-meeting-summary-fatigue-2026/
27. Programming Insider (2026-09-08) https://programminginsider.com/why-ai-note-taker-summaries-go-unread-and-what-fixes-it/
28. Cotera (vendor, search snippet) https://cotera.co/articles/ai-meeting-summary-tool
29. Wispr Flow (vendor, search snippet) https://wisprflow.ai/notetaker/why-ai-meeting-summaries-miss-what-mattered
30. eesel: Otter AI reviews (2026-10-05, competitor vendor) https://www.eesel.ai/blog/otter-ai-reviews
31. NeuronFeed: Otter review (search snippet) https://neuronfeed.com/reviews/otter-ai-review
32. tl;dv: Otter review (competitor vendor, search snippet) https://tldv.io/blog/otter-ai-review/
33. Bitdefender (2025-11-14) https://www.bitdefender.com/en-us/blog/hotforsecurity/otter-ai-keeps-joining-your-meetings-uninvited-heres-how-to-make-it-stop
34. Fabric meeting notes use case (vendor) https://fabric.so/use-cases/meeting-notes

**Lawsuits and compliance**
35. PPC Land: Granola sued (2026-08-01) https://ppc.land/granola-sued-for-recording-meetings-without-consent-to-train-ai-models/
36. Sally: Otter class action (search snippet) https://www.sally.io/blog/otter-ai-class-action-lawsuit
37. AI Incident Database: Justin Brewer (search snippet) https://incidentdatabase.ai/entities/justin-brewer/
38. NYU Libraries: AI transcription tools https://guides.nyu.edu/ai-tools/transcription
39. National Law Review: AI meeting tools wiretapping (search snippet) https://natlawreview.com/article/ai-meeting-tools-face-wiretapping-wake-call

**Multilingual and academic**
40. arXiv 2605.23975: English-Chinese code-switching ASR (2026-05) https://arxiv.org/pdf/2605.23975
41. Recall.ai Multilingual Transcription (search snippet) https://docs.recall.ai/v1.10/docs/multilingual-transcription

**Chinese-language**
42. Sspai: Using Feishu Minutes to improve the learning experience (Zhang Lixing, 2022-01-14) https://sspai.com/post/70960
43. Feishu official site: Feishu Minutes articles (vendor's own claim of 98%) https://www.feishu.cn/content/article/7600354990053559227
44. Bilibili column: Roundup of AI meeting minutes software (search snippet) https://www.bilibili.com/read/cv50268644

**Pricing check**
- Otter Pricing (fetched at the time of writing) https://otter.ai/pricing (used as a fact-check page; not counted toward the number of complaint sources)

---
## Confidence Levels for This Document's Conclusions

| Conclusion | Confidence | Rationale |
|---|---|---|
| "Hallucinations, misattribution, and missed key points" are high-frequency, high-intensity complaints | **High** | Corroborated by multiple independent HN users, examples from healthcare and education settings, and Zoom's official disclaimer |
| Privacy and auto-join are high-intensity issues | **High** | A 612-upvote HN post and reports of two class-action lawsuits (lawsuits are only allegations, not verdicts) |
| "Action items nobody claims or follows up on" is a real gap | **Medium** | Evidence comes mainly from personal observations by independent bloggers and consultants in 2026, with few original user posts; "1/3 untouched" is a personal estimate |
| "Nobody reads the meeting notes" | **Medium** | HN quotes plus blogs, but vendor data (Cotera, Laxis) cannot be trusted |
| "Commitment ledger" is BriefPilot's best differentiation direction | **Medium-low (inference)** | Derived by synthesizing complaints and **not yet validated through user interviews**; also not verified whether a niche product already does this (e.g., Fellow's recurring-meeting action item review, to be verified) |
| Mixed Chinese-English speech is a strong pain point in research settings | **Low (assumption)** | Only indirect academic evidence and 1–2 Trustpilot reviews; no first-hand evidence from Chinese-speaking users |
| Specific values in the scoring table | **Low to medium** | Subjective scoring with a biased sample (English-language, tech-community, complaint channels); use only for relative ranking |
| Verbatim accuracy of quoted remarks | **Medium** | Extracted by a scraping tool; check each one by opening the source before external use |

**Main sources of bias**:
1. First-hand data from Reddit, G2, Capterra, and Chinese-language communities is missing;
2. Channels like Trustpilot skew heavily toward billing and customer-service complaints;
3. HN users skew technical and privacy-sensitive;
4. Some sources are blogs from competing vendors (eesel, tl;dv, Circleback, Laxis, Cotera, Wispr), who have a vested interest;
5. The search quota ran out partway through this round, so the supplementary Chinese-language searches were not completed.
