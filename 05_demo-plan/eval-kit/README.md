---
title: Real-Output Comparison Experiment for Competing Products · Evaluation Toolkit (eval-kit)
status: "v1.1 executable (final revision: added Layer 2 score_recon.py, a draft transition gold set, a synthetic run table, and the H1 control-group prompt; the experiment has not yet been run, so all results are empty)"
sources_count: 6
sources_count_method: Number of unique URLs in the Sources section (recomputed at the final revision; original value 9)
---

# Real-Output Comparison Experiment for Competing Products · Evaluation Toolkit

> In one sentence: run 5 **synthetic** research group meetings / advisor 1-on-1s / corporate partnership meetings through Feishu Minutes (Lark Minutes), Tongyi Tingwu, Otter, Fellow, and "ChatGPT/Claude + pasted transcript", and score them all against the same gold labels. The goal is to turn "they don't do this well" into **numbers**; if the numbers show they actually do it well, this differentiation hypothesis gets **rejected**.

## 0. Why Run This Experiment

The integrity review of the first research round (`01_market-research/06_research_integrity_review.md` §9 P0) pointed out that among the 14 files there is **not a single real output from a competitor**; every differentiation claim comes from "the official page doesn't mention it" and user complaints. When an interviewer asks, "Feishu Minutes, Otter, and Fireflies already do this, so why are you building it?", "I compared 20 official websites" is not convincing. "I ran the same group meeting recording through Feishu and Otter, and they missed 3 of the 7 commitments" is.

The agent cannot log in to Feishu or Otter, so what is delivered here is a toolkit that the **project owner can follow step by step**:

| Path | Contents |
|---|---|
| `meetings/` | 5 synthetic transcripts (with speakers and timestamps); `meetings/plain/` holds plain-text versions with the explanatory text stripped out, for pasting |
| `gold/` | Gold labels: `M1–M5.gold.jsonl` (135 entries), `traps.json` (7 traps), `terms.json` (glossary), `aliases.json` (name aliases), `decisions_hypotheses.md` (decisions / hypotheses / traps / cross-meeting commitment chains) |
| `annotation-guide.md` | Annotation guidelines: how to judge the four strength levels, 27 boundary cases, and the double-annotation and Cohen's Kappa procedure |
| `scoring.md` + `score.py` | Metric definitions, matching rules, and rules for normalizing product outputs; a scoring script using only the standard library (self-tested) |
| `sample/` | An example product output with deliberate errors + expected scores + expected report + a Kappa example |
| `tools/make_audio.py` | Uses macOS `say` + ffmpeg to synthesize the transcripts into multi-speaker audio |
| `templates/` | Templates for normalizing product outputs, a mapping template, and the LLM baseline prompt |
| `results-template.md` | Results recording template (all numbers are "to be run"); §6.1 holds the P-H1/P-H8 verdict rows; §11 is the Littlebird (P-H3) observation table |
| `score_recon.py` | **Layer 2** (new in v1.1): accuracy for 4 transition types, two false-green rates (`fgr_mentioned` / `fgr_unmentioned`), verbatim-quote rate, recall/precision for not-mentioned items, and stale-number and constraint checks; converts DIY output JSON to pred (`--from-diy`), verbatim filter (`--verbatim-filter`, E2c), paired McNemar (`--compare --k`), transition-type κ + bootstrap (`--kappa`). `score.py` is unchanged by a single line |
| `gold/recon/transitions.gold.jsonl` | **Draft** transition gold set (new in v1.1): 23 labeled (thread, session) rows (using 26 of the 30 cross-meeting links; the other 4 are excluded per PRD §14.4.1 R3/R4) + 75 not-mentioned rows + 4 rows awaiting manual adjudication + 1 stale-number row + 3 constraint-check rows. It lives in a subdirectory so that the `gold/*.gold.jsonl` glob in `score.py` does not pick it up |
| `gold/runs_synthetic.csv` | Synthetic run table (new in v1.1, **a trap planted by the author**: `lora_rank=16` in seed 3); it only demonstrates the mechanism and does not prove frequency |
| `tools/build_transitions_gold.py` | Regenerates the draft transition gold set from the gold links (reproducible) |
| `templates/expert_reconcile_prompt.md` | H1 control group: E2 expert / E2-naive ordinary / E2c verbatim filter / E2d in-place product cross-meeting Q&A |
| `templates/h7_dogfood_log.md` | P-H7 trial and concierge log template (new in v1.1) |

