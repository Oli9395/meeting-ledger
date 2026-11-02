---
title: "Competitor Research 01 — In-depth Analysis of AI \"Meeting Transcription / Minutes / Action Item\" Products in the Chinese Market (Feishu Minutes and Others)"
status: draft
sources_count: 47
sources_count_method: Number of unique URLs in the sources section (recalculated at wrap-up; original value 44)
evidence_note: First-round file. The body does not distinguish [Fact] from [Summary] item by item, and sources do not record access dates individually (all set to at the time of writing). Any item marked [Fact] whose body has no "opened the original page" record should be treated as [Summary · to be verified] before citing (added in the wrap-up revision)
---

# Competitor Research 01: AI Meeting Products in the Chinese Market — How Far Do They Actually Take "Meeting → Action Items"?

> **Reading notes**
> - Every key claim carries a label: **[Fact]** means there is a source that can be checked; **[Inference]** means derived from multiple facts but with no direct evidence; **[Assumption]** means it still needs interviews or experiments to verify.
> - **To be verified**: the source is only a third party or a search-engine summary, or the original page cannot be opened, or sources contradict each other. Such figures **must not** be written directly into the PRD or external materials.
> - **Research limitations (important)**: pages on Zhihu, Xiaohongshu, Bilibili, and LINUX DO return 403 or a CAPTCHA to scraping tools, so user quotes from these platforms can only be relayed from **search-engine snippets**. They are separately labeled "relayed from snippet" below. In addition, the WebSearch quota ran out late in this research round, so the latest 2026 AI capabilities of Tencent Meeting, the official pricing of DingTalk Tingji, and the audio-recording minutes capabilities of Doubao and Kimi could not be examined in depth; §9 lists the follow-up checklist.
> - Prices are always written as "source + date". Prices of Chinese SaaS products change frequently, so **please check the official website before citing**.

---

## 0. One-Sentence Conclusions (Answer First, Then the Why)

1. **"Meeting → action items → push to a task system" is already standard in the Chinese market, not a gap.** Feishu, DingTalk, and Tencent Meeting all publicly advertise "extract follow-up person/owner + deadline + sync tasks" [Fact, §2–§4]. Answering "why doesn't Feishu do this?" with "we can turn meetings into tasks" does not hold up.
2. **"Citing/tracing back to the original text" is also becoming standard.** Feishu writes "accurately identifies action items, supports tracing back to the original text", iFlytek Tingjian launched "minutes tracing" in November 2025, and in Notion the summary citations show the corresponding transcript snippet on hover [Fact]. So the "with citations" point in BriefPilot's current PRD **does not in itself constitute differentiation** [Inference].
3. **The real gap is not "whether it exists" but "whether it is correct, who has the final say, and whether it closes the loop across meetings".** The existing evidence points to these places: in testing, DingTalk assigned action items to the meeting organizer by default [Fact]; Tencent Meeting's action items did not name an owner in one comparative review (relayed from snippet, to be verified); **no** vendor has **publicly disclosed** accuracy or recall for action item extraction, only self-reported figures such as transcription accuracy [Fact: not found in searches]; domain terminology and mixed Chinese-English speech remain a hotspot of complaints [Fact]; and for cross-meeting tracking such as "did we do what we promised last week", **no product was found** that makes it a core feature [Inference].
4. **Ecosystem lock-in is a structural boundary for the big vendors.** Each closes the loop within its own IM, calendar, and tasks. Teams working across tools would find it awkward, such as the "WeChat + Zoom + Overleaf + GitHub" combination common in labs [Inference, basis in §8].
5. **Implications for BriefPilot** [Inference]: the direction of differentiation should move from "can extract action items" to the following three things. First, **the credibility of commitment detection**, distinguishing "explicit commitment", "suggestion", and "under discussion". Second, **not guessing missing fields, and publishing its own evaluation results**. Third, **a cross-meeting commitment ledger**, suited to recurring meetings such as weekly meetings / group meetings. Research group meetings are a candidate niche, but this still needs to be validated through user research (see 02_user-research).

---

## 1. Research Scope and Method

| Dimension | Description |
|---|---|
| Subjects | Feishu Minutes / Feishu Smart Meeting Minutes, Tencent Meeting AI Assistant, DingTalk AI Tingji (formerly "Shanji"), iFlytek Tingjian, Tongyi Tingwu, Notion AI Notes (used in Chinese), WPS AI, Doubao / Kimi, Huawei Xiaoyi Huiji / Recorder, Xiaomi Recorder |
| What to examine for each product | Positioning and users, transcription, summary, action item extraction, task integration, knowledge base/Q&A, citation tracing, pricing, user complaints, mixed Chinese-English speech, non-meeting scenarios |
| Method | About 30 Chinese and English web searches and about 30 pages opened with WebFetch, prioritizing official pages and dated media reports |
| Not done | No hands-on testing of products (no accounts or recording samples), no comparison of ASR accuracy (no independent benchmark on the same recordings) |

**Why no hands-on testing?** Without a unified test set, personal testing is only "one result from one recording" and is easily mistaken for a conclusion. The right approach is to run a controlled experiment in phase S1 using the same batch of synthetic group meeting recordings and write it into the evaluation plan (§9) [Inference].

---

## 2. Feishu Minutes + Feishu Smart Meeting Minutes + Feishu Tasks

### 2.1 Positioning and Target Users
- [Fact] Feishu positions smart meeting minutes as "turning every meeting into an enterprise digital asset", covering three stages: before, during, and after the meeting. Before the meeting it identifies scheduling intent from chats, during the meeting it summarizes key points in real time, and after the meeting it generates minutes. Source: Feishu official article https://www.feishu.cn/content/article/7577317993749269689
- [Inference] The target users are **enterprise teams that already keep their IM, documents, and calendar all on Feishu**. A comparative review dated 2026-08-05 says it is "not suitable for individuals who don't use Feishu at all and only occasionally transcribe audio". Source: https://aixiaobailab.com/ai-meeting-notes-tools/

