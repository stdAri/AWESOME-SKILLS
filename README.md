# Awesome SKILLs

> 个人精选的 AI Agent Skills 合集，以 **repo 为单位**进行管理。每个 repo 可包含一个或多个 Skill，服务于 Claude Code、GitHub Copilot 等 AI Agent。

*最后更新：2026-05-07*

---

## 目录

- [Awesome SKILLs](#awesome-skills)
  - [目录](#目录)
  - [学术研究全流程](#学术研究全流程)
  - [AI 自动研究](#ai-自动研究)
  - [科学写作](#科学写作)
  - [通用搜索与信息获取](#通用搜索与信息获取)
  - [工具与扩展](#工具与扩展)
  - [如何使用本库](#如何使用本库)
    - [添加新 Repo](#添加新-repo)
    - [同步各 Repo 的最新更新](#同步各-repo-的最新更新)
  - [目录结构](#目录结构)

---

## 学术研究全流程

| Repo | 描述 | 包含 Skills | 来源 | 最近更新 |
|------|------|-------------|------|----------|
| **[academic-research-skills](academic-research-skills/)** | 覆盖从选题到投稿的完整学术研究流水线，含完整性门控、交叉验证和引用核查 | `academic-paper` · `academic-paper-reviewer` · `academic-pipeline` · `deep-research` | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 2026-05-07<br>· docs: add NOTICE.md (personal project statement) (#75)<br>· spec(v3.7.1): trust provenance & drift transparency design — 8-round codex convergence (#74)<br>· docs(readme): hero install hook + prerequisites + first-command guide (#72)<br>· feat(v3.7.0 Phase 3): version sweep across 8 files (3 inline + 1 fresh PR review → 0 findings) (#71)<br>· feat(v3.7.0 Phase 2.2): SessionStart announce hook (2 inline rounds + fresh PR review → 0 findings) (#70)<br>· …（共 15 条）|
| **[claude-scholar](claude-scholar/)** | 面向 CS/AI 研究者的半自动化研究助手，支持文献综述、实验代码、报告写作和项目知识管理；兼容 Claude Code、Codex CLI、OpenCode | `literature-review` · `experiment` · `paper-writing` · `publication-chart` 等 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 2026-04-27<br>· docs(readme): simplify kb news wording<br>· docs(readme): merge obsidian kb news item<br>· docs(readme): restore recent news history|
| **[Paper Deep Reading Skill](paper-deep-reading-skill/)** | 逐页精读本地学术 PDF，抓取定理链与仿真截图，输出带图证据的结构化中文 Markdown 报告；尤适控制/估计/观测器类论文 | `paper-deep-reading` | [Eroticoo/paper-deep-reading-skill](https://github.com/Eroticoo/paper-deep-reading-skill) | 2026-04-21<br>· Redesign README with tags and detailed workflow<br>· Clarify Windows support and mac experimental usage<br>· Add Codex-assisted install note to README<br>· Flatten skill repo and remove PowerShell installer flow<br>· Rewrite README in Chinese and emphasize installation<br>· …（共 9 条） |
| **[Applied Math Paper Derivation](applied-math-paper-derivation/)** | 面向英文应用数学论文的推导重建 Skill，逐段详解推导、重构创新点公式，输出 IEEE 双栏 PDF + Markdown，难点用紫色标注 | `applied-math-paper-derivation` | [Eroticoo/applied-math-paper-derivation](https://github.com/Eroticoo/applied-math-paper-derivation) | 2026-04-02<br>· Polish README with install guide and visuals<br>· Add publishable applied math derivation skill |
| **[LaTeX arXiv Paper Writer](latex-arxiv-SKILL/)** | Issue 驱动的 IEEEtran 双栏 LaTeX 工作流，两条提示词生成完整 arXiv ML/AI 综述论文，含 BibTeX 引文验证；Claude Code 和 Codex 均支持 | `arxiv-paper-writer` | [renocrypt/latex-arxiv-SKILL](https://github.com/renocrypt/latex-arxiv-SKILL) | 2025-12-29<br>· v0.5 multi-SKILLs and sqlite bib caching<br>· refine the SKILL calling logic<br>· testing multi-skill arrangement<br>· refine the arxiv fetching logic<br>· feat(arxiv-paper-writer): add arXiv registry cache<br>· …（共 8 条） |
| **[Awesome Agent Skills for Empirical Research](Awesome-Agent-Skills-for-Empirical-Research/)** | CoPaper.AI × Stanford REAP 维护的实证研究 Skills 大全，收录 119 个仓库 / 23000+ Skills，覆盖 DID/IV/RDD/PSM 等因果推断全链路 | `StatsPAI` · `Full Empirical Analysis` · `chinese-de-aigc` 等 | [brycewang-stanford/Awesome-Agent-Skills-for-Empirical-Research](https://github.com/brycewang-stanford/Awesome-Agent-Skills-for-Empirical-Research) | 2026-05-04<br>· docs(changelog): 新增 2026-05-04 条目 —— 首个社区 PR 收录 humanize-chinese<br>· docs: vendor humanize-chinese into skills/49 + 更新 README 本地位置<br>· docs: 收录 humanize-chinese 到降 AIGC 检测率章节 (#5)<br>· chore(demo): pin notebook kernel to Python 3.11.0<br>· feat(demo): add LaLonde 5.2 pipeline outputs across StatsPAI/Stata/R + scaffold test-skill|
| **[Awesome Scientific Skills](Awesome-Scientific-Skills/)** | 面向自然科学研究者的开放 Agent Skills 精选合集，涵盖生信/化学信息/文献检索/科学写作/统计分析等，兼容 Claude Code、Codex、Cursor、Gemini CLI | 生信/化学/文献/写作等多类 | [InternScience/Awesome-Scientific-Skills](https://github.com/InternScience/Awesome-Scientific-Skills) | 2026-03-12<br>· chore : rename readme_skills.md<br>· fix : modify readme<br>· feat : add skills-metric dir<br>· fix : fix some bugs<br>· fix : fix unicode bug<br>· …（共 10 条） |

## AI 自动研究

| Repo | 描述 | 包含 Skills | 来源 | 最近更新 |
|------|------|-------------|------|----------|
| **[Auto-claude-code-research-in-sleep](Auto-claude-code-research-in-sleep/)** | ARIS — 让 Claude Code 在你睡觉时自主推进研究：跑评审循环、执行实验、改写叙述。零依赖纯 Markdown，可迁移至任意 Agent | 62+ skills（涵盖多源文献检索、实验追踪、Research Wiki 等） | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 2026-05-07<br>· docs(news): add 2026-05-06 entry for /paper-talk + /slides-polish<br>· feat(paper-talk): end-to-end conference talk pipeline workflow<br>· feat(slides-polish): per-page Codex review + targeted layout/font fixes for talk decks<br>· docs(news): add 2026-05-05 entry for /resubmit-pipeline (#208) (#209)<br>· feat(resubmit-pipeline): new W5 skill + edit-whitelist + citation-audit --soft-only (#208)<br>· …（共 9 条）|
| **[autoresearch](autoresearch/)** | 给 AI Agent 一个迷你 LLM 训练环境，让其自主过夜实验：修改代码→训练5分钟→比对指标→保留或回滚 | `program.md`（Agent 指令驱动，非传统 SKILL.md） | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | 2026-03-25<br>· Bug fix |
| **[OpenResearch](openresearch/)** | 以「声明-证据」原子图谱为核心的 AI/ML 研究协作系统，AI 围绕 claim 自主生成实验、执行、回收结果并回写图谱；graph-first、持续演化，替代 paper-first 的自动科研流水线 | 完整系统（packages/sdks/specs，非单一 SKILL.md） | [openResearch1/openresearch](https://github.com/openResearch1/openresearch) | 2026-05-06<br>· fix(collab): wake on session idle + prevent list_children polling<br>· 新增 GraphRAG 剪枝和评分功能<br>· feat(collab): multi-agent collaboration framework|

## 科学写作

| Repo | 描述 | 包含 Skills | 来源 | 最近更新 |
|------|------|-------------|------|----------|
| **[sciwrite](sciwrite/)** | 基于斯坦福 Sainani《Writing in the Sciences》课程的手稿写作审查 Skill，执行去冗余、主动语态、句子结构、关键词一致性、数据引用完整性五轮审查 | `manuscript-writing-review` | [labarba/sciwrite](https://github.com/labarba/sciwrite) | 2026-04-04<br>· trim README<br>· add hand-edited README<br>· Create LICENSE<br>· add files from local working dir<br>· Initial commit|
| **[Research Paper Writing Skills](Research-Paper-Writing-Skills/)** | ML/CV/NLP 论文写作技能包，基于彭思达教授开放笔记整理，涵盖 Abstract/Introduction/Method/Experiments/Conclusion 各节写作指导 | `research-paper-writing` | [Master-cai/Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills) | 2026-04-23<br>· Add MIT license and reference it in readmes<br>· add research-paper-writing skill and bilingual README<br>· first commit |

## 通用搜索与信息获取

| Repo | 描述 | 包含 Skills | 来源 | 最近更新 |
|------|------|-------------|------|----------|
| **[skills (UniFuncs)](skills/)** | UniFuncs AI 深度搜索能力套件，提供实时网页搜索、URL 内容读取（支持 PDF/Word/Excel）、多源交叉验证的深度搜索和深度研究报告生成 | `unifuncs-search` · `unifuncs-reader` · `unifuncs-deep-search` · `unifuncs-deep-research` | [UniFuncs/skills](https://github.com/UniFuncs/skills) | 2026-03-29<br>· docs: Enhance UniFuncs Deep Research Skill documentation<br>· fix: Update max-words limit in read.py and SKILL.md|

## 工具与扩展

| Repo | 描述 | 包含 Skills | 来源 | 最近更新 |
|------|------|-------------|------|----------|
| **[Karpathy-Inspired Claude Code Guidelines](andrej-karpathy-skills/)** | Karpathy 提炼 LLM 编码四原则，以单一 CLAUDE.md 改善 Claude Code 行为：先思后码、简洁优先、外科修改、目标驱动 | `karpathy-guidelines` | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | 2026-04-20<br>· Sync Chinese README with English version (add Cursor section) (#95)<br>· add cursor support (#92)<br>· Add Chinese translation for README (#93)<br>· Update README with project and social media links<br>· Update README with project and social media links<br>· …（共 9 条） |
| **[SkVM (SJTU-IPADS)](SkVM/)** | 上交大出品的 LLM Agent Skill 编译运行时，对 Skill 做 Profiling、AOT 编译和 JIT 优化，使其跨异构模型和 harness 运行（arXiv:2604.03088） | `skvm-jit` · `skvm-general` | [SJTU-IPADS/SkVM](https://github.com/SJTU-IPADS/SkVM) | 2026-04-27<br>· docs: add CONTRIBUTING.md and issue/PR templates<br>· Bump skvm-data: add deepseek-v4-{flash,pro} profiles<br>· providers+hermes: deepseek thinking-mode echo + hermes managed-mode fix<br>· cli-config: cap config init backups at 5 most recent<br>· docs: capture aot-compile pass-registry follow-up debt<br>· …（共 10 条） |
| **[歸藏 Magazine Web PPT Skill](guizang-ppt-skill/)** | 生成电子杂志风横向翻页单文件 HTML PPT，含 WebGL 背景、5 套主题色、10 种页面布局，由歸藏从线下分享实践沉淀 | `guizang-ppt-skill` | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | 2026-04-28<br>· Update README for Codex image flow<br>· Add Codex image generation guidance|

| **[HTML Anything](html-anything/)** | AI Agent HTML 生成参考项目，用于把需求转化为可交付的 HTML 页面、组件或单文件产物 | HTML 生成 / 前端产物 | [nexu-io/html-anything](https://github.com/nexu-io/html-anything) | （待初始化） |
| **[HTML Effectiveness](html-effectiveness/)** | Anthropic HTML 产物效果评估项目，用于评估 AI 生成 HTML 页面的质量、任务完成度与展示有效性 | HTML 评估 / 质量基准 | [anthropics/html-effectiveness](https://github.com/anthropics/html-effectiveness) | （待初始化） |
| **[OpenHuman](openhuman/)** | tinyhumansai 开放 AI human / agent 交互项目，可作为拟人化 Agent 和应用构建参考 | AI human / Agent 应用 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | （待初始化） |
| **[PPT Master](ppt-master/)** | 演示文稿生成项目，提供中文说明，适合用于 AI 生成、润色和组织 PPT 内容 | PPT 生成 / 演示文稿 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | （待初始化） |

---

## 如何使用本库

### 添加新 Repo

```bash
# 作为子模块添加（推荐，保持与上游同步）
git submodule add <repo-url> <repo-name>

# 或直接 clone
git clone <repo-url> <repo-name>
```

然后在 `README.md` 对应分类中添加条目，并在 `registry.yaml` 中补充元数据。

### 同步各 Repo 的最新更新

`sync.py` 会对每个 git repo 运行 `git pull`，再与 `updated_at` 对比新提交；对有 `skill_source` 的 repo（如 folo）通过 SHA-256 检测远程 URL 变化。默认仅预览，`--apply` 才实际写入。

```powershell
# 预览会做什么（默认）
.venv\Scripts\python.exe scripts\sync.py

# 实际写入 registry.yaml 和 README.md
.venv\Scripts\python.exe scripts\sync.py --apply

# 只同步某个 repo
.venv\Scripts\python.exe scripts\sync.py --apply --repo claude-scholar
```

---

## 目录结构

```
Awesome-SKILLs/
├── README.md                          # 本文件，分类浏览
├── registry.yaml                      # 结构化元数据，供脚本和 AI 查询
├── academic-research-skills/          # 学术研究全流程 skills
├── Auto-claude-code-research-in-sleep/ # ARIS 自动研究框架
├── autoresearch/                      # AI 自主 ML 实验框架
├── claude-scholar/                    # 半自动化学术助手
├── sciwrite/                          # 科学写作审查 skill
├── skills/                            # UniFuncs 深度搜索 skills
└── scripts/
    └── sync.py                        # git pull + SHA-256 检测，同步 registry 和 README
```
