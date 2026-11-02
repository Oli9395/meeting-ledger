---
title: "User Research 04 — Cross-Cutting Constraints and Opportunities: Mixed Chinese-English Speech, In-Person Meetings, Privacy/Localization, the No-Recording Route, and the State of Open Source"
status: draft
sources_count: 59
sources_count_method: Number of unique URLs in the sources section (recalculated at wrap-up; original value 47)
evidence_note: This is a first-round file. The body does not label every item as [Fact] or [Summary], and access dates were not recorded per source (all treated as at the time of writing). Any item labeled [Fact] without a record of having opened the original page in the body should be treated as [Summary·to be verified] before it is cited (note added in the wrap-up revision).
---

# User Research 04: Cross-Segment Constraints — Can Mixed Chinese-English Speech, In-Person Meetings, and Privacy/Localization Become Functional Differentiators?

> **Reading notes**
> - Every claim is labeled with one of three tags: **[Fact]** = verifiable against a source; **[Inference]** = derived from several facts, with no direct evidence; **[Assumption]** = to be validated, requires interviews or experiments.
> - The nature of each source is stated: paper, official documentation, vendor marketing page, third-party or competitor blog. Where only a search snippet was seen and the original was not opened, it is marked "(summary, to be verified)".
> - Method: about 45 Chinese and English web searches, plus about 25 raw page fetches (full HTML of the CS-Dialogue and Fun-ASR papers, the MERaLiON model card, Granola, Otter, Fireflies, official Feishu pages, and the GitHub pages of whisper.cpp, FunASR, SenseVoice, Meetily, and Anarlog). **The search quota ran out in the second half of this round**, so the following could not be searched further: the original Plaud Trust Center page (returned 429), the original Zhihu/Xiaohongshu posts complaining about "Feishu Minutes handling mixed Chinese-English", the target university's official AI tool policy, and details of Granola's "no recording" claim. See Section 9.
> - The local demo's hardware baseline is estimated for a laptop with an **Apple M1 Max and 32 GB of RAM**.

---

## 0. The answer first: five conclusions and why

1. **[Fact→Inference] Mixed Chinese-English speech is hard because of the English half, and in research meetings that English half is exactly the terminology.** On CS-Dialogue, a 104-hour mixed Chinese-English conversation dataset, Paraformer's Chinese CER is only 3.70%, but its English WER is as high as 32.02%; Whisper Large-V2's English WER is 31.11%. Even the best performer, SenseVoice-Small, has an English WER of 15.57%. [Inference] The English words in lab group meetings are mostly terms like "transformer / VLA / baseline / ablation", which carry the highest information density. **The errors concentrate on the most valuable words**, and the action items that follow ("swap the baseline for OpenVLA and rerun the ablation") get distorted along with them.
2. **[Fact→Inference] "Supports mixed Chinese-English recognition" alone cannot be a differentiator; vendors are closing this gap at the ASR layer.** AssemblyAI Universal-3.5 Pro announced native English-Mandarin code-switching support in August 2026. Granola's desktop multilingual mode already lists Mandarin and Cantonese. Alibaba's Fun-ASR treats code-switching as a core feature. What can differentiate is something further up the stack: **a loop from the team's or project's own glossary → recognition correction → action-item fields**, plus a measurable "term recall rate".
3. **[Fact→Inference] For in-person meetings, the "can we record" problem is largely solved; what remains unsolved is "should we record".** Fireflies and Otter have phone recording, Feishu Minutes can upload audio and record live from a phone, Granola captures via the microphone, and there is hardware such as Plaud. On the other side, a 500-person US survey from July 2026 found that among people who had encountered an AI note-taker, only 34.7% said they were "asked for consent every time". Otter (August 2025) and Granola (July 2026) were both hit with class-action lawsuits for "recording without consent and using the recordings for training". Universities including Virginia Tech (March 2026) and CUNY (September 2025) have banned Otter/Read.ai bots. **[Inference] In scenarios like one-on-one advisor meetings and whiteboard discussions, social and compliance costs are the real barrier.**
4. **[Fact→Inference] "Data never leaves the computer" is technically feasible in 2026, but it is only a threshold, not a moat.** whisper.cpp has 54.8k stars and supports Metal/CoreML. SenseVoice-Small runs at roughly 115–131× real time on an M4 Pro. Qwen3-ASR 0.6B/1.7B is open source, and the Qwen3 series runs on Ollama. "Local meeting notes" is also already crowded in open source: Meetily has 32.4k stars and Anarlog (formerly Hyprnote) has 9.7k stars. So localization only works in combination with conclusions 1 and 2; on its own it is not a selling point.
5. **[Assumption] For research settings, a hybrid "notes first, recording optional, audio deleted after the meeting" route may suit better than "record everything".** No direct evidence was found in lab settings; interviews are needed to validate this. Granola itself is not truly "no recording" either: it captures microphone and system audio, then deletes the audio once transcription completes. No mainstream product was found that offers "text-only notes, zero audio".

---

## 1. Research questions and scope

| ID | Question | Why ask (relation to BriefPilot) |
|---|---|---|
| Q1 | How do mainstream ASR systems perform on mixed Chinese-English speech and terminology? What evidence exists on the language environment of Singapore/overseas Chinese teams and domestic labs? | BriefPilot's "action-item drafts" are built on top of transcription. If a term is transcribed wrongly, the "what to do" field is wrong |
| Q2 | How well are in-person meetings (whiteboard, one-on-one) supported? What social concerns do users have about recording? | Much research discussion happens in person, where meeting-joining bots are of no use |
| Q3 | Privacy/localization: what are each product's data policies, and can 2026 local ASR/LLMs support a "data never leaves the computer" demo? | Unpublished data and patentable ideas are highly sensitive information |
| Q4 | Is Granola-style "enhance your own notes" a better fit for research settings? | It might sidestep both the consent problem and the privacy problem |
| Q5 | State of open-source projects: which exist, how active are they, and what is missing | To judge where the increment from building our own lies, and avoid reinventing the wheel |

---
## 2. Q1 Chinese-English Code-Switching

### 2.1 Academic evaluations: only a few have comparable numbers

**CS-Dialogue (2025, arXiv 2502.18913)**: the most direct comparison found so far.
- [Fact] 104 hours of spontaneous dialogue from 200 speakers, all Chinese citizens fluent in English, from across China (most from Sichuan, followed by Beijing and Guangdong). Recorded in pairs on phone microphones, with each conversation moving from "pure Chinese → mixed → pure English". The dataset is "freely available for academic use"; the paper does not specify a license. Source: https://arxiv.org/html/2502.18913
- [Fact] Test set results (paper Table 8):

