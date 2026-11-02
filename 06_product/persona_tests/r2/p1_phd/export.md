# 10月26日组会 · 2026-10-26

## 上次事项的进展

- **会上说已完成** · 陈思雨：重做标定并重跑 baseline（"重标完了，新的 success rate 是 78%，gap 缩小很多，周五就发给您了。"）
- **还没做完或改期** · 林子昂：做出 memory profile 给大家看（"我 profile 做了一半，只跑了 PTv3 的 forward，backward 的还没测，gradient checkpointing 的对比周四前补上。"）
- **会上说已完成** · 陈思雨：写 related work 初稿（"初稿昨天写完了，我已经发到 Overleaf 了。"）
- **会上说已完成** · 我(博三)：补完 occlusion ablation（"做完了，周三晚上跑完的，occlusion 越严重我们的方法优势越明显，已经放进 table 2 了。"）
- **放弃** · 我(博三)：做 failure case 的 visualization（"嗯，页数确实紧，那就不做了，有时间再放 arXiv 版本。"）
- **还没做完或改期** · 林子昂：发邮件约 Prof. Wang 的 meeting（"还没发邮件，我这周补上。"）

## 谁答应了什么（已确认）

**我(博三)**
- [ ] 把 experiment section 整合进主文 — 2026-11-09（原话：11 月 9 号之前）（"博三的，你负责把 experiment section 整合进主文，11 月 9 号之前"）
**陈思雨**
- [ ] polish related work 并检查 reference 格式 — 2026-11-10（原话：11 月 10 号前）（"小陈你负责 related work 的 polish 和 reference 格式检查，11 月 10 号前"）
- [ ] 用新标定重跑 real robot occlusion 实验 — 2026-11-06（原话：下周五前）（"ablation 里 real robot 的部分，需要用新标定重新跑一遍 occlusion 的实验。小陈你和博三一起，下周五前"）
**林子昂**
- [ ] 发邮件约 Prof. Wang 合作 — 2026-10-26（原话：今天）（"好，今天发。"）

## 决议

- 不做 failure case visualization（"页数确实紧，那就不做了"）
- 开始 rebuttal 前的 internal review（"我们离 deadline 还有三周，要开始 rebuttal 之前的 internal review"）
- 取消周三的 meeting（"另外我下周要出差，周三的 meeting 取消"）

## 结果

- 完成 hand-eye 重标定（"重标完了，新的 success rate 是 78%，gap 缩小很多"）
- 完成一半 memory profile（"我 profile 做了一半，只跑了 PTv3 的 forward，backward 的还没测"）
- 完成 occlusion ablation 并放入 table 2（"occlusion 越严重我们的方法优势越明显，已经放进 table 2 了"）
- 写完 related work 初稿（"初稿昨天写完了，我已经发到 Overleaf 了"）

## 转写

[00:00:10] 周明远(导师)：好，开始吧。先对一下上周的事情。小陈，hand-eye calibration 怎么样？
[00:00:35] 陈思雨：重标完了，新的 success rate 是 78%，gap 缩小很多，周五就发给您了。
[00:01:10] 周明远(导师)：很好。小林，memory profile 呢？
[00:01:30] 林子昂：老师不好意思，我 profile 做了一半，只跑了 PTv3 的 forward，backward 的还没测，gradient checkpointing 的对比周四前补上。
[00:02:15] 周明远(导师)：可以，周四前补完。
[00:02:40] 周明远(导师)：博三的，occlusion ablation 呢？
[00:02:58] 我(博三)：做完了，周三晚上跑完的，occlusion 越严重我们的方法优势越明显，已经放进 table 2 了。
[00:03:30] 周明远(导师)：好。visualization 呢？
[00:03:45] 我(博三)：老师，这个我想放弃了。failure case 的 visualization 篇幅放不下，ICRA 只有 8 页，我打算放 supplementary 里或者直接不做。
[00:04:20] 周明远(导师)：嗯，页数确实紧，那就不做了，有时间再放 arXiv 版本。
[00:04:50] 周明远(导师)：related work 小陈你那边？
[00:05:10] 陈思雨：初稿昨天写完了，我已经发到 Overleaf 了。
[00:05:35] 周明远(导师)：OK。接下来讲新的事情。我们离 deadline 还有三周，要开始 rebuttal 之前的 internal review。
[00:06:10] 周明远(导师)：博三的，你负责把 experiment section 整合进主文，11 月 9 号之前。
[00:06:30] 我(博三)：好，11 月 9 号前我整合完。
[00:06:50] 周明远(导师)：小陈你负责 related work 的 polish 和 reference 格式检查，11 月 10 号前。
[00:07:10] 陈思雨：没问题。
[00:07:30] 周明远(导师)：还有，ablation 里 real robot 的部分，需要用新标定重新跑一遍 occlusion 的实验。小陈你和博三一起，下周五前。
[00:07:55] 陈思雨：可以，我来协调机器人时间。
[00:08:10] 我(博三)：OK，我提供脚本。
[00:08:40] 周明远(导师)：另外我下周要出差，周三的 meeting 取消。
[00:09:00] 周明远(导师)：小林，你要和 Prof. Wang 约一下的合作，这个有没有进展？
[00:09:20] 林子昂：还没发邮件，我这周补上。
[00:09:45] 周明远(导师)：今天发。
[00:09:55] 林子昂：好，今天发。
[00:10:20] 周明远(导师)：行，散会。
