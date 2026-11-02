---
title: "How to Find a Good Product: A Product Discovery and Opportunity Identification Handbook"
status: draft
sources_count: 34
evidence_note: First-round document. The body does not label each item individually as [Fact] or [Summary], and sources do not record individual access dates (all uniformly at the time of writing). Any item labeled [Fact] without an "opened the original page" record in the body should be treated as [Summary · to be verified] before citing (added in the closing revision)
---

# How to Find a Good Product: A Product Discovery and Opportunity Identification Handbook

> **Purpose of this document**: This is the 2nd article in the `00_pm-skills` series. It answers one question: "Given that Feishu Minutes, Otter, and Fireflies already turn meetings into tasks, how do we systematically find the small piece of need that they **do not meet**?" This document does not offer conclusions. It offers methods, criteria for judgment, counterexamples, and a pain-point mining checklist that can be used directly.
>
> **Labeling conventions** (strictly applied throughout):
> - **[Fact]** Has an original source that can be checked, with a URL attached.
> - **[Inference]** Reasonably derived from facts, but the source does not say it directly.
> - **[Assumption]** To be validated; must be confirmed or refuted by later interviews or experiments.
> - **[To be verified]** Details relayed by secondary sources, where I could not open the original to check.
>
> **Research method note**: This document is based on about 30 web searches and more than 20 original-page fetches (mainly English, with Chinese as a supplement). Some planned searches (such as specific pain-point articles from Lenny's Newsletter, complaint threads about Otter/Fireflies on Reddit, the latest Y Combinator Requests for Startups, and the literature on the "say-do gap") could not be run because this round's search quota was used up. They are listed in the "Credibility notes" at the end of the document for the next round to complete.

---

## 0. One-Line Overview: A Good Product Is Not "Thought Up," It Is "Noticed"

The core sentence in Paul Graham's "How to Get Startup Ideas" is: **the way to get startup ideas is not to try to think of startup ideas; it is to look for problems, preferably problems you have yourself** ("The way to get startup ideas is not to try to think of startup ideas. It's to look for problems, preferably problems you have yourself."). He also says the verb should be "notice," not "think up." **[Fact]** Source: https://paulgraham.com/startupideas.html

Teresa Torres turned this into a repeatable habit: the product team has contact with real users **at least once a week**, organizes the stories it hears into "opportunities (unmet needs, pain points, desires)," and then derives solutions and experiments from those opportunities. **[Fact]** Sources: https://www.producttalk.org/2016/08/opportunity-solution-tree/ , https://www.producttalk.org/best-customer-interview-questions/

Michael Seibel of YC adds a warning: founders often hold "too tightly onto solutions and too loosely onto problems," while the real opportunity lies in the market problem itself, and the first idea is usually wrong. **[Fact]** Source: https://www.ycombinator.com/blog/the-real-product-market-fit

For BriefPilot, this means: **[Inference]** the current S0 documents (PRD, JTBD table, persona) were written on the premise that "no real users have been interviewed" (the PRD itself is also marked HYPOTHETICAL). They are a "solution," not a "validated problem." The essence of this round of repositioning is to reverse the order: first find a validated problem, then decide how much of the solution to keep.

---

## 1. Why Existing Methodologies All Stress "Problem Before Solution"

### 1.1 Three Consensus Points from Different Schools

| School | Representative | Core claim | Source |
|---|---|---|---|
| Startup incubation | Paul Graham / YC | The most common startup mistake is "solving a problem that nobody has"; the three elements of a good idea: the founders want it themselves, they can build it, and others have not realized it is worth building | https://paulgraham.com/startupideas.html **[Fact]** |
| Product discovery | Teresa Torres | An opportunity = an unmet need, pain point, or desire; opportunities must come from user stories, not team assumptions | https://www.producttalk.org/2016/08/opportunity-solution-tree/ **[Fact]** |
| Lean product | Dan Olsen | The bottom two layers of the PMF pyramid are "target users + unmet needs" (the market), and the top three layers are the value proposition, feature set, and UX (the product); get the bottom layers right before moving up | https://www.mindtheproduct.com/the-playbook-for-achieving-product-market-fit/ **[Fact]** |

**Why do the three arrive at the same place from different paths?** **[Inference]** Because how verifiable a solution is depends on how clear the problem is. A problem not anchored to specific users, specific scenarios, and specific frequency cannot support an experiment where "right/wrong" can be judged; and without experiments, all that is left is "I feel." This is also what interviewers really want to hear when they ask "why build it at all": not a feature list, but how you know the problem exists, how painful it is, and how frequent it is.

### 1.2 An Important Counterintuitive Conclusion: A Crowded Market Is Not a Reason to Give Up

Paul Graham says explicitly that being "late" is not a reason to abandon an idea, because startups are rarely killed by competitors; a crowded market actually shows that the need exists. The key lies in two points: whether there is a group of users who **urgently** need it, and whether you have a thesis about "what the incumbents are overlooking." **[Fact]** Source: https://paulgraham.com/startupideas.html

Sequoia's Arc framework calls this kind of market "Hair on Fire": the need is clear and urgent, users are already actively comparing existing products, and so the field is crowded; the way to win is that "best-in-class products stand out because they are different, not merely better," meaning **by being different, not just better**. **[Fact]** Source: https://www.sequoiacap.com/article/pmf-framework/

**Direct implication for BriefPilot:** **[Inference]** "Meeting → tasks" is a typical Hair on Fire field (users are already comparing Feishu Minutes, Otter, and Fireflies). By Sequoia's logic, it is almost impossible to win on this road by merely doing "slightly more accurate action item extraction." We must find a point of difference that incumbents **structurally do not address** (a different user group, a different workflow, a different trust mechanism), or switch to the "Hard Fact" path (pain points that users have already resigned themselves to and do not think can be solved). This judgment is the core proposition that later market research and user research must validate.

---
## 2. Core Theory Toolbox (for each tool: what it is, why it is useful, how to use it, a counterexample)

### 2.1 Jobs To Be Done (JTBD): Christensen's "Hiring" Perspective

**What it is. [Fact]** Clayton Christensen argued for segmenting markets by the "job" a user hires a product to do, rather than by demographics. In his words: "The fact that you're 18 to 35 years old with a college degree does not cause you to buy a product." Source: https://www.library.hbs.edu/working-knowledge/clay-christensens-milkshake-marketing

**Classic case (the milkshake). [Fact]** A fast-food chain first profiled the "typical milkshake customer" and asked them whether they wanted the shake thicker or thinner. It changed the product, and sales did not move. The researchers then spent a full day observing one store and found that 40% of milkshakes were sold in the early morning, mostly to commuters buying to go. When they interviewed these people the next morning, they found that the job they "hired" the milkshake for was this: the commute is long and boring, they need something to occupy their other hand and keep them from getting hungry until noon, and it must not dirty their work clothes, since only one hand is free. The milkshake beat bagels and donuts because it is clean, filling, and can be sipped slowly through a straw. Source: same as above.

**Why this case matters to us. [Inference]** It shows three things: (1) asking "what kind of product do you want?" yields noise at the solution level; (2) **observation** (spending a whole day in the store) came before interviews and uncovered "time + context" as the real segmentation dimension; (3) the competitor is not "other milkshakes" but bagels and donuts, so **competitors are defined by the job, not by the product category**. For BriefPilot, the competitor to "meeting minutes → action items" may not be Otter, but "posting a message in the group chat after the meeting," "handwriting it in Notion," or "not writing it up at all."

**How to use it.** The 2016 HBR article "Know Your Customers' 'Jobs to Be Done'" (Christensen, Hall, Dillon, Duncan) gives several directions for where to look for jobs. **[To be verified]** I could only open the article's abstract page (https://hbr.org/2016/09/know-your-customers-jobs-to-be-done); the full text is behind a paywall. Secondary sources commonly paraphrase the directions as five: jobs close to oneself, jobs that compete with "doing nothing," workarounds users build for themselves, jobs users want to avoid, and unintended uses of the product. These five are used in this document's checklist, but please treat them as a "widely circulated paraphrase" rather than a quotation from the original.

**Counterexample.** Taking "I want a faster horse" as a need (a solution disguised as a need). The Chinese PM community also lists this as a typical false-need trap. **[Fact]** Source: https://www.woshipm.com/share/5919552.html

### 2.2 Bob Moesta's Four Forces Model and the Switch Interview: Understanding "Why People Switch"

**What it is. [Fact]** Bob Moesta and Chris Spiek proposed the Four Forces model: a user switches only when "forces for change > forces against," that is, **Push + Pull > Anxiety + Habit**.
- Push: "The push is the problem with the current situation."
- Pull: "The pull is the magnetism of the new way."
- Anxiety: "Anxiety is the fear of the unknown."
- Habit: "Habit is the comfortable inertia of what people already know and do."
Source: https://jobstobedone.org/the-four-forces/

**Why it is useful. [Inference]** Differentiation does not happen only on the Pull side (better features). If target users cannot give up their current tools because of Anxiety ("Will the AI assign tasks to the wrong person?", "Will the recording leak experiment data?") or Habit ("the lab has always used a WeChat group + Excel"), then **reducing anxiety or fitting into the existing habit** is itself differentiation. The "draft + human confirmation" and "answer only with citations" features in BriefPilot's original design are essentially Anxiety-side design. This is a direction worth amplifying, but we first need to verify what the target users' anxieties actually are.

**How to use it (Switch interviews). [To be verified]** Secondary sources describe it as follows: interview users who have just switched from A to B (or just abandoned a tool), reconstruct the decision timeline, and identify each of the four forces; within one segment, 10–15 interviews reveal the dominant pattern. Source: https://www.koji.so/docs/switch-interviews-jtbd-method (a commercial blog, used only as a method reference). Q7 in BriefPilot's original interview guide ("Have you ever given up on an AI tool?") is a prototype of the Switch interview; we recommend expanding it into a full four-forces timeline.

### 2.3 Teresa Torres: Opportunity Solution Tree (OST) and Continuous Discovery

**What it is. [Fact]** An OST has four layers: (1) the desired outcome (we recommend a "product outcome" that measures user behavior or attitude); (2) the opportunity space: user needs, pain points, and desires that can drive the outcome; (3) the solution space; (4) assumption tests. "In this context, an opportunity is an unmet customer need, pain point, or desire." Source: https://www.producttalk.org/2016/08/opportunity-solution-tree/

**Key criteria. [Fact]**
- The test for telling an opportunity from a solution: **can this be solved in more than one way?** If not, it is most likely a solution in disguise.
- Opportunities must come from user stories, not from team assumptions.
- Opportunities are assessed on four types of factors: opportunity size (how many users, how often), market factors, company factors (fit with mission/strategy), and customer factors (importance + satisfaction with current solutions). **Do not account for effort yet**; effort is assessed later, at the solution stage.
- "Don't rule out an opportunity too early."
Source: same as above.

**Interview method. [Fact]** Torres advocates story-based interviews. The core prompt is "Tell me about the last time..." and the scope can be narrowed by outcome (example: the last time you watched Netflix on the road). Her rationale: "Humans are not good at accurately answering direct questions out of context." The golden rule of interviewing is "let the interviewee talk about what matters most to them." Source: https://www.producttalk.org/best-customer-interview-questions/. She defines "continuous discovery" as the product team having contact with users at least once a week. **[To be verified]** This definition comes from a secondary paraphrase on a course page: https://producttalk.org/course/continuous-interviewing

**Counterexample.** Treating "we need an AI meeting assistant" as an opportunity: it has only one way to be solved, so it is a solution. A real opportunity would be written as "within 24 hours after a meeting, nobody remembers who promised to do what."
### 2.4 Dan Olsen's PMF Pyramid and the "Importance × Satisfaction" Framework

**What it is. [Fact]** The five-layer pyramid, from bottom to top: target customer → underserved needs → value proposition → feature set → UX. The bottom two layers are the market; the top three are the product. The Lean Product Process has six steps: determine target customers → identify underserved needs → define the value proposition → specify the MVP feature set → create an MVP prototype → test with customers. Source: https://www.mindtheproduct.com/the-playbook-for-achieving-product-market-fit/

**Importance vs. satisfaction. [Fact/To be verified]** Olsen's framework places each need on a two-dimensional chart of "importance to the customer" × "satisfaction with existing alternatives"; the **high importance + low satisfaction** quadrant is the opportunity zone. A secondary source puts it this way: importance is a problem-space concept, while satisfaction is a solution-space concept; delivered value = importance × satisfaction, and remaining opportunity = importance × (1 − satisfaction). Source (secondary): https://productandrew.substack.com/p/product-75 . I have not checked the original book for chapter numbering or the details of the scoring scale, so this is marked **[To be verified]**.

**Ulwick's quantified version. [Fact]** Strategyn (Anthony Ulwick) gives an opportunity algorithm: **Opportunity = Importance + (Importance − Satisfaction)**, where both importance and satisfaction use the "top-two-box" share (the percentage of respondents who rate an outcome "very/extremely important" or "very/extremely satisfied"). "Underserved" refers to outcomes that are "important to the customer but not well satisfied." Source: https://strategyn.com/quantify-your-customers-unmet-needs . Note: the thresholds circulating online (>15 excellent, 12–15 low-hanging fruit, or >10 underserved) conflict across sources, and the Strategyn page itself gives no numeric thresholds, **[To be verified]**.

**Why this is useful for differentiation. [Inference]** Competitors all do "meeting to tasks," but "does it" does not mean "satisfaction is high." The first candidate source of differentiation is therefore to look, within the features competitors already cover, for specific sub-steps where users rate **importance high but satisfaction low** (for example, "action items assigned to the wrong person," "tasks across multiple meetings are not merged," "no provenance, so nothing can be checked"). This is exactly the question that G2/Reddit review mining has to answer.

### 2.5 The Kano Model: Judging Whether "Building It Makes Users More Satisfied"

**What it is. [Fact]** Proposed by Noriaki Kano in 1984. Five attribute types: must-be (done well, users don't notice; done badly, extreme dissatisfaction), one-dimensional/performance (the better it is, the more satisfied users are), attractive (a delight if present, no complaint if absent), indifferent, and reverse (too much of it makes users less satisfied). The questionnaire asks a pair of questions for each feature: "How would you feel if you had…?" (functional) and "How would you feel if you did not have…?" (dysfunctional), with five answer options: like / expect it / neutral / can tolerate / dislike. Combinations map as follows: expect it + dislike → must-be; like + dislike → one-dimensional; like + neutral → attractive; neutral + neutral → indifferent. Attractive attributes decay into one-dimensional and then into must-be as competitors make them common. Source: https://en.wikipedia.org/wiki/Kano_model

**How to use it for differentiation. [Inference]** For meeting-assistant products, "accurate transcription" and "summary generation" are very likely already **must-be** attributes (users don't notice them when present, and give bad reviews when absent), so investing in them produces no differentiation. Differentiation should go into attributes that target users see as **one-dimensional or attractive**. But which attributes are attractive for a "research lab" and indifferent for a "product team" must be validated with a Kano questionnaire split by segment, and cannot be assumed in advance.

**Counterexample.** Treating a lift in transcription accuracy from 95% to 97% as differentiation: marginal investment in a must-be attribute does not buy satisfaction.

### 2.6 "Hair on Fire" and the Sequoia Arc's Three Archetypes: Judging Which Path You Are On

**What it is. [Fact]** A 2016 article by Seibel relays Sequoia's view: the ideal user has their "hair on fire," with a problem so urgent they will accept a half-baked v1 ("You need to find problems so dire that users are willing try half-baked, v1, imperfect solutions."). Real PMF shows up as usage growing faster than the team can keep up with. Source: https://www.ycombinator.com/blog/the-real-product-market-fit

The Sequoia Arc framework's three archetypes (source: https://www.sequoiacap.com/article/pmf-framework/ **[Fact]**):

| Archetype | User mindset | Competition | How to win | Examples |
|---|---|---|---|---|
| Hair on Fire | Already actively solving the problem and comparing products | Crowded | Strong product + fast GTM, "different, not just better" | Wiz, Rippling |
| Hard Fact | Has accepted the pain point as a "fact of life" and is not actively looking for a solution | Fewer | Educate the market first, then harvest; the solution must be "new enough and the problem important enough" | Square, HubSpot |
| Future Vision | Doesn't see the problem, or thinks the solution is a pipe dream | The obstacle is disbelief | Find commercially tractable "gas stations" along the way | Nvidia, OpenAI |

**Judgment framework for this project. [Inference]** If user research finds that the target segment (for example, labs) reacts to "nobody remembers the action items after the meeting" with "that's just how research is, everyone's like this," then it is Hard Fact, not Hair on Fire. That is both bad news (no ready-made urgency) and good news (incumbents won't attack here). This needs to be probed explicitly in interviews: is the user "actively looking for a tool," or "long since resigned to it"?

### 2.7 The Sean Ellis PMF Survey and the Superhuman PMF Engine: Closing the Loop from "Discovery" to Measurement

**The Sean Ellis survey. [Fact]** The core question: "How would you feel if you could no longer use [product]?" Options: very disappointed / somewhat disappointed / not disappointed / no longer use. Ellis benchmarked nearly 100 startups and found that companies struggling to grow were almost all below 40% "very disappointed," while companies with strong growth were almost all above 40%. Respondents should be users who have experienced the core value, used the product at least twice, and used it within the last two weeks; about 40–50 responses give a "directionally correct" reading, though it may be off by 10–15 percentage points. Source: https://learningloop.io/plays/product-market-fit-survey . **Known criticisms** (same source): early users may answer based on the "promised solution" rather than the actual product; surveying only power users inflates the result (Buffer's first survey of top users gave 78%, which it admitted was skewed); and it measures existing users' dependence, not retention, willingness to pay, or the needs of non-users.

**Superhuman's PMF engine (first-hand). [Fact]** Source: https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit
1. In summer 2017 they sent a four-question survey to users who had used the product twice or more in the past two weeks (the Q1 above + "what type of person would benefit most" + "what is the main benefit you get" + "how can we improve"); only **22%** answered "very disappointed."
2. They grouped respondents by their Q1 answer and tagged each with a persona, kept only the personas from the "very disappointed" group (founders, managers, executives, BD), and the score rose to **33%**; they then used Julie Supan's HXC (high-expectation customer) framework, writing the ideal user profile from the Q2 answers.
3. They analyzed the feedback: "very disappointed" users valued speed, focus, and keyboard shortcuts most; for users who were "somewhat disappointed but valued speed," the biggest blocker was the lack of a mobile app. They **ignored** the not-disappointed users and the users who did not value speed. Half the roadmap went to "what users already love" (faster, more shortcuts, automation), and half to "what holds users back" (mobile, integrations, attachments, calendar, unified inbox, search, read receipts).
4. Each new user is surveyed only once; the "very disappointed" share was made the sole KR in the product team's OKR; the survey is rerun every quarter. After three quarters it reached **58%**.

**Why this method matters for "finding differentiation." [Inference]** It provides an **actionable narrowing algorithm**: don't try to make everyone satisfied; find the small group who would be "very disappointed," describe them, and optimize only for them. This is the same thing as PG's "deep well rather than shallow pond" ("well" vs "broad but shallow," source https://paulgraham.com/startupideas.html ). For BriefPilot, the equivalent move is: at the demo stage, finding just 5–10 lab members or small teams who would be "very disappointed" if the product were taken away is worth more than 100 users who think it is "fine."

---
## 3. First-Hand Pain Point Collection Methods (Interviews, Observation, Diaries, Forum Mining)

### 3.1 The Mom Test: Keeping Interviews from Being Fooled by Polite Lies

**Three rules. [Fact]** (Source: https://mtlynch.io/book-reports/the-mom-test/, a detailed book summary; the book's official site https://www.momtestbook.com/ only has an introduction)
1. "Talk about their life instead of your idea."
2. "Ask about specifics in the past instead of generics or opinions about the future."
3. "Talk less and listen more."

**Three kinds of bad data to discard. [Fact]** (Same source)
- **Compliments**: "the fool's gold of customer learning: shiny, distracting, and worthless."
- **Fluff**: generics ("I usually/always/never"), future promises ("I would"), and hypotheticals ("I might"). Countermeasure: pull the conversation back to one specific past instance.
- **Ideas / feature requests**: do not take them at face value; dig into the motivation behind them.

**Good questions vs. bad questions. [Fact]**
- Don't ask "Would you use it?"; ask "How do you handle this problem now, and which alternatives have you tried?"
- Don't ask "How much would you pay?"; ask "How much is this problem costing you right now?"
- At the end, ask "Who else should I talk to?" and "Is there anything I should have asked but didn't?"

**Commitment & advancement. [Fact]** A conversation succeeds not when the other person says "good idea" but when they give up something they value: time (scheduling a follow-up or a trial), reputation (introducing a decision-maker or giving a public endorsement), or money (a letter of intent, pre-order, or deposit), or when they move to the next step of your real funnel. Being turned down is also useful information; "the only failure is not asking."

**Counterexample (a risk in this project's original outline). [Inference]** In the original interview-guide.md, Q4 "If an AI gives you an answer, what evidence would you need before you were willing to use it?" and Q6 "How much longer would you be willing to wait?" are both hypothetical questions about the future, and by the Mom Test standard they are the kind of phrasing that tends to produce fluff. Suggested rewrite: "When was the last time an answer from an AI or a colleague turned out to be wrong? What happened? What did you change afterward?"

### 3.2 YC "How to Talk to Users" (Eric Migicovsky)

**[Fact]** The speaker of this YC Startup School talk is Eric Migicovsky (founder of Pebble). The timestamps in YC's official recap include "five questions for user interviews," the first of which is "What's the hardest part about doing the thing you're trying to solve?" Source: https://www.ycombinator.com/blog/startup-school-week-1-recap-kevin-hale-and-eric-migicovsky. Migicovsky's own blog notes that the talk is "based on The Mom Test." Source: https://ericmigi.com/blog/startup-school-how-to-talk-to-users

**[To be verified]** The remaining four questions are commonly paraphrased in secondary sources as: "Tell me about the last time you ran into this problem," "Why was that hard?," "What have you done to solve it?," and "What don't you like about the solutions you've tried?" I could not check the wording against the original YC video, so treat these as reference only.

### 3.3 Contextual Inquiry and Observation

**[Fact]** NN/g defines it as follows: the researcher observes and interviews users in their own work environment, using an "apprenticeship" model in which the user is the craftsperson and the researcher is the apprentice. Four principles: context (in the natural environment), partnership (the user is not fully directed by the researcher), interpretation (understanding is confirmed together with the user), and focus (a clear research purpose). Four-stage flow: introduction → switch to work mode (and tell the user you will interrupt with questions) → alternate between observation and open-ended questions → wrap up by restating interpretations so the user can correct them. It suits complex systems, deep processes, and expert users; because people cannot accurately recall automated habits, observation reveals "things you wouldn't think of." Risks: the user slips from "demonstrating" back into "describing," the session turns into a complaint session, the researcher brings in assumptions, and the researcher's reactions change the user's behavior. Source: https://www.nngroup.com/articles/contextual-inquiry/

**Why this matters especially for this project. [Inference]** The user is a member of a research lab, which means contextual inquiry can be done **at zero cost**: group meetings, 1:1s with the advisor, and discussions after reading papers are all "meetings" that can be observed directly. The lesson of the milkshake case is to spend a whole day on site first and only then ask questions. The T1–T3 task observations in the original research-plan are a good starting point, but they use fictional Project Orion material; for the lab segment, they should be replaced with the user's own real group meetings (anonymized).

### 3.4 Diary Study

**[Fact]** NN/g: participants record entries themselves, at the time of the event or as soon as possible afterward, over a period ranging from a few days to a month or more. Suited to habits and frequency, attitudes and motivations, change over time, cross-channel/tool use, and external factors (such as collaboration and competing tools). Three ways to trigger entries: event-triggered (log every time it happens), fixed-interval, and signal-triggered (the researcher sends reminders, i.e., experience sampling). Costs: complex planning, possible dropout, higher incentives needed, and large volumes of data. Planning steps include deciding on the logging moments, duration, number and profile of participants, incentives and requirements, tools, communication templates, a pilot, a pre-study briefing, and an exit interview. Source: https://www.nngroup.com/articles/diary-studies/

**How to use it in this project. [Inference]** "Action items lost after meetings" is a phenomenon only visible across days (said in the meeting → nobody acts on it three days later → raised again at the next meeting). One-off interviews rely on recall and tend to underestimate frequency. I suggest having 3–5 lab members keep an event-triggered diary for 2 weeks: "After each meeting, spend 1 minute noting who promised what, where it was recorded, and whether anyone followed up on it before the next meeting." This directly yields first-hand numbers for "frequency × omission rate."

### 3.5 Forum and Review Mining (Reddit / G2 / Zhihu / Xiaohongshu)

**Method. [Fact / To be verified]** Several independent founder blogs describe a consistent method: read competitors' 1-star and 2-star reviews and Reddit complaint threads, log each recurring complaint in a spreadsheet (one guide suggests about 2 hours a day, accumulating 100+ entries), look for patterns, and then validate them in communities where the target users gather. Sources: https://www.wearefounders.uk/stop-guessing-what-people-want-how-to-validate-startup-ideas-using-real-complaints/, https://thebuildingblocks.substack.com/p/find-your-next-killer-feature-in. Indie Hackers has a post specifically about "borrowing SaaS ideas from 1-star reviews," but it was blocked with a 403 when I tried to fetch it, so its content is **[To be verified]**: https://www.indiehackers.com/post/want-a-saas-idea-that-sells-borrow-it-from-1-star-reviews-e1144022b7

**Judgment criteria and limitations. [Inference]** Review mining is good at answering "where do incumbents leave people dissatisfied" (low satisfaction) and poor at answering "which needs no product covers" (because nobody reviews a nonexistent product on G2). So it should be paired with observation and diaries: the former finds "sub-steps that can be improved," the latter finds "scenarios nobody covers." Also: complaining ≠ paying, so willingness to pay must be validated separately. Because the search quota ran out this round, specific negative reviews of Otter/Fireflies/Feishu Minutes have **not** actually been scraped yet; that is a task for `01_market-research`.
### 3.6 Supplementary Frameworks from the Chinese PM Community

**[Fact]** A commonly used judgment framework on Everyone Is a Product Manager (人人都是产品经理, woshipm): a real need (directly addresses a core pain point, receives a lot of feedback, is used frequently); a false need ("seems to solve the user's problem but does not actually touch the core of the pain point", only a few users give feedback, there are clicks but low usage, users don't know how to operate it during prototype trials); and a weak need (solves some problem but not a core pain point for most users). Typical counterexamples: "weather sharing" in social apps, "3D virtual try-on" in e-commerce, and "gesture controls" in office software. Source: https://www.woshipm.com/share/5919552.html

**[Fact]** Another article gives a multi-dimensional qualitative checklist: judging value added or lost; "prioritize needs that are high-frequency and mass-market"; the negation test ("what happens if we don't build it?"); the payment test (whether users are willing to spend money, effort, or time on the solution, with a recommendation to validate quickly via an MVP); the human-nature test (probing deeper motivations); and prioritization by number of users, frequency, and whether the need sits on the main path. Source: https://www.woshipm.com/pmd/4202698.html

**[To be verified]** Liang Ning's *30 Lectures on Product Thinking* defines a pain point as the "fear" that arises when a need goes unmet, and a "thrill point" (爽点) as the feeling of a need being satisfied immediately. These are secondhand accounts (sources: https://www.36kr.com/p/1722246545409 , https://www.woshipm.com/user-research/4209603.html ). No reliable source was found in this round for the definition of an "itch point" (痒点).

---

## 4. Judging Real vs. False Needs: Frequency × Intensity × Willingness to Pay, and How to Measure Each

This section consolidates the criteria from all the schools above into one table. **Note: the "multiplication" in this table is this document's own synthesized framework [Inference], not a direct quote from any single source.**

| Dimension | What it answers | How to measure (prefer first-hand behavioral evidence) | Threshold / decision line | Common false evidence (discard) |
|---|---|---|---|---|
| **Frequency** | How often the problem occurs | Counts from diary studies; interview questions like "when was the last time, and the time before that?"; number of mentions in competitor reviews | Weekly or more often counts as high frequency (**[Inference]**, no general threshold in any source) | "I run into this all the time" (fluff) |
| **Intensity** | How costly it is when it happens | Mom Test: "How much is this problem costing you right now?" (time, money, relationships, reputation); failures/rework seen in observation; how strong the Push is in the Four Forces | The user already uses a **workaround** or already pays for a substitute = strong; "resigned to it" = Hard Fact (strong but not urgent) | Compliments, "it would be nice if there were one" |
| **Willingness to pay / commitment** | Whether they will invest to solve it | The Mom Test's three currencies of commitment: time (scheduling a next meeting/trial), reputation (introductions), money (pre-orders/deposits); fake-door / landing-page / pre-sale tests | At least a time or reputation commitment; a money commitment is strongest | "I'd definitely buy it" (a future promise) |
| **Reach (number of users)** | How many similar users exist | Surveys after segmentation; community size; reachable channels | PG: first find a "deep well", then breadth; it may be small at the start but needs a path to expand | Substituting a large TAM figure for concrete, reachable users |
| **Current satisfaction** | How well incumbents solve it | Olsen/Ulwick importance × satisfaction survey; negative reviews on G2/Reddit | High importance + low satisfaction = opportunity | A "has / doesn't have" comparison of competitor feature lists |

**Three strong signals (synthesized from multiple sources, [Inference])**
1. **The user has already built their own workaround** (an Excel sheet, @-mentions in a chat group, handwritten sticky notes). This is the most reliable of the "where to find the job" cues as relayed from Christensen, and also evidence that the Push in the Four Forces already exists.
2. **The user already pays for a substitute or spends significant time on it.** This is the Mom Test's "what the problem costs right now."
3. **The user proactively asks for a next step** ("let me know when it's ready", "I can have our group try it first"). This is the Mom Test's advancement.

**Four typical counterexamples**
- **"Sitcom-style" ideas** (PG): they sound plausible and friends say "I can imagine using it", but no one actually uses them. Source: https://paulgraham.com/startupideas.html
- **Treating a solution as a need**: "We need an AI assistant" (Torres's "only one possible solution" test).
- **Skewed survey respondents**: asking only the most enthusiastic users yields 78% (the Buffer case). Source: https://learningloop.io/plays/product-market-fit-survey
- **Piling on features to chase trends**: "gesture controls" in office software (the woshipm case).

---

## 5. Playbook: 8 Steps to Discovering a Good Product

Each step gives: purpose, tools/templates, pass criteria, and a counterexample. Time estimates are **[Inference]**, assuming one person working part-time.

### Step 1: Start from your own problems and the "schlep" (1–2 days)
- **Purpose**: Produce 10–20 candidate problems, not candidate products.
- **Tools**: PG's three questions: Do I want this myself? Can I build it? Why hasn't anyone else built it? (Source: https://paulgraham.com/startupideas.html ); the schlep blind-spot question: "What problem do I wish **someone else** would solve for me?" ("what problem do I wish someone else would solve for me?", source: https://paulgraham.com/schlep.html ); "live in the future and build what's missing": the user is writing a VLA survey and sits at the frontier of a fast-changing field, which is exactly the position from which PG says one can "see gaps others can't."
- **Pass criteria**: Each problem can be written as "who + in what situation + stuck at which step + how they currently make do."
- **Counterexample**: Working backward from the product name "AI meeting assistant" to find problems.

### Step 2: Define the desired outcome and set up the OST skeleton (half a day)
- **Tools**: Torres's OST. Put a single **product outcome** at the root node (for example, "number of confirmed completed action items per week for the target team", which is consistent with BriefPilot's original North Star), and leave the second layer empty until interviews fill it in.
- **Pass criteria**: The root node is a measurable user behavior, not a feature.
- **Counterexample**: Writing "ship the meeting-to-task feature" at the root node.
### Step 3: Observe first, then interview (1–2 weeks, in parallel with Step 4)
- **Tools**: Contextual inquiry (the four NN/g principles and four-phase flow); for the lab segment, directly observe 2–3 real group meetings plus the group chat/document changes in the 48 hours after each meeting.
- **Recording template**: Time | Who made which commitment | Where it was recorded (blank if not recorded) | Status after 48h | Workaround the user built themselves.
- **Pass criterion**: See at least 3 complete chains of "action item created → lost/survived."
- **Counter-example**: Running task tests only on fictional material (Project Orion) and never looking at real meetings.

### Step 4: Mom Test–style interviews + Switch interviews (6–10 people, 2 weeks)
- **Tools**: Story-style opener "Tell me about the 24 hours after your last meeting"; Migicovsky's "What's the hardest part?"; four-forces timeline (the last time you switched or abandoned a tool); ask for a commitment at the end (referral / next session / trial).
- **Sample**: Reuse the stratification and stopping rule from the original research-plan (stop after 6 people if 2 consecutive interviews yield no new themes). Add one new stratum: **research lab vs. small company team**, at least 3 people each, to enable comparison.
- **Pass criterion**: Each interview yields at least 1 concrete past event + 1 description of a workaround + 1 commitment (or an explicit refusal).
- **Counter-example**: Asking "Do you think AI Q&A with citations is useful?"

### Step 5: Diary study to measure frequency (2 weeks, 3–5 people)
- **Tools**: NN/g event-triggered diary; a 1-minute form after each meeting.
- **Pass criterion**: Obtain, per person, the number of meetings per week, the number of action items generated, the share recorded within 48h, and the share followed up on/completed one week later.
- **Counter-example**: Substituting an interviewee's "I probably lose two or three a week" for measured data.

### Step 6: Competitor review and community mining (3–5 days)
- **Tools**: G2/Capterra/App Store/Reddit/Zhihu/Xiaohongshu; for Feishu Minutes, Otter, Fireflies, tl;dv, Notion AI, and others, log 1–2 star reviews one by one; categorize them by "sub-step" (transcription, speaker identification, summarization, action item assignment, integration with task systems, privacy/recording consent, cross-meeting tracking, ...); tag frequency.
- **Pass criterion**: Find ≥3 sub-steps with "complaints that recur and are clearly not covered by incumbents' current roadmaps."
- **Counter-example**: Building only a feature-presence matrix.

### Step 7: Place opportunities on "importance × satisfaction" and segment (2–3 days)
- **Tools**: Olsen two-dimensional chart / Ulwick algorithm (Importance + (Importance − Satisfaction), top-two-box); run a short survey with the interviewees plus 15–30 external respondents; segment by "lab / small company team" and compare; use Kano paired questions to determine which attribute type each candidate differentiator belongs to.
- **Pass criterion**: Find an opportunity that is "high importance + low satisfaction" in one segment but not in another — this is a candidate for **user differentiation**; or a sub-step that is "high importance + low satisfaction" in all segments yet that incumbents do not address — this is a candidate for **feature differentiation**.
- **Counter-example**: Averaging scores across all users together (the Superhuman lesson: mixing segments hides the group that truly loves you).

### Step 8: Run minimal validation with commitments and a fake door, then decide the demo scope (1 week)
- **Tools**: Send 5–10 of the most pained users a one-page description plus a "you can use it next week" booking; count Mom Test commitment currencies; if feasible, build a landing page/fake door. A PMF survey is **not usable yet** at this stage (Tristan Kromer's critique: early users answer based on commitment).
- **Pass criterion**: ≥5 people give a time commitment (willing to try it in a real meeting); ≥2 people give a reputation commitment (willing to bring in their group or colleagues).
- **Counter-example**: Treating "20 people said they were interested" as validation.

---

## 6. Pain-Point Mining Checklist Ready for This Project

Each item below is tagged with its source method and the type of evidence it is meant to produce. Please backfill them one by one in `02_user-research/`, keeping the [Fact]/[Inference]/[Assumption] labels when you do.

### A. Self-dogfooding checklist (Step 1 + Step 3, done first by the project owner)
1. List all the meetings you attended in the past 4 weeks (group meetings, advisor 1:1s, collaboration discussions). For each, what did you or others "agree to" afterward, and how many of those can you still trace today? Where did the untraceable ones go? [Method: PG's own-problem principle + workaround observation]
2. What do you currently use to track action items (WeChat group / Notion / paper / your head)? When and because of what incident did you set up this "makeshift solution"? [Four forces: Push/Habit]
3. When was the last time you paid a price because you "forgot who agreed to do what" or "couldn't find the basis for a decision"? What was the cost (redoing an experiment, missing a deadline, embarrassment)? [Mom Test cost question]
4. What is the meeting- or knowledge-related thing you **wish someone else would solve for you** but are too lazy to do yourself? [Schlep blindness counter-question]
5. Have you tried Otter / Feishu Minutes / Notion AI? Why didn't you keep using it? Which specific occasion made you give up? [Switch interview]

### B. Observation checklist (Step 3, for 2–3 real group meetings)
6. How many commitments were explicitly stated in the meeting? How many were written down anywhere within 48 hours afterward? [Frequency + omission rate]
7. Were the "owner" and "due date" of each commitment made clear in the meeting? What share were unclear? [Corresponds to the owner/due_date field assumptions in the original PRD]
8. Did anyone "send a follow-up" summary in the group chat/email after the meeting? Who sent it? Did anyone reply? [Existing workaround]
9. Were there moments in the meeting when someone referred to something "said last time" but no record could be found? How long did it last? [Authenticity of knowledge Q&A J1]
10. Was the meeting recorded / was recording allowed? What was everyone's attitude when unpublished data was involved? [Clues for differentiation on the Anxiety side]

### C. Interview checklist (Step 4, ≥3 lab members + ≥3 small company team members)
11. "Tell me about the 24 hours after your last meeting." (No mention of AI or any product)
12. "What was the hardest part of that? Why was it hard?"
13. "When was the last time an action item from a meeting got lost, or you couldn't find the basis for something, and it caused a problem? How did you handle it afterward?"
14. "What do you use to get by right now? When and why did you start doing it that way?"
15. "Have you ever used or abandoned a meeting or note-taking AI tool? Walk me through the last time before you gave up." (Four-forces timeline)
16. "In your setting, what must never be done automatically by AI? When was the last time AI or a colleague did something on your behalf that they shouldn't have?" (Replaces the hypothetical phrasing of the original Q4/Q5)
17. Closing: "If next week I built something that only solves [the thing you just described], would you be willing to try it at your next group meeting?" "Who else should I talk to?" [Commitment + snowballing]
### D. Diary Form (Step 5, 1 minute after each meeting)
18. Meeting type | Duration | Commitments produced | Where you recorded them (blank = not recorded) | Did it involve "what was said last time" that required digging through records | One sentence: the most annoying thing

### E. Review-Mining Record Sheet (Step 6)
19. Product | Platform | Star rating | Verbatim quote | Sub-step tag | User identity clues (research / education / small team?) | Mentions privacy / recording / data? | Mentions wrong task ownership? | Mentions cross-meeting tracking?

### F. Need Validity and Segment Scoring Sheet (Step 7)
20. For each opportunity: Frequency (weekly?) | Intensity (existing workaround? already paying?) | Commitment (how many currencies obtained) | Segment differences (lab vs. company) | Importance top-2-box | Satisfaction top-2-box | Ulwick score | Kano category | Covered by incumbents? | Sequoia archetype (Hair on Fire / Hard Fact)

### G. Answer Template for the Interviewer's Question (final output, fill in with evidence)
> "Feishu Minutes / Otter / Fireflies solve [the job they cover]. From [n] real group-meeting observations and [m] interviews, I found that users in [a specific segment] rate [a specific sub-step] at importance [x] and satisfaction [y]. They currently get by with [workaround], and [k] of them are willing to try it in a real meeting next week. Incumbents don't address this because of [structural reason]. So what I'm building is not 'yet another meeting assistant' but [one-sentence differentiation]."

---

## 7. Direct Implications for BriefPilot v2 (Strictly Graded)

**[Fact]**
- The existing PRD and interview guide both explicitly state HYPOTHETICAL and that no real users have been interviewed yet (see the earlier v1 docs (not included) and `docs/research/interview-guide.md`).
- The existing North Star (confirmed completed tasks per active team per week) is compatible with Torres's definition of a "product outcome" and can serve directly as the root node of the OST.

**[Inference]**
- "Meeting → tasks" is a Hair on Fire track in the Sequoia sense, so differentiation must be "different" rather than "better"; investing in transcription and summarization, which are now table-stakes attributes, will not produce differentiation.
- The original BriefPilot design choices of "draft + human confirmation," "answer only with citations," and "refuse to answer" are designs on the Anxiety side of the Four Forces. This is a differentiation direction that can be amplified, provided the target users' anxiety is confirmed to exist and is strong enough.
- Review mining and observation/diary studies are complementary: the former finds sub-steps where incumbents have low satisfaction (feature differentiation), while the latter finds scenarios nobody covers (user differentiation).

**[Assumption] (to be validated in Steps 3–8)**
- H-A: In research labs, action items are lost from group meetings at a frequency of ≥ 1 time per person per week, and the main reasons existing tools have not been adopted are sensitivity around recordings/data (Anxiety) and habit (WeChat groups + Excel), not missing features.
- H-B: Lab members rate "action items must be traceable to who said it in which meeting" (citation/provenance) as significantly more important than small company teams do.
- H-C: At least one sub-step (for example, commitment tracking across multiple meetings, correcting owner attribution, or linking to papers/experiment records) appears repeatedly in competitors' negative reviews with no clear roadmap coverage.
- If any one of the three above is falsified, go back to Step 1 and list candidate problems again, rather than patching the solution.

---

## 8. Source List

**Primary / original-author sources**
1. Paul Graham, How to Get Startup Ideas — https://paulgraham.com/startupideas.html
2. Paul Graham, Schlep Blindness — https://paulgraham.com/schlep.html
3. Paul Graham, Do Things that Don't Scale — https://paulgraham.com/ds.html (this round only read key points such as "recruit users manually" via search snippets, **[to be verified]**)
4. Teresa Torres, Opportunity Solution Trees — https://www.producttalk.org/2016/08/opportunity-solution-tree/
5. Teresa Torres, Ask Teresa: What Are the Best Customer Interview Questions? — https://www.producttalk.org/best-customer-interview-questions/
6. Product Talk, Continuous Interviewing course page (definition of "weekly customer contact," **[to be verified]**) — https://producttalk.org/course/continuous-interviewing
7. jobstobedone.org, The Four Forces — https://jobstobedone.org/the-four-forces/
8. HBS Working Knowledge, Clay Christensen's Milkshake Marketing — https://www.library.hbs.edu/working-knowledge/clay-christensens-milkshake-marketing
9. HBR, Know Your Customers' "Jobs to Be Done" (only the abstract is visible) — https://hbr.org/2016/09/know-your-customers-jobs-to-be-done
10. Michael Seibel / YC, The Real Product Market Fit — https://www.ycombinator.com/blog/the-real-product-market-fit
11. Sequoia, The Arc Product-Market Fit Framework — https://www.sequoiacap.com/article/pmf-framework/
12. First Round Review, How Superhuman Built an Engine to Find Product-Market Fit — https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit
13. Strategyn (Ulwick), Quantify Your Customer's Unmet Needs — https://strategyn.com/quantify-your-customers-unmet-needs
14. Mind the Product, The Playbook for Achieving Product-Market Fit (write-up of a Dan Olsen talk) — https://www.mindtheproduct.com/the-playbook-for-achieving-product-market-fit/
15. NN/g, Contextual Inquiry — https://www.nngroup.com/articles/contextual-inquiry/
16. NN/g, Diary Studies — https://www.nngroup.com/articles/diary-studies/
17. YC Blog, Startup School Week 1 Recap: Kevin Hale and Eric Migicovsky — https://www.ycombinator.com/blog/startup-school-week-1-recap-kevin-hale-and-eric-migicovsky
18. Eric Migicovsky's blog (states that the talk is based on The Mom Test) — https://ericmigi.com/blog/startup-school-how-to-talk-to-users
19. The Mom Test official site (introduction only) — https://www.momtestbook.com/
20. Wikipedia, Kano model (includes citation of the original 1984 paper) — https://en.wikipedia.org/wiki/Kano_model

**Secondary / compiled sources**
21. mtlynch.io, The Mom Test book notes — https://mtlynch.io/book-reports/the-mom-test/
22. Learning Loop, Product-Market Fit Survey (compilation of the Sean Ellis survey, including criticism) — https://learningloop.io/plays/product-market-fit-survey
23. Product Andrew, The Lean Product Playbook summary — https://productandrew.substack.com/p/product-75
24. Koji, Switch Interviews (commercial blog) — https://www.koji.so/docs/switch-interviews-jtbd-method
25. We Are Founders, Validate Startup Ideas Using Real Complaints — https://www.wearefounders.uk/stop-guessing-what-people-want-how-to-validate-startup-ideas-using-real-complaints/
26. The Building Blocks, Find Your Next Killer Feature in G2 Reviews — https://thebuildingblocks.substack.com/p/find-your-next-killer-feature-in
27. Indie Hackers, Borrow SaaS Ideas from 1-Star Reviews (403; body text not read) — https://www.indiehackers.com/post/want-a-saas-idea-that-sells-borrow-it-from-1-star-reviews-e1144022b7
28. Indie Hackers, The Painkiller/Vitamin Analogy — https://www.indiehackers.com/post/the-painkiller-vitamin-analogy-myth-or-fact-b6cd1d84a7
29. Koji, Smoke Tests and Fake Door Tests (commercial blog) — https://www.koji.so/docs/smoke-test-product-validation
30. Everyone Is a Product Manager (woshipm), judging real / fake / weak needs — https://www.woshipm.com/share/5919552.html
31. Everyone Is a Product Manager (woshipm), checklist for judging need value — https://www.woshipm.com/pmd/4202698.html
32. 36Kr repost of Liang Ning's course notes (pain points / "thrill points," secondary) — https://www.36kr.com/p/1722246545409
33. Everyone Is a Product Manager (woshipm), paraphrase of Liang Ning's definition of pain points (secondary) — https://www.woshipm.com/user-research/4209603.html
34. PDMA review of Ulwick's *What Customers Want* (one source of the threshold claims, **[to be verified]**) — https://www.pdma.org/page/review_what_customer

**Internal project files**
- The earlier v1 docs (not included): README, PRD, portfolio case study, interview guide, research plan

---
## 9. Confidence Notes for This Document's Conclusions

**High confidence (checked against the original sources)**: PG's three elements and the "deep well" argument, the schlep question, Torres's four-layer OST and opportunity/solution testing, story-based interview phrasing, the four-forces formula and its four definitions, the milkshake case details (40% sold in the early morning), Sequoia's three archetypes and "different, not better", Superhuman's 22%→33%→58% and its four questions, Ulwick's formula and top-two-box, the five Kano categories and questionnaire mapping, NN/g's four principles of contextual inquiry and three trigger types for diary studies, the Mom Test's three rules, three types of bad data and three currencies of commitment, and the YC lecture's speaker and first question.

**Medium confidence (reliable secondary summaries, original books not checked)**: Sean Ellis's "nearly 100 companies" benchmark and the 40–50 sample size; Olsen's "problem space / solution space" framing of the importance × satisfaction matrix and her value formula; the Chinese community's real-vs-fake demand framework.

**Low confidence / to be verified**: The specific list of "five places to look for a job" in the 2016 HBR article; the wording of the other four questions in Migicovsky's lecture; Ulwick's score thresholds; the "10–15 interviews" sample-size recommendation for Switch interviews; Liang Ning's definitions of pain point / thrill point / itch point; details of PG's *Do Things That Don't Scale*.

**What this document did not do (limited by search quota; recommended for the next round)**:
- Did not look up specific Lenny's Newsletter articles on pain-point discovery (only found third-party summaries).
- Did not actually scrape negative reviews of Otter, Fireflies, and Feishu Minutes on Reddit/G2 (this belongs in `01_market-research`).
- Did not check the latest YC Requests for Startups for entries related to "AI for science / research tools".
- Did not search academic or industry literature on the "say-do gap" to support "observation beats self-report".
- Did not search for writing on founder-market fit / "earned secret" to support "dogfooding as a source of differentiation".

**The single most important judgment in this document ([Inference], not a fact)**: BriefPilot's differentiation is unlikely to come from "converting meetings into tasks more accurately". It is more likely to come from "high importance + low satisfaction for a specific user segment in a specific sub-step", or from a trust mechanism that "lowers switching anxiety". This judgment must be supported or overturned by the first-hand evidence from Steps 3–8; until that evidence arrives, any positioning document should continue to be marked HYPOTHETICAL.