| Model | Chinese CER | English WER | Mixed MER |
|---|---|---|---|
| Whisper Large-V2 | 10.7% | 31.11% | 15.29% |
| Qwen2-Audio | 7.15% | 19.82% | 9.76% |
| Paraformer | **3.70%** | 32.02% | 9.65% |
| SenseVoice-Small | 4.42% | **15.57%** | **6.71%** |

- [Inference] Several readings: (a) all four models have English WER far above Chinese CER, so the English segments within code-switched speech are a shared weak spot; (b) Paraformer is best on Chinese and worst on English, showing that "strong on Chinese" does not mean "strong on code-switching"; (c) Whisper is the default engine in many open-source meeting tools, but ranks last on this set; (d) these are phone recordings in quiet environments, while real group meetings add far-field audio, multiple speakers, and whiteboard noise, so error rates can only be higher (to be tested).

**Numbers from other papers** (different evaluation setups, not comparable across rows):
- [Fact] Fun-ASR technical report (Alibaba Tongyi, arXiv 2509.12508), Section 6.2.4: on two Chinese-English code-switching test sets, offline-mode WER is about 1.59% and 4.50% (after RL), and streaming is about 2.28% and 5.07%. One test set comes from TTS-synthesized dialogue and the other is internal recordings. This is a vendor self-evaluation and is not compared against Whisper/SenseVoice in the same table. Source: https://arxiv.org/html/2509.12508v3
- [Fact] Same report, Section 6.2.5: the hotword mechanism is retrieval-augmented, with hotword recall above 0.97 on most topics and 1.0 on the "person names" topic. On model size, Fun-ASR-nano is about 0.8B (0.2B encoder + 0.6B LLM decoder), and the full version is a 0.7B encoder + 7B LLM. Source as above.
- [Fact] The winning MER in the ISCSLP 2022 Chinese-English code-switching challenge was 16.70% (abstract, to be verified). Source: https://arxiv.org/pdf/2210.06091
- [Fact] A 2023 work adds adapters to Whisper, training only 5.6% additional parameters, and reaches a MER of 14.2% (abstract, to be verified). Source: https://arxiv.org/html/2312.08856v2
- [Fact] The case analysis in DOTA-ME-CS (2025) shows that both Paraformer and SenseVoice misrecognize Chinese nouns embedded in English sentences (e.g., "菠萝包", pineapple bun), also misrecognize "bakery", and make clearly more errors under speed and timbre variation (abstract, to be verified). Source: https://arxiv.org/pdf/2501.12122
- [Note] A paper comparing Whisper and LLM-ASR on code-switching (arXiv 2412.00721) has been **withdrawn**, with the authors noting the "work is not yet complete"; its numbers are not cited. Source: https://arxiv.org/abs/2412.00721

### 2.2 Commercial products and APIs: support for Chinese-English code-switching (as of 2026-11)

| Product / engine | Code-switching support | Terminology / hotword capability | Nature of evidence |
|---|---|---|---|
| OpenAI Whisper (open source) | Can output mixed text, but code-switching is not an official feature. GitHub discussion #976 asks whether Chinese and English can be kept as spoken; no one replied | `initial_prompt` can carry terms (third-party suggestion) | [Fact] https://github.com/openai/whisper/discussions/976 ; an individual developer's WhisperPen claims large-v3-turbo "performs well" on mixed Chinese-English and terminology, which is anecdotal https://penchan.co/en/ai/coding/introducing-whisperpen/ |
| Alibaba Paraformer / SenseVoice / Fun-ASR (open source + cloud) | See 2.1; Fun-ASR lists code-switching as a core feature | Paraformer's `generate()` supports a `hotword` parameter; the official SenseVoice repo has **no** hotword feature (the third-party streaming-sensevoice does) | [Fact] https://github.com/modelscope/FunASR ; https://github.com/FunAudioLLM/SenseVoice |
| iFlytek Tingjian (讯飞听见) | App store descriptions mention "mixed Chinese-English recognition", but which app they belong to is to be verified (many third-party apps share the name); a third-party roundup says its "hotword weights are adjustable" | To be verified | Marketing page plus third-party roundup, **to be verified** https://peihuachen.github.io/ai-tools-hub/posts/commercial-asr-comparison-chinese-english-dialect-2026.html |
| Feishu Minutes | Officially claims support for multiple languages and dialects; **no standalone evaluation of Chinese-English code-switching found** | Keywords can be replaced after the meeting; the lark-minutes CLI supports editing Minutes outputs (abstract) | [Fact] https://www.feishu.cn/content/article/7600354924362337245 ; https://tessl.io/registry/skills/github/larksuite/cli/lark-minutes/review ; one blogger collected recurring misrecognitions (e.g., "语法弹" → "语法糖") into replacement rules and fixes them in batch with a script https://jimmylv.substack.com/p/nw5i3ei (abstract) |
| ByteDance Doubao / Seed-ASR | The official blog says it can use context to improve person names and new terms but **does not explicitly mention code-switching**; a third-party page says the Doubao input method supports mixed Chinese-English input | Context-aware | [Fact] https://team.doubao.com/blog/doubao-s-listening-skills-unboxing-live-see-how-seed-asr-overcomes-the-speech-recognition-bottleneck ; no code-switching numbers found in the technical report |
| Google Chirp 3 | Has `cmn-Hans-CN`; "language-agnostic transcription" outputs in the **dominant language** and does not state per-segment switching; region and GA status differ between the Chinese and Japanese docs | Speech Adaptation | [Fact] https://cloud.google.com/speech-to-text/v2/docs/chirp_3-model?hl=zh-cn (abstract, to be tested) |
| Deepgram Nova-3 | Code-switching supports 10 languages, and **Mandarin is not among them**; what was added on 2026-03-31 is monolingual Mandarin support | Keyterm prompting | [Fact] https://developers.deepgram.com/docs/multilingual-code-switching ; https://developers.deepgram.com/changelog/2026/3/31 (abstract) |
| AssemblyAI Universal-3.5 Pro | A 2026-08-19 blog post announces **native English-Mandarin code-switching support** (18 languages), with a demo recognizing a single Chinese character inside an English sentence; **no WER numbers given** | Natural-language contextual prompting | [Fact] https://assemblyai.com/blog/universal-3-5-pro-code-switching-contextual-prompting |
| Azure Speech | In 2024 a user reported "no mixed Chinese-English locale, only zh-CN plus hotwords"; the official reply pointed to a multilingual **speech translation** preview | Custom Speech / hotwords | [Fact] https://learn.microsoft.com/en-us/answers/a/1575915 |
| Otter | A third-party review says it supports 6 languages, with Chinese in beta/experimental status and **only one language selectable per meeting** | Custom vocabulary | Third-party, **to be verified** https://www.laxis.com/blog/otter-ai-review/ |
| Granola | The desktop multilingual mode lists Mandarin and Cantonese (the blog post is dated September 2; the page does not show the year); older docs advise "if most meetings are in English, keep English selected for better quality" | None seen | [Fact] https://www.granola.ai/blog/granola-now-supports-32-languages ; https://docs.granola.ai/help-center/customising-granola/multi-language |
| MERaLiON-3-3B-ASR (Singapore) | Targets code-switching among Singapore English, Mandarin, Malay, etc. (including Singlish). Average WER on the code-switching test sets is 22.65 (26.24 for the older 10B version); the test sets are mostly private; self-hosting requires a single 80GB GPU | — | [Fact] vendor self-evaluation https://huggingface.co/MERaLiON/MERaLiON-3-3B-ASR |