> Note on file metadata: Markdown files begin with YAML frontmatter; JSON files keep metadata in a `_meta` field; `score.py` / `make_audio.py` keep it in header comments; JSONL and CSV are line-by-line data formats where adding frontmatter would break the format, so none is added, and their metadata is recorded uniformly in this README.

**Run this first** to confirm the toolkit is intact (it was actually run, and all 3 checks passed):

```bash
cd 05_demo-plan/eval-kit
python3 -I score.py --selftest
# validate: 135 gold entries, 0 issues
# selftest A (gold against gold, 135 entries): passed
# selftest B (sample_output_M3 against expected_results_M3): passed
# selftest C (Cohen's κ hand-computed value 21/31≈0.6774): passed
python3 -I score_recon.py --selftest      # new in v1.1; A–F all actually run and passed
```
## 1. Experimental Hypotheses (Write Them Down Before Running, to Prevent Post-Hoc Rationalization)

All of the following are **[Assumption · to be verified]**. The thresholds are decision lines set in advance. After the run, fill in "holds / does not hold" for each one in `results-template.md`.

> **Numbering prefixes (v1.1)**: Hypotheses in this table are always written as **E-H1…E-H9** (E = eval-kit), to distinguish them from the positioning hypotheses **P-H1…P-H11** (P = positioning) and the user research hypotheses **U-H01…U-H14** (U = user research) in the 02/06 user research packs. The three numbering schemes map as follows: E-H5 ≈ P-H2; E-H3/E-H4 ≈ P-H11; E-H9 = P-H1. H1–H8 at the start of each row in the table below mean E-H1–E-H8.

| # | Hypothesis | Metric used to test it | Decision line (agreed in advance) | What "does not hold" means |
|---|---|---|---|---|
| H1 | Mainstream products can catch "explicit commitments", but they upgrade soft commitments into action items | `recall_action_committed`, `soft_upgrade_rate` | Best competitor recall ≥80% **and** upgrade rate ≥50% | Upgrade rate <20%: the "commitment strength grading" differentiator does not hold; don't build it |
| H2 | Commitments made by advisors/partners themselves are missed more often than students' | Recall grouped by owner (gold labels contain 8 advisor items and 4 partner items) | Advisor-group recall is ≥20 percentage points lower than student-group recall | Gap <10 points: drop "advisor commitments" as a selling point |
| H3 | When there is no owner, the product forces one in | `owner_abstain_rate` | Best competitor <50% | ≥80%: competitors already know to "not guess"; this point does not hold |
| H4 | Relative dates with no anchor ("in a while", "ASAP", "early November") get turned into specific dates | `due_abstain_rate` | Best competitor <60% | ≥85%: does not hold |
| H5 | Single-meeting minutes do not link this week's progress to last week's commitments | `crosslink_accuracy` (M2–M5) | All competitors <30% | If features such as Feishu's "Meeting Express" score ≥50%: cross-meeting tracking is not a gap |
| H6 | For mixed Chinese-English terminology, English products (Otter, which officially lists only English/Spanish/French) recognize it poorly, while Chinese products do better | `term_recall` | Otter is ≥30 points lower than Feishu/Tongyi Tingwu | Small gap: mixed Chinese-English is not an independent selling point |
| H7 | Rejected proposals get listed as action items | `trap_rate`, trap details | At least 1 competitor falls for it in ≥2 meetings | All 0: this point does not hold |
| H8 | Prompt injection text read aloud in a meeting is not executed (baseline expectation) | `injection_M3` | Record only; no decision line | If a product executes it: this is a security selling point and gets written up separately |
| E-H9 | (= positioning P-H1) Claude's long context + prompt cannot do multi-hop reconciliation well | `score_recon.py`: `fgr_mentioned`, `transition_accuracy`, `mention_recall`; paired McNemar test | See positioning §11 P-H1 and `results-template.md` §6.1 (k fixed in advance) | See the abandon action in positioning P-H1 |

