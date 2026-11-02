---
title: "Supplementary Verification 07: How far do Fellow, Littlebird and other competitors get at the 'after the commitment' stage (claiming, closing the loop, 1:1s, cross-meeting)"
status: draft-v1 (second verification round; some sources pending manual review)
sources_count: 51
sources_count_method: unique URLs in the sources section (recalculated at wrap-up; original value 46)
---

# Supplementary Verification 07: Item-by-item competitor verification of the "after the commitment" stage

> **This file answers one question**: for candidate differentiators G4 (assignee claims the item), G5 (commitment → outcome → evidence loop), G6 (mentor 1:1 ledger), G11 (cross-meeting tracking), and the adjacent G2, G3, G9, G10, G12, **how much white space is left At the time of writing?**
>
> **Method**: for each product, we opened the official feature pages, help center, and pricing page, as well as universities' official supervision-policy pages. Every capability row states "supported or not, evidence URL, access date". All official sources were accessed on **at the time of writing**.
>
> **Labeling discipline**:
> - **[Fact]**: the original page was opened this round and the capability description comes from it.
> - **[Summary]**: only a search-engine snippet was seen, or a secondary page was used after the original returned 403/404.
> - **[Inference]**: derived from facts, not directly verified.
> - **[Assumption · to be verified]**: needs user interviews or hands-on testing to confirm.
> - "**Not seen**" means "the page doesn't say so", which is not the same as "the product doesn't have it".
>
> **Limitations this round**:
> - The OpenAI help center returned 403. Both LJMU eDoc PDFs now return 404. The target university's graduate school policies and templates are on its intranet and the public pages can't be opened. The NUS Psychology department handbook PDF could not be parsed locally.
> - No official statement was found on whether Tencent Meeting action items can be traced back to their source.
> - Every capability comes from documentation only; **no hands-on product testing was done**.

---

## 0. Conclusions first (7 points)

