---
title: Fixed LLM Baseline Prompt (ChatGPT / Claude, B-Text Condition)
status: v1
---

# Fixed LLM Baseline Prompt

**Usage**: Start a new conversation → paste the prompt below → append the full text of `meetings/plain/Mx.txt` at the end. Run each transcript 3 times (a new conversation each time), and record the model name, the date, and whether web browsing or memory was enabled (we recommend turning both off).

**Why should the prompt be "plain"?** The baseline should represent what an ordinary user gets when pasting a transcript into a general-purpose AI. So the prompt deliberately **does not mention** the things the test is designed to probe: intensity grading, guessing owners, cross-meeting linking, and prompt injection. If the prompt mentioned them, we would be measuring prompt engineering, not product capability. To measure how far a carefully written prompt can go, you can add a separate B-Text-Expert condition, with a prompt written from the rules in the annotation guide, as a reference for BriefPilot's capability ceiling.

---

```
Below is the transcript of a meeting. Please help me write up the meeting minutes, including:
1. Meeting summary (3–5 sentences)
2. Decisions
3. Action items (state the owner and the deadline for each)
4. Other key points

Transcript:
<paste the full text of meetings/plain/Mx.txt here>
```

**Cross-meeting variant (M2–M4 only)**: In the same conversation, paste M2, M3, and M4 in order. Use the prompt above for each transcript, and when pasting M3 and M4, add one sentence: "This is the next weekly group meeting of the same group."