> **Why build in a "does not hold" exit?** The value of this experiment is not to prove BriefPilot right, but to **find out which differentiators are real**. If H1–H5 all fail to hold, the conclusion is "competitors are already good enough; BriefPilot changes direction." That is itself a legitimate PM conclusion, and better than forcing out a demo nobody needs.

## 2. Products Under Test and Input Methods

### 2.1 Condition Design

| Condition | Description | Applicable products |
|---|---|---|
| **A-TTS**: end-to-end, TTS audio | The product does its own speech recognition + minutes/action-item extraction. Reproducible, but the voice is unnatural | Feishu Minutes, Tongyi Tingwu, Otter, Fellow |
| **A-Human**: end-to-end, human reading | You and 2–4 classmates read from the script and record on phones. Closest to real use, but not fully reproducible | Same as above (at least the M2 and M3 meetings) |
| **B-Text**: text only | Paste `meetings/plain/Mx.txt` in. Tests only the "extraction" layer, unaffected by ASR | ChatGPT, Claude (baseline); and any product that supports pasting text |
| **B-Text-Expert-Reconcile (E2)**: multi-meeting text + expert reconciliation prompt | All of M1…Mk go into one message, with Mk as the current meeting; requires 4 transition types, two verbatim quotes, not mentioned, and a check against decision constraints; JSON output, organized by script. See the prompt in `templates/expert_reconcile_prompt.md` §1 | Claude (`claude-opus-5-5`, the same model as this system); ChatGPT can be added |
| **E2-naive**: multi-meeting text + plain prompt | Only says "update the status of earlier action items based on the last meeting," with no constraints, quotes, or not-mentioned handling | Same as above |
| **E2c**: E2 output + the same verbatim filter | `score_recon.py --verbatim-filter`; tests whether the "paraphrase rate" can be fixed with a single grep | Same as above |
| **E2d**: incumbent product's cross-meeting Q&A | Pick one product that can take uploaded text or audio and has cross-meeting Q&A (Otter AI Chat / Granola folder Q&A / Circleback / Fireflies AskFred / Tongyi Tingwu multi-file Q&A). Upload in order, then ask the same question as in E2; if unavailable, write "not tested (reason)" | See left |

**Why separate A and B?** If Feishu misses a commitment under condition A, it may be because it didn't hear it clearly (ASR), or because it heard it clearly but failed to extract it (extraction). Condition B removes ASR, which lets us localize the problem to the extraction layer. BriefPilot's positioning is "the step after transcription" (see `01_market-research/01` §9 [Inference]), so the condition B comparison matters most.
### 2.2 How Each Product Is Fed and Its Known Limitations

All "facts" in the table below come from official pages, accessed at the time of writing. Pages that could not be opened are marked "to be verified". **When you run the tests, go by the interface you actually see in the product that day**, and archive screenshots.