### 2.2 Core Features
| Capability | Status | Source |
|---|---|---|
| Transcription | [Fact] Transcription supports "24 languages including Chinese and English" and multiple dialects. Another official FAQ states that **minutes** input supports Chinese, English, and Japanese, and output supports Chinese and English; mixed Chinese-English discussions are "transcribed in the original language", and when English predominates the summary is in English | 7600354912756681687; 7577317993749269689 |
| Summary structure | [Fact] Includes a meeting summary, chapter-by-chapter summaries (with jump links), action items, per-speaker viewpoint summaries, playback, and the full text. It adapts to the meeting type, which includes single-topic discussion, multi-topic business meeting, weekly task follow-up, report, sharing session, interview, and so on | 7577317993749269689 |
| Action item extraction | [Fact] The official wording is "automatically breaks down into standardized action items, containing three elements: owner, deadline, and core task content"; "if the meeting did not specify an owner or deadline, users can add them manually" | https://www.feishu.cn/content/article/7600354912756681687 |
| Task integration | [Fact] To the right of each action item there is a "Create task" button, which links directly to Feishu Task Center, lets you set priority and reminders, and the owner receives a message | Same as above |
| Tracing | [Fact] The official wording is "accurately identifies action items, supports tracing back to the original text", and "each key point is linked to a Feishu Minutes timestamp". **Note**: the two official articles do not say exactly the same thing, and whether "an action item itself can jump back to the original sentence one by one" is not made clear in the second article, to be verified | 7577317993749269689; 7600354912756681687 |
| Knowledge/aggregation | [Fact] There is a "Meeting Digest" that summarizes recent minutes by week. A third-party developer built lark-retro, which reads the calendar, minutes, and tasks through the Feishu CLI to generate retrospectives and weekly reports, showing there is demand for cross-meeting aggregation that the official product does not fully satisfy | 7577317993749269689; https://www.v2ex.com/t/1209427 |
| Open interfaces | [Summary] Feishu's official lark-minutes Agent Skill treats "Feishu Minutes AI action items" as a separate object that can be added, deleted, and modified, and the documentation specifically notes "this is not lark-task". In other words, **AI action items and formal tasks are two separate layers in the data** | https://mcpservers.org/zh-CN/agent-skills/larksuite/lark-minutes (page returns 403, relies on search snippet) |
| Data commitment | [Fact] "We will not use customer data for AI model training" | 7577317993749269689 |

> **Why does "AI action item ≠ formal task" matter?** It shows that Feishu **already has a "draft → confirm → formal task" layer** in its architecture, consistent with the core design of the BriefPilot PRD (action item draft → human confirmation → formal task) [Inference]. BriefPilot cannot present "human confirmation" as something unique to itself. What it can talk about is **what is shown** at the confirmation step: evidence snippets, commitment strength, and missing fields, and **what is tracked** after confirmation: cross-meeting status.
### 2.3 Pricing (as of what could be found in 2026-11)
- [Summary] Official Feishu announcement: starting **2024-12-03**, the basic (free) plan gives each user **300 minutes** per month of Minutes speech-to-text quota, counting meeting recordings, audio recordings, local uploads, and cloud file imports. Once exceeded, "newly generated Minutes no longer include a text transcript," until the quota resets on the 1st of the next month; paid plans have no duration limit but are subject to storage capacity. Source: https://www.feishu.cn/new-announcement/pricing-adjustment2024 (direct fetch returned only the title; the body is paraphrased from search snippets, **to be verified**)
- [Fact] The billing unit for AI meeting notes is "the number of AI meeting notes successfully generated": one meeting consumes 1 quota unit, and generating both a document and a Minutes summary for the same meeting still consumes only 1; quota is shared within the tenant, and admins can allocate it by department. Whether the "12,000" cap on the page means count or minutes could not be confirmed, **to be verified**. Source: 7577317993749269689
- [Fact] Voiceprint recognition requires the Business Professional plan or higher (third-party comparison, 2026-08-05, **to be verified**). Source: aixiaobailab
- Prices for each tier: the official "plan comparison" page https://www.feishu.cn/service could not be fetched. A third-party blog's "Enterprise plan ¥30/person/month" has no official source and is **not adopted**.

