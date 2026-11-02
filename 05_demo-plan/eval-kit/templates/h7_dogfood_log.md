---
title: P-H7 Trial (Dogfood) and P-H12 Concierge Gate Log Sheet
status: Template v1 (not yet used; real data may be recorded only after the IRB determination reply and a one-time informed consent from the whole group)
---

# P-H7 Trial and P-H12 Concierge Gate Log Sheet

> Corresponds to: `03_positioning/03_final_positioning.md` §11 P-H7, P-H12; `04_prd/01_PRD_v2.md` §8.1 North Star (binary retention).
> Discipline: **"Was I reminded of something, and was it useful" is ticked by the participant personally**; the project owner does not fill it in on their behalf (to reduce social-desirability bias). The project owner records only objective events (timestamps, whether exported).

## 0. Preconditions (do not start if any is unmet)

| Item | Status | Date |
|---|---|---|
| IRB determination email has been replied to (02_user-research/06 §6.3 template) | To do | |
| **One-time informed consent from the whole group** of the participant's group (including the advisor); if consent cannot be obtained from the whole group, record only the participant's own commitment | To do | |
| Group consent rate = number consenting / number in the group who should consent (P-H7 observation item) | __/__ | |
| Model and provider used (must be a tool approved by the target university and confirmed in P-H10, or a local model that has passed the W2 Qwen3 release evaluation) | To do | |

## 1. P-H12 Concierge Gate (W1–W2, zero code)

The project owner manually produces 2 reconciliation sheets each for 2 fellow students (**at least 1 not from the same group**), using the eval-kit format, completed by hand.
**Written down in advance**: if 0 of 2 people are willing to paste the reconciliation sheet (or any part of it) into their own slides / weekly report → stop UI development and deliver only the evaluation work.

| Student (code) | Same group / other group | Round | Delivery time | Pasted into slides / weekly report (ticked by the student) | What was changed (written by the student) | Reason for not using it (written by the student) |
|---|---|---|---|---|---|---|
| S1 | | 1 | | ☐ Yes ☐ No | | |
| S1 | | 2 | | ☐ Yes ☐ No | | |
| S2 | | 1 | | ☐ Yes ☐ No | | |
| S2 | | 2 | | ☐ Yes ☐ No | | |
| **Gate result** | | | | __/2 people answered "Yes" at least once | | Pass / Stop UI |

## 2. P-H7 Weekly Log (from W3, 4 group-meeting weeks)

| Participant | Week | Group meeting date | Reconciliation completed within 24 h after the meeting (system timestamp) | Reconciliation sheet exported before the next group meeting (system timestamp) | **Was I reminded of something this week because of it** (ticked by the participant) | Preparation time (self-reported by the participant, minutes) | Where the post-meeting follow-up was sent after being copied (ticked by the participant) | Reason for not using it |
|---|---|---|---|---|---|---|---|---|
| | W1 | | ☐ | ☐ | ☐ Yes ☐ No | | ☐ Not sent ☐ DM to peer ☐ DM to advisor ☐ Group chat | |
| | W2 | | ☐ | ☐ | ☐ Yes ☐ No | | ☐ Not sent ☐ DM to peer ☐ DM to advisor ☐ Group chat | |
| | W3 | | ☐ | ☐ | ☐ Yes ☐ No | | ☐ Not sent ☐ DM to peer ☐ DM to advisor ☐ Group chat | |
| | W4 | | ☐ | ☐ | ☐ Yes ☐ No | | ☐ Not sent ☐ DM to peer ☐ DM to advisor ☐ Group chat | |

**North Star (binary retention)**: in a given week, both boxes ticked — "reconciled within 24 h **and** exported before the next group meeting" — = that participant is retained for that week.
**P-H7 verdict**: ≥2 people retained for 3 consecutive group meetings → holds; 0 people in week 2 → handle as the P-H7 abandon action in the positioning doc.

## 3. Week-2 Checkpoint Interview (5 minutes, answered by the participant)

1. What is the reason you did not paste any text this week? (No text / forgot / felt it was useless / did not want the AI to see it / other)
2. Did you send the post-meeting follow-up? Where did you send it? If the follow-up recipient is the advisor, would you send it?
3. Was there any item in the reconciliation sheet that you would otherwise have forgotten? (Please point to the specific item; if you cannot, write "None".)