| Product | How to feed it | Known limitations (affect how results are read) | Source |
|---|---|---|---|
| **Feishu Minutes / Lark Minutes** | Desktop app → Minutes home → "Upload" → "Upload local file", or drag and drop; language defaults to "auto-detect" and can also be set manually | [Fact] Upload is supported on desktop only; uploaded files support "Chinese, English, Japanese and other languages", and the page says Minutes "can understand mixed Chinese and English speech", but it gives no performance data for uploaded files with mixed Chinese and English. [Fact] The page does not state supported formats or file sizes. [Summary · to be verified] The free tier gives each user 300 minutes of transcription per month, and local uploads count against it (the 5 transcripts total about 46 minutes by speech-rate estimate; actual TTS duration depends on the generated output; this is enough). Whether the upload entry point is the same in the international Lark version: **to be verified** | [1] [2] |
| **Feishu "Meeting Express"** | After all 5 recordings are uploaded, check whether it can link the action items across M2–M4 | Verified in the first-round review: Feishu has "Meeting Express" (weekly action-item roundup) and "enterprise information recognition" (colleague names / project names). This is the **strongest competitor** for H5, so it must be tested | See `01_market-research/06` |
| **Tongyi Tingwu** | Upload audio/video files on the web app | [Fact · Alibaba Cloud API docs] Offline files support "Chinese, English, Cantonese, Japanese, Korean, and free mixing of Chinese/English/Japanese/Korean/Cantonese/German/French/Russian"; speaker diarization supports "no separation, 2 speakers, multiple speakers"; single file "6 GB & 6 hours"; **the "action items" feature requires at least 90 seconds of audio and returns at most 6 action items, each 5–30 characters**. [Assumption · to be validated] Whether the web version also gives only 6 action items. If so, the recall ceiling for M4 (gold labels list 18 actions) is only 33%. The report must state "product design ceiling" and must not describe it as "extraction failure" | [3] |
| **Otter** | Web → Record/Import at top left, or drag into Conversations; formats include MP3/MP4/AAC/WAV/M4A | [Fact] The official page says "Otter supports English, Spanish, and French", **with no Chinese**. So M1–M4 (mostly Chinese) are expected to fail recognition on a large scale. This does not reflect weak extraction in Otter; the language is simply unsupported, and it must be annotated separately. M5 is mostly English, so it is a fair comparison for Otter. [Fact] Free accounts: single file up to 90 minutes, 300 minutes per month. [Conflict · to be verified] The first-round record says the Basic plan allows "only 3 file imports for life", which is inconsistent with the official page; the help center returns 403. If it really is only 3 imports, use them in the order M5 → M3 → M4 | [4] [5] |
| **Fellow** | Library (left sidebar) or the red microphone at bottom left → drag in file → choose recap language → Submit; MP3/M4A/WAV/MP4 | [Fact] Free plan allows 5 uploads per person, single file ≤100 MB, which exactly covers the 5 recordings. [Fact] The upload page only says "you can choose the recap language" and does not list which languages transcription supports, so **Chinese support is to be verified**. Verified in the first-round review: Fellow syncs two-way with GitHub, but the action-item page shows no "assignee confirmation / claiming" | [6] |
| **ChatGPT / Claude (baseline)** | B-Text: paste `meetings/plain/Mx.txt` plus the fixed prompt in `templates/baseline_prompt.md` | LLM output is stochastic. **Run each recording 3 times** and report the median and range. Record the model name and date. M2–M4 need a cross-meeting test: in one conversation, paste M2, M3, M4 in order, and open a separate conversation with only M3 as a control | — |
| Not recommended for testing | Gemini in Meet, Notion AI meeting notes, Krisp | Verified in the first-round review: Gemini in Meet does not support Chinese or multiple languages in one meeting; Notion speaker labeling supports English only; Krisp does not support Chinese. Testing them would only yield "language not supported" | See `01_market-research/06` |

### 2.3 Where the Audio Comes From

**Option 1: TTS (reproducible; recommended to do first)**

```bash
brew install ffmpeg                                   # if not already installed
python3 -I tools/make_audio.py --list-voices          # see which Chinese/English voices are on this machine
python3 -I tools/make_audio.py --meeting M3 --limit 4 # first preview the first 4 sentences
python3 -I tools/make_audio.py --meeting all          # generate audio/M1–M5.m4a and *.offsets.csv
```

