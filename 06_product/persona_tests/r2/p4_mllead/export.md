# ML weekly sync 2 · 2026-11-02

## 上次事项的进展

- **会上说已完成** · Daniel Tan：Investigate tokenizer diff and post findings（"The root cause is the new tokenizer splitting product codes. I posted the writeup on Friday."）
- **还没做完或改期** · Mei Lin：Send signed contract to the team（"I'll send it by 2026-11-13."）
- **会上说已完成** · Arjun Mehta：Draft A100 hours request for infra（"Sent it to infra on Wednesday and they approved 200 extra hours."）
- **还没做完或改期** · Sofia Reyes：Write first draft of model card（"I got about half done, the evaluation section is missing. I'll finish it by EOD Friday."）
- **放弃** · Mei Lin：Update annotation guideline and share with vendor（"We did not get to it, and honestly I think the sarcasm cases are rare enough that we should drop it."）
- **还没做完或改期** · Daniel Tan：Add tokenizer regression test to CI（"Not started, I'll add it by 2026-11-20."）

## 谁答应了什么（已确认）

**Sofia Reyes**
- [ ] Set up and share A/B experiment config — 2026-11-12（原话：2026-11-12）（"I'll set it up and share it with the team by 2026-11-12."）
**Arjun Mehta**
- [ ] Benchmark reranker serving cost at 100 QPS — 2026-11-06（原话：EOD Friday）（"I'll benchmark it and report back by EOD Friday."）
**Priya Nair**
- [ ] Get launch criteria from product manager — 2026-11-06（原话：this week）（"Yes, I'll talk to the product manager and get the launch criteria this week."）

## 决议

- Drop the annotation guideline update（"Agreed, let's drop that."）
- Table the spot instance migration again（"The spot instance migration, we tabled it last week. Now that quota is approved, let's table this again."）

## 结果

- Identify root cause of recall regression（"The root cause is the new tokenizer splitting product codes. I posted the writeup on Friday."）
- Get GPU quota request approved（"Sent it to infra on Wednesday and they approved 200 extra hours."）

## 转写

[00:00:04] Priya Nair：Okay, welcome back everyone. Let's go through last week's items first.
[00:00:12] Priya Nair：Daniel, what did you find on the recall regression?
[00:00:20] Daniel Tan：The root cause is the new tokenizer splitting product codes. I posted the writeup on Friday.
[00:00:33] Priya Nair：Perfect. And the CI regression test?
[00:00:40] Daniel Tan：Not started, I'll add it by 2026-11-20.
[00:00:50] Priya Nair：Mei, did the vendor contract get signed?
[00:00:58] Mei Lin：Legal is still reviewing one clause, so it slipped to next week. I'll send it by 2026-11-13.
[00:01:12] Priya Nair：Okay. Arjun, the GPU quota request?
[00:01:20] Arjun Mehta：Sent it to infra on Wednesday and they approved 200 extra hours.
[00:01:32] Priya Nair：Great. Sofia, how's the model card?
[00:01:40] Sofia Reyes：I got about half done, the evaluation section is missing. I'll finish it by EOD Friday.
[00:01:55] Priya Nair：Okay. Mei, the annotation guideline update?
[00:02:03] Mei Lin：We did not get to it, and honestly I think the sarcasm cases are rare enough that we should drop it.
[00:02:15] Priya Nair：Agreed, let's drop that.
[00:02:22] Priya Nair：The spot instance migration, we tabled it last week. Now that quota is approved, let's table this again.
[00:02:33] Arjun Mehta：Makes sense.
[00:02:40] Priya Nair：New topic, the A/B test for the new reranker. Sofia, can you set up the experiment config?
[00:02:50] Sofia Reyes：I'll set it up and share it with the team by 2026-11-12.
[00:03:02] Priya Nair：Arjun, can you check the serving cost of the reranker at 100 QPS?
[00:03:12] Arjun Mehta：I'll benchmark it and report back by EOD Friday.
[00:03:25] Daniel Tan：Should we involve product for the launch criteria?
[00:03:33] Priya Nair：Yes, I'll talk to the product manager and get the launch criteria this week.
[00:03:45] Priya Nair：Anything else? No? Thanks all.