**[Inference] Summary**:
- Before 2025, "Western products don't understand Chinese-English code-switching" was broadly true. By the second half of 2026, AssemblyAI and Granola have caught up, while Deepgram has not. Domestic Chinese engines and Alibaba's open-source models have always been strong on Chinese, but **English terminology segments remain a shared weakness** (see the table in 2.1).
- So the differentiator cannot be framed as "we support mixed Chinese-English". It can be framed as: **"On your lab's terminology, our term recall is X%, and the tool you use now is Y%"**, provided that this evaluation is built first.
### 2.3 Language-environment evidence: Singapore, overseas Chinese communities, domestic labs

- [Fact] The SEAME corpus was collected by a Singapore university and other institutions. It contains spontaneous conversations and interviews from 156 speakers in Singapore and Malaysia, mostly in Mandarin mixed with English. Recognition difficulties include missed switch points, language misidentification, and accent mismatch (JSALT 2022 report). Sources: https://voxkitchen.readthedocs.io/en/latest/datasets/seame/ ; https://www.clsp.jhu.edu/wp-content/uploads/2022/07/2022_07_06.pdf (summary)
- [Fact] Research on colloquial Singapore Mandarin by Cher Leng Lee (NUS): university students often mix in English when talking with peers and parents, but have clear difficulty when talking with grandparents. Source: https://fass.nus.edu.sg/srn/2022/03/07/filling-gaps-or-code-choice-code-switching-across-generations-in-colloquial-singapore-mandarin/ (summary)
- [Fact] Local Singapore institutions train dedicated Singlish/code-switching models (the MERaLiON series, and Polyglot-Lion, fine-tuned from Qwen3-ASR, which admits that "the lack of a code-switching test set is a major limitation"). [Inference] This suggests there is real local demand that general-purpose models do not cover well. Source: https://arxiv.org/pdf/2603.16184 (summary)
- [Evidence gap] **No study or survey on "language use in research-lab group meetings" was found**; searches in both Chinese and English returned nothing. That group meetings at domestic universities are "mostly Chinese, with terminology in English" is a common-sense observation, **[Assumption]; to be verified by counting the share of English tokens in 1–2 self-recorded samples**. The project owner works in a lab at the target university, so this can be done at low cost (consent from those present is required before recording; see Section 3).
- [Inference] Terminology characteristics of VLA research: many English abbreviations and model names (RT-2, OpenVLA, π0, LIBERO, SimplerEnv, action chunking, diffusion policy), most of which are out-of-vocabulary for general-purpose ASR, and pronunciation is not standardized (whether "π0" is read as "pi zero" or as the Chinese "派零" (pài líng, "pie zero")). So a "project glossary" is more valuable in research settings than in typical company meetings.

---

## 3. Q2 Social concerns around offline meetings and recording

### 3.1 Product support for offline recording ("can it record?")

| Product | Offline approach | Evidence |
|---|---|---|
| Fireflies | One-Touch Record in the mobile app: record, pause, and save, with the result going automatically into the Notebook; the official help page does not mention uploading existing audio, or language and duration limits | [Fact] https://guide.fireflies.ai/articles/4565146696-how-to-transcribe-offline-meetings-using-fireflies-mobile-app |
| Otter | The mobile app can transcribe face-to-face conversations in real time; a third-party review says "it has to be started manually at the table" | Third-party https://letterly.app/blog/otter-app-review/ (summary) |
| Feishu Minutes | In the client: "New Minutes → Upload audio/video"; the article also mentions that real-time recording on mobile can be transcribed too | [Fact] Feishu official-site article https://www.feishu.cn/content/article/7578773484596153570 (marketing article; upload limits not stated in official documentation) |
| Granola | Captures microphone and system audio locally, with no bot; audio is cached only temporarily during transcription and deleted afterward | [Fact] https://docs.granola.ai/help-center/consent-security-privacy/security-privacy-data-faqs |
| Plaud (hardware recorder card/pendant) | The App Store listing claims support for 112 languages, speaker labeling, and custom vocabularies, and claims HIPAA/GDPR/SOC2 compliance | Marketing page https://apps.apple.com/sg/app/id6450364080 (summary; **performance on mixed Chinese-English speech unknown**) |

[Inference] **Offline "can it record" is not a blank space**; tools are already abundant. BriefPilot should not treat "supports offline recording" as a differentiator.

### 3.2 "Should it record?": consent, trust, and litigation

