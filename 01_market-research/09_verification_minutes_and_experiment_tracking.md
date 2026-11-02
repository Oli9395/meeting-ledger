---
title: "Supplementary Verification 09: How Far Minutes (Open-Source Closeout) and Experiment-Tracking Tools Go on the \"Decision → Subsequent Run\" Step"
status: "v1 (desk verification, zero product testing; backfills I-07 in 05_demo-plan/04_consistency_check.md)"
sources_count: 10
---

# Supplementary Verification 09: Minutes and Experiment-Tracking Tools

> **Why this file exists**: Only during the second positioning round did we discover that the open-source project Minutes has a closeout skill (positioning §10.2), but `01_market-research/` was never backfilled. The most direct substitute for the second beat of the positioning, "decisions as constraints," is experiment-tracking tools (W&B, MLflow, Neptune, Comet), yet W&B appears 0 times in `03_competitors_research_lab_tools.md`. This file covers both gaps. **It records only what the official documentation says**; anything that could not be opened is marked "to be verified".
>
> **Labeling rules**: [Fact] = the original page was opened and quoted verbatim; [Summary] = only a search snippet or a secondhand paraphrase was seen; [Inference] = derived from facts. All sources were accessed at the time of writing. "The page doesn't say so" does not mean the product lacks the feature.
>
> **What this file did not do**: No tool was installed or run; no W&B or Comet account was logged into to view the UI. **Hands-on competitor testing (06 review P0-1) is still not done**, so the positioning remains "conditionally valid."

---

## 0. Conclusions First (5 points)

1. **Minutes' closeout is "one item at a time, the user picks the outcome, and the owner must confirm"**. It is isomorphic to this project's "proactively propose 4 kinds of status transitions in batch and require confirmation," but at a different scale. Its Markdown has `action_items.status` and `decisions` fields, and an example can answer "did it stick?" across two meetings. The page **does not say** anything about automatic cross-meeting tracking or automatically marking items complete [Fact].
2. **W&B's Runs table can group, filter, and sort by config columns, and a run can carry notes and tags; Reports are for "Describe your findings" and "Share updates with collaborators"** [Fact]. The official documentation pages **do not say** anything about turning "decisions made in a meeting" into check conditions for subsequent runs. So "group-by shows rank 16 in 30 seconds" (positioning O11) is true, but only if **the user remembers that rank 32 was decided at the meeting** [Inference].
3. **MLflow can search runs by params / metrics / tags, and a run can have a note (`mlflow.note.content`)** [Fact]; likewise it says nothing about "decision → constraint check."
4. **Neptune has announced its shutdown**: the docs home page says "Following its acquisition by OpenAI, Neptune services will be permanently discontinued," and the top banner reads "Neptune Service Shutdown - March 5, 2026" [Fact]. It is no longer a substitute, but its users are migrating. This is a timing signal, not evidence of opportunity [Inference].
5. **Comet**'s logging overview page says it automatically records hyperparameters, metrics, code, Git metadata, and so on [Fact]. The pages opened this round did not mention filtering by parameter or decision checks (**other pages to be verified**).

**Implication for the positioning** [Inference]: Experiment-tracking tools record very clearly "what ran in the run," and meeting tools record very clearly "what was said in the meeting"; neither side says it "checks the rules set at the meeting against later runs." This is exactly the narrowed wording of positioning U2: "Capturing decisions already exists (Fabric, Minutes, ZoomMate); a deterministic comparison of decisions × run config has not been seen." But the **demand frequency** for this cell is determined by P-H6, and there is currently zero data.

---

## 1. Minutes (Open Source, Local-First)

