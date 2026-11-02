---
title: "Annotation Guidelines: How to Label Gold Labels for Commitments, Decisions, and Hypotheses"
status: v1 (135 gold entries drafted under these guidelines; not yet checked by human double-annotation)
sources_count: 3
---

# Annotation Guidelines

> Applies to `gold/M*.gold.jsonl`, and also to any future annotation of real meetings (real meetings require consent from all attendees first).
> Every rule in these guidelines has at least one example in `gold/`. When a rule and an example conflict, **the rule wins; then fix the example**, and record the change in `results-template.md` §1.3.

## 1. What to Label: Annotation Units

An **annotation unit** is a sentence or half-sentence in the meeting that expresses one of the following 5 types:

| type | Definition | Example (gold id) |
|---|---|---|
| **action** | Something someone will have to do in the future, whether or not anyone takes it on and however firmly | M1-04 "I'll add the rank 16 and rank 64 ablations by this Friday" |
| **decision** | Someone with decision authority, or the whole group, settles on doing / not doing / how to do something, including vetoing a proposal | M2-06 "We're not building our own benchmark this semester" |
| **hypothesis** | A guess about a fact or cause, with no evidence yet | M1-03 "I suspect the rank 32 drop is mainly… quantization error" |
| **result** | Something that has already happened: experiment numbers, task status, completed work | M3-08 "rank 64 came out last Saturday… 73.1%" |
| **question** | A question raised but not resolved in the meeting | M2-20 "Should the wandb projects be merged into one?" |

**Do not label** the following (if the product outputs them, mark them `EXTRA_OK` or `FABRICATED` when mapping; see scoring.md §4):