- [Fact] A survey commissioned by Kolmogorov Law from Pollfish (2026-07-08, employed US adults, n=500): 33.4% had seen an AI note-taker in a meeting; of those 167 people, only 34.7% said they were "always asked for consent," 25.1% said they were "never asked," and 18.8% of respondents found out only afterward that they had been recorded. The law firm commissioned the survey and has a stake in the result. Source: https://krdo.com/stacker-business-economy/2026/07/16/ai-notetakers-have-sat-in-on-1-in-3-us-workers-meetings-but-only-a-third-say-they-were-asked-first/
- [Fact] Otter class action (Brewer, US federal court, Northern District of California, 2025-08): the plaintiff alleges that Otter by default asks only the host for consent and not the other participants, and uses the conversations for training; the plaintiff also claims that Otter's de-identification cannot remove confidential information. No 2026 developments were found. Source: https://www.npr.org/2025/08/15/g-s1-83087/otter-ai-transcription-class-action-lawsuit
- [Fact] Granola class action (Chamberlain, case no. 3:26-cv-07926-EMC, filed 2026-07-30): alleges that "no-bot" capture does not notify others by default, **both online and offline** (a chat message or on-screen notice has to be enabled separately), that training is on by default for Free/Business plans, and that Business users can only opt out one by one. These are allegations, and Granola had not publicly responded at the time. Source: https://ppc.land/granola-sued-for-recording-meetings-without-consent-to-train-ai-models/
- [Fact] At the university level: Virginia Tech (2026-03) notified that Otter.ai was used without authorization and required accounts to be deleted; CUNY (2025-09) blocked Read.ai and Otter.ai from joining meetings; the University of New Mexico restricts recording in meetings that discuss high-risk data such as identifiable-subject information; Santa Clara specifies "don't use it if any participant objects." Sources: https://news.vt.edu/notices/it/2026/03/it-ai-meeting-assistants.html ; https://mailings.york.cuny.edu/cgi-bin/dada/mail.cgi/archive/faculty_ft/20250903165544/ ; https://airesources.unm.edu/ai-guidance/ai-meeting-capture.html ; https://www.scu.edu/ai-resources/guidelines/ai-meeting-assistant-guidelines/
- [Fact] Singapore: secondary legal commentary says no statute prohibits a participant from recording a conversation themselves (close to one-party consent), but when an **organization** makes business-related recordings, the PDPA requires prior notification and consent. The original PDPC text has not been verified. Sources: https://singaporelegaladvice.com/can-an-organisation-record-a-conversation-without-consent/ ; https://www.recordinglaw.com/singapore/recording-laws/ (summary, to be verified)
- [Fact] A blog quotes a Reddit user as saying an AI note-taker is like "a silent, faceless stenographer in the room," especially awkward in sensitive discussions (secondhand account). Source: https://affine.pro/blog/bot-vs-no-bot-ai-meeting-recorder (summary)

**[Inference] What this means for research settings**:
- One-on-one meetings with an advisor involve a **power asymmetry**: a student can hardly say "let me record this" to the advisor, and can hardly refuse when the advisor records the student. "Don't record if anyone objects" is effectively empty in this kind of relationship.
- In group meetings, people present unpublished results, and even conjectures they themselves are unsure of. Being recorded may discourage sharing half-formed ideas, which is exactly what makes group meetings valuable ([Assumption]; needs interview validation).
- This points to an opportunity: **a "consent-first" interaction design**. Show a clear on-screen notice before recording, display who has consented, support "off the record for this segment" (an off-the-record button), delete audio after the meeting by default, and keep only the confirmed text. These are feature-level differences, and they are also consistent with BriefPilot's existing "human confirmation" philosophy.

---
## 4. Q3 Privacy and Localization

### 4.1 Data-Training Policies of the Main Products (Checked Against the Original Text)

| Product | Trains on user data? | Key wording / takeaways | Source |
|---|---|---|---|
| Otter | **Yes**: trains its own AI on de-identified audio and transcripts; the policy notes that transcripts "may contain personal information"; there is no dedicated training opt-out, only the general right to withdraw consent / object to processing | Effective date 2026-06-16 | [Fact] https://otter.ai/privacy-policy |
| Granola | By default "may use anonymized data to improve the service"; **off by default for Enterprise**; individuals can turn it off in Settings; OpenAI/Anthropic are not allowed to use the data for training; the effect of turning it off on past data is not stated | — | [Fact] https://docs.granola.ai/help-center/consent-security-privacy/model-training |
| Fireflies | States that meeting content (audio, video, transcripts, summaries) is **never** used to train any AI model; has zero data retention (ZDR) agreements with its transcription and LLM providers; data localization is available only on Enterprise | The page only says "updated 17 days ago" | [Fact] https://guide.fireflies.ai/articles/2154538358-policy-on-keeping-information-safe |
| Feishu | An article on its official site says that "**without customer authorization**, enterprise private data is not used for model training, and existing internal enterprise data assets are not proactively scanned" (about "Doubao in Feishu"); the article also advises relying on the contract and actual configuration | Product description, not a contract term | [Fact] https://www.feishu.cn/content/article/7667878625560677345 |
| Plaud | Secondary sources disagree: one says training requires a manual opt-in, another quotes its policy as "does not use personal data for training"; fetching the original from the trust center failed (429) | — | **To be verified** https://www.mentalyc.com/blog/is-plaud-hipaa-compliant |