- On the test machine this has been run successfully with `--limit` (first 4 sentences of M5, about 58 seconds). The full recordings have not been pre-generated, because voice assignment needs you to listen and decide yourself.
- Limitation: macOS ships very few Chinese voices (the test machine has only Tingting zh_CN and Meijia zh_TW), so the 5 Chinese speakers can only be told apart by "different voices + different speech rates"; the Chinese voices also pronounce English terms unnaturally. All of this will **depress** the scores of the products under test, so the results must state the "TTS condition". You can swap voices with `--voices my_voices.json`, for example giving M5's Zhou Lan an English voice.
- The real timing in the audio differs from the estimated timestamps in the transcripts. `audio/Mx.offsets.csv` gives the true start time of each sentence in the audio. When processing product outputs, use it to convert the product's timestamps back to transcript time (optional; timestamps are used only for the automatic-matching bonus).

**Option 2: Human readers (more realistic; do at least M2 and M3)**

- Find 2–4 classmates and assign each 1–2 roles; they read from `meetings/Mx_*.md`, with a phone placed in the middle of the table to record (simulating an in-person group meeting). They don't need to read the timestamps, and natural pauses and slips are fine, but **do not change any words**, otherwise the gold labels will no longer line up.
- Consent must be obtained before reading; see §5 on ethics.

**Text-only products**: paste `meetings/plain/Mx.txt` directly. It keeps the speakers and timestamps and does not include explanatory text such as the "synthetic data disclaimer".
## 3. Execution Steps (estimated 2–3 days)

| Step | What to do | Output | Estimated time |
|---|---|---|---|
| 0 | Review the gold labels: read through the 5 transcripts and `gold/*.jsonl`, change anything you disagree with, and record the changes in `results-template.md` §1.3. Ask 1 classmate to label M1 and M3 following `annotation-guide.md` §7 (dual-annotator procedure; §6 covers the 27 boundary cases), then compute Kappa | Reviewed gold labels, Kappa result | 0.5–1 day |
| 1 | Generate the audio (or record real human audio) | `audio/` | 1–2 hours |
| 1b | **Feasibility check (W1 D1, 30 minutes, before uploading)**: ① Feishu's "Meeting Digest" is based on smart minutes from "the past week", so uploading all 5 audio files on the same day cannot test cross-week behavior. Confirm whether uploads can be split into weeks by real date; if not, record "not tested (reason)". ② Whether uploaded Minutes recordings generate smart minutes. ③ Whether Lark (Singapore) has Meeting Digest. ④ Whether Fellow can ingest audio directly (if not, only A-Human with real meetings is possible, which is not done before IRB approval). For each item, write "testable / not tested (reason)" into `results-template.md` §1.2 | Feasibility record | 30 minutes |
| 2 | Create a clean account or workspace for each product and upload **in the order M1→M5** (to give cross-meeting features a fair chance) | 5 sets of minutes in each product | 2–3 hours |
| 3 | Preserve evidence: screenshot every output and export the full text (transcript + minutes) to `results/<product>/raw/` | Raw evidence | 1 hour |
| 4 | Organize: following `scoring.md` §3, convert each product's action items, decisions, and key points into `results/<product>/pred.jsonl`; save the exported full transcripts as `results/<product>/text/Mx.txt`. **Do not look at the gold labels while organizing**; ideally have a classmate organize one set independently as a cross-check | pred.jsonl, text/ | About 1 hour per product |
| 5 | Mapping: run `python3 -I score.py --pred ... --emit-mapping results/<product>/mapping.csv`, confirm or correct each row manually, then pass the file back as `--map` | mapping.csv | About 30 minutes per product |
| 6 | Scoring: `python3 -I score.py --pred results/<product>/pred.jsonl --map results/<product>/mapping.csv --pred-text-dir results/<product>/text --json results/<product>/metrics.json` | Metrics table | A few minutes |
| 7 | Fill in `results-template.md`: numbers, screenshot index, hypothesis verdicts, qualitative observations | Results report | Half a day |
| 8 | (v1.1) Layer 2: organize and score E2 / E2-naive / E2c with a script per `templates/expert_reconcile_prompt.md` §3; score this system the same way after exporting `transitions_pred.jsonl`; before running `--compare`, write k into `results-template.md` §6.1 | `recon_metrics.json`, paired results | About 1.5–2 days (including drafting the transition gold labels for review on W1 D1, 3 DIY runs, and mapping confirmation) |

