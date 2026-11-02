---
title: "Market Research 08: Academic Benchmarks and Evaluation Methods for Extracting Meeting Action Items, Decisions, and Commitments (with Positioning of This Project's Evaluation)"
status: draft
sources_count: 55
sources_count_method: "Number of unique URLs in the sources section (recounted at wrap-up; original value 46)"
---

# Market Research 08: Academic Benchmarks and Evaluation Methods for Extracting Meeting Action Items, Decisions, and Commitments

> **Reading notes**
> - This document answers the question left open in 06_研究完整性审查 §7: if I say "I built the first public action-item evaluation," will an interviewer with an NLP background refute it on the spot? Which datasets, annotation schemes, and metrics already exist in academia? Where is the **real increment** of this project's evaluation?
> - Labeling rules follow the rest of the project: **[Fact]** means the original page or PDF was opened in this round, with a URL attached; **[Summary]** means only a search-engine snippet was seen and the original page was not opened; **[Inference]** is derived from facts without direct evidence; **[Assumption·to be verified]** requires an experiment or an inquiry; **to be verified** means the page could not be opened or sources contradict each other. All sources were accessed at the time of writing.
> - **How this round was verified**: WebSearch was available, with about 35 searches run; WebFetch opened about 45 pages. Nine paper PDFs (Purver 2007, Fernández 2008, Liu 2023 AMC-A, MUG 2023, Chen & Hakkani-Tür 2016 AIMU, Azarbonyad 2019, Cohen 2021 AIR, Cohen 2004, Lampert 2008) were downloaded, had their full text extracted locally, and were read passage by passage by keyword. The annotation fields, κ values, and F1 numbers below are therefore the original numbers, not paraphrases of abstracts.
> - **Limitation**: the search cannot be exhaustive. "No benchmark satisfying X, Y, and Z was found" only means "not seen within the search scope listed below"; it does not mean "does not exist". §6 lists the search terms and the sources that were not opened.

---

## 0. Conclusions First

1. **[Fact] The phrase "the first public meeting action-item evaluation" cannot be used.** Public annotations and metrics for meeting action-item detection have existed since 2005:
   - On the ICSI meeting corpus, there is the action-item annotation of Gruenstein et al. 2005 (κ only 0.36), and the four-class sub-act annotation of 18 meetings by Purver et al. 2007 (task description D, timeframe T, owner O, agreement A; κ 0.64–0.78).
   - The AMI corpus allows indirect labels to be derived from the ACTIONS section of its summaries: 101 meetings, 381 action items.
   - In 2023, Alibaba DAMO Academy released the Chinese AMC-A, with 424 meetings and 1,506 action items, and set up an action-item detection track (Track 5 AID) in the ICASSP 2023 MUG Challenge.
   - In 2021, Microsoft released the AIR action-item rewriting dataset, whose public portion has 426 meetings and 2,519 action items.
   - "Commitment/request detection" in the email domain is more mature: Cohen et al. 2004, Lampert et al. 2008, Azarbonyad et al. 2019 (Microsoft), and Smart To-Do 2020 (Microsoft).