[Inference]
- Policies are tightening quickly: Fireflies markets "no training," and Granola's enterprise tier is off by default. So "we don't train on your data" has already become an **industry baseline** and is no longer a differentiator.
- The real structural difference is **whether data leaves the device**. Any cloud route will lead university IT to require a vendor contract and a data sharing agreement (DSA); see the guidance from Penn State and other universities in 3.2. Cloud tools used by individual researchers mostly have no such agreement. Running locally can sidestep the compliance obstacle of "no contract" ([Inference]; the target university's specific policy was **not found**, to be verified).
- Unpublished research data: no university policy specifically addressing "unpublished results discussed in group meetings" was found (an evidence gap). However, several universities classify "meetings involving participant information" as high-risk, which can serve as an analogy.

### 4.2 Local ASR Availability in 2026

| Option | Status (as of the time of the fetch) | What it means for M1 Max/32GB |
|---|---|---|
| whisper.cpp | 54.8k stars, MIT; supports Metal, Core ML (ANE), CUDA, Vulkan, etc.; built-in Silero VAD; speaker diarization is only the experimental tinydiarize (`[SPEAKER_TURN]`) [Fact] https://github.com/ggml-org/whisper.cpp | Can run large-v3-turbo. [Inference] 1 hour of audio is expected to take a few minutes to a dozen or so minutes, **to be tested on this machine** |
| SenseVoice-Small | 9.7k stars; code is MIT, weights follow the FunASR model license (maintainers say commercial use is fine as long as the license is followed); supports Chinese, Cantonese, English, Japanese, Korean; non-autoregressive, officially claimed to be more than 15x faster than Whisper-Large; has timestamps; **no official hotword support** [Fact] https://github.com/FunAudioLLM/SenseVoice | A third party measured it on an M4 Pro with MLX: a 27-minute Chinese podcast in 13.83 seconds, about 115–131x real time; Chinese CER 7.69%, English WER 8.46% (FLEURS read speech). **Mixed Chinese-English not tested** [Fact] https://whispernotes.app/blog/sensevoice-fastest-cjk-transcription |
| FunASR toolkit (Paraformer, Fun-ASR-Nano 0.8B, etc.) | 20.9k stars; toolkit is MIT, model weights are licensed separately; Paraformer supports hotwords; speaker diarization relies on an FSMN-VAD + CAM++ pipeline, with anonymous labels; can be run via llama.cpp/GGUF, an OpenAI-compatible service, an MCP server, and more [Fact] https://github.com/modelscope/FunASR | Hotword support is the most direct technical lever for "glossary-based correction" |
| Qwen3-ASR 0.6B/1.7B | Open-sourced 2026-01-29, includes ForcedAligner-0.6B; 52 languages and dialects; license reportedly Apache-2.0 (third-party claim, to be verified); code-switching not explicitly stated officially [Fact] https://github.com/QwenLM/Qwen3-ASR ; https://pypi.org/project/qwen-asr/ | Third-party Mac test: Chinese CER 6.49%, English WER 4.49%, about 7.6x real time, peak memory 2.43 GiB (same whispernotes source as above) |
| FireRedASR2 (Xiaohongshu) | Open-sourced 2026-02-12, Apache-2.0; the README claims Mandarin CER better than Doubao-ASR and Fun-ASR (self-reported) [Fact] https://huggingface.co/FireRedTeam/FireRedASR2-AED/blob/main/README.md ([Summary]) | Can serve as a fallback; code-switching is not its main selling point |
| WhisperX | About 21.7k–24k stars (aggregator sites disagree); wav2vec2 forced alignment provides word-level timestamps, pyannote handles speaker diarization (requires an HF token), BSD-2 ([Summary], to be verified) https://gittrend.io/repo/m-bain/whisperX | One of the most mature open-source routes for speaker diarization, but it is built on Whisper and so inherits Whisper's weakness with mixed-language speech |
### 4.3 Local LLM (action item extraction, summarization)

- [Fact] The Ollama registry has qwen3.6, offered in 27B (about 17GB) and 35B (about 24GB) versions with a 256K context window. Source: https://registry.ollama.ai/library/qwen3.6 (summary)
- [Fact] An internal team Ollama configuration log shows that on a laptop with 12GB of VRAM, qwen3:8b fits entirely in VRAM and runs 4.8x faster than 14B; in their 16-question general test, qwen3.6 scored 15/16 and qwen3:14b scored 11/16 (anecdotal, not a summarization task). Source: https://git.azcomputerguru.com/azcomputerguru/claudetools/src/commit/44247909366d7bae7e3d683847b583fbbd6fc596/.claude/OLLAMA.md
- [Evidence gap] **No public evaluation was found of small local models on "Chinese / mixed Chinese-English meeting action item extraction."** The meeting-extraction evaluations that turned up almost all use cloud models; for example, Amazon Nova's faithfulness on QMSum is about 0.80–0.83.
- [Inference] Running ASR and a 27B-class LLM at the same time on 32GB of unified memory will be very tight. There are two options: transcribe first, free the memory, then extract; or use an 8B/14B model for extraction, at the cost of having to rely on evaluation to backstop JSON structure stability and the ability to "not make things up." BriefPilot already has two gates, "leave missing fields blank rather than guess" and "human confirmation," which act as a natural buffer against hallucination risk from local models.

**[Inference] Conclusion: for a "data never leaves the computer" demo, feasibility is high for the ASR layer and medium for the LLM extraction layer**, and the latter needs to be demonstrated with our own evaluation set.

---

## 5. Q4: Is a "no recording, text notes only" approach (Granola-style) a better fit for research settings?

- [Fact] Granola's core interaction is "the user jots down key points, and the AI enhances the notes using the transcript." But it **still captures audio** (microphone + system audio) and only deletes it after transcription; see 3.1. So Granola is not "no recording" but rather "no stored audio, no bot." In July 2026 it was sued, and one of the allegations is precisely that it captures audio "invisibly" without notifying others.
- [Inference] **Pros and cons for research settings**:

| Dimension | Full recording + transcription | Notes-first + optional local recording (audio deleted immediately) | Text notes only (zero audio) |
|---|---|---|---|
| Consent and social cost | High (especially in 1-on-1s with an advisor) | Medium (can be toggled per segment, can be disclosed) | **Lowest** |
| Privacy and compliance | Depends on the cloud provider's policy | Low when processed locally | **Lowest** |
| Completeness of information | Highest | Medium-high | Low; depends on the note-taker's habits |
| Mixed Chinese-English terminology | Depends on ASR | Terms in the notes are correct and can be used to **back-correct** the transcript | No ASR problem |
| Difficulty of action item extraction | Medium (noisy) | **Medium-low** (notes are a strong signal) | High (notes are sparse; "who/when" is often missing) |
| Fit with BriefPilot's current design | The current PRD's input is "meeting minutes text" | Good fit | **Perfect fit**: the PRD already takes minutes text as input |

- [Inference] One point worth noting: the input of BriefPilot's current PRD is already "meeting minutes text," not audio. So "**text first, audio optional, local processing**" not only fits the social constraints of research settings but is also the cheapest route from an engineering standpoint. The demo can start with "text notes → action items" and treat "local audio transcription" as a pluggable enhancement.
- [Inference] "Back-correcting the transcript with notes" is a **somewhat novel** idea: terms the user jots down (such as "OpenVLA") are fed to the ASR or post-processing as on-the-spot hotwords or prompts. No product was found that explicitly does this (limited evidence, **[Assumption], to be verified**).
- [Assumption] Will graduate students actually take notes during group meetings? If they don't already, "notes-first" has no input. Interviews need to ask: who takes notes now, where (paper, Notion, Feishu docs, WeChat), and what they write down.

---

## 6. Q5: Current state of open-source projects and feature gaps

| Project | Activity (at time of fetch) | What it does | What it doesn't do or is unclear | Source |
|---|---|---|---|---|
| Meetily (Zackriya-Solutions/meetily) | 32.4k stars, 3.6k forks; MIT; labeled Pre-Release, v0.4.1 | Local real-time transcription with Whisper/Parakeet, mixing microphone and system audio; summaries via Ollama or Claude/OpenAI, etc.; supports audio import (Beta); macOS/Windows/Linux | README **does not mention action items**; speaker identification, chatting with the meeting, and custom templates are PRO or "coming soon"; supported languages are not listed | [Fact] https://github.com/Zackriya-Solutions/meeting-minutes |
| Anarlog (formerly Hyprnote → Char → Anarlog) | 9.7k stars, 822 forks; community edition MIT, enterprise components under commercial license | No bot; captures device audio; local transcription on supported Macs; LLM can connect to Ollama/LM Studio; data stored in local SQLite; mobile beta | Chinese support, in-person meetings, and action items are all **not specified**; the team's focus has shifted to another product, char | [Fact] https://github.com/fastrepl/anarlog ; https://anarlog.so/blog/char-is-now-anarlog |
| whisper.cpp / WhisperX / FunASR / SenseVoice | See 4.2 | Engine layer | Not responsible for meeting semantics | See above |
| Feishu lark-minutes CLI | Official open-source skill | Uploads audio to generate Feishu Minutes, edits the outputs | Depends on the Feishu cloud | https://tessl.io/registry/skills/github/larksuite/cli/lark-minutes/review (summary) |

**[Inference] Summary of gaps**:
1. Open-source meeting tools all stop at "transcription + summary"; **not one treats "action items → human confirmation → tracking" as a first-class concern**.
2. None has a "team glossary → recognition correction → measurable term recall" pipeline. Hotword capability exists only at the engine layer (Paraformer, Fun-ASR), and no one has productized it for non-technical users.
3. The default engine is mostly Whisper-based. By the CS-Dialogue numbers, it ranks last on mixed Chinese-English speech, so it is not the best choice for Chinese-speaking teams.
4. None has a "consent-first" interaction for in-person discussions, such as off-the-record segments or consent records.
5. Meetily's 32k stars show there is real demand for "local, private meeting notes" ([Inference]: stars measure attention, not willingness to pay). BriefPilot doesn't need to compete with it on engines; it can build a "research commitment layer" **on top of** tools like it, and could even reuse its transcription output directly.

---
## 7. Cross-Cutting Constraints: Four-Column Summary Table (Status Quo — Evidence — Opportunity — Demo Technical Feasibility)

| Constraint | Status quo | Evidence (key sources) | Opportunity (differentiator) | Technical feasibility for the demo |
|---|---|---|---|---|
| **C1 Mixed Chinese–English speech** | ASR is strong on Chinese but weak on English segments; AssemblyAI and Granola added mixed-language support in 2026, while Deepgram does not support Mandarin code-switching | CS-Dialogue Table 8 (English WER 15.6–32.0%); AssemblyAI blog post, 2026-08; Deepgram docs | Don't advertise "supports code-switching"; advertise **"higher recall on your own lab's terminology"** and back it with evaluation numbers | **High**: SenseVoice/Fun-ASR/Qwen3-ASR run locally, Paraformer has hotwords, Whisper has a prompt |
| **C2 Domain terminology** | Hotwords and contextual biasing are engine capabilities that products have barely built on; Feishu users write their own replacement rules | Fun-ASR hotword recall above 0.97 (self-reported); a blogger's replacement rules; FunASR README | **A glossary generated automatically from project materials** (paper titles, Zotero/BibTeX, last week's minutes), then used for recognition and post-processing correction; terms in action items link back to their source | **High**: glossary construction and post-processing correction are deterministic code; hotword injection depends on the engine |
| **C3 In-person meetings** | Mobile apps, hardware, and uploads are all mature | Fireflies One-Touch, Feishu upload, Granola microphone, Plaud | "Being able to record" is not the opportunity; the opportunity lies in C4 | High (ffmpeg + local file import is enough) |
| **C4 Recording consent and social concerns** | Only about 1/3 of people are "always asked"; Otter and Granola have been sued; multiple universities have banned Otter | Kolmogorov survey; NPR; ppc.land; VT, CUNY | **Consent-first interaction**: pre-recording notice, off-the-record segments, audio deleted immediately, only confirmed text retained | **High** (UI logic); but **the value needs to be validated through interviews** [Assumption] |
| **C5 Data policy/privacy** | Otter trains on de-identified data; Granola trains on anonymized data by default (except enterprise plans); Fireflies says it does not train; Feishu says "no training without authorization" | Original text of each vendor's policy | "No training" is already table stakes; **"never leaves the device" is the structural differentiator**, and it can sidestep universities' "no uploads without a contract" restrictions | See C6 |
| **C6 Local deployment** | Local ASR is mature; there is no public evaluation of local LLM extraction quality; open-source local meeting tools already include projects at the 32k-star level | whisper.cpp, SenseVoice, Meetily, Anarlog GitHub | Treat local deployment only as the **foundation**, layered with C1, C2, C4, and "human-confirmed commitment tracking" | ASR **high**; LLM extraction **medium** (requires a self-built evaluation); running 8–14B models on M1 Max/32GB is feasible, 27B is tight |
| **C7 No recording / notes-first** | Granola is "notes + audio deleted immediately," not zero-audio; no mainstream zero-audio product was found | Granola FAQ and complaint filing | **"Text first, audio optional"**: resolves C4 and C5 at once, and is consistent with BriefPilot's current PRD (input is minutes text) | **Highest**: the main pipeline can be demonstrated without relying on ASR |
| **C8 Open-source competition** | Both engines and "transcription + summary" are saturated | See Section 6 | Build what open-source tools haven't: action item confirmation and tracking, terminology recall evaluation, consent interaction | Open-source components can be reused, reducing engineering effort |

