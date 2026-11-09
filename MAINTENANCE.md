# 维护说明

## 更新流程（每期）
1. `git pull` 取最新版本。
2. 按下方“渠道与取数方式”收集本期内容与数据。
3. 修改 `data.json`：
   - 新增一期：在 `weeks` 末尾加一条（`id`、`label`、`asOf`、`stage`、`summary`、`observations`、`next`、`quality`、`metrics.edm`、`metrics.social`）；在 `events` 加新条目并标 `week`；重写 `overall`（汇总）；更新 `meta.channels`、`meta.known`、`meta.metricsMethod`。
   - 手动刷新（非周一）：不新增一期，把最新一期区间延至当天（`asOf` 改为当天，`label` 注明“M/D 刷新”）。
   - 新渠道需加入 `channelOrder`。
4. 运行 `python3 build.py`，将数据写入 `index.html`；浏览器打开检查（含“汇总 · 全部期数”视图）。
5. 提交并推送：`git commit -m "第 N 期 · M/D"`，`git push`。
6. 同步发布到 Claude Artifact：https://claude.ai/artifact/6kUB9vGV1NA8cW5zDgbU2H

## 渠道与取数方式
- EDM（Klaviyo）：query_metric_aggregates（Clicked Email）用 `any(URL,[...])` 过滤各 P16 页面（/pages/p16-landing-page、/pages/p16-all-in-one-angled-smith-machine、/products/all-in-one-angled-smith-machine-p16），按 Campaign Name + URL + Bot Click 分组，Bot Click=0 的 unique 合计为“P16 链接点击（人）”；get_campaign_report 取送达、打开率、点击率、CTOR、退订率；自动化流程 “P16 | Early Bird Welcome”。
- 官网：新落地页、安装服务页 /pages/merach-smith-assembly、/collections/strength、商品页。
- Google 搜索广告 / PR / 媒体：Google 搜索 "Merach P16"（gl=us&hl=en&pws=0，qdr:w）。
- Instagram：@merachfit 主页取 shortcode，逐条读取 /p/<id>/ 的 og:description（日期、赞、评论）；主页中的合作帖需核对是否为 P16。
- Facebook：merachfit.us 主页 feed；单帖链接可从 Google 结果取得。
- Threads：@merachfit。X：x.com/Merachfit。
- YouTube：@Merachfit/videos 与 /shorts，页面源码取 viewCount、likeCount、publishDate。TikTok：@merachfit。
- Reddit：无法直接访问，只用 Google（`site:reddit.com/r/Merach_Fitness` 与 `reddit "Merach" "P16"`），再用标题加引号搜索取日期与评论数；链接指向社区或发帖账号主页。
- Amazon：搜索 merach p16 smith machine。
- 社媒与 Reddit 需在连接用户电脑（Chrome）时核查；云端运行时标“未核查”，下期补录。
- 社媒曝光 / 触达、Google Ads 数据需后台权限，当前未接入。

## 页面格式约定
- 板块顺序：发布阶段 → 本期要点 → 本期新增内容（渠道 × 日期矩阵）/ 渠道累计表现 → 渠道状态 → 已知产品信息 → 渠道数据明细 → 内容质量分析 · 分渠道 → 累计时间线 → 数据口径 → 署名。
- 评级：优 / 良 / 中 / 弱 / —（未产出或未核查）。每条内容附具体来源链接；中文书面语，简洁。
- 页面公开分享，不收录内部测试邮件（[Preview]）。

© Cristobal Du Peiming (杜沛明) — All Rights Reserved / 知识产权所有