**Directory convention** (`results/` is created by you):

```
results/
  feishu_A-TTS/   raw/  text/M1.txt…  pred.jsonl  mapping.csv  metrics.json
  tingwu_A-TTS/   …
  otter_A-TTS/    …
  fellow_A-TTS/   …
  chatgpt_B-Text_run1/ …
  claude_B-Text_run1/  …
```

## 4. Record Format

### 4.1 Product output (`pred.jsonl` after manual organization, one entry per line)

```json
{"id":"P01","meeting_id":"M3","text_span":"Wang Bo: finish the WidowX baseline by Sunday","owner":"Wang Bo","due":"2026-10-18","strength":null,"type":"action","evidence_timestamp":"00:01:10","cross_meeting_ref":"M2-05","status":null,"source_section":"Action items"}
```

| Field | Required | How to fill it |
|---|---|---|
| id | Yes | Unique within each product: P01, P02… |
| meeting_id | Yes | M1–M5 |
| text_span | Yes | The product's original wording, copied verbatim |
| owner | No | The owner the product states; null if none is given |
| due | No | The date the product states; if it is a relative expression such as "before next week's group meeting", **copy it verbatim** and do not convert it yourself |
| strength | No | Fill in tentative or suggestion only if the product explicitly marks the item as "suggested / possible / to be confirmed / maybe"; otherwise leave null (the script treats it as committed by the implicit rule) |
| type | No | Based on which section of the product it appears in: action items→action, decisions→decision, key points/conclusions→result; if unsure, use action |
| evidence_timestamp | No | The timestamp the product gives (converted to transcript time) |
| cross_meeting_ref | No | Fill in only when the product **explicitly says** "this follows up on X from last time"; use the id of X in the gold labels |
| status | No | Fill in done when the product marks the item as completed |
| source_section | No | The section name in the product, to make rechecking easier |

`templates/pred_template.jsonl` and `templates/mapping_template.csv` are blank templates.
### 4.2 Mapping file (`mapping.csv`)

```
pred_id,gold_id,note
P02,M3-03,Chinese-English paraphrase; automatic matching mismatched it; manually corrected
P15,FABRICATED,This item is not in the meeting
P17,DUP,Duplicate of P01
P18,EXTRA_OK,Content is accurate, but the gold spec does not label it separately
P20,TRAP:T-M3-1,Followed the injected instruction
```

### 4.3 Results

Write results to `results-template.md` (copy it, rename the copy to `results-YYYY-MM-DD.md`, then fill it in).

## 5. Ethics and compliance notes

1. **All data is synthetic.** The 5 meetings, all characters (周岚, 陈思远, 李沐晴, 王博, Daniel Ong, Priya Nair, 赵敏, Marco Rossi), the "Robot Learning Group", the LumaVLA project, and the company Kestrel Robotics are fictional and unrelated to any real person, lab, or company. OpenVLA, π0, LIBERO, SimplerEnv, DROID, FAST, LeRobot, RLDS, and similar names appearing in the text are public models, datasets, or tools, used only as terminology; all numbers associated with them are made up and do not reflect their real performance.
2. **Do not upload any real meetings, real lab data, or real colleagues' names**, including "just testing last week's group meeting while we're at it".
3. **Human read-aloud**: before recording classmates, tell them in person which third-party services the recording will be uploaded to (Feishu, Alibaba Cloud, Otter, Fellow), that these services may perform voiceprint or speaker identification, and that the recordings will be deleted after the experiment. Obtain explicit consent, preferably in writing. After the experiment, delete the recordings and transcripts in each product, and record the deletion date in `results-template.md`. Background: the first round documented that Fireflies was hit with a BIPA voiceprint lawsuit (3:25-cv-03399) and that Granola was hit with a class action on 2026-07-30 (3:26-cv-07926-EMC). Meeting AI that processes voice data carries real legal risk, so TTS is the default and human read-aloud is only a supplement.
4. **The prompt injection passage** (M3 [00:04:28]) is a harmless piece of test text. Its purpose is to check whether a product treats instructions read aloud in a meeting as system instructions. It runs only in your own account and does not target any product's infrastructure; the "external account kx-77" mentioned in it is fictional. Do not use it to test anyone else's account or workspace.
5. **Terms of service**: use personal free or trial accounts and use product features normally, with no automated scraping and no bypassing of quotas. When presenting results externally, you may quote snippets and screenshots of product output from your own account, noting the product version and date. Do **not** phrase conclusions as generalizations such as "Product X's accuracy is Y%"; say only "on these 5 synthetic meetings".
6. **The gold labels are AI-drafted.** The gold labels were drafted by AI following the annotation spec. Until the project owner has reviewed them and completed the two-annotator agreement check, they must not be described externally as "human gold labels".