---

## 8. If Building a Local/Multilingual Demo: Candidate Tech Stacks and Risks

### 8.1 Three Candidate Stacks

**Stack A: "Fully local" (recommended as the main demo, [Inference])**
```
Input: (1) the user's handwritten key points (Markdown)  (2) optional: local recording m4a/wav
  → ffmpeg normalizes to 16k mono
  → ASR: SenseVoice-Small (speed) or Fun-ASR-Nano / Paraformer (hotwords); control group uses whisper.cpp large-v3-turbo + initial_prompt
  → Glossary: extracted from BibTeX/paper titles/last week's minutes → hotword injection + post-processing correction (edit distance/pinyin similarity + allowlist)
  → Text alignment: note key points ↔ transcript segments (attach "verbatim evidence" to each action item)
  → Local LLM (Ollama: qwen3 8B/14B, optionally qwen3.6 27B): strict JSON schema extraction of who/what/when/evidence, leave blank when missing
  → Human confirmation UI (Streamlit/Gradio): confirm / edit / reject; audio deleted by default
  → Storage: local SQLite + Markdown export
```
- Selling points: data never leaves the computer, terminology recall is measurable, action items carry verbatim evidence, consent-first.
- Main risks:
  1. SenseVoice has no official hotword support; if hotwords are needed, switch to Paraformer/Fun-ASR, or compensate with post-processing.
  2. Local LLMs risk unstable JSON output and "fabricated dates/owners"; this requires an evaluation set and schema validation with retries.
  3. Loading both ASR and LLM in 32GB of memory is tight, so they must run in separate stages.
  4. Weak speaker diarization: FSMN-VAD + CAM++ only provides anonymous labels, so the "who" field still depends on notes or manual assignment.
  5. Model weight licenses: FunASR models and the Qwen series each have their own terms; fine for a demo, but must be re-checked before commercial use.
  6. Whisper has hallucination and repetition problems on long audio (third-party observation, pending hands-on testing), so it needs VAD-based segmentation.

**Stack B: "Local ASR + cloud LLM (ZDR)"**
- Transcription runs locally, and only text is sent to an API with zero-retention terms. Extraction quality is more stable, but the "never leaves the computer" narrative is weakened and the university contract problem remains. Suitable as a quality upper-bound comparison.