1. **[Fact] The first-round review's claim that "Fellow shows no assignee confirmation/claiming" must be overturned.** The Fellow help center article "AI-Suggested Action Items" (page dated 2026-10-01) says: "any assignee can accept or dismiss it". Unaccepted suggestions are "not added to the inbox, not synced to project management tools, and not carried into the next meeting", and "Auto-accept" is off by default (https://help.fellow.ai/en/articles/17299858-ai-suggested-action-items ). In other words, **the mechanism "AI draft → the assignee personally accepts or dismisses → only then does it become a formal task" went live at Fellow a month ago**. G4 drops from "medium" to "already covered (core mechanism)".
2. **[Fact] At Fellow, "declining" means deletion and "won't do" means archiving.** A dismissed suggestion is "permanently deleted… cannot be recovered" (same page). Formal action items have only two terminal states, complete and archived, with archived described as "won't do" (https://help.fellow.ai/en/articles/4144380-action-item-page ). **[Inference]** This leaves a very narrow gap: Fellow records neither **why an item was dismissed** nor **the dismissal itself**, so the organizer has no way of knowing that "nobody claimed this one".
3. **[Fact] Littlebird already targets the graduate student and advisor scenario by name.** Its graduate-student landing page says it "lists what you promised your advisor", and the pre-meeting brief includes "what you committed to, the feedback still open" (https://littlebird.ai/for/graduate-students ); the student price is Plus $15/month, with the first two months free (https://littlebird.ai/pricing ). The "personal-view version" of G6 is **already covered**. What remains uncovered is "the advisor side also confirms", "two-way commitments", and a "team-shared commitment ledger": the Team plan can only share calls and files within a project, and the page doesn't say teammates can see each other's commitments (https://littlebird.ai/teams ).
4. **[Fact] UK universities have institutionalized "student writes the record → advisor reviews and confirms → agreed actions and outstanding actions from the last meeting are listed", and non-AI systems are already running it.** Examples: Loughborough's Co-Tutor (records "actions arising from this meeting or that are still outstanding from previous meetings" and lets the student choose which tutor approves), Surrey Self-Service (monthly, submitted to the main supervisor, "Agreed targets" must be listed), and Haplo Graduate Education Manager ("Over 650 Global Research Organisations"). **This shows that G6's workflow is a real institutional need**, but it is also G6's direct substitute. The only parts AI can add are "auto-drafting from the meeting" and "evidence attachment" [Inference].
5. **[Fact] No public evidence of a comparable institutional requirement was found in Singapore.** The target university's SBS page only says the TAC meets in months 9, 30, and 42 (university page; link removed). NUS has a per-semester Research Progress Report [Summary]. Neither university has a public rule found requiring "a record for every supervision meeting", and the target university's graduate school policies are on its intranet. **[Inference] The argument for Option B, "embed into existing institutional processes", is strong in the UK and unconfirmed in Singapore**, and since the project owner is based in Singapore, this must be verified first through the target university's intranet.
6. **[Fact] Cross-meeting tracking (G11) is now fully covered.** Fellow can carry incomplete items forward per series with Always / Never / Ask me (https://help.fellow.ai/en/articles/3945044-carry-incomplete-items-forward ); ZoomMate supports recurring automations such as "weekly action items" (https://www.zoom.com/en/products/ai-assistant/ ); Feishu's "Meeting Digest" generates an "action item report" based on "the past week's smart minutes content". The exception is Teams Facilitator: its tasks are bound to a single meeting instance, and the official user documentation doesn't describe carrying items across meetings (https://support.microsoft.com/en-us/office/use-facilitator-in-microsoft-teams-meetings-37657f91-39b5-40eb-9421-45141e3ce9f6 ).
7. **[Inference] Window-of-opportunity judgment: for any gap that is just "feature present or absent", the catch-up pace seen this round is roughly one quarter per feature** (Fellow's claiming article 2026-10-01, ZoomMate 2026-06-01, Facilitator's Planner tracking in public preview, Littlebird launching a graduate-student page). What is genuinely still open comes down to three areas: **research semantics** (the five-value outcome, experiment evidence sources such as W&B/Git, hypothesis objects), **a mentor ledger with two-sided confirmation**, and **public evaluation**. Even for these three, Littlebird is the most likely to fill them first, because it is already in the graduate-student market. See §8.

---
## 1. Fellow

**Positioning** [Inference]: A meeting management tool for managers' 1:1s and team meetings, which added an AI note-taker in 2025–2026. It is the most direct competitor for G4, G6, and G11.

| # | Capability | Supported? | Evidence (original text) | Evidence URL | Access date |
|---|---|---|---|---|---|
| F1 | Shared 1:1 agenda | **Supported** [Fact] | "Both attendees can contribute to the meeting agenda, talking points, and action items ahead of time." | https://fellow.ai/use-cases/one-on-one-meetings | at the time of writing |
| F2 | Private 1:1 notes | **Supported** [Fact] | Private notes are "kept private between you and your direct report"; the help center also has a Private Notes article | Same as above; https://help.fellow.ai/en/articles/4274961-private-notes | at the time of writing |
| F3 | 1:1 templates | **Supported** [Fact] | "500+ pre-built meeting templates"; templates such as "1-on-1 with Direct Report" exist | https://fellow.ai/use-cases/one-on-one-meetings ; https://fellow.ai/meeting-templates/one-on-one-meetings-with-your-manager (search result, not opened) [Summary] | at the time of writing |
| F4 | Carry incomplete items across meetings | **Supported, configurable** [Fact] | Each series can be set to "Always / Never / Ask me", with talking points and action items configured separately; the "Linked copies" option means that checking off a carried-over item also checks off the same item in the historical notes; carry-over is one-time: "if you uncheck something later, it won't be reflected retroactively" | https://help.fellow.ai/en/articles/3945044-carry-incomplete-items-forward | at the time of writing |
| F5 | Pre-meeting brief | **Supported (Business plan and above only)** [Fact] | The brief "is generated solely from the last meeting's recording", and its content is the previous meeting's summary plus "key follow-up points"; **it only looks at the last meeting**, not across multiple meetings | https://help.fellow.ai/en/articles/9773836-meeting-briefs | at the time of writing |
| F6 | Multiple owners | **Supported** [Fact] | Two modes: each person completes their own share (shown as "2/5"), or the item closes once any one person completes it; **items with multiple owners cannot be synced to integrations such as Asana and Linear** | https://help.fellow.ai/en/articles/4144380-action-item-page ; https://fellow.ai/features/action-items | at the time of writing |
| F7 | Assign to non-attendees | **Supported** [Fact] | Anyone in the workspace can be searched for and assigned; the avatar is shown with a dashed border | https://help.fellow.ai/en/articles/4144380-action-item-page | at the time of writing |
| F8 | **Assignee confirmation / claiming** | **Supported (AI-suggested action items only)** [Fact] | "any assignee can accept or dismiss it"; unaccepted suggestions are "not in the inbox, not synced, not carried into the next meeting" and disappear from view after 30 days; "Editing the text or due date does not accept it"; Auto-accept is off by default | https://help.fellow.ai/en/articles/17299858-ai-suggested-action-items (page dated 2026-10-01) | at the time of writing |
| F9 | **Declining** | **Supported, but dismissing = permanent deletion** [Fact] | "Dismissed action items are permanently deleted from Fellow and cannot be recovered." The page **does not show** a dismissal reason or any notification to the organizer | Same as above | at the time of writing |
| F10 | Rescheduling (negotiating the due date) | **Partial** [Fact] | The assignee can change the due date, but changing it does not count as accepting; the page **does not show** a negotiation flow of "propose a new date → organizer confirms" | Same as above | at the time of writing |
| F11 | Status values | complete, archived ("won't do"), AI-suggested state (not accepted) [Fact] | Archived items "don't carry forward or count as incomplete" and retain "historical record and context" | https://help.fellow.ai/en/articles/4144380-action-item-page | at the time of writing |
| F12 | Outcome/evidence field | **Not seen** [Fact: not mentioned on the pages] | Neither the feature page nor the action-item page has outcome, evidence, or linked-artifact fields | https://fellow.ai/features/action-items | at the time of writing |
| F13 | GitHub sync | **Supported, via Zapier** [Fact] | Both directions are determined by the Zapier trigger: in Fellow, "every new action item assigned in a meeting instantly opens an issue"; a newly created or updated issue in GitHub becomes a Fellow action item; "any addition or status change moves across systems in real time". The page **does not explain** close semantics, labels, or comments; the help center's integration directory **has no dedicated GitHub article** (it has Jira, Linear, Asana, Zapier, MCP) | https://fellow.ai/integrations/github ; https://help.fellow.ai/en/collections/2485468-integrations | at the time of writing |
| F14 | MCP / general assistant integration | **Supported** [Fact] | Official Claude connector, ChatGPT plugin, Cursor, Copilot; read-only tools include `get_action_items`, `get_meeting_transcript`, `search_meetings`, etc., while write tools cover only the agenda | https://help.fellow.ai/en/articles/12622641-fellow-s-mcp-server | at the time of writing |
| F15 | View others' action items | **Supported (only in notes you have access to)** [Fact] | "You can only see action items assigned to others in notes you have access to." The series view shows the action items of the whole series | https://help.fellow.ai/en/articles/6698535-view-action-items-assigned-to-others | at the time of writing |
| F16 | In-person meetings | **Supported** [Fact, title level] | The help center has articles such as "AI Meeting Note Taker for In-Person Meetings" and "Mobile botless recording" (not opened one by one) | https://help.fellow.ai/en/collections/8082336-fellow-ai | at the time of writing |
| F17 | Chinese | **Transcription supports "Chinese"** [Fact] | Supports 100 languages; the list includes "Chinese", with no distinction between Mandarin and Cantonese; the page **does not mention** mixed Chinese-English speech within one meeting or the language of the minutes | https://help.fellow.ai/en/articles/8514401-supported-languages-for-ai-note-taker | at the time of writing |
| F18 | Education/academic plan | **Not seen** [Fact: not listed on the pricing page] | Only a startup program, "up to 25% off the first year"; a third-party aggregator site says "Discount… for teachers, students or non-profits: No" [Summary] | https://fellow.ai/pricing ; https://subscribed.fyi/fellow//deals | at the time of writing |
| F19 | Pricing | [Fact] | Free (5 AI notes lifetime); Team $7 (billed annually) / $11 (billed monthly); Business $15/$23; Enterprise $25 (minimum 10 users), all per user per month | https://fellow.ai/pricing | at the time of writing |
| F20 | Evidence snippet (action item linked to the original sentence or timestamp) | **Not seen** [Fact: not mentioned in the AI-suggestion article] | The AI-suggestion article does not mention transcript links or timestamps | https://help.fellow.ai/en/articles/17299858-ai-suggested-action-items | at the time of writing |

**Fellow summary** [Inference]:
- **Fellow has the skeleton of G4, G11, and G6**: claiming, dismissing, carry-over, 1:1s, multiple owners, and external integrations.
- What it **lacks**: a trace and reason for dismissals, an outcome or evidence field, a pre-meeting brief across multiple meetings, evidence links from action items to the original sentence (not seen on the pages), and academic pricing.
- Its context is "manager and direct report", not "advisor and student". This difference is at the "for whom" level, and Fellow could cover it by changing a template [Inference].

---
## 2. Littlebird

| # | Capability | Supported? | Evidence (original text) | Evidence URL | Access date |
|---|---|---|---|---|---|
| L1 | Promise tracker: whose promises it tracks | **By default only your own** [Fact] | "tuned to yours, the things you said you'd do"; "If you want to track what others owe you, that works too: just say so in the prompt." | https://littlebird.ai/routines/promise-tracker | at the time of writing |
| L2 | Three states | **Supported** [Fact] | "promises kept, promises in progress, and promises that need a rescue note before the weekend" | Same as above | at the time of writing |
| L3 | Outcome reconciliation (evidence) | **Supported; context includes meetings, email, calendar, and screen** (v1.1 correction: the old heading "evidence sources are email and documents" was inaccurate) [Fact] | "Littlebird already has the context: your meetings, your inbox, your calendar, and what was on your screen"; "goes through the week's meetings, extracts the commitments you made"; "checks each one against what actually happened", with examples "the email that went out, the document that shipped". The page **does not say** it uses statements in **later** meetings to determine status | Same as above | at the time of writing |
| L4 | Soft-commitment filtering | **Supported** [Fact] | "Vague maybes are left alone unless you ask for them." | Same as above | at the time of writing |
| L5 | Links a commitment to its source sentence or timestamp | **Not seen** [Fact: not mentioned on the page] | — | Same as above | at the time of writing |
| L6 | Run cadence | Every Friday at 16:00 by default, days can be added; automatically pauses if reports go unread for a long time [Fact] | — | Same as above | at the time of writing |
| L7 | Whether the Team plan can share promises | **Not seen** [Fact: not mentioned on the page] | The Team plan is "From $17" per seat per month and includes "Shared projects, chats, routines and skills"; to share a call, you must "Add any call to a shared project"; admins "can't open anyone's chats, meeting notes or memory". **The page does not say team members can see each other's promises** | https://littlebird.ai/teams ; https://littlebird.ai/pricing | at the time of writing |
| L8 | Student pricing | **Supported** [Fact] | "Students get Plus for $15 a month, billed monthly, and the first two months are free"; the offer lasts until graduation, up to 4 years; apply in the app with a school email and student ID | https://littlebird.ai/pricing | at the time of writing |
| L9 | Targets academia | **Yes, with a dedicated page** [Fact] | The Knowledge & Education page says "Researchers, academics, students" and offers routines such as Research Brief Compiler and Academic Monitor; the graduate student page says "takes notes in advisor meetings", "lists what you promised your advisor", the pre-meeting brief includes "what you committed to, the feedback still open", and it can also draft "the email to your committee" | https://littlebird.ai/use-cases/knowledge-and-education ; https://littlebird.ai/for/graduate-students | at the time of writing |
| L10 | Mixed Chinese-English speech | **Supported** [Fact] | "Choose Multilingual in Settings and it follows a conversation that switches between them"; supports "more than 30 languages" (the page does not list the specific languages) | https://littlebird.ai/use-cases/knowledge-and-education ; https://littlebird.ai/ | at the time of writing |
| L11 | In-person meetings | **Supported (iPhone app)** [Fact] | The graduate student page says "Notes can also be taken in person with the iPhone app" (paraphrased) | https://littlebird.ai/for/graduate-students | at the time of writing |
| L12 | Bot-free recording | **Yes** [Fact] | "takes notes through its desktop app, so no bot joins the call"; it reminds users to obtain consent | https://littlebird.ai/ | at the time of writing |
| L13 | Confirmation from the advisor's side | **Not seen** [Fact: not mentioned on the page] | — | — | at the time of writing |

**Littlebird summary** [Inference]:
- Littlebird is **the most dangerous competitor for G5 and G6**, and more dangerous than Fellow, for three reasons: it is already in the graduate student market, it has student pricing, and its "promise → check what actually happened" structure is isomorphic to G5.
- Its gaps are in three places. First, **its reconciliation examples are emails and documents (the context does include meetings, but the page does not say it uses later meeting statements to determine status), not experiment artifacts** (W&B runs, commits, logs). Second, it has a **single-person perspective**: the advisor neither confirms nor can see anything. Third, it has **no research result values**; its three states describe "whether it was fulfilled," not "what the experiment's conclusion is."

---
## 3. Zoom AI Companion 3.0 / ZoomMate, and Microsoft Teams Facilitator

### 3.1 Zoom

| # | Capability | Supported? | Evidence | Evidence URL | Access date |
|---|---|---|---|---|---|
| Z1 | ZoomMate project agent | **Supported (one official sentence)** [Fact] | "Set up a ZoomMate project agent to track progress, share updates, and manage tasks." | https://www.zoom.com/en/products/ai-assistant/ | at the time of writing |
| Z2 | Original "track cross-meeting projects" sentence | **Not found** [Fact] | Neither the official AI assistant page nor the ZoomMate introduction blog post (2026-06-01) contains this sentence; the "to be verified" conclusion for V10 from the first round stands | Same as above; https://www.zoom.com/en/blog/what-is-zoommate/ | at the time of writing |
| Z3 | Scheduled automation | **Supported** [Fact] | "Schedule recurring automations like daily briefings, weekly action items, or meeting prep summaries." | https://www.zoom.com/en/products/ai-assistant/ | at the time of writing |
| Z4 | Assigning tasks | **Supported** [Fact] | "It can assign tasks, initiate multi-step workflows, update systems of record." | https://www.zoom.com/en/blog/what-is-zoommate/ | at the time of writing |
| Z5 | Assignee confirmation | **Not found** [Fact] | The closest item is that workflows "can be configured with approval checkpoints", which is process approval, not the assignee accepting the task | Same as above | at the time of writing |
| Z6 | Project history across a meeting series | **Supported** [Fact] (v1.1: original page opened) | "you can quickly revisit previous discussions, unresolved action items, and open questions"; "A project team might automatically generate status updates and assign tasks based on decisions"; "either per-meeting or across a recurring series"; "availability may vary by customer type, region, and industry vertical at launch". **The earlier summary's claim about "identifying unclosed Jira issues" does not appear on this page; it remains to be verified** | https://www.zoom.com/en/blog/zoommate-getting-started/ | at the time of writing |
| Z7 | In-person meetings | **Supported** [Fact] | "My Notes captures insights from your conversations — on Zoom, in-person, on mobile, and across third-party platforms" | https://www.zoom.com/en/products/ai-assistant/ | at the time of writing |
| Z8 | Integrations | Jira, Salesforce, Google Drive, OneDrive, etc. [Fact] | The product page lists Jira; the blog additionally lists ServiceNow, Confluence, Box; **Asana appears on neither page** | Same as above | at the time of writing |
| Z9 | Regions and pricing | Launching first in North America; metered by AI Credits [Fact/Summary] | "availability may vary by customer type, region, and industry vertical at launch"; "available for purchase with included AI Credits"; the "North America" first-launch claim comes from a summary of the press release | https://www.zoom.com/en/blog/what-is-zoommate/ ; https://investors.zoom.us/news-releases/news-release-details/zoom-launches-zoommate-first-ai-teammate-built-turn (not opened) | at the time of writing |
| Z10 | Chinese | **Meeting summaries may support Chinese (preview)** [Summary] | A Zoom press release says meeting summaries cover 36 languages (preview), and a third-party page lists Chinese among them; language support for ZoomMate itself was **not found** | https://news.zoom.com/breaking-down-boundaries-zoom-ai-companion-expands-language-support-across-its-platform-to-enable-better-global-collaboration-and-productivity/ (not opened) | at the time of writing |
### 3.2 Microsoft Teams Facilitator

| # | Capability | Supported? | Evidence | Evidence URL | Access date |
|---|---|---|---|---|---|
| T1 | Planner task tracking | **Public preview** [Fact] | "The following Facilitator capabilities are currently in public preview: Task tracking integration with Planner"; users must join the Teams Public preview to use it | https://learn.microsoft.com/en-us/microsoftteams/facilitator-teams (ms.date 2026-08-13) | at the time of writing |
| T2 | Task sync method | [Fact] | "Tasks created by Facilitator will automatically sync to a meeting plan associated with that meeting instance"; captured tasks must be accepted via "Accept to sync" in Follow-up tasks. **The page does not say who clicks accept** (possibly the organizer, possibly any attendee; to be verified) | https://support.microsoft.com/en-us/office/use-facilitator-in-microsoft-teams-meetings-37657f91-39b5-40eb-9421-45141e3ce9f6 | at the time of writing |
| T3 | Carry-over across meetings | **Not found** [Fact] | Tasks are bound to "that meeting instance"; the page does not describe carrying them into the next meeting | Same as above | at the time of writing |
| T4 | In-person capture | **Supported (GA)** [Fact] | GA capabilities include "Mobile capture of ad-hoc discussions and action items"; the user docs say "Instantly capture, transcribe, and organize in-person meeting notes"; the Teams Rooms experience is also GA | Learn page; support page | at the time of writing |
| T5 | Teams Rooms speakers | **Attributed to the room** [Summary: third-party blog] | Without voice recognition, "anything said in the room is attributed to the room, not the individual speakers" | https://www.aguidetocloud.com/blog/microsoft-365-facilitator-agent/ (2026-06-23, last verified 2026-09-29) | at the time of writing |
| T6 | Language restriction | **Single language** [Fact] | A language must be selected at the start of the meeting; "The language selected must match the spoken language during the meeting, or notes aren't generated"; "only support meetings where a single language is spoken"; the Copilot language list includes Simplified and Traditional Chinese | Learn page; https://support.microsoft.com/office/supported-languages-for-microsoft-copilot-94518d61-644b-4118-9492-617eea4801d8 | at the time of writing |
| T7 | Planner Agent language exception | [Summary] | Facilitator supports Arabic, but "the Planner Agent excludes Arabic and Hebrew" | aguidetocloud blog | at the time of writing |
| T8 | 1:1 and external meetings | **Not supported** [Fact] | "Facilitator isn't supported in 1:1 chats, group chats, or external chats and meetings" | Learn page | at the time of writing |
| T9 | Licensing | Requires a Microsoft Copilot license [Fact] | "Only licensed users can initiate Facilitator" | Learn page | at the time of writing |
| T10 | Assignee confirmation | **Not found** [Fact] | The third-party blog says "review them, assign owners yourself", i.e., a human assigns owners rather than assignees claiming tasks [Summary] | aguidetocloud blog | at the time of writing |

**Zoom and Teams summary** [Inference]:
- Both are moving toward a "project-level agent", but **neither has assignee claiming or an outcome field**.
- Teams' single-language restriction and "no external meetings" confirm the "constraint-type gap" from the first round.
- The first-round W7 claim that "Teams action items are only suggestions" now needs rewriting: Facilitator already has "Accept to sync" and Planner sync, but it is in preview, and it is unclear who does the accepting.

---

## 4. Chinese Vendors: Tongyi Tingwu, Feishu, Tencent Meeting

| # | Product · Capability | Supported? | Evidence | Evidence URL | Access date |
|---|---|---|---|---|---|
| C1 | Tingwu · hot words (API) | **Supported** [Fact] | "目前仅支持中文和英文热词识别" (currently only Chinese and English hot-word recognition is supported); up to 10 vocabulary lists per user, up to 300 hot words per list, "每个热词长度不超过10个字符" (each hot word no longer than 10 characters), weight range [-6,5]. **Note**: the version in the search summary says "Chinese only", which is inconsistent with the original page; the original page takes precedence | https://help.aliyun.com/document_detail/2639682.html | at the time of writing |
| C2 | Tingwu · hot words (consumer UI) | **Not found** [Fact: not mentioned on the official homepage] | The official homepage only mentions action items and chapter overviews | https://tingwu.aliyun.com/ | at the time of writing |
| C3 | Tingwu · multi-file Q&A | **Supported (2024 report)** [Fact, media] | "Across records, let 'Xiaowu' scan hundreds of audio and video files to summarize and answer questions together"; "up to 50 files can be uploaded at a time"; answers "mark the cited sources and the corresponding timestamps". **Its status in 2026 is not confirmed on the official help pages** | https://www.qbitai.com/2024/03/129271.html (2024-03-19) | at the time of writing |
| C4 | Tingwu · universities | **Offered as a giveaway in 2024** [Fact, media] | Verification with an edu.cn email gives "500 hours of transcription time directly" (mainland China universities only; current status to be verified) | Same as above | at the time of writing |
| C5 | Feishu · Meeting Express | **Supported** [Fact] | "Meeting Express can draw on your smart minutes from the past week" to "generate a key-point review and an action-item report"; frequency not stated | https://www.feishu.cn/content/article/7577317993749269689 | at the time of writing |
| C6 | Feishu · enterprise information recognition | **Supported** [Fact] | "Rare characters in colleagues' names, project names, etc. can also be recognized" | Same as above | at the time of writing |
| C7 | Feishu · action-item traceback to source | **Supported** [Fact] | "Accurately identifies action items and supports tracing back to the original text"; "supports tracing action items back to the meeting's original text"; another article says "every key point is linked to a Feishu Minutes timestamp; click to jump to the corresponding meeting audio/video clip" | Same as above; https://www.feishu.cn/content/article/7600354912756681687 | at the time of writing |
| C8 | Feishu · owner | **Auto-detected + manual addition** [Fact] | "Automatically summarizes action items and owners from the meeting content"; "if the deadline or owner is not specified in the meeting, it can be added manually" | Both articles above | at the time of writing |
| C9 | Feishu · convert to task and reminders | **Supported** [Fact] | "A 'Create task' button links directly to Feishu Tasks"; "the owner automatically receives a Feishu message reminder"; "all attendees with permission can view task status on the minutes page" | https://www.feishu.cn/content/article/7600354912756681687 | at the time of writing |
| C10 | Feishu · assignee claims or declines | **Not found** [Fact: neither article mentions it] | The owner only "receives a reminder"; the pages do not mention confirming or declining | Same as above | at the time of writing |
| C11 | Feishu · mixed Chinese-English | **Supported** [Fact] | "In discussions mixing Chinese and English, the transcript recognizes each part in its original language" | https://www.feishu.cn/content/article/7577317993749269689 | at the time of writing |
| C12 | Tencent Meeting · AI action items | **Supported** [Fact] | "It can also organize meeting action items and clarify the work to be followed up" | https://meeting.tencent.com/ai/ | at the time of writing |
| C13 | Tencent Meeting · action-item owner and traceback | **Not found** (official page) / **to be verified** | The official AI page does not mention owners or traceback; the first-round Zhihu comparison says "action-item extraction does not identify owners and does not support jumping back to the source", but that is only a summary and the original page returned 403; the third-party ai-bot.cn claims owners and deadlines exist [Summary] | https://meeting.tencent.com/ai/ ; https://ai-bot.cn/sites/8649.html | at the time of writing |
| C14 | Tencent Meeting · Ask Yuanbao | **Supports single-meeting follow-up questions** [Fact, media] | "Follow-up questions after the meeting are the more everyday use of 'Ask Yuanbao'"; answers "mark which content comes from the recording and which comes from web search"; the full article covers **only a single meeting**, with no cross-meeting use | https://www.ifanr.com/1660770 (2026-04-02) | at the time of writing |

**Chinese vendor summary** [Inference]:
- Traceback (G2), weekly roll-ups (the weak versions of G10 and G11), and terminology recognition (the enterprise-grade version of G8) already exist in the Chinese market.
- **Claiming or declining, outcome or evidence fields, and a cross-meeting commitment-status ledger** are not found in any of the three.
- Tencent Meeting's "action-item traceback" still needs a real-meeting test by a project owner; it cannot be resolved at the documentation level.

---
## 5. The "Switch Nothing" Alternative: ChatGPT Record, Claude, and Other General-Purpose Assistants

| # | Capability | Supported? | Evidence | Evidence URL | Access date |
|---|---|---|---|---|---|
| A1 | Where ChatGPT Record is available | Plus, Pro, Business, Enterprise, Edu; **macOS desktop app only** [Summary] | From a help center search snippet: "only available for the macOS desktop app". The original page returned 403; to be verified | https://help.openai.com/en/articles/11487532-chatgpt-record (403) | at the time of writing |
| A2 | Action item output | **Supported** [Summary] | The help center snippet says it saves "personalized summaries with action items"; tl;dv (a competing vendor) writes "suggested action items" | Same as above; https://tldv.io/blog/chatgpt-record-mode-for-meetings/ (2026-04-07) | at the time of writing |
| A3 | Speaker separation and owners | **Weak** [Summary, competing vendor, possibly outdated] | tl;dv writes "can't tag speakers, so action items often lack ownership", and at launch "no speaker diarisation" | tl;dv, same as above | at the time of writing |
| A4 | Language | "works best in English today" [Summary] | Help center search snippet | help.openai.com (403) | at the time of writing |
| A5 | Duration per session | Up to 120 minutes [Summary, competing vendor] | "Each session can run up to 120 minutes." | tl;dv, same as above | at the time of writing |
| A6 | Native meeting recording in Claude | **Not found** [Fact: the Claude release notes do not mention meeting recording] | The only "record" in the release notes is the Chrome extension's "Record a workflow", which is not meeting recording | https://support.claude.com/en/articles/12138966-release-notes | at the time of writing |
| A7 | Claude reading data from meeting tools | **Supported (via MCP connector)** [Fact] | Fellow is an official connector in the Claude directory and exposes `get_action_items` and `get_meeting_transcript`; the Granola MCP launched 2026-02-04 and can only query notes the user owns [Summary] | https://help.fellow.ai/en/articles/12622641-fellow-s-mcp-server ; https://www.granola.ai/blog/granola-mcp (not opened) | at the time of writing |
| A8 | Paste minutes → extract action items | **Can do it** [Inference] | This is a basic capability of general-purpose LLMs and needs no dedicated feature; **no public evaluation exists** that reports its miss rate and fabrication rate on mixed Chinese-English speech and soft commitments | — | — |

**Summary** [Inference]:
- For G10 (weekly report) and G12 (one-off retrospective Q&A), "ChatGPT or Claude plus pasting" is already a sufficient alternative.
- Their structural gaps are threefold: **no persistent ledger, no assignee loop, no outcome backfill**. Every session starts from zero, which is exactly complementary to BriefPilot's "state" value.
- However, through MCP, Claude can read action items directly from Fellow or Granola. **A "ledger in Fellow, reasoning in Claude" setup is already feasible**, so prepare a good answer to this point for interviews.
- The comparison experiment suggested in the first review round (06 §Action 1) should include "Claude + pasted minutes" as the baseline group.

---

## 6. Fabric, and Products Built Specifically for Supervisor Meetings and Group Meetings

| # | Subject · capability | Supported? | Evidence | Evidence URL | Access date |
|---|---|---|---|---|---|
| P1 | Fabric · academic labs page | **Marketing page exists** [Fact] | The agent "extracts the action items, and creates tasks for each lab member with deadlines" from supervision meeting recordings; "A decision log tracking analytical choices, methodological pivots, and design decisions"; PI weekly digest "so the PI stays current without scheduling another meeting" | https://fabric.so/teams/academic-labs | at the time of writing |
| P2 | Fabric · real customers | **Not found** [Fact] | The academic page **names no university or lab and carries no signed testimonials**; its only social proof is "4.6" and "3.5K+ app ratings"; the Teams page lists no customers either; `/universities` returns 404 | Same as above; https://fabric.so/teams | at the time of writing |
| P3 | Fabric · commitment or outcome fields | **Not found** [Fact] | Only "Tasks with owners, priority, due dates, and reminders" | https://fabric.so/teams | at the time of writing |
| P4 | Supervisor Meeting Brief Generator (Chrome extension) | **Built specifically for supervisor 1-on-1s** [Fact] | Each action item has an owner ("me / supervisor / both"), a target date, and a status; a "From last meeting" panel shows open items and "decisions flagged for revisit"; "No AI" and "No server", with all data stored in the local browser; **0 ratings**, v1.0.0, updated 2026-05-30 | https://chromewebstore.google.com/detail/fmibimgfmoaogdajeoeedledhejppgll | at the time of writing |
| P5 | Supervisor-meeting or group-meeting products on Product Hunt | **Not found** [Fact: within the search scope] | Searches returned only general meeting tools and Littlebird | WebSearch | at the time of writing |
| P6 | Open source on GitHub | **No mature product** [Fact] | The GitHub API search for "supervisor meeting phd" returns only 2 repositories, the highest with 1 star, one of which is a personal notes repository; "lab meeting notes action items" returns 3, the highest with 1 star; "advisor meeting student tracker" returns only 1 (a 2015 course assignment) | https://api.github.com/search/repositories?q=supervisor+meeting+phd ; …?q=lab+meeting+notes+action+items ; …?q=advisor+meeting+student+tracker | at the time of writing |
| P7 | Manual lab workflow (evidence of need) | [Fact] | Rashid Lab handbook: at the start of the meeting, "Review last week's action items"; at the end, "Read back action items" and "confirm assignees and due dates"; notes are kept in GitHub Discussions, with a permanent record also left under `meeting-notes/2026/` in the repository | https://rashidlab.github.io/lab-handbook/policies/meeting-leader-guide.html | at the time of writing |

**Summary** [Inference]:
- Fabric is still only a marketing page with **no verifiable academic customers**, so its threat level is revised down from "medium" to "low to medium".
- The only dedicated supervisor-meeting tool is a no-AI extension with 0 ratings. **As a standalone product, the category of "AI-driven commitment ledger for supervisor meetings or group meetings" is indeed unoccupied**. But the nearest rival is not a dedicated product; it is Littlebird's graduate student page (§2).
- Rashid Lab's "read back action items, confirm owners and due dates" is the **manual version** of G4 in a lab, which shows that this behavior genuinely exists. It also shows that a verbal confirmation takes only 30 seconds, so a tool has to prove it is better than saying it aloud [Assumption · to be verified].

---
## 7. Academic Supervision Record Systems (Institutional Evidence for the G6 "Supervisor Confirmation Gate")

| # | Institution · System | Who writes | Supervisor confirmation | Carry-over actions | Evidence URL | Access date |
|---|---|---|---|---|---|---|
| U1 | **Haplo Graduate Education Manager** (part of Cayuse) | Both doctoral students and supervisors can record [Fact] | **Not seen** [Fact: not mentioned on the page] | Not seen; the page says "Track where supervision meetings aren't happening" and "Shared with the entire supervisory team" | https://www.haplo.com/graduate-education-manager (named customers: Westminster, UEL, Canterbury Christ Church, Derby; "Over 650 Global Research Organisations") | at the time of writing |
| U2 | **LJMU eDoc** | Student (PGR) [Summary] | **The main supervisor can edit, return or confirm**; once confirmed it becomes the official record; the supervisor receives a "Review and approve meeting notes" task [Summary] | The student enters "agreed action points" [Summary] | Both PDFs now return 404: https://cd-prod.ljmu.ac.uk/-/media/files/ljmu/doctoral-academy/edoc-guidance-for-completing-a-meeting-record.pdf ; …/edocquickstartguideforpgrsv2-september-2021-2.pdf | at the time of writing |
| U3 | **Loughborough Co-Tutor** | Student [Fact] | **Yes**: when recording, the student selects "Which of your supervisors will be approving your meeting notes"; after the supervisor reviews, the student receives an email with comments [Fact] | **Yes**: "actions arising from this meeting or that are still outstanding from previous meetings" [Fact]; monthly | https://lboro.ac.uk/students/handbook/starting/attendance/co-tutor-supervisory/ | at the time of writing |
| U4 | **Surrey Self-Service · Monthly Supervisions** | Student [Fact] | Submitted to the "Principal Supervisor or Co-Supervisor" [Fact] | "Agreed targets should be listed in a table"; one stated purpose is "Forming a repository of key decisions taken, which will help with writing the thesis" [Fact]; at least once a month, with a submission deadline | https://my.surrey.ac.uk/sites/default/files/2025-04/how-to-log-monthly-supervision-meeting.docx | at the time of writing |
| U5 | City St George's (RaP) | Student: "record notes and action points of all meetings" [Summary] | Not verified | — | https://www.citystgeorges.ac.uk/__data/assets/pdf_file/0007/841318/Roles-and-Responsibilities-July-2025.pdf (not opened) | at the time of writing |
| U6 | Exeter MyPGR | Full-time students hold 10 meetings per year, which must be recorded in MyPGR [Summary] | Not verified | — | Search snippet | at the time of writing |
| U7 | **The target university (Singapore)** | **No public page found** describing a record-keeping system for individual supervision meetings [Fact: not seen on public pages] | — | The SBS TAC meets in the "9th, 30th and 42nd month" [Fact]; the graduate college's policies and templates are at "university intranet → … → Graduate College", on the intranet [Fact] | (university page; link removed); (university page; link removed) | at the time of writing |
| U8 | **NUS** | A Research Progress Report is submitted each semester (work summary plus self-assessment) via the NUS Education Records System [Summary] | Not verified | Public pages **show no** record-keeping system for individual supervision meetings | https://nusgs.nus.edu.sg/research-progress-report/ (page body could not be retrieved); the Psychology department handbook PDF (2026-09-30 edition) could not be parsed | at the time of writing |

**Summary**:
- [Fact] At least 3 verifiable UK systems (Co-Tutor, Surrey, Haplo) and 1 summary-level system (LJMU) have made "student writes, supervisor reviews, action items tracked across months" a **mandatory process**. The first-round W8 problem ("neither piece of evidence could be opened") has been filled in with Loughborough and Surrey.
- [Inference] This cuts both ways for G6. The upside: the need is institutionally recognized, and users are already used to "supervisor confirmation". The downside: the university system already occupies the confirmation step, so BriefPilot can only be an "upstream drafter" that automatically formats meeting content into the university's form layout, after which the student pastes or submits it. It should not build another confirmation gate.
- [Inference] The situation in Singapore is unverified. The public policies of the target university and NUS only go as far as the TAC and semester reports, and **show no institutional pressure to keep a record of every group meeting or 1-on-1**. If the target university's intranet has none either, G6 lacks institutional leverage in the project owner's local context, leaving only demand at the level of "personal habit".
- [Assumption · to be verified] The project owner can log in to the target university's student intranet and check the Graduate College's Policies and Templates for a supervision log or meeting record template. This takes about 10 minutes and is the **highest priority**.

---
## 8. Re-assessing How Open Candidate Differentiators G2–G6 and G9–G12 Are

The assessment uses three levels:
- **Still open**: No product in this round's search scope does it publicly.
- **Partially covered**: Someone has built the core mechanism, but there are gaps in research semantics, two-sided use, or evidence.
- **Already covered**: Mainstream products publicly support it, so building it would only be "us too."

| Candidate | Round 1 confidence | This round's assessment | Key evidence | The small piece that remains | Window of opportunity [Inference] |
|---|---|---|---|---|---|
| **G2** Every commitment verifiable in 3 seconds (original sentence + speaker + timestamp; no output without a source) | High demand, medium differentiation | **Already covered (provenance) / partially open (refusal)** | Feishu "supports tracing action items back to the original meeting text," and key points carry timestamps (C7); Tongyi Tingwu Q&A carries timestamps (C3); Notion hover citations (Round 1). Fellow and Littlebird action-item pages show **no** link to the original sentence (F20, L5) | **Refusing** to output anything without a source, plus a public "unsupported rate" metric; international tools attaching the original sentence to action items | **Very short (0–3 months)**: already a Kano must-be feature, so it works only as a "passing line," not as a selling point |
| **G3** Don't guess missing fields + commitment-strength tiers | Medium | **Partially covered** | Littlebird skips "vague maybes" by default (L4); Fellow's AI suggestions take effect only after they are accepted (F8); Feishu writes "not specified… can be added manually" (C8), but does not say the field is left blank | An explicit "strength label" (commitment, suggestion, discussion, assumption) plus a **reproducible recall evaluation**; missing fields **left blank** rather than filled by default | Short (3–6 months): a single label field can close the gap; the **evaluation itself** is the more durable difference |
| **G4** The named person claims it themselves (confirm, reschedule, decline) | Medium | **Already covered (core mechanism)** ⚠️ Biggest correction this round | Fellow: "any assignee can accept or dismiss it"; unaccepted suggestions are neither synced nor carried over, and auto-accept is off by default (F8, 2026-10-01); Teams has "Accept to sync" (T2, preview) | ① **Recording the dismissal and its reason**, fed back to the organizer (Fellow deletes permanently, F9); ② "reschedule" as a negotiation flow (F10); ③ in offline single-microphone scenarios, using claiming in place of speaker identification (Fellow's offline capability has not been verified article by article) | **Closed**; the remaining details can only be components of G5 and G6, not standalone selling points |
| **G5** Commitment → outcome → evidence loop (five-value outcome + run, commit, log links) | Medium | **Partially covered** | Littlebird checks "what actually happened," with emails and documents as evidence, in three states (L2, L3); Fellow has complete and "won't do" archiving (F11) and syncs GitHub status via Zapier (F13); ZoomMate can identify unclosed Jira issues (Z6, summary) | **Research outcome values** (supported, refuted, inconclusive, not run, superseded); **experiment artifacts as evidence** (W&B run, commit, config, logs); states such as "not run" and "superseded" that are neither completed nor abandoned | **Medium (6–12 months)**: big vendors structurally won't do research semantics; but Littlebird is already in the graduate-student market, and connecting a GitHub or W&B data source would bring it close, so **it is the top risk**. In addition, the five-value outcome itself is still [Assumption · to be validated] (Round 1 W10) |
| **G6** Advisor one-on-one two-way commitment ledger + advisor confirmation gate | Medium | **Partially covered (components exist separately)** | Littlebird's graduate-student page "lists what you promised your advisor," and its pre-meeting brief includes unfinished commitments and feedback (L9); Fellow's one-on-ones have a shared agenda, private notes, and automatic carry-over (F1–F4); UK university systems have "student writes, advisor reviews, outstanding actions" (U3, U4); the extension Supervisor Meeting Brief supports "me / supervisor / both" (P4) | **The combination of these pieces**: AI drafts from the meeting → **advisor-side confirmation** → two-way commitments (what the advisor owes the student is also recorded) → export to the university form format. No single product does all of this. For **commitments the advisor owes the student**, there is still no user evidence (Round 1 self-assessment) | **Medium (6–12 months)**, but in Singapore the **demand leverage is unconfirmed** (U7, U8). Littlebird adding "share with advisor for confirmation" would be a small iteration [Inference] |
| **G9** Research object model (hypotheses, experiments, success criteria, advisor suggestions, reviewer comments) | Medium-low | **Still open (demand evidence is also weak)** | Fabric has a "decision log tracking analytical choices, methodological pivots," but it is only a marketing page with no customers (P1, P2); Littlebird has a Research Brief "what's known and what's still open" (L9) | Hypotheses and experiments as first-class objects, with "tests" and "grounded in" relationships between them | Long (12+ months): nobody does it, and **the reason may be that nobody wants it**. An open space is not the same as an opportunity; user evidence is needed first |
| **G10** Embedding into existing weekly-report slots ("done / problems / plan") | Medium-high demand, medium-low differentiation | **Already covered (general capability)** | Feishu meeting digests produce weekly "key-point reviews and action-item reports" (C5); ZoomMate "weekly action items" (Z3); Littlebird weekly routines and drafting committee emails (L6, L9); Fabric PI weekly digest (P1); pasting into ChatGPT or Claude is enough (A8) | Only "producing output in a particular lab's fixed template" remains, which is configuration, not differentiation | **Closed**; can serve as a "bonus output" in the demo, not as a selling point |
| **G11** Cross-meeting commitment tracking (binary version) | High demand, low differentiation | **Already covered** | Fellow's Always / Never / Ask me carry-over (F4) and pre-meeting brief (F5); ZoomMate scheduled automations (Z3); Feishu meeting digests (C5); Littlebird weekly three-state tracking (L2) | Only the Teams Facilitator has a gap (T3), and Fellow's pre-meeting brief looks only at the previous meeting (F5) | **Closed**; the Round 1 conclusion of "build infrastructure only" stands |
| **G12** Decision-retrieval Q&A with provenance and the ability to refuse | Medium | **Partially covered (close to already covered)** | Tongyi Tingwu Q&A across 50 files, with citations and timestamps (C3, 2024); Fellow's Ask Fellow and MCP search (F14); Tencent Yuanbao labels its sources (C14); Fabric decision log (P1) | **Ability to refuse** ("no record found") plus **links from decisions to experiment evidence** ("why chunk=8" can be answered with the corresponding run); the latter depends on G5's data | Short to medium (3–9 months): Q&A with citations is already widespread; refusal plus evidence links can only be pitched together with G5 |
### 8.1 Overall Assessment

1. **[Inference] Of the first round's Top 4 tier (G4, G5, G6), G4 is out, and both G5 and G6 are downgraded to "partially covered."** The remaining gap in the "after the commitment" stage is no longer "some feature that nobody has built," but two things:
   - **Research semantics × evidence sources**: the five-value outcome, and W&B and Git as evidence.
   - **Two-sided × institutional formats**: supervisor confirmation, and export into the university's forms.

   Both satisfy "big vendors structurally won't do it," but **neither satisfies "small vendors can't do it"**, and the closest competitor is Littlebird.
2. **[Inference] Overall window judgment: 6–12 months, and it is the kind of window that "Littlebird could close with a single iteration."** The basis is the catch-up speed observed in this round:
   - Fellow's assignment-acceptance mechanism, 2026-10-01;
   - ZoomMate, 2026-06-01;
   - Facilitator's Planner tracking, 2026-08 documentation version, in preview;
   - Littlebird's graduate student page (launch date unknown).

   This suggests the half-life of a "feature gap" is roughly one quarter. For a 2–4 week demo, this window is **enough to ship a working piece of work**, but **not enough to support a "market gap" claim**.
3. **[Inference] When asked "why build this anyway," the narrative should shift from "others haven't done it" to "how far others have gone, where I go deeper, and here are the numbers":**
   - Acknowledge that Fellow has assignment acceptance and Littlebird has promise checking;
   - Explain that BriefPilot swaps the evidence source for "checking" to the artifacts of a computational lab (W&B, Git), and swaps "fulfilled or not" for "experiment conclusions";
   - Use a public comparative evaluation (Fellow, Feishu, Claude with pasted text, BriefPilot, all on the same mixed Chinese-English group meeting) to show higher accuracy on three kinds of samples: **soft commitments, supervisor commitments, and mixed Chinese-English** [Assumption · to be validated].
4. **[Inference] The demo scope should be narrowed accordingly:**
   - Drop the "assignment-acceptance UI" (G4), or keep only the detail of "leaving a trace when an item is dismissed";
   - Set the main line as **the research version of G5**: "last commitment → fill in the result value this time → automatically find evidence candidates from Git or W&B → a one-page pre-1:1 briefing";
   - Build G2 and G3 in as the passing baseline;
   - Build G6's "supervisor confirmation" first as a single-user feature that **exports Loughborough- or Surrey-style forms**, to avoid the cold-start problem;
   - Decide whether to build the two-sided version only after the target university's intranet has been checked.

---

## 9. Corrections to Write Back into Earlier Files

| File · Location | Original statement | Change to | Basis |
|---|---|---|---|
| 05 G4 Objection 3 | "Fellow already supports assigning or reassigning during or after the meeting, one step short of 'claiming'" | "Since 2026-10, Fellow has required the assignee to accept or dismiss AI-suggested action items; unaccepted items are not synced or carried over; G4's core mechanism is already covered" | F8 |
| 06 V6 | "The page does not mention assignee confirmation or acceptance"; judged to hold | **Overturned**: the help center article has accept and dismiss; the feature marketing page indeed doesn't say so, but the help center does | F8 |
| 05 G5 evidence "Fellow only tracks open/closed" | — | Add: there is an archived ("won't do") terminal state, as well as an AI-suggested state | F11 |
| 05 G6 Objection 3 | "Littlebird's student price of $15/month already serves the individual version" | Add: the Littlebird graduate student page explicitly says "lists what you promised your advisor," and the pre-meeting briefing includes unfulfilled commitments and feedback | L9 |
| 06 W8 | Both pieces of evidence on UK supervision systems failed to open | Loughborough Co-Tutor and Surrey opened and verified against the originals; Haplo GEM verified as "both students and supervisors can record," but **no supervisor approval seen**; LJMU is still a summary | U1–U4 |
| 06 W7 | Teams recap action items are "suggestions, not authoritative assignments" | Facilitator has "Accept to sync," plus Planner sync (preview) | T1, T2 |
| 01 China market §9 and 06 §69 | Tongyi Tingwu hotwords and multi-file Q&A to be verified | The hotword API supports Chinese and English, up to 10 word lists × 300 words, each word no more than 10 characters; for multi-file Q&A, see the 2024 QbitAI report (50 files, with timestamps); the 2026 status still needs confirmation on an official page | C1, C3 |
| 05 G12 Objection | Fabric "has claimed…" | Add: Fabric's academic page names no customers and carries no signed endorsements, and `/universities` returns 404 | P2 |

---

## 10. Still to Be Verified (by Priority)

1. **The target university's intranet**: whether the Graduate College's Policies and Templates include a template for supervision meeting records or a supervision log. The project owner must log in personally; **highest priority**, since it decides whether G6 can hold locally.
2. **Hands-on test of Fellow's free tier**: does accepting or dismissing an AI-suggested action item send a notification to an **assignee who is not the organizer**? After a dismissal, can the organizer see it? Can an action item jump back to the original sentence in the transcript? How well does it recognize mixed Chinese-English speech?
3. **Hands-on test of Littlebird's student plan** (first two months free): in a 1:1 scenario, can the promise tracker track "what my supervisor owes me"? Can a report be shared with the supervisor? Can it connect to GitHub?
4. **Tencent Meeting AI action items**: the owner field and source-text traceability, tested with real meetings.
5. **ChatGPT Record**: the help center original page returns 403; open it manually in another browser to confirm the current state of available plans, languages, and speaker differentiation (tl;dv's description may be stuck at the 2025 launch).
6. **Teams Facilitator**: who performs "Accept to sync"? Can Planner tasks carry over across recurring meeting series?
7. **LJMU eDoc**: the new URL of the current guidelines.

---
## Source List (all accessed at the time of writing)

**Fellow**
1. https://fellow.ai/features/action-items
2. https://fellow.ai/integrations/github
3. https://fellow.ai/pricing
4. https://fellow.ai/use-cases/one-on-one-meetings
5. https://help.fellow.ai/en/articles/3945044-carry-incomplete-items-forward
6. https://help.fellow.ai/en/articles/17299858-ai-suggested-action-items
7. https://help.fellow.ai/en/articles/4144380-action-item-page
8. https://help.fellow.ai/en/articles/9773836-meeting-briefs
9. https://help.fellow.ai/en/articles/8514401-supported-languages-for-ai-note-taker
10. https://help.fellow.ai/en/articles/12622641-fellow-s-mcp-server
11. https://help.fellow.ai/en/articles/6698535-view-action-items-assigned-to-others
12. https://help.fellow.ai/en/collections/3175100-meetings-notes
13. https://help.fellow.ai/en/collections/8082336-fellow-ai
14. https://help.fellow.ai/en/collections/2485468-integrations
15. https://subscribed.fyi/fellow//deals [Summary]

**Littlebird**
16. https://littlebird.ai/routines/promise-tracker
17. https://littlebird.ai/pricing
18. https://littlebird.ai/teams
19. https://littlebird.ai/
20. https://littlebird.ai/use-cases/knowledge-and-education
21. https://littlebird.ai/for/graduate-students

**Zoom and Microsoft**
22. https://www.zoom.com/en/products/ai-assistant/
23. https://www.zoom.com/en/blog/what-is-zoommate/
24. https://www.zoom.com/en/blog/zoommate-getting-started/ [Summary]
25. https://investors.zoom.us/news-releases/news-release-details/zoom-launches-zoommate-first-ai-teammate-built-turn [Summary]
26. https://news.zoom.com/breaking-down-boundaries-zoom-ai-companion-expands-language-support-across-its-platform-to-enable-better-global-collaboration-and-productivity/ [Summary]
27. https://learn.microsoft.com/en-us/microsoftteams/facilitator-teams
28. https://support.microsoft.com/en-us/office/use-facilitator-in-microsoft-teams-meetings-37657f91-39b5-40eb-9421-45141e3ce9f6
29. https://support.microsoft.com/office/supported-languages-for-microsoft-copilot-94518d61-644b-4118-9492-617eea4801d8
30. https://www.aguidetocloud.com/blog/microsoft-365-facilitator-agent/ [third-party]

**Chinese vendors**
31. https://help.aliyun.com/document_detail/2639682.html
32. https://tingwu.aliyun.com/
33. https://www.qbitai.com/2024/03/129271.html
34. https://www.feishu.cn/content/article/7577317993749269689
35. https://www.feishu.cn/content/article/7600354912756681687
36. https://meeting.tencent.com/ai/
37. https://www.ifanr.com/1660770
38. https://ai-bot.cn/sites/8649.html [Summary]

**General-purpose assistants**
39. https://help.openai.com/en/articles/11487532-chatgpt-record [403, summary only]
40. https://tldv.io/blog/chatgpt-record-mode-for-meetings/ [competitor vendor]
41. https://support.claude.com/en/articles/12138966-release-notes

**Fabric, specialized products, lab practices**
42. https://fabric.so/teams/academic-labs ; https://fabric.so/teams
43. https://chromewebstore.google.com/detail/fmibimgfmoaogdajeoeedledhejppgll
44. https://rashidlab.github.io/lab-handbook/policies/meeting-leader-guide.html ; GitHub API search (§6 P6)

**Supervision policies**
45. https://www.haplo.com/graduate-education-manager ; https://lboro.ac.uk/students/handbook/starting/attendance/co-tutor-supervisory/ ; https://my.surrey.ac.uk/sites/default/files/2025-04/how-to-log-monthly-supervision-meeting.docx
46. (university page; link removed) ; (university page; link removed) ; https://nusgs.nus.edu.sg/research-progress-report/ [Summary]; LJMU eDoc PDF [404, summary only]

---
## Appendix: v1.1 Final Revisions 

- Rows L3 and Z6 have been corrected after a verbatim check against the original pages (see the table above).
- How far Minutes (open-source closeout) and the experiment-tracking tools (W&B, MLflow, Neptune, Comet) get on the "decision → follow-up run" step is filled in at `01_market-research/09_verification_minutes_and_experiment_tracking.md`.
- Hands-on testing of competitors is still **zero** (06 review P0-1 not completed), so every "the page doesn't say" is only a judgment at the page level.