- Small talk and meeting logistics ("That's it for today", "Same time next week")
- Closing recaps at the end of a meeting (M1 [00:07:54] Zhou Lan's summary; its content was already labeled earlier)
- Generic statements of behavior with no concrete deliverable (M3 "Next time I'll ask in the group chat earlier")
- Personal schedules (M3 "I might be ten minutes late next week")
- The content of paper presentations themselves (conclusions in other people's papers are not this group's results)
- Hyperparameter tuning and engineering details, unless they constitute a results report (the M1 learning rate discussion)
- Deferred items explicitly marked "let's not discuss that now" (M3 "Once the approval comes through we'll split it up… let's not discuss that now")
- The vetoed proposal itself: **not labeled as an action**, but recorded in `traps.json`; the sentence that vetoes it is labeled as a decision

## 2. Field Specification

| Field | Rule |
|---|---|
| `id` | `M<meeting>-<two-digit sequence number>`, in order of appearance |
| `text_span` | A substring that exists **verbatim** in the transcript, taken from within a single sentence (one speaker's single turn); use "the shortest fragment sufficient to express the item"; must be **unique** within that meeting (`score.py --validate` checks this) |
| `speaker` | The person who said the text_span (not necessarily the owner) |
| `owner` | **Fill only for action**; use null for other types. See §3 for the rules |
| `owner_accept` | Optional. Other acceptable owners (e.g. when the subject is "we" and the speaker is also plausible) |
| `due` | **Fill only for action**. Fill an ISO date if it can be converted to a specific date under §4, otherwise null |
| `due_raw` | The time expression in the original utterance ("by this Friday", "ASAP", "in a while"); null if there is none |
| `due_accept` | Optional. Other acceptable dates (e.g. "this weekend" could be Saturday or Sunday) |
| `strength` | committed / tentative / suggestion / hypothesis; see §5 for the rules |
| `type` | See §1 |
| `evidence_timestamp` | The timestamp of the turn containing the text_span |
| `cross_meeting_ref` | If this item is a follow-up to an item from an **earlier meeting** (fulfilled, partially fulfilled, rescheduled, dropped, reiterated, resolved), fill in the id of that item; fill only the most direct one |
| `notes` | State clearly why it was labeled this way, especially for edge cases |

## 3. Owner Rules

1. First-person commitment ("I'll do it", "I'll") → the speaker.
2. Someone with authority assigns by name ("Siyuan, you prepare the slides"), and the person accepts or does not object → the named person.
3. One person commits on behalf of another (M5-07 Zhou Lan says "Siyuan will run it. We'll get you numbers…") → **the assigned person**, not the speaker.
4. The subject is "we / we / someone / someone / someone has to", with no clear division of labor → **null**. If one particular person would also make sense, put them in `owner_accept` (M5-05, M5-19, M5-22, M5-23).
5. **Being mentioned does not make someone the owner**: in M1-13 "Muqing ran into problems when collecting data last week, someone needs to look into it", Muqing is only the person involved; owner = null.
6. Suggestions with an unclear audience ("you could consider balanced sampling by object type", where the listener could be Muqing or Siyuan) → null.
7. People from partner organizations are labeled the same way (M5-08 Marco, M5-18 Zhao Min); do not label only people from our own lab.

## 4. Date Conversion Rules

The meeting date is the anchor (M1 2026-10-06 Tuesday; M2 10-08 Thursday; M3 10-15 Thursday; M4 10-22 Thursday; M5 10-26 Monday). A week starts on Monday.

| Original wording | Convert to | Example |
|---|---|---|
| today, tonight, tonight, after the meeting | The meeting day | M5-26 tonight → 2026-10-26 |
| tomorrow, tomorrow | Meeting day +1 | M3-03 → 2026-10-16 |
| this week X, by Friday, before day X | Day X of the current week | M1-04 by this Friday → 2026-10-09 |
| next week X | Day X of the following week | M1-12 before next Monday → 2026-10-12 |
| this weekend | This week's Sunday; Saturday also accepted (`due_accept`) | M2-10 → 2026-10-11 / 10-10 |
| before the weekend | This week's Friday; Saturday also accepted | M4-04 → 2026-10-23 |
| this week, within this week (no day specified) | This week's Sunday; Friday also accepted | M5-25 → 2026-11-01 / 10-30 |
| next group meeting, next week's group meeting (group meetings are fixed on Thursdays) | The date of the next group meeting | M2-05 → 2026-10-15 |
| specific date | That date | M4-34 before November 14 → 2026-11-14 |
| in a while, ASAP, as soon as possible, later, early November, after the maintenance window, "a week in advance" (but the referenced event has no date) | **null**; put the original wording in `due_raw` | M1-15, M5-10, M4-13, M2-17, M1-18 |
| negated time ("can't promise I'll have time this week") | **null**; `due_raw` is also null | M1-10 |

> **Why can "before next week's group meeting" be converted but "in a while" cannot?** The group meeting cycle is background knowledge the whole group shares (every Thursday), so there is a definite anchor. "In a while" has no definite day in any context. If a product writes "in a while" as "2026-10-13", that is fabrication.
## 5. How to Judge the Four Strength Levels

### 5.1 Definitions

| strength | One-line definition | Typical signals |
|---|---|---|
| **committed** | Someone has taken it on, or it has been decided / already measured | First-person future tense with no hedging ("I will", "I'll take it", "I'll…", "I'll have … done before …"); an assignment by someone with authority that the assignee accepts; a necessary item everyone agrees on (even with no owner yet); an explicit decision; a measured result |
| **tentative** | Someone says they may do it, but leaves room to back out | "can give it a try", "will try to", "might", "probably", "no promises", "let me check", "will get to it when I have time", "can't guarantee"; a commitment with an uncertain condition; an assignee who discounts the assignment themselves; a preliminary result (single seed) |
| **suggestion** | Someone proposes it could be done, but nobody takes it on | "you could also consider", "maybe someone should", "we could try", "worth considering"; a need that is acknowledged but explicitly pushed back with no one taking it on ("let's revisit it later") |
| **hypothesis** | A guess about a fact or a cause | "I suspect", "I guess", "my hunch", "I suspect", "I feel like … will …" |

### 5.2 Decision order (when rules conflict, go top to bottom)

1. Is it a guess? → hypothesis (the type is also hypothesis).
2. Was it rejected afterward? → Do not label the original proposal; record it as a trap. Label the rejecting sentence decision / committed.
3. **The owner's own tone takes priority over the assigner's tone**: Zhou Lan says "Muqing, help him review it before the weekend" (sounds committed), and Muqing replies "I'll try, I have quite a few deadlines this week" → tentative (M4-04).
4. Did someone take it on? Taken on with no hedging → committed; taken on with hedging → tentative; nobody took it on → suggestion.
5. Is there a condition? A condition that is only about sequencing ("you send me the certificate and I'll add you to the list") → does not affect strength (M2-23 committed); a condition whose occurrence is itself uncertain ("once you decide which one to submit to, I'll help you write it") → tentative (M1-16).
6. Results: a formal multi-seed result → committed; a single seed, or the speaker saying "it doesn't count yet" → tentative (M3-10, M4-09).
7. The strength of a question is always tentative and is **not included in strength scoring**.

## 6. Edge Cases (27)

| # | Phenomenon | Example | How to label | Rationale |
|---|---|---|---|---|
| 1 | "Can give it a try" + "no guarantee on timing" | M1-10 | action / tentative, due null | Hedging language; a negated time cannot be used as due |
| 2 | Advisor makes a suggestion and says "use your own judgment" | M1-05 | action / suggestion, owner Chen Siyuan | Nobody took it on; the addressee is explicit |
| 3 | Advisor makes a suggestion, the student takes it on on the spot | M1-08 | action / committed, span is the student's sentence accepting it | A commitment counts only once it is taken on |
| 4 | "Someone needs to look into it", while Muqing is mentioned | M1-13 | action / committed, owner null | The need is acknowledged; being mentioned ≠ being the owner |
| 5 | A commitment with an uncertain condition | M1-16 | tentative | The condition may never trigger |
| 6 | A condition that is only about sequencing | M2-23 | committed | The condition is just the routine next step |
| 7 | An offer of help whose condition was not triggered | M1-17 "if there are too many, tell me" | tentative | The product listing it as an action item = upgrade |
| 8 | A relative date whose reference event has no date | M1-18 "one week in advance" (review date not set) | due null, due_raw records the original wording | The anchor is unknown |
| 9 | End-of-meeting recap | M1 [00:07:54] | Do not label separately | Avoid double counting |
| 10 | A rejected proposal | T-M1-1, T-M2-1, T-M4-1, T-M5-1 | Do not label as action; goes into traps.json; label the rejecting sentence as decision | Product lists it as an action item = trap hit |
| 11 | A requirement that has already been completed | M2-16, M3-05 | result | Not an action item |
| 12 | Advisor restates their own earlier commitment | M2-18 | A new action, cross_meeting_ref = M1-12 | Tests cross-meeting linking |
| 13 | A date with no anchor is later anchored | M2-17 → M3-27 | The earlier one has due null; the later one has due 2026-10-20 | The date becomes explicit as meetings progress |
| 14 | The assignee discounts the assignment | M4-04 | tentative | Rule 5.2-3 |
| 15 | One sentence assigns 4 people | M4-34~37 | Split into 4 entries, each taking its own substring | One entry per person |
| 16 | The subject is "we" | M5-05, M5-19, M5-22, M5-23 | owner null + owner_accept | Do not penalize reasonable inference, and do not reward wild guessing |
| 17 | "Let me check" | M5-15 | tentative | Weak commitment |
| 18 | A preliminary result from a single seed | M3-10 | result / tentative | The product writing it as a firm conclusion = strength misjudgment |
| 19 | A prompt injection read aloud in the meeting | T-M3-1 | Label no entries for it; label only the subsequent "close the issue" (M3-17) | Text read aloud is not a meeting decision |
| 20 | A behavioral statement | M3 "Next time I'll ask in the group chat earlier" | Do not label | No concrete deliverable |
| 21 | An open question is postponed, then later resolved | M1-11 → M2-03 | question → decision, the latter linking to the former | Tests cross-meeting linking |
| 22 | Advisor commits on the student's behalf | M5-07 | owner Chen Siyuan | Rule 3-3 |
| 23 | "Plan to + vague date" | M4-13 "I plan to start writing in early November" | committed, due null, due_raw "early November" | "Plan to" carries no hedging; "early November" is not a specific day |
| 24 | "this week" | M5-25 | 2026-11-01, 10-30 is also accepted | Conversion rule in §4 |
| 25 | A need is acknowledged but "let's revisit it later", and nobody takes it on | M4-24 | suggestion, owner null | Weaker than "someone needs to look into it" |
| 26 | Discussion deferred | M3 "let's not discuss it for now" | Do not label | No decision was made |
| 27 | A decision with "I think" | M5-13 "That one I think is fine" | decision / tentative | The decision-maker themself hedges |
## 7. Dual Annotation and Cohen's Kappa

### 7.1 Why this is required

The current gold labels were drafted by AI. Without human review and dual annotation, the "gap between competitor output and gold" would be mixed with the gap caused by "the AI and a human judging the same sentence differently". When an interviewer asks "is your gold standard reliable?", you need to be able to answer with a Kappa value.

### 7.2 Procedure

| Step | What to do | Command |
|---|---|---|
| 1 | **Annotator A** (you) reviews the gold labels one by one and changes anything you disagree with | — |
| 2 | Find **Annotator B** (a fellow student, ideally also doing research). B reads this spec for 30 minutes, then practices on the first 10 items of M2 and discusses them | — |
| 3 | **Attribute agreement**: give B a file with strength / type / owner / due cleared, and have B fill them in independently | `python3 -I score.py --blank gold/M1.gold.jsonl > blank_M1.jsonl` (same for M3) |
| 4 | Compute Kappa | `python3 -I score.py --kappa gold_A_M1M3.jsonl annotatorB_M1M3.jsonl` |
| 5 | **Unit identification agreement** (optional but recommended): without looking at the gold labels, B finds items directly from the transcript and writes them in pred format. Then use `score.py` to score with A as gold and B as pred. Recall and precision then measure how much the items found by the two people overlap | `python3 -I score.py --gold gold/M1.gold.jsonl --pred annotatorB_units_M1.jsonl` |
| 6 | **Adjudication**: discuss each disagreement. If the spec was unclear, revise the spec and add a boundary case; if one side missed something, correct the annotation. Record the outcome in `results-template.md` §1.3 | — |

Sample size: at least M1 + M3 (46 items), ideally all 135 items.

### 7.3 How Kappa is computed and how to read it

Cohen's κ = (p_o − p_e) / (1 − p_e). p_o is the proportion of items on which the two annotators agree, and p_e is the proportion of agreement expected by chance if each annotator assigned labels at random according to their own category proportions. The script includes an example you can verify by hand (selftest C): A = aabbccaabb, B = aabbcaabbb, p_o = 0.8, p_e = 0.4×0.4 + 0.4×0.5 + 0.2×0.1 = 0.38, κ = 0.42 / 0.62 ≈ 0.677.

Commonly used interpretation bands: 0.41–0.60 moderate, 0.61–0.80 substantial, above 0.81 almost perfect agreement [Source 1, original not opened · to be verified]. This project adopts the following thresholds:

- **strength κ ≥ 0.6** is required before drawing conclusions from strength-related metrics (`strength_error_rate`, `soft_upgrade_rate`); otherwise revise the spec first and annotate another round.
- **type κ ≥ 0.7**.
- owner and due are open-valued, so only report the agreement rate, with a target of ≥ 90%.

**Watch for the "high agreement, low κ" phenomenon** [Source 2, original not opened · to be verified]: when one category accounts for the vast majority (in gold, 53 of the 70 action items have strength committed), the chance-agreement probability p_e is very high and κ gets pushed down. `sample/kappa_annotatorA_M3.jsonl` and `sample/kappa_annotatorB_M3.jsonl` are one such example: B changed only 6 items, the strength agreement rate is 81.5%, yet κ is only 0.372. So **always report p_o, κ, and the confusion for each category together**; do not report κ alone.

```bash
python3 -I score.py --kappa sample/kappa_annotatorA_M3.jsonl sample/kappa_annotatorB_M3.jsonl
# | strength | 0.372 | 0.815 | 27 |
# | type     | 0.945 | 0.963 | 27 |
```

## 8. Sources

1. Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174. https://doi.org/10.2307/2529310 [original not opened · to be verified; the band divisions are commonly cited]
2. Feinstein, A. R., & Cicchetti, D. V. (1990). High agreement but low kappa: I. The problems of two paradoxes. *Journal of Clinical Epidemiology*, 43(6), 543–549. https://doi.org/10.1016/0895-4356(90)90158-L [original not opened · to be verified]
3. Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement*, 20(1), 37–46. https://doi.org/10.1177/001316446002000104 [original not opened · to be verified; the formula itself has been verified by the hand-computed example in score.py selftest C]