| # | Item | Conclusion | Verbatim evidence | Source | Access date |
|---|---|---|---|---|---|
| M1 | Tagline | [Fact] | "Your conversations. Your memory. Ready for the AI you use." | https://github.com/silverstein/minutes | at the time of writing |
| M2 | License and scale | MIT; about 1.6k stars (sidebar shows 1.6k, 180 forks) [Fact] | "Minutes is MIT licensed and staying that way: no relicensing, no paid tier for anything in this repo." | Same as above | at the time of writing |
| M3 | Local vs. cloud | Capture, transcription, and storage run locally; if a cloud AI is chosen, the authorized content is sent to that provider [Fact] | "Capture, transcription, and storage run locally."; "If you choose a cloud AI assistant or summarizer, the meeting context you authorize is sent to that provider." | Same as above | at the time of writing |
| M4 | Data format | A meeting is Markdown with YAML frontmatter; `action_items` has assignee / task / due / status, and `decisions` has text [Fact] | "Meetings are plain markdown with structured YAML frontmatter." | Same as above | at the time of writing |
| M5 | Cross-meeting | Example question "What did we decide about monthly billing, and did it stick?", answered "spans two meetings a month apart: launched on Feb 28, reversed on Mar 25" [Fact]; the page **does not say** anything about a promise of automatic cross-meeting tracking or automatically marking items complete | Same as left | Same as above | at the time of writing |
| M6 | MCP | "MCP server (34 tools)", "Local meeting tools and resources for any MCP client" [Fact] | Same as left | Same as above | at the time of writing |
| M7 | What the closeout skill does | One outcome → one existing thread [Fact] | "Turn one clear meeting outcome into a proposed closeout for one existing X1 coordination thread." | https://tessl.io/registry/skills/github/silverstein/minutes/minutes-x1-closeout | at the time of writing |
| M8 | How many items per run | One [Fact] | The skill requires "resolve exactly one open thread the signed-in X1 actor can read" | Same as above | at the time of writing |
| M9 | Who picks the outcome | The user [Fact] | "Ask the user to choose the X1 outcome if they haven't already."; outcome enum `resolved` / `escalated_elsewhere` / `deferred` / `no_longer_relevant` | Same as above | at the time of writing |
| M10 | Owner confirmation | [Fact] | "The accountable participant must review and commit in X1." | Same as above | at the time of writing |
| M11 | "Said ≠ done" | [Fact] | "Meeting language that money was sent, a wire was approved, or a payment was discussed doesn't prove settlement." | Same as above | at the time of writing |

**How far it goes (following the 07 template)**:

| Stage | How far Minutes goes | How this project differs |
|---|---|---|
| Extracting action items and decisions | Yes (YAML fields) | Baseline |
| Answering "was the decision overturned" across meetings | Can answer when asked (example) | Baseline (≈ cross-meeting Q&A in incumbent products) |
| Using the next meeting's remarks to **proactively, in batch** propose the status of all commitments from the previous meeting | Page doesn't say; closeout is one item at a time, user picks the outcome | This project's increment (P-H1 decides whether DIY can catch up) |
| Decision × run config comparison | Page doesn't say | This project's second beat (P-H6 decides whether it is worth building) |

**Impact on the positioning**: The Minutes entry in positioning §10.2 was originally labeled "[Fact, paraphrased via WebFetch, key sentences pending verbatim check]"; this round has verified them verbatim, so it is **relabeled [Fact]**. The DIY route "Claude Code + Minutes MCP" stays in the P-H1 comparison group (E2b).

---
## 2. How far experiment-tracking tools go on the "decision → subsequent run" step

> Evaluation criteria (written down in advance): does the page describe ① grouping / filtering runs by config; ② adding notes or tags to a run; ③ registering an "agreement" (e.g., "from now on, use rank 32") as a check rule and automatically flagging runs that don't comply. ① and ② are the passing bar; only ③ overlaps with the second beat of this proposal.

### 2.1 Weights & Biases (docs moved to docs.coreweave.com)