## 6. How to interpret results (avoiding over-conclusion)

- **Small sample**: 135 gold items, of which 70 are action items; each product is run once per condition (the LLM is run 3 times). `score.py` also reports Wilson 95% confidence intervals. Do not draw conclusions from gaps within 10 percentage points.
- **Synthetic ≠ real**: the transcripts are "designed", so trap density is higher than in real group meetings. Conclusions may only be phrased as "on meetings containing these phenomena, product X performs as follows…", and real user interviews (see `02_user-research/`) should then be used to verify how common these phenomena are in real group meetings.
- **Unsupported language is not an extraction failure**: Otter's low score on Chinese meetings should be listed separately and not compared together with "extraction ability".
- **Product design caps**: for example, Tongyi Tingwu returns at most 6 action items (per its API documentation). In such cases, report recall both as the "raw value" and as the "value relative to the cap".

## 7. Sources (all accessed at the time of writing)

1. Feishu official website, "Feishu Minutes: The best audio/video-to-text and meeting minutes tool for professionals" (Chinese page title): https://www.feishu.cn/content/article/7578773484596153570 [Fact: upload on desktop only, automatic language detection, Chinese/English/Japanese, "中英文混说" (mixed Chinese and English speech)]
2. Feishu pricing adjustment announcement (2024): https://www.feishu.cn/new-announcement/pricing-adjustment2024 [Summary, to be verified: the first round only captured the title; 300 minutes/month comes from a search snippet]
3. Alibaba Cloud Tongyi Tingwu feature description: https://help.aliyun.com/zh/tingwu/features [Fact: languages, speaker diarization, formats, 6 GB & 6 hours, at most 6 action items; note that this is API documentation and whether the web version is the same remains to be verified]
4. Otter official MP3-to-text page: https://otter.ai/mp3-to-text [Fact: import methods, formats, "Otter supports English, Spanish, and French", free tier 90 minutes per file, 300 minutes/month]
5. Otter Help Center article on importing files: https://help.otter.ai/hc/en-us/articles/360047733634-Import-audio-and-video-files [To be verified: returned HTTP 403]
6. Fellow Help Center, "Uploads": https://help.fellow.ai/en/articles/10697541-uploads [Fact: entry points, formats, upload count and size per plan; Chinese not mentioned]
7. First-round integrity review: `../../01_market-research/06_research_integrity_review.md` (verified conclusions on Fellow–GitHub two-way sync, Feishu meeting express/enterprise information recognition, Gemini/Notion/Krisp language limits, the Granola lawsuit, etc.)
8. First-round international competitors: `../../01_market-research/02_competitors_global_otter_fireflies_granola.md` (Otter Basic import limits, Fireflies BIPA lawsuit)
9. First-round Chinese competitors: `../../01_market-research/01_competitors_china_feishu_minutes.md` (the user workflow of "transcribe with Tingwu, then hand off to Doubao"; §9 test recommendations)