### 2.4 User complaints and weaknesses
- [Fact] V2EX, 2022-12-21: "试用了飞书妙记，功能很不错就是错误太多，还有说话人识别错误很多。" (Tried Feishu Minutes; the features are very good but there are too many errors, and speaker identification is wrong a lot.) https://v2ex.com/t/903915 (fairly old; ASR may have improved since)
- [Fact] V2EX, 2026-05: "不想用在线的，像飞书妙记（因为不是会员的话，有额度限制）。" (Don't want to use online tools like Feishu Minutes, because without a membership there is a quota limit.) The poster wanted a "**free, local, secure tool** for summarizing long recorded meetings". https://www.v2ex.com/t/1214814
- [Fact] Sspai, 2023-07-19: "These two online tools (Feishu Minutes, Tongyi Tingwu) both have a free trial duration or a storage capacity limit, so moderate-to-heavy users quickly reach the point of paying." https://sspai.com/post/81308
- [Summary paraphrase, to be verified] On Zhihu there is a question titled "Feishu Minutes 300 minutes is not enough". https://www.zhihu.com/question/13742351426
- [Summary paraphrase, to be verified] Several older Sspai articles mention that **specialized terminology in professional courses is easily missed or mis-transcribed**; Minutes has no folder hierarchy; the personal edition has few AI features, so users export the text and hand it to another AI for a second pass. (Search entry point https://sspai.com/post/73374 etc.; which specific article says this was not checked by opening each one.)
- [Summary paraphrase, to be verified] Zhihu comparison: after an external recording is uploaded, **voiceprint recognition is not triggered**, so support for recordings from sources outside Feishu is limited. Another piece says its output is "more like meeting minutes, requiring manual extraction of key points". https://zhuanlan.zhihu.com/p/1933666294118483724

### 2.5 Mixed Chinese-English and non-meeting scenarios
- Mixed Chinese-English [Fact]: notes input supports only Chinese, English, and Japanese, and mixed discussion is transcribed in the original language; this counts as an explicit product-level treatment. However, there is no public data on recognition of **technical terms and abbreviations** (e.g. VLA, RT-2, ablation), **to be tested**.
- Non-meeting [Fact]: the quota rules list "audio recordings" and "local file uploads", which indicates that offline recording and import are supported. The summary templates include "interview" and "sharing session" but **do not** include research templates such as "experiment discussion", "advisor 1:1", or "group meeting progress report" [Fact: none appear in the official template list]. How well the "weekly task follow-up" template works for a research group meeting is **unknown** [Assumption].

---

## 3. Tencent Meeting AI Assistant (Hunyuan / Yuanbao Notes)

### 3.1 Positioning and features
- [Fact] Launched 2024-02-22, based on the Hunyuan large model. Features include "real-time meeting notes during the meeting" and "intelligent post-meeting note extraction", which can "automatically organize post-meeting key follow-up items, follow-up owners, and completion times". Source: Kuai Keji / Ifeng https://tech.ifeng.com/c/8XNZFk4mxCO
- [Fact, 2026-08-05 third party] After the meeting, notes can be imported into **Yuanbao** to generate an action plan; "timestamp jump is a highlight". Source: aixiaobailab
- [Summary] In September 2025, Tencent Meeting said its AI feature user base grew by more than 150% year over year. Source: https://www.pingwest.com/a/307746 (not opened directly)
- Positioning [Inference]: aimed at **people who already hold online meetings in Tencent Meeting**; AI is a value-added layer on the meeting software, not a standalone note-taking product. The comparison's view is that it is "not suitable for teams that mainly meet on Zoom or Teams".

### 3.2 Action item handling
- [Fact] Official promotion says it extracts "follow-up owners and completion times" (ifeng).
- [Summary paraphrase, to be verified] Zhihu comparison "Which AI meeting notes tool is best? Feishu, DingTalk, Tencent Meeting tested!": for Tencent Meeting, "the notes are short, content mining is limited, **action item extraction does not specify the owner, and jumping back to the source is not supported**". https://zhuanlan.zhihu.com/p/1969726007952007258 (403; relies on the snippet. This conflicts with "timestamp jump is a highlight"; it may be a version difference, or a difference between "the notes can jump but action items cannot".)
- How it integrates with Tencent's own task system: **not found in searches**, to be verified.

### 3.3 Pricing
- [Fact, secondhand] Tencent Meeting's 2024-12-06 business adjustment notice: from January 2025 the plans become Free, Professional, Business, and Enterprise, with the student discount retained. Source: woshipm / Toutiao (search snippet) https://www.toutiao.com/zixun/7550862619368933419/
- [Third party, to be verified] Professional plan "about ¥98/month", with AI Assistant Pro / Yuanbao Notes included in the Professional plan and above (aixiaobailab, 2026-08-05). Another source says "Professional plan ¥88/month/account"; the two figures are inconsistent. The Business plan "from ¥4,788/year" is consistent across several sources (search snippets, https://www.nbd.com.cn/articles/2023-03-14/2710441.html, etc.).
- [Summary paraphrase, to be verified] Free transcription is "about 120 minutes per month", and notes get only a small number of free uses per month (Zhihu comparison).
### 3.4 Complaints and weaknesses
- [Fact] A CSDN usage tutorial lists "low transcription accuracy" as a common problem for new users. https://blog.csdn.net/shaudhaidhwo/article/details/161049023
- [Fact] Quote from a comparative review: "Clear Mandarin is officially rated at 95%–98%, but accents, noise, jargon, and interruptions all pull it down." The author argues that "summaries and action items affect real-world value more than word-for-word accuracy." aixiaobailab
- Mixed Chinese-English: **no official documentation was found**; to be verified. Non-meeting use: the AI assistant depends on Tencent Meeting's cloud recording; how it covers in-person offline meetings was not found; to be verified.

---

## 4. DingTalk AI Listening Notes (formerly DingTalk Flash Notes) + DingTalk To-Do / Teambition

### 4.1 Positioning and evolution
- [Fact] Originally called "DingTalk Flash Notes" (钉钉闪记), later renamed AI Listening Notes (AI 听记). A media report says recognition previously "relied on a rule framework… with accuracy of only 80-something percent," and that after the speech model was rebuilt it "reached 97%-98%" (**vendor claim**, not independently verified). Source: Leiphone, 2025-12-24 https://www.leiphone.com/category/CorporateServices/laMyPOOWyk7FzjEa.html
- [Fact] On 2025-11-17, DingTalk 8.1.5 launched "illustrated minutes" (图文纪要): a full-content overview map, a timeline embedded in each chapter, flowcharts and mind maps. Action items can be "synced to DingTalk To-Do in one click, with an assignee and a due date," and transcription with translation into 72 languages is supported. Source: QbitAI https://www.qbitai.com/2025/11/353375.html
- [Fact] On 2025-12-11, DingTalk 8.1.10 enabled AI Listening Notes to "identify action items and to-dos mentioned in conversation" and added **AI Q&A** on the minutes detail page. It supports "recording, taking photos, and marking highlights at the same time," and can generate **class minutes**. Source: ITHome https://www.ithome.com/0/904/104.htm
- [Fact] There is a hardware entry point: the DingTalk A1 / A1 Pro recorder card. According to a 2026-04 report, the A1 Pro is priced at 1,299 CNY and includes 6 months of transcription allowance at 1,500 minutes per month (search snippet, https://www.yzwb.net/news/ch/202604/t20260430_348102.html , to be verified).
- Positioning [Inference]: it is expanding from "meetings" to "all offline conversations," using hardware to cover in-person scenarios. **It is the most aggressive domestic player in non-meeting scenarios.**

### 4.2 Action item approach (the best-documented of the competitors)
- [Fact] Woshipm (人人都是产品经理), 2025-09-05: "If information such as the task owner is not matched, manual association is supported," and task cards sync to DingTalk "To-Do." https://www.woshipm.com/share/6265011.html
- [Fact] Woshipm, 2025-09-19, a hands-on test with a 55-minute meeting: the AI generated 6 action items from 6 conclusions and "**automatically assigned the tasks to the meeting organizer by default**." Users can reassign, set due dates, and sync to To-Do. The author also notes that "transcription is occasionally inaccurate with technical terms, English abbreviations, and fast speech." https://www.woshipm.com/share/6269848.html
> **Why does this evidence matter?** "Default to the organizer" is a **silent guess**: when the owner is not identified, the system does not leave the field empty but fills in a plausible-looking value. In a group meeting setting, the organizer is often the advisor, which creates the illusion that "the advisor has a pile of students' tasks under their name" [Inference]. BriefPilot's approach of "leave missing fields empty + mark them 'to be confirmed'" targets exactly this issue, but a controlled experiment is needed to prove it is actually better [Assumption].

### 4.3 Pricing
- [Fact] DingTalk "365 Membership" (personal) launched on 2024-09-23 at a standard price of 39 CNY/month, an "AI price" of 15 CNY for a continuous monthly subscription, and 169 CNY per year. Benefits include AI search, a personal AI assistant, and more; **the original text does not mention listening-notes minutes**. https://www.ithome.com/0/797/696.htm
- [Search snippet, to be verified] Listening notes: "Standard membership is free, with 300 minutes of transcription per month, 5 illustrated minutes, and 30 AI Q&A queries; Premium membership gets 3,000 minutes per month at ¥59/person/month." The official page https://page.dingtalk.com/wow/dingtalk/default/dingtalk/czWaaDTBTVh4XklaQFXW could not be scraped for body text, so it **must not be cited directly**.

### 4.4 Complaints
- **Few** public negative quotes were found (most results are sponsored content). The weaknesses that can be confirmed are: inaccuracy on technical terms and English abbreviations (woshipm 6269848), and the default-owner issue. Heimao Complaints (黑猫投诉) and Xiaohongshu could not be scraped; to be added.

---

## 5. iFLYTEK Tingjian (including iFLYTEK Meeting / Tingjian Huiji)

- [Fact] A 2025-11-06 report: the iFLYTEK Tingjian SaaS platform has "surpassed 98 million" users. After the "adaptive meeting minutes" upgrade, it can combine personal notes, images, and voice into minutes and produce role-based summaries. A new "**minutes traceability**" button links back to the original text; "200+ dialects without switching"; "**mixed Chinese-English-Cantonese recognition**"; available on PC, with "Enjoy Pack" (畅享包) users getting priority access. Source: China.com https://m.tech.china.com/hea/articles/20251106/202511061760505.html
- Action items: this report **does not mention** action items. Third-party articles say in general terms that it "can automatically extract action items," **to be verified**. Task system integration: iFLYTEK has no collaboration suite of its own, and **no related capability was found** [Inference: this is a structural weakness].
- Pricing: a third party lists "Professional edition 99 CNY/month," **to be verified**. V2EX, 2022-12: after registration, "only fifteen minutes of trial" (https://v2ex.com/t/903915).
- [Paraphrased summary] A Zhihu comparative review holds that it is "more stable for professional transcription, but lacks automatic summarization" (an early assessment that may no longer hold given the 2025 upgrades).
- Positioning [Inference]: **a "dictation specialist" whose core selling points are transcription accuracy and dialect support**. Its public marketing on mixed Chinese-English-Cantonese is the clearest of the group, but its "meeting-to-execution" loop is very weak.

---
## 6. Tongyi Tingwu (Alibaba)

- [Fact] Released 2023-06-01; the stated use cases are "meeting discussions, teaching and training, research interviews, and video watching" (会议讨论、教学培训、调研访谈、视频观看). Source: IT Home https://www.ithome.com/0/696/842.htm
- [Summary] A 2024-03 report is headlined "Q&A across 100+ audio and video files at once" (multi-file Q&A). The product owner said "Tongyi Tingwu currently has no plans to charge consumers (C-end users)". https://news.bjd.com.cn/2024/03/20/10725488.shtml ; https://news.qq.com/rain/a/20240319A07G9G00
- [Fact] API capabilities: under the LLM analysis items, "key point extraction: supports keyword and action item extraction"; translation supports Chinese, English, Japanese, Korean, German, French, and Russian. Source: Alibaba Cloud docs https://help.aliyun.com/zh/model-studio/product-introduction-2
- [Fact] **API pricing** (Alibaba Cloud billing page; the page shows no update date; captured at the time of writing): real-time or file transcription on the new API (including speaker diarization) costs **CNY 0.6/hour**; LLM capabilities such as chapter overview, full-text summary, and **action items** are "CNY 0.064/hour, billed separately and stackable"; real-time translation is CNY 4/hour; new users get a 90-day free trial. The legacy API starts at CNY 10.5/hour with tiered pricing. https://help.aliyun.com/zh/tingwu/pricing-and-billing-rules/
  > **Why list API prices?** They give a cost reference for a build-your-own approach. If BriefPilot used an ASR like Tingwu underneath, the **marginal cost of transcription + action items is roughly CNY 0.66/hour**. Price is not a moat; any differentiation can only come from the product layer [Inference].
- Consumer (C-end) pricing: third parties report "Pro membership CNY 228/year", plus a claim that "university faculty and students get 500 free hours with an education email" (https://www.aigcmap.cn/sites/782.html ; https://aiproducthub.cn/sites/tongyi-tingwu.html ). **Both need verification.**
- Complaints [paraphrased summary, needs verification]: some feel that "the summary is more like compressed text, not a properly organized set of minutes"; recognition accuracy drops for dialects and accented Mandarin (Zhihu https://zhuanlan.zhihu.com/p/2016870058333324568 , 403). A sspai author found the full-text summary and chapter overview "rather stiff", and in practice "transcribes with Tingwu, then hands it to Doubao to write the minutes" (sspai search snippet).
- Positioning [Inference]: **a standalone tool + Alibaba Cloud API foundation**. It is not tied to an IM platform, so it has no native task-system integration. That suits "cross-ecosystem" users, and it is also its gap in closing the execution loop.

---

## 7. Other Players

### 7.1 Notion AI Meeting Notes (used by Chinese-speaking teams)
- [Fact] Requires a Business or Enterprise plan; supports 16 languages, including Chinese; **speaker labels currently support English only**; citations in the summary "can be hovered to view the corresponding transcript snippet, and clicking jumps to it"; it can identify "key points and action items"; it recommends obtaining consent from all participants before transcribing, and clicking Start transcribing counts as confirming consent; audio retention is clearly documented (up to 3 days on web and desktop for retries). Sources: https://www.notion.com/zh-cn/help/ai-meeting-notes ; TechCrunch 2025-05-13 https://techcrunch.com/2025/05/13/notion-takes-on-ai-notetakers-like-granola-with-its-own-transcription-feature
- Assessment [Inference]: citation traceability and the **consent flow** are the most well-executed here. But speaker diarization is unavailable for Chinese, so "who made the commitment" cannot be determined, and extracting action item owners in Chinese is a critical weakness.

### 7.2 WPS AI
- [Fact] WPS AI membership is CNY 25/month on auto-renewing monthly billing, and the "Premium Membership" that includes Super Membership Pro is CNY 35/month (IT Home, 2025-05-17). https://www.ithome.com/0/853/778.htm
- [Fact] In an official WPS article of 2026-06-26 on AI meeting minutes, the transcription tools given as examples are **Feishu Minutes, Tongyi Tingwu, and iFlytek Tingjian (讯飞听见)**, while WPS itself covers "minutes to PPT" and cloud document distribution; the article also advises "mark AI output as 'pending review', then finalize and distribute after verification". https://www.wps.cn/article/lYpe6hOk.html
- Assessment [Inference]: in this chain WPS sits **downstream of the minutes** (documents and reporting); no first-party meeting transcription or action-item loop was found. Even WPS officially advocates "pending review", which shows that "human confirmation" is an industry consensus, not a differentiator.

### 7.3 Doubao / Kimi
- Doubao [paraphrased summary, low credibility]: one user says typing "录音" (record) is enough to start recording and organize minutes (short-video content, 2025-02). One article says exporting recordings is difficult and that it "wrote 'offline' as 'online' … and missed several key points", but that article promotes another tool and is **not credible**. "Doubao Work" can connect to Feishu to produce scheduled daily summaries. https://ai-bot.cn/doubao-work-pc-review/
- Kimi: **no reliable information was found** on an official Kimi meeting recording or minutes feature; needs verification.
- Assessment [Inference]: general-purpose LLM assistants play the role of a "**second-pass processor**" in this chain. Users' real workflow is often "tool A transcribes → Doubao/Kimi summarizes" (the sspai author's approach), which suggests that no single product's minutes quality satisfies users, who are willing to take an extra step.

### 7.4 Huawei (Voice Recorder / Xiaoyi Huiji)
- [Fact] Voice Recorder: HarmonyOS 5.0.0.115 and above supports speech-to-text and "smart summary", and the summary can be "added to the original text"; Huawei officially acknowledges that results are affected by noise, volume, and dialects. https://consumer.huawei.com/cn/support/content/zh-cn16042743/ (search snippet)
- [Fact] Xiaoyi Huiji (HarmonyOS 6.0 and above): summary overview (generated once the transcript reaches 200 characters), **Huiji Q&A: tapping a Q&A source locates and highlights the corresponding original transcript text**, and smart reminders (pushed when the transcript hits keywords). "**Speech-to-text currently supports only Mandarin Chinese, and does not yet support dialects or other languages**". https://consumer.huawei.com/cn/support/content/zh-cn16073727/
- Action items: the Huiji overview contains an "action items" content entry, but Huawei does not define its rules, and there is also **no task-system integration** [Fact].
- Assessment [Inference]: the advantage of system-level phone recording is that it is **always at hand and covers 1-on-1 and offline settings**. But "Mandarin only" means research discussions that mix Chinese and English are excluded outright.
### 7.5 Xiaomi (Voice Recorder / AI Voice Recognition)
- [Fact] 2025-11-24 HyperOS 3 upgrade roundup: the Voice Recorder adds a **structured recording summary**, AI voice recognition improves on technical terms and dialects, and it can remove redundant wording. https://finance.sina.com.cn/tech/roll/2025-11-24/doc-infynrnz5791392.shtml
- "Automatically extracts conclusions and action items from recordings" appears only in one third-party blog post and is **yet to be verified**. https://www.tixiaolu.com/posts/ai-xiaomi-ai-2026/
- Assessment: like Huawei, this is a personal note-taking layer with no team task loop.

---

## 8. Feature Matrix

Legend: ● = supported by public evidence; ◐ = partially supported or limited; ○ = not found in search / none; ? = conflicting claims or to be verified. **This table reflects "public marketing and press coverage," not hands-on testing.**

| Dimension | Feishu | Tencent Meeting | DingTalk Tingji | iFLYTEK Tingjian | Tongyi Tingwu | Notion | WPS AI | Huawei Huiji | Xiaomi Recorder |
|---|---|---|---|---|---|---|---|---|---|
| Transcription | ● | ● | ● | ● | ● | ● | ○ | ● (Mandarin only) | ● |
| Structured summary | ● (adapts to meeting type) | ● | ● (illustrated minutes) | ● | ◐ (reviewed as "stiff") | ● | ◐ (downstream processing) | ● | ● |
| Action item extraction | ● | ● / ? (summary says no owner) | ● | ? | ● (API) | ● | ○ | ◐ (undefined) | ? |
| Assign owner | ● (manual fill when missing) | ? | ◐ (defaults to the initiator) | ? | ? | ◐ (speakers in English only) | ○ | ○ | ○ |
| Due date | ● | ● | ● | ? | ? | ? | ○ | ○ | ○ |
| Human confirmation before becoming a task | ◐ (one-click create; AI action items and tasks are separate layers) | ? | ◐ (synced after selection) | ○ | ○ | ? | — | ○ | ○ |
| Task system integration | ● (Feishu Tasks) | ? | ● (DingTalk to-dos) | ○ | ○ | ◐ (Notion database) | ○ | ○ | ○ |
| Citation / source tracing | ● (key points have timestamps) | ? (conflicting) | ◐ (timestamp jump; source tracing unconfirmed) | ● (minutes traced to source) | ? | ● (hover citations) | ○ | ● (Q&A traced to source) | ? |
| Cross-meeting Q&A / aggregation | ◐ (Meeting Express) | ? | ◐ (single-meeting AI Q&A) | ? | ● (multi-file Q&A, 2024) | ◐ (workspace search) | ○ | ○ | ○ |
| Cross-meeting commitment status tracking | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ |
| Mixed Chinese-English | ● (transcribes in the original language) | ? | ? (abbreviations inaccurate) | ● (Chinese/English/Cantonese mixed) | ◐ (multilingual translation) | ◐ | — | ○ | ? |
| Terminology / hot words | ? | ? | ? | ? | ? | ? | — | ○ | ◐ (claimed improvement) |
| Offline / 1-on-1 / non-meeting | ● (recording, upload) | ? | ● (hardware, classroom) | ● | ● (interviews, teaching) | ◐ (desktop) | ○ | ● | ● |
| Public action item accuracy | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ |
| Free quota (personal) | 300 min/month (from 2024-12) | ? (about 120 min/month) | ? (300 min/month) | Trial | ? (claims conflict) | Requires Business | — | Built into the system | Built into the system |

**How to read this table**
- The bottom two rows, "Cross-meeting commitment status tracking" and "Public action item accuracy," are **all ○**. This is the only place in the table where an entire row is blank [Fact: not found within the scope of this search].
- The "Assign owner" row is all ◐ and ?. Every vendor **advertises "can identify the owner," but none explains clearly what happens when it can't**; DingTalk's hands-on results indicate that at least one silently fills in a default value [Inference].

---

## 9. Shared Shortcomings of Existing Products (List)

Each item is tagged with its evidence strength. These are candidate gaps; **whether any of them can become BriefPilot's differentiator must wait for validation by 02_user-research**.

1. **No one publishes the quality of "action item extraction."** [Fact: this search found no vendor-published precision/recall for action items; all transcription accuracy figures are vendor self-reported] Users can only fall back on "manual review"; both official WPS material and a Weibo article recommend marking items "pending review" or "confirming each item against the recording" (https://weibo.com/2/detail/comos:niwmapc3412577 ). → **Opportunity** [Inference]: BriefPilot publishes its evaluation set and metrics (field-level accuracy, and the "no-guess rate" for missing fields) as a source of product trust and a portfolio highlight.
2. **The risk of "guessing rather than leaving blank" for owners and due dates.** [Fact: DingTalk defaults to the initiator; a Weibo article says the AI "makes up" owners and "non-existent dates"] [Inference: large vendors tend to fill every field so the output "looks complete"] → **Opportunity**: explicitly mark missing fields as "to be confirmed," and show "whether this sentence is a commitment or a suggestion."
3. **"Commitment strength" is not tiered.** [Inference; no direct counter-evidence] In public descriptions, every vendor treats "I'll do it," "let's think about it," and "we could try it" alike as action items, or as "conclusion → action item" (DingTalk generates action items from **conclusions**). Research discussions contain many **hypotheses and suggestions** ("should we try swapping the backbone?"), and mixing them into action items creates noise [Assumption].
4. **The cross-meeting commitment ledger is blank.** [Fact: the whole row in the feature matrix is ○; Feishu only has the "Meeting Express" roundup, and the third-party lark-retro is filling this gap] **Recurring meetings** such as weekly meetings and group meetings most need "did we do what we said last time?" → This is the **most natural intersection** with BriefPilot's two lines, "knowledge Q&A + action items" [Inference].
5. **Ecosystem lock-in hurts cross-tool teams.** [Fact: Feishu does not trigger voiceprint recognition for externally recorded audio (as paraphrased in a summary); Tencent AI is tied to Tencent Meeting; a comparative review says "migration costs often exceed the time saved on note cleanup"] [Inference: university labs often lack a unified enterprise IM, and meetings take place across Zoom, Tencent Meeting, and in person]
6. **Technical terms and mixed Chinese-English remain frequent complaints.** [Fact: DingTalk hands-on testing found "English abbreviations inaccurate"; Sspai notes "technical vocabulary is easily missed in transcription"; Huawei supports Mandarin only; a Juejin article says: "with heavy accents, people talking over each other, and mixed Chinese-English, recognition and translation quality falls off a cliff; the terminology list is… the decisive variable" https://juejin.cn/post/7696662898145345587 ] Whether a "glossary/hot words" capability exists was **not established from any vendor's public information** and is yet to be verified. → **Note**: BriefPilot should not build its own ASR. What it can do is perform **error correction and entity normalization against a project glossary** after ASR, for example unifying "RT two" into "RT-2" [Inference].
7. **Non-meeting scenarios can be "recorded" but are not "understood."** [Fact: Feishu, DingTalk, Tingwu, and Huawei can all record offline sessions and interviews] [Fact: no dedicated minutes template for "experiment discussions / advisor 1:1s / group meetings" was found] → In research settings, "can record" is not the gap; "understanding by research structure" (experimental setup, results, next steps, blockers) may be [Assumption].
8. **Quota thresholds for individuals and students, plus privacy concerns.** [Fact: Feishu gives 300 min/month; a V2EX user wants "free, local, and secure"; Sspai says "moderate to heavy users will quickly hit the point where they need to pay"] [Inference: for overseas universities like the target university, storing data on domestic Chinese SaaS may raise compliance concerns, to be confirmed in the 4th item of 02_user-research]
9. **Users stitch together their own workflow: A transcribes → B summarizes.** [Fact: Sspai "transcribe with Tingwu, then hand off to Doubao"; Feishu personal edition "export, then hand off to another AI"] This shows that **a single product's minutes output did not satisfy users**, and also that users are willing to use multiple tools. BriefPilot can **cover only the "after transcription" segment** and not compete with large vendors on ASR [Inference].
### What BriefPilot "can't say / can say"
| Can no longer say (already table stakes) | Can try saying (candidate differentiators, to be validated) |
|---|---|
| "We turn meetings into action items" | "We distinguish commitments, suggestions, and discussion; we don't guess missing fields; and we publish our evaluation numbers" |
| "We include citations" | "Every action item shows the original sentence that triggered it and its commitment strength, so you can judge at a glance when confirming" |
| "We require human confirmation" | "We keep following up after confirmation: the next group meeting automatically lists the status of last meeting's commitments" |
| "We support Chinese and English" | "We normalize mixed Chinese-English entities (model names, dataset names) against the project glossary, which is testable and regression-checkable" |

---

## 10. Uncovered Items and Follow-up Checklist (Next Round)

1. Tencent Meeting's AI minutes in 2025–2026: whether action items have owners and can be traced back to the source (sources currently contradict each other), and how they integrate with Tencent Docs and action items.
2. DingTalk AI Listening's official pricing and quotas. We currently only have search snippets.
3. Whether each vendor has a **hotword / glossary** feature (Feishu, Tongyi Tingwu, and iFLYTEK may all have one, but it was not verified this time).
4. Recording-summary capabilities of Doubao and Kimi, and the feature differences between international Lark and domestic Feishu (Lark is what users in Singapore can actually access).
5. Verbatim user comments from Xiaohongshu, Bilibili, Black Cat Complaints, and App Store reviews (blocked this time by 403 errors or CAPTCHAs; needs manual browsing to fill in).
6. **Suggested hands-on test**: make 3 synthetic group-meeting recordings (mixed Chinese-English + terminology + vague commitments), run each through Feishu, Tongyi Tingwu, and DingTalk, and measure the "mis-fill rate" and "miss rate" for owners and deadlines. This data would be the strongest evidence for answering an interviewer's question "why build this at all?" [Inference].

---

## Source List

**Official / primary sources**
1. Feishu: Smart meeting minutes article https://www.feishu.cn/content/article/7577317993749269689
2. Feishu: AI summarizes key points and breaks down action items https://www.feishu.cn/content/article/7600354912756681687
3. Feishu: Minutes quota rules announcement (body text taken from search snippet) https://www.feishu.cn/new-announcement/pricing-adjustment2024
4. Feishu: Edition comparison (body text could not be fetched) https://www.feishu.cn/service
5. Feishu lark-minutes Skill (403, relies on snippet) https://mcpservers.org/zh-CN/agent-skills/larksuite/lark-minutes
6. Alibaba Cloud: Tongyi Tingwu billing https://help.aliyun.com/zh/tingwu/pricing-and-billing-rules/
7. Alibaba Cloud: Tongyi Tingwu product introduction https://help.aliyun.com/zh/model-studio/product-introduction-2
8. Notion: AI Meeting Notes help (Chinese) https://www.notion.com/zh-cn/help/ai-meeting-notes
9. Huawei: Xiaoyi Huiji https://consumer.huawei.com/cn/support/content/zh-cn16073727/
10. Huawei: Recorder speech-to-text and smart summary (search snippet) https://consumer.huawei.com/cn/support/content/zh-cn16042743/
11. WPS official: AI for writing meeting minutes (2026-06-26) https://www.wps.cn/article/lYpe6hOk.html
12. DingTalk: AI Listening page (body text could not be fetched) https://page.dingtalk.com/wow/dingtalk/default/dingtalk/czWaaDTBTVh4XklaQFXW

**Media coverage**
13. Kuai Keji / Ifeng: Tencent Meeting AI assistant launches (2024-02-22) https://tech.ifeng.com/c/8XNZFk4mxCO
14. PingWest: Tencent Meeting AI user growth (search snippet) https://www.pingwest.com/a/307746
15. Toutiao: Tencent Meeting edition changes (search snippet) https://www.toutiao.com/zixun/7550862619368933419/
16. National Business Daily: Tencent Meeting pricing (2023, search snippet) https://www.nbd.com.cn/articles/2023-03-14/2710441.html
17. QbitAI: DingTalk AI Listening illustrated minutes (2025-11-17) https://www.qbitai.com/2025/11/353375.html
18. ITHome: DingTalk 8.1.10 (2025-12-11) https://www.ithome.com/0/904/104.htm
19. Leiphone: DingTalk Listening accuracy and investment (2025-12-24) https://www.leiphone.com/category/CorporateServices/laMyPOOWyk7FzjEa.html
20. ITHome: DingTalk 365 membership (2024-09-23) https://www.ithome.com/0/797/696.htm
21. Yangtze Evening Post: DingTalk A1 Pro (2026-04, search snippet) https://www.yzwb.net/news/ch/202604/t20260430_348102.html
22. China.com: iFLYTEK Tingjian upgrade (2025-11-06) https://m.tech.china.com/hea/articles/20251106/202511061760505.html
23. ITHome: Tongyi Tingwu launch (2023-06-01) https://www.ithome.com/0/696/842.htm
24. Beijing Daily: Tongyi Tingwu multi-file Q&A (2024-03-20, search snippet) https://news.bjd.com.cn/2024/03/20/10725488.shtml
25. Tencent News: Tongyi statement that consumer use is free of charge (2024-03-19, search snippet) https://news.qq.com/rain/a/20240319A07G9G00
26. ITHome: WPS AI membership pricing (2025-05-17) https://www.ithome.com/0/853/778.htm
27. Sina Tech: HyperOS 3 upgrade roundup (2025-11-24) https://finance.sina.com.cn/tech/roll/2025-11-24/doc-infynrnz5791392.shtml
28. TechCrunch: Notion AI Meeting Notes (2025-05-13) https://techcrunch.com/2025/05/13/notion-takes-on-ai-notetakers-like-granola-with-its-own-transcription-feature

**User communities / reviews (in descending order of credibility)**
29. V2EX: Feishu Minutes accuracy is rather low (2022-12-21) https://v2ex.com/t/903915
30. V2EX: Need for local summarization of long recordings (2026-05) https://www.v2ex.com/t/1214814
31. V2EX: lark-retro, a Feishu CLI Skill https://www.v2ex.com/t/1209427
32. Sspai: Feishu Minutes and Tongyi Tingwu quotas (2023-07-19) https://sspai.com/post/81308
33. Sspai: Experience using Feishu (search snippet) https://sspai.com/post/73374
34. Everyone Is a Product Manager: DingTalk AI Listening experience (2025-09-05) https://www.woshipm.com/share/6265011.html
35. Everyone Is a Product Manager: DingTalk AI Listening 55-minute hands-on test (2025-09-19) https://www.woshipm.com/share/6269848.html
36. AI Xiaobai Lab: Feishu / Tencent / Otter comparison (2026-08-05) https://aixiaobailab.com/ai-meeting-notes-tools/
37. Zhihu: Hands-on test of Feishu / DingTalk / Tencent Meeting (403, snippet) https://zhuanlan.zhihu.com/p/1969726007952007258
38. Zhihu: Comparison of 5 AI meeting-minutes tools (403, snippet) https://zhuanlan.zhihu.com/p/1933666294118483724
39. Zhihu: One month with Tongyi Tingwu (403, snippet) https://zhuanlan.zhihu.com/p/2016870058333324568
40. Zhihu: Feishu Minutes' 300 minutes aren't enough (snippet) https://www.zhihu.com/question/13742351426
41. CSDN: Pitfalls to avoid with the Tencent Meeting AI assistant https://blog.csdn.net/shaudhaidhwo/article/details/161049023
42. Weibo article: AI that doesn't make up tasks and owners https://weibo.com/2/detail/comos:niwmapc3412577
43. Juejin: Mixed Chinese-English and glossaries in international meetings https://juejin.cn/post/7696662898145345587
44. Third-party directory sites (pricing; low credibility): https://www.aigcmap.cn/sites/782.html ; https://aiproducthub.cn/sites/tongyi-tingwu.html ; https://www.tixiaolu.com/posts/ai-xiaomi-ai-2026/ ; https://ai-bot.cn/doubao-work-pc-review/

---
## Confidence Notes on This Document's Conclusions

| Conclusion | Confidence | Rationale |
|---|---|---|
| Turning meetings into action items, with task integration, is already standard in Feishu and DingTalk | **High** | Official articles and multiple media reports agree |
| Citations / source tracing are becoming standard | **Medium-high** | First-hand evidence from Feishu, iFlytek, Notion, and Huawei; Tencent's statements are contradictory |
| No vendor publishes action-item accuracy | **Medium** | This means "not found in search," which does not mean it doesn't exist; it may simply not be public |
| DingTalk assigns action items to the meeting organizer by default | **Medium** | Based on a single hands-on test, on the 2025-09 version; it may have been changed since |
| Cross-meeting commitment tracking is a gap | **Medium-low** | It was only not found within the scope of this search; Feishu's "meeting digest" (会议速递) and Tongyi Tingwu's multi-file Q&A come close, and we need to test whether these features can answer "was the commitment from last time fulfilled?" |
| Pricing and quotas | **Low to medium** | Only Feishu's 300 minutes (summary of an official announcement) and Tongyi Tingwu's API pricing (official page) are reasonably reliable; everything else needs verification |
| Verbatim user complaints | **Medium-low** | Only V2EX and Sspai (少数派) could be opened directly, and mostly old posts; Zhihu and Xiaohongshu are relayed through summaries |
| Lack of dedicated templates for research settings may be an opportunity | **Low (assumption)** | The only evidence is "not found in search"; user interviews are needed to verify whether "structured minutes for research" is really a pain point |

**Most important reminder**: What this document can strongly support is "**what is no longer a differentiator**"; for "what is a differentiator," it can only offer candidates. The next step, user research and small-scale hands-on testing (§10, item 6), is the only way to turn candidates into evidence.