**Stack C: "Cloud baseline" (for evaluation comparison only, not a product)**
- Run the same audio through Feishu Minutes (upload), AssemblyAI Universal-3.5 Pro, and the Whisper API, and compute terminology recall and MER as evidence for "where we beat existing tools." Note: **use only synthetic or de-identified samples that you recorded yourself, with every participant's consent, and containing no unpublished content**.
### 8.2 The "differentiating evidence" the demo should show (suggested metrics)
- **Term Recall**: the share of glossary terms that are written correctly in the transcript or in the action items. This is the number this research most wants to show the client.
- **MER**: mixed error rate for Chinese-English speech, aligned with the academic convention (Chinese counted per character, English per word).
- **Action item P/R**, plus a "fabrication rate": the share of action items that contain an owner or date not present in the source.
- **End-to-end time**: how long the full pipeline takes to process a 1-hour meeting on an M1 Max.
- Evaluation samples: we suggest producing 3–5 self-made "mock group meetings" of 10–20 minutes (the user and a peer reading a script, plus free discussion), with content drawn from public VLA papers so that no unpublished data is used. The comparison group covers SenseVoice, Paraformer + hotwords, Whisper + prompt, as well as Feishu Minutes and AssemblyAI.

### 8.3 Risk overview

| Risk | Type | Impact | Mitigation |
|---|---|---|---|
| Vendors quickly add code-switching support, shrinking the differentiation window | Market | High | Place the differentiation in "glossary + confirmation + commitment tracking", not in ASR |
| Local LLM extraction quality is insufficient | Technical | Medium | Human confirmation as a backstop; schema validation; test both 8B and 14B; can switch to Stack B |
| The lab does not actually care about privacy or recordings | Demand | Medium-high | Validate in interviews first ([Assumption]); keep a cloud toggle in the demo |
| Students do not take notes in group meetings, so "notes-first" has no input | Demand | Medium | Make recording optional as a fallback; ask about current practice in interviews |
| Self-recorded samples are not representative enough | Evaluation | Medium | Cover at least two accents and two microphone distances, and add one segment with whiteboard noise |
| Model or data licensing | Compliance | Low (demo) | Record the license of each model; CS-Dialogue is limited to academic use |

---

## 9. Gaps and Next Steps

**Not covered (search quota exhausted or pages inaccessible)**
- The original Plaud Trust Center text (429) and Plaud's performance on mixed Chinese-English speech.
- Real user complaints on Zhihu and Xiaohongshu about Feishu Minutes, Tongyi Tingwu, and iFLYTEK Tingjian recognizing mixed Chinese-English speech; these can be filled in by the "user complaint mining" report.
- Official policies of the target university or Singapore universities on AI note-taking tools.
- Otter's official language support page (so far only a third-party review says "only one language can be selected per meeting").
- Quantitative data on Doubao/Seed-ASR for mixed Chinese-English speech.
- Quality of Chinese action item extraction by local 8B/14B models (no public evaluations; can only be self-tested).

**Suggested next steps**
1. **A 1-hour experiment on the local machine** (highest feasibility, greatest evidentiary value): install Ollama and FunASR, take a 10-minute self-recorded mixed Chinese-English VLA discussion, run SenseVoice, Paraformer (with hotwords), and whisper.cpp on it, and compute Term Recall.
2. Add three questions to the interviews: Who takes notes in group meetings and 1-on-1s today, and where? Does anyone object to or avoid recording? What kind of data handling is acceptable (cloud, local, no audio retained)?
3. Hand C2, C4, and C7 from this document to the "positioning" stage. Candidate positioning statement: **"A locally run meeting commitment assistant for Chinese-English code-switching research teams, with accurate terminology and human confirmation"** ([Assumption]).

---

## Source List

**Academic papers and datasets**
1. CS-Dialogue (arXiv 2502.18913, HTML full text) https://arxiv.org/html/2502.18913
2. Fun-ASR Technical Report (arXiv 2509.12508v3) https://arxiv.org/html/2509.12508v3
3. ISCSLP 2022 CS ASR Challenge Summary https://arxiv.org/pdf/2210.06091 (summary)
4. Whisper adapters for code-switching (arXiv 2312.08856) https://arxiv.org/html/2312.08856v2 (summary)
5. DOTA-ME-CS (arXiv 2501.12122) https://arxiv.org/pdf/2501.12122 (summary)
6. Retracted: LLM-ASR vs Whisper (arXiv 2412.00721) https://arxiv.org/abs/2412.00721
7. Polyglot-Lion (arXiv 2603.16184) https://arxiv.org/pdf/2603.16184 (summary)
8. SEAME dataset description https://voxkitchen.readthedocs.io/en/latest/datasets/seame/ (summary)
9. JSALT 2022 report https://www.clsp.jhu.edu/wp-content/uploads/2022/07/2022_07_06.pdf (summary)
10. NUS, intergenerational code-switching in colloquial Singapore Mandarin https://fass.nus.edu.sg/srn/2022/03/07/filling-gaps-or-code-choice-code-switching-across-generations-in-colloquial-singapore-mandarin/ (summary)
11. Blog post from a Singapore university's BLIP lab (children's code-switching; weak relevance) (university page; link removed)

**ASR products and models**
12. MERaLiON-3-3B-ASR model card https://huggingface.co/MERaLiON/MERaLiON-3-3B-ASR
13. AssemblyAI Universal-3.5 Pro code-switching blog post https://assemblyai.com/blog/universal-3-5-pro-code-switching-contextual-prompting
14. AssemblyAI code-switching docs https://assemblyai.com/docs/code-switching (summary)
15. Deepgram multilingual code-switching docs https://developers.deepgram.com/docs/multilingual-code-switching (summary)
16. Deepgram changelog 2026-03-31 https://developers.deepgram.com/changelog/2026/3/31 (summary)
17. Google Chirp 3 docs https://cloud.google.com/speech-to-text/v2/docs/chirp_3-model?hl=zh-cn (summary)
18. Microsoft Q&A: Azure mixed Chinese-English transcription https://learn.microsoft.com/en-us/answers/a/1575915
19. Whisper GitHub Discussion #976 https://github.com/openai/whisper/discussions/976 (summary)
20. WhisperPen (personal project anecdote) https://penchan.co/en/ai/coding/introducing-whisperpen/ (summary)
21. Doubao Seed-ASR blog https://team.doubao.com/blog/doubao-s-listening-skills-unboxing-live-see-how-seed-asr-overcomes-the-speech-recognition-bottleneck (summary)
22. 2026 commercial ASR comparison (secondary roundup, 2026-07-30) https://peihuachen.github.io/ai-tools-hub/posts/commercial-asr-comparison-chinese-english-dialect-2026.html
23. FireRedASR2 README https://huggingface.co/FireRedTeam/FireRedASR2-AED/blob/main/README.md (summary)
24. Qwen3-ASR GitHub https://github.com/QwenLM/Qwen3-ASR ; PyPI https://pypi.org/project/qwen-asr/ (summary)
25. FunASR GitHub https://github.com/modelscope/FunASR
26. SenseVoice GitHub https://github.com/FunAudioLLM/SenseVoice
27. whisper.cpp GitHub https://github.com/ggml-org/whisper.cpp
28. Whisper Notes: SenseVoice, Qwen3-ASR, and Whisper tested on Mac https://whispernotes.app/blog/sensevoice-fastest-cjk-transcription
29. WhisperX (aggregator site) https://gittrend.io/repo/m-bain/whisperX (summary)