| # | Capability | Conclusion | Verbatim evidence | Source |
|---|---|---|---|---|
| W1 | Docs location | `docs.wandb.ai/guides/...` returns a 301 redirect to `docs.coreweave.com/guides/...` [Fact] | — | https://docs.wandb.ai/guides/runs/grouping/ → https://docs.coreweave.com/guides/runs/grouping/ |
| W2 | Run grouping | Runs can be grouped by "common purpose" and also organized by job type [Fact] | "Organize your runs into *groups*. A group is a collection of runs that share a common purpose…" | https://docs.coreweave.com/guides/runs/grouping/ |
| W3 | Group / filter / sort by config | **Yes** [Fact] | "Use the Runs tab to filter, group, and sort your runs."; "select a config column to dynamically group your runs, for example by architecture."; "Click the Group button above the table to group all rows by the value in a particular column." | https://docs.coreweave.com/products/wandb/track/project-page.md |
| W4 | Run notes and tags | **Yes** [Fact] | "You can add notes to a run with the W&B App or programmatically with the Python SDK."; "Tags are useful for organizing related runs together or applying temporary labels like `baseline` or `production`." | https://docs.coreweave.com/products/wandb/runs/view-logged-runs.md |
| W5 | Limits of config search | Nested parameters cannot be searched [Fact] | "Weights & Biases does not search for nested config or summary parameters." | Same as above |
| W6 | Reports | Used to organize runs, embed visualizations, describe findings, and share with collaborators [Fact] | "Organize Runs."; "Describe your findings."; "Share updates with collaborators, either as a LaTeX zip file or a PDF." | https://docs.coreweave.com/guides/reports/ |
| W7 | Whether Reports mentions meetings, decisions, or checking runs against agreements | **Not described on the page** [Fact: not mentioned on the page] | — | Same as above |
| W8 | Official MCP (`compare_runs_tool`) | [Fact]; cited from §5.1 R5 (opened on the day of Proposal 1) | — | https://github.com/wandb/wandb-mcp-server |
| W9 | Whether automations / alerts can express "the lora_rank of all subsequent runs must be 32" | **To be verified** (the Automations / Alerts docs were not opened in this round) | — | — |

### 2.2 MLflow

| # | Capability | Conclusion | Verbatim evidence | Source |
|---|---|---|---|---|
| L1 | What is recorded | params, metrics, start and end times, artifacts [Fact] | "Each run records metadata (various information about your run such as metrics, parameters, start and end times)" | https://mlflow.org/docs/latest/ml/tracking/ |
| L2 | Search by tag / parameter | **Yes** [Fact] | "You can associate arbitrary tags with each run, which allows you to filter and search runs based on tags."; "Searching for runs by parameter or metric value" | Same as above |
| L3 | Run notes | **Yes** [Fact] | "A system tag `mlflow.note.content` can be used to add descriptive note about this run." | Same as above |
| L4 | Registering an agreement as a check rule | **Not described on the page** | — | Same as above |
### 2.3 Neptune

| # | Capability | Conclusion | Verbatim evidence | Source |
|---|---|---|---|---|
| N1 | Service status | **Discontinued** [Fact] | "Following its acquisition by OpenAI, Neptune services will be permanently discontinued."; "All remaining data will be deleted at shutdown and cannot be recovered."; banner "Neptune Service Shutdown - March 5, 2026" | https://docs.neptune.ai/ |
| N2 | Comparison / filtering / reporting features | Not described on the home page (only lists "Create a report" and "Fetch runs across all projects") [Fact: page does not elaborate] | — | Same as above |

### 2.4 Comet

| # | Capability | Conclusion | Verbatim evidence | Source |
|---|---|---|---|---|
| C1 | Automatic logging | Hyperparameters, command-line arguments, training metrics, code, Git metadata and patch, environment info, etc. [Fact] | "Model hyperparameters (see below)"; "Git metadata and patch"; "Environment GPU, CPU, host name, and more" | https://www.comet.com/docs/v2/guides/experiment-management/log-data/overview/ |
| C2 | Filtering / comparing by parameter, tags | **Not mentioned on this page**; other pages **to be verified** | — | Same as above |
| C3 | Registering an agreement as a check rule | **To be verified** | — | — |

### 2.5 Summary: how far each tool gets on the "decision → later runs" step