2. **[Fact] "Research group meetings" is not a blank space either.** The ICSI corpus itself consists of natural weekly meetings of the Berkeley ICSI research groups (the LDC page's original wording is "natural, regular weekly meetings of various ICSI working teams"; Purver 2007 writes "naturally-occurring research group meetings"). The "Academic" domain in QMSum and MISeD also uses ICSI meetings. So we cannot claim "the first research-group meeting data"; we can only claim "group meetings in the 2020s, with mixed Chinese-English speech, in an LLM-extraction setting".
3. **[Fact] The common form of existing benchmarks is "sentence-level binary classification + positive F1", not "structured field extraction".**
   - AMC-A and MUG label as positive any sentence containing **any one** of task description, time, or owner information. Owner and deadline are **not output as independent fields**.
   - Purver 2007 makes owner and timeframe independent utterance classes, but "who" the owner is is explicitly left as a speaker/addressee identification problem and is not solved.
   - AIR outputs rewritten action-item sentences, not fields either.
4. **[Inference, not seen within the search scope] There are 4 evaluation dimensions for which no public benchmark was found that tests them directly:**
   - (a) When the owner or deadline is missing from the source text, does the model **refuse to guess** (missing-not-guessed rate, fabrication rate)?
   - (b) **Multi-level** grading of commitment strength and its evaluability. In the email domain there are only annotation guidelines for "conditional/indirect commitments", and on the product side only Littlebird's binary split;
   - (c) Recall of key action-item terms in **mixed Chinese-English** meetings. The Chinese-English mixed datasets (SEAME, ASRU 2019, CS-Dialogue, ASCEND) only have ASR transcription annotations and no action-item annotations; the Chinese set with action-item annotations (AMC-A) is pure Mandarin;
   - (d) A side-by-side comparison of **real outputs from multiple commercial products** on the same set of meetings. The only public item is AWS testing "action-item faithfulness" on QMSum with its own Nova models (0.63–0.83), with no cross-product comparison.
5. **Suggested interview wording** (details in §5.1): "Action-item detection in meetings already has benchmarks in academia, such as ICSI/AMI and the Chinese AMC-A. But they evaluate 'which sentence is an action item'. I evaluate three things these benchmarks do not cover: whether the model fabricates when the owner and deadline are missing, whether it can tell strong commitments from weak ones, and whether mixed Chinese-English terms get dropped. And I compared the real outputs of Feishu Minutes, Otter, and other products on the same set of CC BY-licensed meeting audio."
6. **What can be borrowed directly** (details in §5.3):
   - **ICSI** (CC BY 4.0, English research group meetings) as a publicly reproducible English foundation, re-annotating a subset with this project's field-level annotation scheme;
   - **The AMC-A test set** as a comparable Chinese baseline, reporting positive F1 for comparison with the MUG baseline of 66.65 and the paper's best value of 70.82; the data license is **to be verified**;
   - **Purver's D/T/O/A decomposition annotation method** (which raised κ from 0.36 to 0.64–0.78) + **Lampert's conditional/indirect commitment guidelines** (which raised commitment κ from 0.54 to 0.74), used directly as the annotation specification;
   - **MeetingQA2's "unanswerable questions + attribution accuracy"** and **ELITR-Bench's "different WER noise levels + LLM-judge calibration"**, as evaluation design templates for "missing-not-guessed" and "ASR robustness".

---
## 1. Get the terminology straight first (this is where NLP interviewers are most likely to pick holes)

| Term | Common academic definition | Representative work | Relation to this project |
|---|---|---|---|
| **action item** | A proposal and confirmation in a meeting that "someone will do something by some time". Purver 2007 splits it into four utterance types: task description (D), timeframe (T), owner (O), and agreement (A) | Purver 2007; AMC-A 2023 | Core object |
| **AI = commitment or request** | Cohen et al. 2021 (Microsoft): "An AI is a commitment or a request to perform a certain task by any of the parties involved". That is, both "please do it" and "I'll do it" count | AIR 2021 | This project separates requests from commitments: the former need to be claimed by the assignee |
| **commitment (email)** | Azarbonyad 2019 (following Corston-Oliver 2004): a sentence in which the sender promises to do something, which may enter their action items or is worth a reminder. Lampert 2008 also counts sentences that "impose an obligation on a third party" as commitments | Lampert 2008; Azarbonyad 2019 | Synonymous with this project's "commitment tracking" |
| **decision** | Fernández 2008: four decision-related utterance types: issue, resolution proposal, resolution restatement, and agreement | Hsueh & Moore 2007; Fernández 2008 | The object of resolution write-back (Option F) |
| **actionable item** | Chen & Hakkani-Tür (Microsoft): utterances in a meeting that can trigger an assistant action, with 10 intents such as find_email, send_email, and create_calendar_entry | AIMU 2015/2016 | **Not a commitment**; it is intent recognition for voice assistants. Do not conflate them when citing |
| **CommitmentBank (false friend)** | A semantics term: the speaker's degree of certainty that the embedded clause is true; 1,200 discourse items scored on a seven-point scale from −3 to 3 | de Marneffe et al. 2019 | **Unrelated to action items**. The name contains "commitment", but it measures factuality and presupposition projection. Do not cite it wrongly in an interview |
| **hedge / uncertainty** | Whether a sentence carries uncertainty cues (such as may, possibly), and the scope of those cues | CoNLL-2010 shared task | Can be borrowed as weakener-word features and annotation reference for "commitment strength" |

Sources: Cohen 2021 original, §1 (https://aclanthology.org/2021.findings-acl.253.pdf ); Azarbonyad 2019 §3.1 (https://microsoft.com/en-us/research/uploads/prod/2019/01/AzarbonyadWSDM2019.pdf ); Lampert 2008 §2.2 (https://aclanthology.org/U08-1009.pdf ); Fernández 2008 Table 1 (https://aclanthology.org/W08-0125.pdf ); AIMU original (university page; link removed); CommitmentBank (https://github.com/mcdm/CommitmentBank ); CoNLL-2010 is a [Summary] (https://rgai.inf.u-szeged.hu/node/118 ).

---

## 2. Overview table

For the three columns "owner / deadline / strength": ✔ = has a separate field or separate category; △ = the information is part of the criterion for a positive example but is not output separately; ✘ = absent. "Demo usability" is an **[Inference]** based on the license text and is not legal advice.

| # | Dataset / work | Task | Owner | Deadline | Strength | Size | Language | License / access | Demo usability | Reported metrics |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **ICSI Meeting Corpus** | Underlying corpus (transcripts + dialogue acts) | – | – | – | 75 meetings, about 72 hours (LDC); the Edinburgh page says about 70 hours | English (many non-native speakers) | Edinburgh mirror: signals, transcripts, and some annotations under CC BY 4.0; the LDC version LDC2004S02 requires signing a user agreement and paying | **High** (CC BY) | – |
| 1a | Gruenstein et al. 2005 ICSI action item annotation | Action item utterance annotation | △ | △ | ✘ | ICSI subset | English | The AMC-A paper says it is "no longer publicly available" | Low | κ = 0.36; Morgan 2006 used it for classification, F ≈ 0.3 |
| 1b | **Purver et al. 2007** | Action item sub-dialogue detection + summary phrase extraction | ✔ (O-type utterances; specific people not identified) | ✔ (T-type + time phrase extraction) | ✘ (only the A "agreement/commitment" type) | 18 ICSI meetings | English | Annotations not found to be public | Method can be borrowed | Per-type κ 0.64–0.78; per-utterance F < 0.3; sub-dialogue overlap F ≈ 0.5; time phrase F 0.51 / P 0.62 |
| 1c | **AIMU** (Chen & Hakkani-Tür, Microsoft 2015/16) | Actionable intent detection (10 assistant intents + slots) | contact_name in slots | date/start_time in slots | ✘ | 22 ICSI meetings, 21K utterances, 318 positive turns (about 1.5%) | English | The Microsoft link given in the paper is **to be verified** (old research.microsoft.com address) | Low | Binary κ 0.644, overall κ 0.673 |
| 2 | **AMI Meeting Corpus** | Underlying corpus; summaries contain DECISIONS / ACTIONS sections | ✘ (not mentioned on the official annotation page) | ✘ | ✘ | Official page: about 100 hours; the AMC-A paper says 171 meetings (145 scenario-based + 26 natural meetings); Cohen 2021 says 154 meetings | English (including non-native speakers) | Signals, transcripts, and some annotations under CC BY 4.0; **whether the summary annotations fall under CC BY is not stated on the official page (to be verified)** | **High** (transcripts) | – |
| 2a | AMI indirect action item labels | Treats dialogue acts linked to ACTIONS summaries as positive examples | △ | △ | ✘ | 101 meetings, 381 items | English | Derived from AMI's public annotations | Medium-high | StructBERT positive F1 about 38.7–43.1 (AMC-A paper, Table 3) |
| 2b | **Hsueh & Moore 2007/2008** | Decision-related dialogue act detection (AMI DecisionDetector) | ✘ | ✘ | ✘ | AMI subset | English | – | Method can be borrowed | F = 0.35 (2007, as cited in Fernández 2008) |
| 2c | **Fernández et al. 2008** | Decision sub-dialogue detection (four types: I/RP/RR/A) | ✘ | ✘ | ✘ | 17 AMI meetings, 15,680 dialogue acts | English | Annotations not found to be public | Method can be borrowed | κ 0.63–0.73; decision region F = 58%; decision utterances are only 4.3% |
| 3 | **AIR** (Cohen et al. 2021, Microsoft + Bar-Ilan) | Action item detection → rewriting into self-contained sentences using context | Included in the rewritten sentence | Included in the rewritten sentence | ✘ | Full set: 1,020 meetings, 7,957 action items; public part: 426 meetings, 2,519 action items, 7,218 rewrites | English | The paper says "will be made publicly available in the future"; **whether it has been released is to be verified** | To be verified | Systematic human evaluation; BART/UniLM baselines; action items are about 1% of sentences |
| 4 | **AMC-A** (Liu et al. 2023, Alibaba DAMO Academy) | Sentence-level binary classification of action items | △ (including the owner counts as positive) | △ (including time counts as positive) | ✘ | 424 meetings (295/65/64), 306,846 sentences, 1,506 action items | Chinese (Mandarin) | ModelScope `Alimeeting4MUG`; code under Apache 2.0; **data license to be verified** (the underlying AliMeeting audio is CC BY-SA 4.0) | Medium (license must be confirmed) | κ 0.47; positive F1: BERT 64.76, StructBERT 67.84, best 70.82 |
| 4a | **MUG / AliMeeting4MUG** (ICASSP 2023 challenge) | 5 tracks, including Track 5 action item detection | Same as above | Same as above | ✘ | 654 meetings, of which 524 have annotations for all 5 categories; average 10,772.5 tokens per meeting | Chinese | Same as above | Same as above | AID baseline StructBERT: P 62.73 / R 71.1 / F1 66.65 |
| 5 | **AliMeeting** (M2MeT) | Multi-speaker ASR / speaker diarization | – | – | – | 118.75 hours; 212/8/20 meetings; 2–4 participants per meeting | Chinese | OpenSLR 119, CC BY-SA 4.0 | **High** (note the share-alike requirement) | – |
| 6 | **AISHELL-4** | Meeting ASR / speaker diarization | – | – | – | About 120 hours, 211 meetings, 4–8 participants per meeting | Chinese | OpenSLR 111, CC BY-SA 4.0 | **High** | – |
| 7 | **VCSum** (Findings ACL 2023) | Chinese meeting summarization (topic segmentation, titles, segment summaries, full summaries, salient sentences) | ✘ | ✘ | ✘ | 239 meetings, 230+ hours | Chinese | GitHub repository labeled MIT; arXiv paper page labeled CC BY-NC-SA 4.0; **meeting sources and data copyright to be verified** | Medium | Summarization metrics (not checked item by item) |
| 8 | **QMSum** (NAACL 2021) | Query-based meeting summarization | ✘ | ✘ | ✘ | 232 meetings, 1,808 query-summary pairs; three domains: Academic (ICSI) / Product (AMI) / Committee | English | GitHub MIT | **High** | ROUGE, etc. |
| 9 | **MeetingBank** (ACL 2023) | City council meeting segment summarization | ✘ | ✘ | ✘ | 1,366 meetings, 3,579+ hours of video, 6 US cities; 6,892 segment samples | English | HF labeled CC BY-NC-SA 4.0 | Medium (non-commercial) | ROUGE, etc. |
| 10 | **ELITR Minuting Corpus** (LREC 2022) / AutoMin | Automatic minuting | ✘ | ✘ | ✘ | 166 meetings (English 113, Czech 53), 160+ hours, technical project meetings | English, Czech | LINDAT record lists CC BY-NC-SA 4.0 [Summary] | Medium | AutoMin 2023/2025: human + LLM evaluation [Summary] |
| 11 | **ELITR-Bench** (COLING 2025) | Long-context LLM meeting assistant QA | ✘ | ✘ | ✘ | 271 human-written questions, based on ASR transcripts of ELITR meetings, including noisy versions at different WER levels | English | GitHub utter-project organization [Summary] | Medium | GPT-4 judge agrees with humans, but can only distinguish about 3 tiers |
| 12 | **MeetingQA** (ACL 2023) / **MeetingQA2** (Findings EMNLP 2026) | Meeting QA; QA2 is generative and speaker-centric | – | – | – | QA2: 1,033 QA pairs, of which 108 are unanswerable | English | Not verified | Medium | MeetingQA: model F1 57.3 vs. human 84.6 [Summary]; QA2: adds attribution accuracy and factual correctness |
| 13 | **MISeD** (Google, Findings EMNLP 2024) | Information-seeking dialogue over meetings (LLM-generated + human-verified + attributed spans) | – | – | – | 225 QMSum meetings (AMI 134 / ICSI 58 / parliamentary 33) [Summary] | English | Open-sourced on GitHub [Summary] | Medium-high | Attribution quality [Summary] |
| 14 | **Golia & Kalita 2023** | Action-item-driven long meeting summarization | ✘ | ✘ | ✘ | AMI | English | – | – | BERTScore 64.98 (**not** action item accuracy) |
| 15 | **AWS Nova blog** (2025-06-18) | LLM action item extraction, LLM judge | ✘ | ✘ | ✘ | 30 randomly sampled QMSum meetings | English | Vendor blog | Method can be borrowed | Action item faithfulness: Premier 0.83 / Pro 0.80 / Micro 0.70 / Lite 0.63; **no completeness metric** |
| 16 | **SEAME** (LDC2015S04) | Mandarin-English code-switching ASR | – | – | – | About 192 hours, 156 speakers (over 60% Singaporean, the rest Malaysian), spontaneous conversation + interviews | Mandarin-English code-switching | LDC non-member agreement, paid at the price shown after login | Medium (paid, research use only) | CS ASR metrics |
| 17 | **ASRU 2019 Mandarin-English CS Challenge** | Mandarin-English code-switching ASR | – | – | – | 500 hours of Mandarin + 240 hours of Mandarin-English CS (200 train + 40 dev) | Mandarin-English code-switching | Distributed by Datatang to participants; **access after the challenge is to be verified** | Low–medium | MER; on average 8.6 Chinese characters + 1.6 English words per utterance, with English mostly nouns [Summary] |
| 18 | **CS-Dialogue** (2025) | Mandarin-English code-switching spontaneous dialogue ASR | – | – | – | 104.02 hours, 200 speakers, 100 two-person conversations; topics include technology, education, work, etc. | Mandarin-English code-switching | HF `BAAI/CS-Dialogue`: CC BY-NC-SA 4.0 | Medium (non-commercial demos are fine) | Whisper large-v2 zero-shot MER 15.29%; Whisper medium after fine-tuning 7.53% |
| 19 | **ASCEND** (LREC 2022) | Mandarin-English code-switching multi-turn dialogue ASR | – | – | – | 10.62 hours, about 12.3K utterances, 23 speakers [Summary], Hong Kong | Mandarin-English code-switching | HF: CC BY-SA 4.0 | **High** | Best CER 22.69% / MER 27.05% [Summary] |
| 20 | **Singapore NSC** (IMDA) | Singapore English speech (Parts 3–6 are conversation-level) | – | – | – | About 1.2 TB [Summary] | Singapore English, etc. | Application required; third parties cite the Singapore Open Data Licence [Summary], **to be verified** | To be verified | – |
Work on email commitments and requests is listed separately in §3.2. It is not meeting data, but it is the source of the task name "commitment detection".

---

## 3. Item-by-Item Details

### 3.1 English meetings: ICSI / AMI and the action-item and decision research built on them

#### ICSI Meeting Corpus
- **[Fact]** LDC catalog number LDC2004S02: about 72 hours across 75 meetings, recorded 2000–2002. The content is "natural, regular weekly meetings of various ICSI working teams", in English, with many non-native speakers. The license is the LDC User Agreement; the fee is visible after login (https://catalog.ldc.upenn.edu/LDC2004S02 ).
- **[Fact]** The Edinburgh mirror page gives about 70 hours, with signals, transcripts and some annotations released under CC BY 4.0. Close-talk microphone audio, orthographic transcripts and dialogue act annotations can be downloaded (https://groups.inf.ed.ac.uk/ami/icsi/ ).
- **[Fact]** The AIMU paper explains that ICSI contains three kinds of weekly meetings: Bed (Even Deeper Understanding), Bmr (Meeting Recorder) and Bro (Robustness, signal processing) (AIMU paper, LREC 2016; link removed).
- **[Inference] Significance for this project**: this is the **only meeting corpus that is both permissively licensed (CC BY) and made of real research group meetings**. It can serve as an English public foundation for "research group meeting action items": others can reproduce results, and it can be legally uploaded to competing products for comparison. The limitations are that it is over 20 years old, English-only and from the speech research field, so it differs greatly from the mixed Chinese-English group meetings of a 2026 computing lab at the target university.

#### Gruenstein et al. 2005 → Morgan et al. 2006 (first generation of ICSI action items)
- **[Fact, cited secondhand]** Purver 2007 writes that Morgan et al. 2006 classified action items on the ICSI subset annotated by Gruenstein et al. 2005, with "f-scores limited to approximately 0.3, even given manual transcripts and dialogue act tags". The reason is that a task description and its properties are often spread across multiple utterances. Human annotation agreement was also low: "inter-annotator agreement was as low as κ = 0.36" (https://aclanthology.org/2007.sigdial-1.4.pdf ).
- **[Fact, cited secondhand]** Liu et al. 2023 state that only 18 ICSI meetings have action-item annotations, and "these annotations are no longer publicly available" (https://arxiv.org/pdf/2303.16763 ).

#### Purver, Dowding, Niekrasz, Ehlen, Noorbaloochi, Peters 2007 (SIGdial)
- **Task definition [Fact]**: two steps. First detect the subdialogues in which an action item is "proposed and committed to", then extract from them the phrases that summarize the task.
- **Annotation fields [Fact]**: four classes of action item dialogue acts (AIDA): D task description, T timeframe, O owner assignment (to oneself or to others), A explicit agreement or commitment. One utterance can belong to several classes at once.
- **Scale [Fact]**: 18 ICSI meetings annotated by 3 authors; only 1.4% of utterances were labeled with any AIDA class.
- **Agreement [Fact]**: pairwise κ across classes is 0.64–0.78, significantly higher than the 0.36 of Gruenstein 2005.
- **Metrics and results [Fact]**:
  - 4 sub-classifiers + 1 super-classifier (10-utterance window), 18-fold cross-validation, linear SVM;
  - per-utterance F is below 0.3 throughout, and subdialogue "overlap F" is close to 0.5;
  - the best timeframe phrase extraction reaches F 0.51, P 0.62; the baselines are TIMEX annotation (F 0.31) and the whole-sentence 1-best transcript (F 0.39).
- **[Fact] Key quote on owners**: the owner "is more often specified through the interaction itself", typically in forms like "I guess I'll ..." (volunteering) or "Could you maybe ..." (requesting). The paper explicitly says that owner identification "becomes a problem of speaker and addressee identification, which we leave aside for now".
- **[Inference] Significance for this project**: (1) the D/T/O/A decomposition is a ready-made annotation scheme that raised agreement from "unusable" to "usable"; (2) owner attribution was already defined as a hard problem in 2007 and set aside. This project's "do not guess when the owner is missing + the assignee claims it" fits exactly into that gap, and this quote can be cited as academic grounding.

#### AIMU (Chen, Hakkani-Tür, He, Microsoft Research, ASRU 2015 / LREC 2016)
- **[Fact]** On 22 ICSI meetings and 21K utterances, the authors annotated "actionable items" that can trigger assistant actions, covering 10 intents across 5 domains (e.g., find_email, send_email, create_calendar_entry), and annotated slots such as contact_name, date and start_time. 318 turns are positive examples, about 1.5%. Binary κ is 0.644 and overall κ is 0.673. The data link is research.microsoft.com/projects/meetingunderstanding/ (AIMU paper, LREC 2016; link removed).
- **[Inference]** This is the most frequently cited item among "Microsoft's meeting action item research", but it measures **in-meeting assistant intents**, not commitments or action items. If asked in an interview, "Didn't Microsoft already do meeting actionable items long ago?", you need to be able to explain this difference. Whether the original link is still accessible: **to be verified**.
#### AMI Meeting Corpus
- **[Fact]** Official page: about 100 hours of meeting recordings; the signals, transcripts and some annotations are CC BY 4.0, with the caveat "not all annotations are public" (https://groups.inf.ed.ac.uk/ami/corpus/ ).
- **[Fact]** The annotation page lists: dialogue acts, topic segmentation, extractive and abstractive summaries, named entities, body movements, focus of attention, and more. Abstractive summaries are about 200 words and contain four subheadings: ABSTRACT, DECISIONS, PROBLEMS/ISSUES, ACTIONS. Extractive summaries cover about 10% of the full text and link to sentences in the abstractive summary. **The page lists no standalone action item or decision annotation, and no owner or due-date fields** (https://groups.inf.ed.ac.uk/ami/corpus/annotation.shtml ).
- **[Fact] Indirect action item labels**: Following earlier work, Liu et al. 2023 treat "dialogue acts linked to ACTIONS summary sentences" as positive examples, yielding 101 meetings and 381 action items. StructBERT reaches a positive F1 of only 38.67–43.12 on AMI, far below the roughly 70 on AMC-A (https://arxiv.org/pdf/2303.16763 , Table 1, Table 3).
- **[Fact]** Most of AMI consists of scripted scenario meetings: 4 participants play the project manager, marketing expert, user interface designer, and industrial designer of a design team (Fernández 2008 §4).
- **Inconsistent size figures (to be verified)**: The AMC-A paper says 171 meetings (145 scenario + 26 naturally occurring), while Cohen 2021 says 154 meetings / 100 hours. State which figure is used when citing.
- **License reminder (to be verified)**: The official page only says that "some annotations" are CC BY 4.0. This round found no clear statement on whether the ACTIONS summaries are included. A 2006 project newsletter once stated CC BY-NC-SA 2.5 [Summary]; defer to the current official page.

#### Hsueh & Moore 2007/2008; Fernández et al. 2008 (Decision Detection)
- **[Fact, cited second-hand]** On AMI, Hsueh & Moore 2007 labeled as decision-related those extractive-summary dialogue acts that support a decision in the abstractive summary, and obtained F = 0.35 with a maximum entropy classifier (Fernández 2008 §2, https://aclanthology.org/W08-0125.pdf ). Hsueh & Moore 2008 (MLMI) proposed the AMI DecisionDetector [Summary] (https://era.ed.ac.uk/handle/1842/4140 ).
- **[Fact] Fernández et al. 2008**:
  - 17 AMI meetings, 15,680 dialogue acts, about 30 minutes per meeting;
  - Four classes of decision dialogue acts: issue, resolution proposal, resolution restatement, agreement;
  - κ 0.63–0.73 (RP highest, A lowest); decision-related utterances make up only 4.3%;
  - A hierarchical classifier detects decision regions, F = 58% (https://aclanthology.org/W08-0125.pdf ).
- **[Inference]** Decision detection and action item detection are methodologically isomorphic (subclass decomposition + region detection). Option F, "write back resolutions," can directly reuse the I/RP/RR/A annotation scheme.

#### AIR: Automatic Rephrasing of Transcripts-based Action Items (Cohen, Kantor, Hilleli, Kolman; Microsoft + Bar-Ilan; Findings of ACL 2021)
- **[Fact] Task**: Given a meeting transcript and an action item, generate a coherent, self-contained rephrasing. For example, rewrite "I will do it" in context as "X will prepare the presentation by Thursday."
- **[Fact] Data**:
  - Sources: ICSI 75 meetings (722 action items), AMI 145 meetings (461), 206 public board meetings such as LSC (1,283), and 594 internal software development meetings (5,356);
  - Full set: 1,020 meetings, 7,957 action items, 22,038 rephrasings; public portion: 426 meetings, 2,519 action items, 7,218 rephrasings;
  - Both the dev and test sets come from ICSI, on the grounds that ICSI samples have the highest annotation agreement;
  - A regex pre-classifier first filters out 93% of sentences (P 17%, R 90% for action items), then 5 annotators judge the rest; if agreement falls below 80%, 4 more are added;
  - The paper states that action items are "found in roughly 1% of sentences" (https://aclanthology.org/2021.findings-acl.253.pdf ).
- **[Fact]** The paper states that some of the data is sensitive: "while datasets will be made publicly available in the future, some parts of the data cannot be shared". **Whether the public version has been released: to be verified.**
- **[Inference] Relevance to this project**: (1) Of the "Microsoft meeting action item research" mentioned in the task, this is the one that **genuinely targets commitments/requests**; (2) "Rephrasing into a self-contained sentence" essentially means filling the owner and time into the sentence. It does not separately evaluate "whether the owner is correct, and whether one is fabricated when missing"; this project's field-level evaluation can plug in here; (3) Note: the user's task mentions "Cohen et al. 'Learning to detect commitments in email'", but this round **did not find that title**. Related work by authors of the same name is Cohen, Carvalho & Mitchell 2004 (CMU, email speech acts, see §3.2) and this entry, Cohen et al. 2021 (Microsoft, meeting action items). Do not cite that title.
#### Golia & Kalita 2023
- **[Fact]** On AMI, "action-item-driven recursive summarization of long meetings" reached a BERTScore of 64.98, about 4.98% higher than fine-tuned BART. **It evaluates summarization, not action-item extraction accuracy** (https://arxiv.org/abs/2312.17581 ).

### 3.2 Commitment / request detection in email (the source of the term "commitment detection")

| Work | Institution | Task and labels | Data | Agreement | Metrics | Source |
|---|---|---|---|---|---|---|
| **Cohen, Carvalho, Mitchell 2004** (EMNLP) | CMU | Email "speech acts" = verb + noun ontology; verbs include Request, Propose, Amend, Commit, Deliver, plus a Meeting class | CSpace corpus: about 15,000 emails from about 50 teams of 277 MBA students in a 14-week simulated-company course | κ on the N03F2 subset: Meeting 0.82, Deliver 0.75, Commit 0.72, Request 0.81, Amend 0.83, Propose 0.72 | Classification accuracy, etc. | [Fact] https://aclanthology.org/W04-3240.pdf |
| **Corston-Oliver et al. 2004** | Microsoft | Task-oriented email summarization; Azarbonyad 2019's definition of commitment follows this paper | – | – | As relayed by Purver 2007: sentence-level F about 0.6, whole-email about 0.8 | [Fact, cited secondhand] Purver 2007 §2; Azarbonyad 2019 reference [13] |
| **Bennett & Carbonell 2005** (SIGIR poster) / 2007 (HLT-NAACL) | CMU; Bennett later at Microsoft | Email action-item detection: document detection, document ranking, sentence detection | – | – | n-grams (n≤4) + χ² feature selection + position features, up to 10% improvement over unigrams | [Summary] https://www.microsoft.com/en-us/research/publication/detecting-action-items-e-mail/ |
| **Lampert, Dale, Paris 2008** (ALTA) | CSIRO / Macquarie | Requests and commitments; commitments include "obligations imposed by the sender on a third party" | Sample from 250,000 deduplicated Enron emails | Sentence-level commitment κ: 0.54 → 0.74 (after adding explicit guidelines for conditional/indirect commitments); message-level 0.78 | Proposes 8 categories of boundary cases | [Fact] https://aclanthology.org/U08-1009.pdf |
| **Lin, Kang, Gamon, Pantel 2018** (AAAI) | Microsoft | Annotates email intent by "the action the recipient will take" (e.g., reply, schedule a meeting) | IRC, Reddit, email | – | Reparameterized RNN outperforms multi-task baselines | [Summary] https://ojs.aaai.org/index.php/AAAI/article/view/11931 |
| **Azarbonyad, Sim, White 2019** (WSDM) | University of Amsterdam + Microsoft | Sentence-level binary commitment classification: "Does the highlighted sentence contain a specific action that the sender must complete or is obliged to do? (The action must be on the sender and must not already be complete)" | Enron 65,398 sentences (3,337 positive); Avocado 13,021 sentences (4,484 positive, sampled with classifier bias) | Krippendorff α 0.73 | In-domain F1: Enron 0.78, Avocado 0.81; clear drop cross-domain | [Fact] https://microsoft.com/en-us/research/uploads/prod/2019/01/AzarbonyadWSDM2019.pdf |
| **Smart To-Do** (Mukherjee et al. 2020, ACL) | Microsoft | First finds sentences with a commitment classifier, then selects context, and finally generates the to-do | New dataset built on Avocado | – | BLEU 0.23, ROUGE 0.63 | [Summary] https://aclanthology.org/2020.acl-main.767 |

**On "Lin et al. 2022 email/meeting commitments"**: in this round, searching by author, year, and keywords **did not find** this paper. The closest is Lin et al. 2018 (AAAI, Microsoft, email intent). Another easily confused name is COLING 2020's "Lin: Unsupervised Extraction of Tasks from Textual Communication", where "Lin" is the name of the method, not an author (Diwanji et al.) [Summary]. Until the original paper is found, **do not cite "Lin et al. 2022"** in documents or interviews.

**[Fact] The 8 boundary-case categories listed in Lampert 2008** (§4.1–4.8):
1. Locus ambiguity
2. Meeting invitations and notifications
3. Pleasantries (e.g., "let me know if you have any questions")
4. Requests for inaction ("don't do X")
5. Process descriptions
6. Requests to review attachments
7. Reported requests and commitments
8. Third-party commitments as requests

**[Inference]** Of these, 1, 3, 7, and 8 are equally frequent in meetings: the pleasantry "let's talk about it later", the reported request "the professor said it's due next week", and the commitment on someone else's behalf "he'll take care of it". These can go directly into the annotation guidelines as negative examples and boundary cases for this project's "commitment strength tiers".

**[Fact] Azarbonyad 2019's cross-domain finding**: a commitment model trained on one email corpus shows a marked drop in precision or recall when moved to another corpus (Avocado→Enron precision 0.82→0.74). **[Inference]** This gives a methodological analogy for "a general-purpose meeting product will perform worse on research group meetings", but it is only an analogy, not direct evidence.
### 3.3 Chinese Meeting Datasets

#### AMC-A (AliMeeting-Action Corpus; Liu, Deng, Zhang, Chen, Wang; Alibaba DAMO Academy; ICASSP 2023)
- **Task [Fact]**: Sentence-level binary classification: decide whether a sentence contains action item information. A positive example is defined as "sentences containing action item information (task description, time frame, owner)".
- **Annotation process [Fact]**: Candidate sentences containing both a time expression (e.g., "明天", "tomorrow") and an action verb (e.g., "完成", "complete") were first filtered out, highlighted, and given to 3 independent annotators, with context. Disagreements were reviewed by an expert on the basis of the majority vote; the expert changed only 5%–10% of the majority-vote results. Average pairwise κ was 0.47.
- **Size [Fact]**: 424 meetings (200 new meetings added on top of the 224 already released in M2MeT), split into 295 train / 65 dev / 64 test meetings; 306,846 sentences; 1,506 action items, averaging 3.55 per meeting. Meetings have 2–4 participants and last 15–30 minutes, "biased towards work meetings in various industries".
- **Metric [Fact]**: positive F1. BERT 64.76, Longformer 65.35, StructBERT 67.84; Context-Drop, which adds local and global context, is best at 70.82.
- **License [Fact / to be verified]**: The paper's footnote points to ModelScope `modelscope/Alimeeting4MUG`; the SpokenNLP code repository is Apache 2.0, but **the data license page could not be opened this round (the ModelScope page returned only a title), so this is to be verified**. The underlying AliMeeting audio is CC BY-SA 4.0 on OpenSLR.
- Sources: https://arxiv.org/pdf/2303.16763 ; https://github.com/alibaba-damo-academy/SpokenNLP/tree/main/action-item-detection
- **[Fact] The paper's own claim**: "To the best of our knowledge, AMC-A is so far the first Chinese meeting corpus and the largest meeting corpus in any language labeled for action item detection." — **This is the direct evidence that a "first" claim would be refuted.**

#### MUG (ICASSP 2023 General Meeting Understanding and Generation Challenge)
- **[Fact]**:
  - 5 tracks: topic segmentation, topic-level and session-level extractive summarization, topic title generation, keyword extraction, and action item detection (AID);
  - AliMeeting4MUG contains 654 Mandarin meetings, averaging 10,772.5 tokens and 376.3 utterances per meeting; 524 meetings have all 5 types of annotation;
  - AID requires "detecting sentences containing information about actionable tasks", reports positive P/R/F1, and the leaderboard ranks by positive F1;
  - Baseline StructBERT: P 62.73 ± 1.39, R 71.1 ± 0.35, F1 66.65 ± 0.87 (https://arxiv.org/pdf/2303.13932 ; dataset paper https://arxiv.org/abs/2303.13939 ).
- **[Inference]** If this project reports only a single "action item F1" on Chinese, interviewers will directly compare it with MUG's 66.65. So either report a comparable number on the AMC-A test set, or state explicitly that "I measure fields, not sentences".

#### AliMeeting (OpenSLR 119) and AISHELL-4 (OpenSLR 111)
- **[Fact]** AliMeeting: 118.75 hours (104.75 train / 4 eval / 10 test), 212/8/20 meetings, 2–4 participants and 15–30 minutes per meeting, Mandarin, 8-channel far-field array + close-talk headset microphones, CC BY-SA 4.0 (https://www.openslr.org/119/ ).
- **[Fact]** AISHELL-4: about 120 hours, 211 meetings, 4–8 participants per meeting, Mandarin, 8-channel circular array, CC BY-SA 4.0 (https://www.openslr.org/111/ ).
- **[Inference]** Both have only ASR / speaker annotations, so they can serve as transcription stress tests under "in-person multi-speaker meetings with far-field recording" conditions. CC BY-SA requires derivative data to be shared under the same terms, so any self-built annotations based on them must also be released under CC BY-SA.

#### VCSum (Wu et al., Findings of ACL 2023)
- **[Fact]** 239 real meetings, 230+ hours; annotations include topic segmentation, titles, segment summaries, full-text summaries, and salient sentences. **There are no action item annotations.** The GitHub repository is labeled MIT, while the arXiv paper page is labeled CC BY-NC-SA 4.0 (https://arxiv.org/abs/2305.05280 ; https://github.com/hahahawu/VCSum ).
- **To be verified**: the source of the meetings (neither of the two pages opened this round says), and the copyright ownership of the original videos.

### 3.4 Meeting-Understanding Benchmarks in the LLM Era (2021–2026)

| Benchmark | Year / Venue | What it does | Relation to action items | Reusable evaluation design | Source |
|---|---|---|---|---|---|
| QMSum | NAACL 2021 | Query-based meeting summarization; 232 meetings, 1,808 queries; three domains | One can ask queries "about action items", but there are no field annotations [Inference] | General/specific query types + relevant-span annotation | [Fact] https://arxiv.org/abs/2104.05938 ; https://github.com/Yale-LILY/QMSum |
| MeetingBank | ACL 2023 | City council segment-level summarization; 1,366 meetings | None | Segment alignment reduces the difficulty of long texts | [Fact] https://arxiv.org/abs/2305.17529 ; https://huggingface.co/datasets/huuuyeah/meetingbank |
| MeetingQA | ACL 2023 | Extractive QA; questions come from meeting participants, and answers can span multiple segments across speakers | The paper says prior meeting work is "restricted to summarization and extraction of action items" [Summary] | Multi-span answers, human upper bound (F1 84.6) | [Summary] https://aclanthology.org/2023.acl-long.837 |
| MeetingQA2 | Findings of EMNLP 2026 | Generative, speaker-centric QA; 1,033 questions, 108 of them unanswerable | None | **Unanswerable questions + attribution accuracy + factual correctness**. Strong LLMs drop the most on attribution accuracy | [Fact] https://aclanthology.org/2026.findings-emnlp.1728/ |
| MISeD | Findings of EMNLP 2024 | Information-seeking dialogue over meetings; LLM-generated, human-verified, with attribution spans marked | None | Cost control through semi-automatic data creation + human verification | [Summary] https://arxiv.org/abs/2405.01121 |
| ELITR-Bench | ICML 2024 workshop → COLING 2025 | Long-context LLM meeting-assistant QA; 271 questions; includes a noisy ASR-transcript version | None | **Robustness measured in WER bands**; the GPT-4 judge agrees with humans but can only separate about 3 levels | [Fact] https://arxiv.org/abs/2403.20262 ; [Summary] details of the noisy version |
| AutoMin 2023 / 2025 | Shared task | Automatic minuting; 2025 adds meeting QA (English monolingual + Czech-English cross-lingual) | Minutes may contain action items, but they are not evaluated separately [Inference] | Cross-lingual QA setup | [Fact] https://arxiv.org/abs/2509.13814 (abstract page only) |
| QMSum Mistake / MESA (Kirstein et al.) | COLING 2025 / arXiv 2024 | 200 LLM meeting summaries with 9 human-labeled error types (e.g., structural errors, omissions); multi-LLM judges | The error types can be borrowed to build an action item error taxonomy | Error taxonomy | [Summary] https://arxiv.org/abs/2407.11919 ; https://arxiv.org/abs/2411.18444 |
| MISP-Meeting | ACL 2025 | Multimodal long-meeting transcription + summarization; visual cues such as lip movement reduce CER from 36.60% to 20.27%; ASR quality correlates with summary coherence | None | Correlation analysis of "ASR quality → downstream quality" | [Fact] https://aclanthology.org/2025.acl-long.753/ (language not stated on the page, **to be verified**) |
| Meeting Delegate | arXiv 2025 | An LLM attends meetings on a person's behalf | None | – | [Summary] https://arxiv.org/html/2502.04376v1 |
| Asthana et al. (Microsoft, CSCW 2024) | CSCW 2024 | LLM meeting-recap system (summaries, highlights, action items), trialed by 7 Microsoft employees in real work meetings | Product-design study; no public action item accuracy | Users' additions, deletions, and edits as feedback signals | [Fact] https://arxiv.org/abs/2307.15793 |
| AWS Nova blog | 2025-06-18 | LLM summarization + action item extraction; 30 QMSum meetings; Claude 3.5 Sonnet as judge | **The only "action item faithfulness" public figure found** (0.63–0.83); vendor-run, tested only on the vendor's own models | Faithfulness = share of output statements supported by the source text; the authors explicitly do not measure coverage | [Fact] https://aws.amazon.com/blogs/machine-learning/meeting-summarization-and-action-item-extraction-with-amazon-nova/ |

**[Inference] Summary**: LLM-era meeting benchmarks concentrate on **summarization and QA**. Action items are either treated as part of the summary or measured only for faithfulness. **Within the scope of the search, no public 2023–2026 benchmark was found that models action items as structured fields ("owner, due date, commitment strength, evidence span") and allows "unknown" as a correct answer.** The closest designs are MeetingQA2's unanswerable questions and the attribution evaluation in MISeD/MeetingQA2.
### 3.5 Mixed Chinese-English ASR Datasets (Singapore Scenario Focus)

#### SEAME (Mandarin-English Code-Switching in South-East Asia, LDC2015S04)
- **[Fact]**:
  - About 192 hours of mixed Chinese-English speech from 156 speakers (49.7% female, 50.3% male, aged 19–33). More than 60% are Singaporean and the rest are Malaysian;
  - The format is unscripted free conversation (two speakers) and interviews (only the interviewee is recorded), recorded in a quiet room;
  - The authors' institutions are **the target university** and Universiti Sains Malaysia;
  - Released on 2015-04-15 under the LDC non-member agreement; the fee is visible only after logging in (https://catalog.ldc.upenn.edu/LDC2015S04 ).
- **[Summary]** The original 2010 paper describes 30 hours of word-level transcription; the ASRU 2019 challenge paper says that at the time "only SEAME, a small set of 30 hours" was publicly available. The 192 hours is the full Phase II release (https://arxiv.org/pdf/2007.05916 ).
- **[Assumption, to be verified]** The owner is at the target university, and SEAME was produced with the university's participation. The university may be an LDC member or hold an internal copy; ask the lab or the library. Even if access is possible, the LDC agreement usually restricts redistribution, so the data could only be used for internal evaluation and could not go into a public evaluation package.
- **[Inference] Relevance to this project**: SEAME is the closest public corpus to "Singaporean Chinese code-switching accents", but it consists of casual conversation and interviews, not meetings, and has no action item annotation. It is suitable for testing at the ASR layer whether "English terms get lost in Singapore-accented Chinese-English code-switching", and not suitable for testing action item extraction.

#### ASRU 2019 Mandarin-English Code-Switching Challenge
- **[Fact]** Participants were given 500 hours of Mandarin plus 240 hours of Mandarin-English intra-sentential code-switching speech (https://arxiv.org/abs/2007.05916 ).
- **[Summary]** The data was provided by Datatang, recorded on mobile phones in quiet rooms, with speakers from 30 provinces in China. Each utterance averages 8.6 Chinese characters + 1.6 English words, and the English is mostly nouns, personal names, and song titles. Whether the data can be obtained after the challenge: **to be verified**.
- **[Inference]** The statistic that "the English is mostly nouns" is consistent with this project's argument that "the key nouns in action items are often English terms" and can be cited as indirect support. However, these are read or semi-read phone recordings, not meetings.

#### CS-Dialogue (Zhou et al. 2025, Nankai University + Beijing Academy of Artificial Intelligence)
- **[Fact]**:
  - 104.02 hours, 200 speakers (IELTS 6 or above, or passed TEM-4), from 30 provincial-level regions in mainland China; 100 pairs of face-to-face dialogues;
  - Each topic segment is allocated 8 minutes of Chinese, 6 minutes of mixed, and 6 minutes of English; topics include personal, entertainment, technology, education, work, philosophy, and sports;
  - The HF page lists the license as CC BY-NC-SA 4.0;
  - Whisper large-v2 zero-shot MER is 15.29%; after fine-tuning, Whisper medium drops from 15.88% to 7.53% (https://huggingface.co/datasets/BAAI/CS-Dialogue ; https://arxiv.org/html/2502.18913v2 ).
- **[Inference]** The license allows non-commercial demo use. It is currently the largest spontaneous mixed Chinese-English dialogue set with complete dialogue transcripts, and can serve as a public test source for "Chinese-English code-switching ASR term recall". However, the speakers are mainland students whose accents differ from Singaporean ones.

#### ASCEND (Lovenia et al., LREC 2022, HKUST)
- **[Fact]** HF card: CC BY-SA 4.0, 10.62 hours, about 12.3K utterances (train 9,869 / validation 1,130 / test 1,315), recorded in Hong Kong, multi-turn spontaneous dialogue, with each utterance labeled zh/en/mixed (https://huggingface.co/datasets/CAiRE/ASCEND ).
- **[Summary]** 23 speakers; the best wav2vec 2.0 result is CER 22.69% and MER 27.05% (https://arxiv.org/abs/2112.06223 ).

#### Singapore National Speech Corpus (IMDA)
- **[Summary]** Parts 3–6 are conversation-level data; access is by application, a third party reports use of the Singapore Open Data Licence; about 1.2 TB. Whether it contains mixed Chinese-English meeting-style dialogue: **to be verified** (https://www.imda.gov.sg/about-imda/emerging-technologies-and-research/artificial-intelligence/national-speech-corpus ).

**[Inference] Summary of mixed Chinese-English data**: All mixed Chinese-English datasets have **ASR-layer annotation only**, with no action item, decision, or commitment annotation; all datasets with action item annotation are **monolingual** (English ICSI/AMI, Chinese AMC-A). The intersection of "code-switched meetings + action item field annotation" is empty within the search scope. This is the most defensible data contribution of this project.

---

## 4. "Hard-Problem Findings" Already Known in Academia That Can Be Cited Directly

| # | Finding | Evidence | Implication for this project's evaluation design |
|---|---|---|---|
| L1 | Action items are sparse events, making up only about 1%–1.5% of utterances | Purver 2007: 1.4%; AIMU: about 1.5%; AIR: about 1% | Random-sampling annotation is extremely costly. Either pre-filter with rules first, as AMC-A and AIR do (AIR's regex pre-filter reaches 90% recall), or annotate whole meeting segments |
| L2 | Directly labeling "is this an action item" yields very low inter-annotator agreement | Gruenstein 2005: κ 0.36; AMC-A: κ 0.47 | Binary annotation alone is not enough; this project must report its own κ, otherwise the metrics are not credible |
| L3 | Agreement improves significantly after decomposition into subcategories | Purver: D/T/O/A κ 0.64–0.78; Fernández: four decision categories κ 0.63–0.73 | Field-level annotation is more reliable than judging "whether the whole action item is correct", which matches this project's field-level evaluation direction |
| L4 | Writing clear rules for conditional sentences and indirect expressions can greatly improve commitment annotation agreement | Lampert 2008: commitment κ 0.54 → 0.74 | "Commitment strength tiers" must come with an annotation guideline containing positive and negative examples, and a small-scale agreement pilot must be run first |
| L5 | Owners are mainly expressed through interaction ("I'll do it", "Could you…"), relying on speaker and addressee identification | Purver 2007 original text, which explicitly sets this aside | Owner errors should be attributed to two categories: ASR or speaker diarization errors (product layer) versus semantic attribution errors (LLM layer). Count them separately during evaluation |
| L6 | The same model performs much worse on scripted-scenario meetings (AMI) than on real work meetings (AMC-A) | AMI positive F1 about 39–43 vs AMC-A about 68–71 (same method, same paper) | Data source has a huge effect on metrics. Report "which meetings it was tested on" and avoid comparing numbers directly across datasets |
| L7 | Commitment models lose accuracy when transferred across corpora | Azarbonyad 2019 | Supports the argument that "general-purpose products need separate evaluation in specific settings (research group meetings, code-switching)" (by analogy) |
| L8 | LLM judges broadly agree with humans, but their ability to distinguish fine-grained levels is limited | ELITR-Bench: GPT-4 can reliably distinguish only about 3 levels | Do not use an LLM judge for 5-point scoring of strength tiers. Use human gold labels + a limited number of levels (3–4) |
| L9 | ASR noise propagates downstream | ELITR-Bench noise levels; MISP-Meeting ASR quality correlates with summary coherence | Report scores for both "human transcript input" and "ASR input" to separate transcription errors from extraction errors |

---
## 5. Where This Project's Evaluation Fits

### 5.1 Interview talking points: what not to say, and what to say

| Don't say | Why | Say instead |
|---|---|---|
| "The first public evaluation of meeting action items" | The AMC-A paper claims to be the first and largest in Chinese; ICSI/AMI have existed since 2005; MUG has a track | "Existing benchmarks evaluate sentence-level detection. As far as I could find (ACL Anthology, arXiv 2023–2026, MUG/AutoMin), no public evaluation covers **whether the model fabricates an owner or deadline when it is missing**, **graded commitment strength**, or **recall of mixed Chinese-English terms**." |
| "The first research group meeting dataset" | ICSI is itself a research group's weekly meetings | "ICSI is an English-language group meeting from Berkeley, 2000. I work with 2026 group meetings that mix Chinese and English, in an LLM-extraction setting, and I reproduced the same metrics on an ICSI subset so the results can be compared." |
| "Nobody has evaluated action-item accuracy" | Academia has a string of F1 results; AWS has published faithfulness | "**Commercial products** have no public action-item metrics (05 K1). Academic benchmarks exist, but they don't cover the fields where products actually go wrong." |
| "Microsoft's Lin et al. 2022 did…" | This paper was not found in this round | Cite Azarbonyad 2019 (Microsoft, email commitments) and Cohen 2021 (Microsoft, meeting action-item rewriting) instead |
| "My F1 is X%, higher than Feishu" | An F1 reported without κ and sample size will be challenged | "On a gold-label set of N action items with annotator κ = Y, Feishu scores a%, ours b%, with a 95% confidence interval of ±c." |

### 5.2 Existing work vs. this project's increment

| Evaluation dimension | Existing in academia | Existing on the product side | This project's increment | Strength of increment |
|---|---|---|---|---|
| **Research group meeting setting** | **Yes**: ICSI (English, 2000–2002, a speech research group), the Academic domain of QMSum/MISeD | Fabric, Littlebird and others claim to target labs (file 03), with no metrics | Contemporary, mixed Chinese-English, computing labs; action-item types closer to research practice (running experiments, revising papers, booking GPUs, getting an advisor's signature) [Inference] | **Medium** (new setting, but cannot be called "first") |
| **Owner / deadline fields** | Partial: Purver has O/T categories and time-phrase F1; AMC-A uses them only as criteria for positive examples; AIR rewrites them into sentences | No public metrics | Field-level accuracy + **no-guess rate when missing** (the share of cases where the gold label is "unknown" and the output is "unknown") + **fabrication rate** (names or dates in the output with no basis in the source text) | **High** (not seen within the search scope) |
| **Commitment-strength tiers** | Email-domain annotation guidelines for conditional/indirect commitments (Lampert); hedge detection in CoNLL-2010 | Littlebird: a binary split between explicit commitments and vague "maybe", no public metrics | 3–4 strength levels (explicit commitment / conditional / suggestion or under discussion / hypothetical or rejected) + confusion matrix + agreement κ | **Medium-high** (a basic version of "tiering" has been done; "multi-level + evaluable" not seen) |
| **Recall of mixed Chinese-English terms** | At the ASR layer there are SEAME, ASRU 2019, CS-Dialogue, ASCEND (MER/CER); none at the action-item layer | Feishu claims to recognize mixed Chinese-English speech and enterprise entities (verified in 06); Gemini and Krisp do not support Chinese | **Recall of key English terms within action items** (e.g., GPU names, model names, dataset names, conference deadline names), reported at both the ASR layer and the extraction layer | **High** (the intersection cell is empty within the search scope) |
| **Side-by-side comparison of real competitor outputs** | None (academic papers compare models, not products) | AWS only tests its own Nova | Upload the same audio to Feishu Minutes, Tongyi Tingwu, Otter, etc., and count failure modes by field | **High**, but limited by each product's terms of service and regional availability |
| **Traceable evidence (quoting the original sentence)** | MISeD and MeetingQA2 have attribution evaluation (question-answering tasks) | Most products offer timestamp jumps (files 01, 02) | Whether each action item's evidence snippet really supports it (attribution accuracy), transferred to the action-item task | **Medium** |
| **Assignee acknowledgment** | None (this is not an NLP task) | No acknowledgment seen on Fellow's action-item page (verified in 06) | This is at the interaction-design layer; for evaluation, we can test whether requests and commitments are told apart correctly among items that need acknowledgment | **Medium** (a product-layer difference) |

### 5.3 Datasets we can borrow directly

| Purpose | Recommended dataset | Why | License notes |
|---|---|---|---|
| Public English research-group-meeting foundation (reproducible, can be uploaded to competitors) | **ICSI** (Edinburgh version) | Real research group weekly meetings; CC BY 4.0; the test sets of Purver and AIR both come from it, so results can be tied to the literature | Attribution is enough; our own annotations can be made public |
| English comparable baseline | **AMI indirect labels** (101 meetings / 381 items) | Comparable with the numbers in the AMC-A paper (positive F1 around 40) | Transcripts are CC BY 4.0; the license for the summary annotations is to be verified |
| Chinese comparable baseline | **AMC-A test set** (64 meetings, 270 action items) | Report positive F1 and compare with MUG's 66.65 and the paper's 70.82, answering "what score do you get on the standard Chinese set" | **License to be verified**; confirm the ModelScope terms before use |
| ASR stress test for Chinese in-person multi-speaker meetings | AliMeeting, AISHELL-4 | Far-field, multi-speaker, real meetings | CC BY-SA: derivatives must use the same license |
| ASR term recall for mixed Chinese-English | **CS-Dialogue** (primary), ASCEND (secondary) | Large scale, spontaneous conversation, technology and education topics | CS-Dialogue is CC BY-NC-SA, usable for a non-commercial demo; ASCEND is CC BY-SA |
| Singapore-accented mixed Chinese-English | **SEAME** (if obtainable through the target university) | Singaporean and Malaysian speakers; a Singapore university was involved in producing it | LDC agreement, no redistribution; internal testing only [Inference] |
| Meeting QA / attribution comparison | QMSum, MISeD, MeetingQA2 | The knowledge Q&A module (the "cited Q&A" in the earlier v1 docs, not included) can be benchmarked against these directly | QMSum is MIT; the rest are to be verified |
### 5.4 Metrics and Methods We Can Borrow Directly

1. **Positive P/R/F1 (MUG / AMC-A)**: sentence-level detection, used for alignment with the literature.
2. **Sub-dialogue overlap F1 (Purver 2007)**: a prediction counts as a hit if its predicted region overlaps the gold-label region. This suits meetings where an action item is spread across several sentences, and is fairer than strict sentence matching.
3. **Field phrase F1 (Purver 2007 time phrases)**: word-level overlap F1 for the due-date and task-description fields; exact match for the owner field (person name or speaker ID).
4. **Agreement κ / Krippendorff α**: report each field separately. The target is the 0.6–0.8 range reached by Purver/Fernández; below 0.5 means the annotation guidelines need revision [Inference].
5. **Unanswerable-question mechanism (MeetingQA2) → no-guess-when-missing rate**: items whose gold owner or due date is "unknown" are grouped separately, and we measure the proportion of cases where the model outputs "unknown". Conversely, we measure the fabrication rate: cases where the gold label is unknown but the model gives a concrete value.
6. **Faithfulness (AWS Nova) + attribution accuracy (MISeD / MeetingQA2)**: each action item is accompanied by an evidence snippet, and we judge whether the snippet supports the item. AWS does not measure coverage, so this project must **also report recall**, to avoid "reporting fewer items yields a high score".
7. **Noise tiers (ELITR-Bench)**: the same set of meetings is fed in as human transcripts, competitor ASR, and Whisper transcripts, and we observe how extraction metrics change with WER/MER.
8. **MER (ASRU 2019 / CS-Dialogue) + glossary recall**: report MER at the ASR layer, then report "the proportion of English entities in the glossary that appear correctly in the transcript".
9. **Error taxonomies (Lampert's 8 categories + QMSum's 9 Mistake categories)**: use fixed categories when tallying failure modes, for example pleasantry false positives, paraphrase false positives, wrong attribution of third-party commitments, omissions, owner mix-ups, and fabricated dates, so we can build a "competitors vs. ours" failure-mode frequency table.

### 5.5 Proposed Evaluation Protocol Draft (Fit for 2–4 Weeks, One Person)

> Everything below is **[Inference]**: design suggestions based on the literature above, not yet executed.

- **Annotation unit**: each "action item candidate" has the following fields:
  - `type`: commitment / request / decision
  - `task`: task description
  - `owner`: person name, speaker ID, or UNKNOWN
  - `due`: absolute date, relative expression, or UNKNOWN
  - `strength`: L3 explicit commitment / L2 conditional commitment / L1 suggestion or under discussion / L0 hypothetical, pleasantry, or rejected
  - `evidence`: utterance ID or timestamp of the evidence
  - `terms`: English terms involved
- **Three data tiers**:
  1. **ICSI subset**: about 10 meetings, with a 15–20 minute excerpt from each; English, public, and reproducible;
  2. **AMC-A test set**: detection only, reporting positive F1 to align with the literature;
  3. **Self-built Chinese-English mixed research group meetings**: about 10–20 segments, either real group meetings with the members' informed consent or role-played from real agendas; used to test Chinese-English terms and fields.

  Tier 3 is the incremental contribution; it is small in scale, so the annotation guidelines and samples must be made public.
- **Comparison groups**: the same audio is given to Feishu Minutes, Tongyi Tingwu, and Otter (products with Chinese-language limitations are marked "not applicable"), as well as this project's pipeline. Tier 1 uses CC BY audio, which can be legally uploaded; Tier 3 requires participants' consent to upload to third-party services.
- **Dual annotation**: at least 20% of samples are independently annotated by two annotators, with κ reported per field.
- **Sample size reminder**: with 100 action items and accuracy around 80%, the 95% confidence interval is about ±8 percentage points (binomial approximation, √(0.8×0.2/100)≈0.04). So a demo claim that "we beat the competitor by 5 points" is not statistically defensible; either expand the sample or report only fields with a clear gap (≥15 points) [Inference].
- **Six required numbers**:
  1. Item-level F1 (overlap matching)
  2. Owner accuracy (on the subset where the gold label is known)
  3. No-guess-when-missing rate (on the subset where the gold label is UNKNOWN)
  4. Fabrication rate
  5. Weighted κ or confusion matrix over strength tiers
  6. Chinese-English term recall (split into ASR layer and extraction layer)

  Every number must state its data tier and sample size.

### 5.6 Likely Interviewer Follow-ups and Prepared Answers

| Follow-up | Prepared answer (citing evidence in this document) |
|---|---|
| "Doesn't AMC-A already have Chinese action items?" | Yes: 424 meetings, κ 0.47, F1 around 67–71. But it is sentence-level binary classification; a positive only needs to contain one of task, time, or owner, it outputs no fields, and it has no Chinese-English code-switching. I report a comparable F1 on its test set and add field-level metrics on top. |
| "Didn't Purver 2007 already have owner and timeframe?" | It has the categories, but the paper's own wording is that owner identification is something "we leave aside for now". Time-phrase F1 is 0.51, a 2007 SVM result. I am measuring the LLM-era step of "giving a specific person and date", and whether the system fabricates when there is no basis. |
| "You annotate and test it yourself. Aren't you both player and referee?" | The annotation guidelines, samples, and all gold labels on the ICSI subset are made public, and dual-annotator κ is reported; ICSI is CC BY, so anyone can reproduce it. |
| "Your sample size is too small." | Agreed, and I report confidence intervals; I draw conclusions only on fields with a clear gap. The purpose of a small sample is to find failure modes, not to build a leaderboard. |
| "Strength tiers are too subjective." | Lampert 2008 showed that guidelines spelling out conditional/indirect commitments raised κ from 0.54 to 0.74. I will first do a trial annotation of 50 items with 2 annotators, and merge tiers if κ is below 0.6. |
| "Why not use an LLM as the judge to save effort?" | ELITR-Bench shows a GPT-4 judge can reliably distinguish only about 3 tiers; field correctness is judged by rules or by humans, and the LLM judge is used only for semantic matching, with sampled human review. |

---

## 6. Unverified Items and Search Scope

- **Search scope**: WebSearch keywords included meeting action item detection benchmark LLM, commitment detection email/meeting, decision detection AMI, AliMeeting action item, code-switching Mandarin English corpus, ELITR, MeetingQA, MISeD, Kirstein meeting summarization, and others, restricted to arxiv.org and aclanthology.org. We **did not systematically go through** all Interspeech/ICASSP 2024–2026 papers, and did not search Chinese journals (such as the *Journal of Chinese Information Processing*) or CNKI.
- **To be verified**:
  1. Data license for AMC-A / AliMeeting4MUG on ModelScope (the page returned only the title);
  2. Whether the AMI summary annotations (including the ACTIONS segments) fall under CC BY 4.0;
  3. Whether the public version of AIR has been released;
  4. Whether the old Microsoft AIMU link still works;
  5. Whether the ASRU 2019 data can be obtained after the competition;
  6. VCSum meeting sources and copyright;
  7. License of the ELITR Minuting Corpus (the LINDAT page timed out twice; only a search snippet states CC BY-NC-SA 4.0);
  8. Language of MISP-Meeting (not stated on the page);
  9. Whether Singapore's NSC contains meeting-style Chinese-English mixed dialogue;
  10. Whether SEAME can be obtained through the target university;
  11. The "Lin et al. 2022" and Cohen et al. "Learning to detect commitments in email" mentioned in the user's task: **no matching papers were found for either**; the citations may be misremembered.
- **Items at [Summary] level** (only search snippets were seen): Bennett & Carbonell 2005/2007, Lin 2018 AAAI, Smart To-Do 2020, MeetingQA, MISeD, the Kirstein series, ASCEND speaker counts, ASRU 2019 details, NSC, CoNLL-2010, Hsueh & Moore 2008.
- **"Not seen" does not mean "does not exist"**: for the "high incremental value" judgment in §0 item 4 and §5.2, the worst counterexample would be a meeting LLM benchmark released in 2026 that happens to do field-level extraction with an "unknown" option. We recommend running one more arXiv search for "meeting action item owner deadline benchmark" a week before the interview.

---
## 7. Source List (all accessed at the time of writing)

**Meeting action items / decisions**
1. Purver et al. 2007, Detecting and Summarizing Action Items in Multi-Party Dialogue — https://aclanthology.org/2007.sigdial-1.4.pdf [Fact, full text]
2. Fernández et al. 2008, Modelling and Detecting Decisions in Multi-party Dialogue — https://aclanthology.org/W08-0125.pdf [Fact, full text]
3. Hsueh & Moore 2008, Automatic Decision Detection in Meeting Speech — https://era.ed.ac.uk/handle/1842/4140 [Summary]
4. Liu et al. 2023, Meeting Action Item Detection with Regularized Context Modeling (AMC-A) — https://arxiv.org/abs/2303.16763 ; https://arxiv.org/pdf/2303.16763 [Fact, full text]
5. SpokenNLP action-item-detection repository — https://github.com/alibaba-damo-academy/SpokenNLP/tree/main/action-item-detection [Fact]
6. ModelScope Alimeeting4MUG — https://www.modelscope.cn/datasets/modelscope/Alimeeting4MUG/summary [To be verified: the page returned only the title]
7. Overview of the ICASSP 2023 MUG Challenge — https://arxiv.org/pdf/2303.13932 [Fact, full text]
8. MUG: A General Meeting Understanding and Generation Benchmark — https://arxiv.org/abs/2303.13939 [Fact, abstract page]
9. Chen & Hakkani-Tür 2016, AIMU — (university page; link removed) [Fact, full text]
10. Chen, Hakkani-Tür, He 2015, Detecting Actionable Items in Meetings (ASRU) — https://www.microsoft.com/en-us/research/?p=238152 [Summary]
11. Cohen, Kantor, Hilleli, Kolman 2021, Automatic Rephrasing of Transcripts-based Action Items (AIR) — https://aclanthology.org/2021.findings-acl.253.pdf [Fact, full text]
12. Golia & Kalita 2023, Action-Item-Driven Summarization — https://arxiv.org/abs/2312.17581 [Fact]
13. Deng et al. 2023, Aspect-based Meeting Transcript Summarization — https://arxiv.org/abs/2311.04292 [Fact, abstract page]
14. Asthana et al. 2024 (CSCW), LLM-powered meeting recap system — https://arxiv.org/abs/2307.15793 [Fact, abstract page]
15. AWS, Meeting summarization and action item extraction with Amazon Nova (2025-06-18) — https://aws.amazon.com/blogs/machine-learning/meeting-summarization-and-action-item-extraction-with-amazon-nova/ [Fact]

**English meeting corpora and benchmarks**
16. AMI Corpus home page — https://groups.inf.ed.ac.uk/ami/corpus/ [Fact]
17. AMI Corpus annotation page — https://groups.inf.ed.ac.uk/ami/corpus/annotation.shtml [Fact]
18. ICSI Corpus (Edinburgh) — https://groups.inf.ed.ac.uk/ami/icsi/ [Fact]
19. ICSI Meeting Speech LDC2004S02 — https://catalog.ldc.upenn.edu/LDC2004S02 [Fact]
20. QMSum paper — https://arxiv.org/abs/2104.05938 [Fact]
21. QMSum repository — https://github.com/Yale-LILY/QMSum [Fact]
22. MeetingBank paper — https://arxiv.org/abs/2305.17529 [Fact]
23. MeetingBank on Hugging Face — https://huggingface.co/datasets/huuuyeah/meetingbank [Fact]
24. ELITR Minuting Corpus (LREC 2022) — https://aclanthology.org/2022.lrec-1.340/ [Fact]
25. ELITR Minuting Corpus page — https://ufal.mff.cuni.cz/elitr-minuting-corpus [Fact]; LINDAT record https://lindat.mff.cuni.cz/services/catalog/view/http:__hdl_handle_net_11234_1-4692 [Summary, page timed out]
26. AutoMin 2025 Findings — https://arxiv.org/abs/2509.13814 [Fact, abstract page]
27. ELITR-Bench — https://arxiv.org/abs/2403.20262 [Fact]
28. MeetingQA (ACL 2023) — https://aclanthology.org/2023.acl-long.837 [Summary]
29. MeetingQA2 (Findings EMNLP 2026) — https://aclanthology.org/2026.findings-emnlp.1728/ [Fact]
30. MISeD — https://arxiv.org/abs/2405.01121 [Summary]
31. MISP-Meeting (ACL 2025) — https://aclanthology.org/2025.acl-long.753/ [Fact]
32. Kirstein et al., What's Wrong? (QMSum Mistake) — https://arxiv.org/abs/2407.11919 ; MESA https://arxiv.org/abs/2411.18444 [Summary]

**Email commitments / requests**
33. Cohen, Carvalho, Mitchell 2004, Learning to Classify Email into "Speech Acts" — https://aclanthology.org/W04-3240.pdf [Fact, full text]
34. Bennett & Carbonell 2005, Detecting Action-Items in E-mail — https://www.microsoft.com/en-us/research/publication/detecting-action-items-e-mail/ [Summary]
35. Lampert, Dale, Paris 2008, Requests and Commitments in Email are More Complex Than You Think — https://aclanthology.org/U08-1009.pdf [Fact, full text]
36. Lin et al. 2018, Actionable Email Intent Modeling with Reparametrized RNNs — https://ojs.aaai.org/index.php/AAAI/article/view/11931 [Summary]
37. Azarbonyad, Sim, White 2019, Domain Adaptation for Commitment Detection in Email — https://microsoft.com/en-us/research/uploads/prod/2019/01/AzarbonyadWSDM2019.pdf [Fact, full text]
38. Mukherjee et al. 2020, Smart To-Do — https://aclanthology.org/2020.acl-main.767 [Summary]

**Chinese meeting / mixed Chinese-English corpora**
39. AliMeeting OpenSLR 119 — https://www.openslr.org/119/ [Fact]
40. AISHELL-4 OpenSLR 111 — https://www.openslr.org/111/ [Fact]
41. VCSum — https://arxiv.org/abs/2305.05280 ; https://github.com/hahahawu/VCSum [Fact]
42. SEAME LDC2015S04 — https://catalog.ldc.upenn.edu/LDC2015S04 [Fact]
43. ASRU 2019 CS Challenge — https://arxiv.org/abs/2007.05916 [Fact, abstract page]; details https://arxiv.org/pdf/2007.05916 [Summary]
44. CS-Dialogue — https://huggingface.co/datasets/BAAI/CS-Dialogue ; https://arxiv.org/html/2502.18913v2 [Fact]
45. ASCEND — https://huggingface.co/datasets/CAiRE/ASCEND [Fact]; https://arxiv.org/abs/2112.06223 [Summary]
46. IMDA National Speech Corpus — https://www.imda.gov.sg/about-imda/emerging-technologies-and-research/artificial-intelligence/national-speech-corpus [Summary]

**Terminology reference (non-core)**: CommitmentBank https://github.com/mcdm/CommitmentBank [Fact]; CoNLL-2010 Shared Task https://rgai.inf.u-szeged.hu/node/118 [Summary].