**Meeting products: languages, offline use, data policies**
30. Otter third-party review (languages) https://www.laxis.com/blog/otter-ai-review/ (summary)
31. Granola blog post on 32 supported languages https://www.granola.ai/blog/granola-now-supports-32-languages
32. Granola multi-language docs https://docs.granola.ai/help-center/customising-granola/multi-language (summary)
33. Granola security and data FAQ https://docs.granola.ai/help-center/consent-security-privacy/security-privacy-data-faqs
34. Granola model training statement https://docs.granola.ai/help-center/consent-security-privacy/model-training
35. Otter privacy policy (effective 2026-06-16) https://otter.ai/privacy-policy
36. Fireflies information security policy https://guide.fireflies.ai/articles/2154538358-policy-on-keeping-information-safe
37. Fireflies offline recording help https://guide.fireflies.ai/articles/4565146696-how-to-transcribe-offline-meetings-using-fireflies-mobile-app
38. Feishu Minutes official site articles (upload and transcription) https://www.feishu.cn/content/article/7578773484596153570 ; https://www.feishu.cn/content/article/7600354924362337245 (marketing articles)
39. Feishu AI data security article https://www.feishu.cn/content/article/7667878625560677345
40. Feishu lark-minutes CLI skill https://tessl.io/registry/skills/github/larksuite/cli/lark-minutes/review (summary)
41. Plaud App Store https://apps.apple.com/sg/app/id6450364080 ; Mentalyc review https://www.mentalyc.com/blog/is-plaud-hipaa-compliant (summary, to be verified)

**Consent, law, and university policies**
42. Kolmogorov Law survey (reprinted by KRDO) https://krdo.com/stacker-business-economy/2026/07/16/ai-notetakers-have-sat-in-on-1-in-3-us-workers-meetings-but-only-a-third-say-they-were-asked-first/
43. NPR: Otter class action https://www.npr.org/2025/08/15/g-s1-83087/otter-ai-transcription-class-action-lawsuit
44. PPC Land: Granola class action https://ppc.land/granola-sued-for-recording-meetings-without-consent-to-train-ai-models/
45. University policies: Virginia Tech https://news.vt.edu/notices/it/2026/03/it-ai-meeting-assistants.html ; CUNY https://mailings.york.cuny.edu/cgi-bin/dada/mail.cgi/archive/faculty_ft/20250903165544/ ; UNM https://airesources.unm.edu/ai-guidance/ai-meeting-capture.html ; Santa Clara https://www.scu.edu/ai-resources/guidelines/ai-meeting-assistant-guidelines/ (some are summaries)
46. Singapore recording law commentary https://singaporelegaladvice.com/can-an-organisation-record-a-conversation-without-consent/ ; https://www.recordinglaw.com/singapore/recording-laws/ (summary, unofficial)
47. Open-source meeting tools: Meetily https://github.com/Zackriya-Solutions/meeting-minutes ; Anarlog https://github.com/fastrepl/anarlog ; rename announcement https://anarlog.so/blog/char-is-now-anarlog ; Ollama qwen3.6 https://registry.ollama.ai/library/qwen3.6 (summary); Ollama internal configuration record https://git.azcomputerguru.com/azcomputerguru/claudetools/src/commit/44247909366d7bae7e3d683847b583fbbd6fc596/.claude/OLLAMA.md ; Bot vs no-bot blog post https://affine.pro/blog/bot-vs-no-bot-ai-meeting-recorder (summary)
---

## Confidence Notes for This Document's Conclusions

| Conclusion | Confidence | Rationale |
|---|---|---|
| In mixed Chinese-English speech, error rates on English segments are far higher than on Chinese segments | **High** | Same paper, same test set, consistent across four models; but only one dataset, and the setting is phone recordings in a quiet environment |
| Vendors are closing the gap on "mixed-language support" | **Medium-high** | Verifiable from official AssemblyAI and Granola pages; no quantified results; Deepgram's Mandarin mixed-language status is taken from a changelog summary |
| Offline (in-person) recording is not a blank space | **High** | Verifiable from multiple official help pages |
| Recording consent is a core obstacle in research settings | **Medium** | US surveys, lawsuits, and university policies are indirect evidence; **there is no first-hand evidence from labs or from Singapore/China**; the power asymmetry in advisor one-on-ones is an inference |
| "No training on user data" is already an industry baseline; "data never leaves the device" is the structural differentiator | **Medium-high** | Verifiable from policy text; the university rule "no uploads without a contract" comes from US universities and has not been verified for the target university |
| Local ASR is highly feasible | **High** | Open-source repositories plus third-party Mac benchmarks; the baseline machine (M1 Max) is older than the M4 Pro used in testing, so speed needs to be re-tested locally |
| Local LLM extraction is moderately feasible | **Medium-low** | No public evaluations; can only be tested in-house |
| No open-source tool does "action item confirmation and tracking, or terminology recall" | **Medium** | Based on scraping READMEs; may miss small projects and features not documented in READMEs |
| "Notes-first" suits research better | **Low (assumption)** | Logical reasoning only; interviews are needed to verify "whether students take notes" and "whether they are averse to recording" |
| Lab language is "mostly Chinese, with English terminology" | **Low (assumption)** | No dedicated study found; needs to be measured by recording and tallying our own samples |

> Overall assessment: **The individual horizontal constraints (mixed-language speech, offline settings, privacy) have mostly been partly covered by the market, and none of them alone constitutes a moat. But in the niche of "bilingual Chinese-English research teams," they stack up and hit three constraints at once: high cost of terminology errors + high social cost of recording + sensitive data. No existing product solves all three at once ([Inference]).** This is the "one small point" that BriefPilot v2 is best placed to prove with a demo and evaluation numbers.