| Tool | ① Group / filter by config | ② Run notes / tags | ③ Meeting agreement → automatically check later runs | Implication for beat 2 of this proposal [Inference] |
|---|---|---|---|---|
| W&B | Yes [Fact] | Yes [Fact] | Not stated on the page; Automations to be verified | A diligent student can spot rank 16 in 30 seconds, **provided they remember that rank 32 was agreed at the meeting**; this proposal's added value lies only in the step of "automatically turning the decision into a check condition" |
| MLflow | Yes (search by params / tags) [Fact] | Yes (note tag) [Fact] | Not stated on the page | Same as above |
| Neptune | — | — | — | Discontinued (2026-03-05); not a substitute |
| Comet | To be verified | To be verified | To be verified | To be verified |
| Meeting tools (Fabric, Minutes, ZoomMate, Feishu) | Do not touch runs | Do not touch runs | Capture decisions: yes; comparing against run pages: not stated | See positioning §5.1 R9–R11 |

**[Inference] The most likely "30-second substitute"**: group by `lora_rank` in the W&B Runs table, plus a handwritten run note saying "per the 10/15 group meeting decision, use rank 32". It can do most of what beat 2 of this proposal does; what it lacks is "automatically extracting the decision from meeting text and automatically matching it against what was verbally fulfilled". Whether this step is worth anything depends on the real frequency of P-H6; **there is currently zero data, so beat 2 can only serve as a demo mechanism, not as a selling point**.

---

## 3. Still to be checked (listed in review 06, still unaddressed this round)

| Subject | What to check | Status this round | Reason |
|---|---|---|---|
| Lark (international version of Feishu) in Singapore | Whether it has "meeting express" (会议速递); whether its features match Feishu | **To be verified** | Requires login or a look through the Lark help center; already included in the 30-minute feasibility check in eval-kit README §3 step 1b |
| Plaud, Bluedot, MeetGeek, Sembly | Whether they update commitment status across meetings | **To be verified** | This round's time went first to blocker fixes and the Minutes / experiment-tracking tools |
| Doubao, Kimi | Whether long context + multi-file Q&A can reconcile across meetings | **To be verified** (by nature a DIY baseline for P-H1; can be folded into the E2 series) | Same as above |
| W&B Automations / Alerts | Whether they can express "all subsequent runs must satisfy X" | **To be verified** | Same as above |
| Comet filter / compare pages | Whether they support filtering and comparing by parameter | **To be verified** | Same as above |

---

## 4. Source list (all accessed at the time of writing)

1. Minutes GitHub — https://github.com/silverstein/minutes
2. Minutes `minutes-x1-closeout` skill — https://tessl.io/registry/skills/github/silverstein/minutes/minutes-x1-closeout
3. W&B Organize runs (via 301 redirect) — https://docs.coreweave.com/guides/runs/grouping/
4. W&B Project page / Runs tab — https://docs.coreweave.com/products/wandb/track/project-page.md
5. W&B View logged runs (notes, tags, config search) — https://docs.coreweave.com/products/wandb/runs/view-logged-runs.md
6. W&B Reports overview — https://docs.coreweave.com/guides/reports/
7. W&B MCP server (cited from positioning §5.1) — https://github.com/wandb/wandb-mcp-server
8. MLflow Tracking — https://mlflow.org/docs/latest/ml/tracking/
9. Neptune docs home page (shutdown notice) — https://docs.neptune.ai/
10. Comet log data overview — https://www.comet.com/docs/v2/guides/experiment-management/log-data/overview/
## 5. Confidence Notes

- **High**: The entries in §1 for Minutes and in §2 for W&B, MLflow, and Neptune are the result of opening the original pages and requiring verbatim quotes.
- **Medium**: The "30-second substitute" judgment in §2.5 is an [Inference], based on the documented capabilities and not tried in a real project.
- **Limitations**: No tool was tested hands-on; Comet, W&B Automations, Lark, Plaud, and others still need to be verified; "the page doesn't say so" does not mean "it doesn't exist."
