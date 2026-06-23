# Awesome SKILLs

> 个人精选的 AI Agent Skills / Agent Research 项目索引，以 **repo 为单位**管理。每个条目可能包含一个或多个 Skill，也可能是可供 Claude Code、Codex、Cursor、Gemini CLI 等 Agent 参考的完整框架或基准项目。

*最后更新：2026-06-13；最近同步数据见 `registry.yaml`。*

---

## 目录

- [快速选型](#快速选型)
- [分类索引](#分类索引)
  - [学术研究流水线](#学术研究流水线)
  - [论文阅读、推导与文献处理](#论文阅读推导与文献处理)
  - [科学写作与投稿产出](#科学写作与投稿产出)
  - [自主研究与实验系统](#自主研究与实验系统)
  - [搜索、信息获取与知识源](#搜索信息获取与知识源)
  - [Agent 开发、运行时与行为规范](#agent-开发运行时与行为规范)
  - [演示、HTML 与可视化产物](#演示html-与可视化产物)
  - [综合合集与外部索引](#综合合集与外部索引)
- [维护方式](#维护方式)
  - [添加完整上游 repo](#添加完整上游-repo)
  - [添加只保存总结的外部 repo](#添加只保存总结的外部-repo)
  - [同步各 repo 的最新更新](#同步各-repo-的最新更新)
- [目录结构](#目录结构)

---

## 快速选型

| 需求 | 优先看 |
|---|---|
| 从选题、检索、写作到审稿的完整学术流水线 | [Academic Research Skills](academic-research-skills/)、[ARIS](Auto-claude-code-research-in-sleep/)、[Claude Scholar](claude-scholar/) |
| 深读单篇论文、重建数学推导 | [Paper Deep Reading Skill](paper-deep-reading-skill/)、[Applied Math Paper Derivation](applied-math-paper-derivation/) |
| 写论文、改 manuscript、生成 arXiv/IEEE 风格产物 | [Nature Skills](nature-skills/)、[SciWrite](sciwrite/)、[Research Paper Writing Skills](Research-Paper-Writing-Skills/)、[LaTeX arXiv Paper Writer](latex-arxiv-SKILL/) |
| 让 Agent 自主跑实验或持续推进研究 | [autoresearch](autoresearch/)、[OpenResearch](openresearch/)、[ARIS](Auto-claude-code-research-in-sleep/) |
| 深度搜索、RSS、外部知识获取 | [UniFuncs Agent Skills](skills/)、[Folo CLI Skill](folo/)、[QMD](qmd/) |
| 研究 Agent Skill 的工程化、运行时、行为约束 | [SkVM](SkVM/)、[Karpathy-Inspired Claude Code Guidelines](andrej-karpathy-skills/)、[Conductor](conductor/)、[Matt Pocock Skills](mattpocock-skills/) |
| 生成 PPT、HTML 页面或评估前端产物 | [歸藏 Magazine Web PPT Skill](guizang-ppt-skill/)、[PPT Master](ppt-master/)、[HTML Anything](html-anything/)、[HTML Effectiveness](html-effectiveness/) |

---

## 分类索引

### 学术研究流水线

面向“从研究问题到论文产出”的端到端流程，通常包含文献检索、研究计划、实验/证据、写作、审稿或项目知识管理。

| Repo | 重点能力 | 形式 | 最近同步 |
|---|---|---|---|
| **[Academic Research Skills](https://github.com/Imbad0202/academic-research-skills)** | 从选题到投稿的完整学术研究流水线，含完整性门控、引用核查、交叉验证和 VLM 图表验证 | Skill 套件 | 2026-06-06 |
| **[Claude Scholar](https://github.com/Galaxy-Dawn/claude-scholar)** | 面向 CS/AI 研究者的半自动化研究助手，覆盖文献综述、实验代码、分析报告写作和项目知识管理 | 框架 / commands / skills | 2026-06-05 |
| **[ARIS — Auto Research In Sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)** | 让 Claude Code overnight 推进研究：评审循环、实验执行、叙述改写、多源文献检索 | Markdown 工作流 / Skill 集 | 2026-06-05 |

### 论文阅读、推导与文献处理

面向“读懂论文”和“把论文中的论证、公式、证据拆开”的工具，适合作为论文精读和方法复现的辅助。

| Repo | 重点能力 | 形式 | 最近同步 |
|---|---|---|---|
| **[Paper Deep Reading Skill](https://github.com/Eroticoo/paper-deep-reading-skill)** | 逐页精读本地学术 PDF，抓取定理链与仿真截图，输出带图证据的中文 Markdown 报告 | Skill | 2026-04-21 |
| **[Applied Math Paper Derivation](https://github.com/Eroticoo/applied-math-paper-derivation)** | 面向英文应用数学论文的推导重建，逐段详解公式与创新点，输出 IEEE 双栏 PDF + Markdown | Skill | 2026-04-02 |
| **[Awesome Agent Skills for Empirical Research](https://github.com/brycewang-stanford/Awesome-Agent-Skills-for-Empirical-Research)** | 实证研究 Skills 大全，覆盖 DID、IV、RDD、PSM 等因果推断链路 | 外部合集 / skill registry | 2026-06-05 |

### 科学写作与投稿产出

面向 manuscript、论文结构、语言风格、LaTeX/BibTeX、会议或 arXiv 产物。

| Repo | 重点能力 | 形式 | 最近同步 |
|---|---|---|---|
| **[SciWrite — Manuscript Writing Review](https://github.com/labarba/sciwrite)** | 基于 Stanford Writing in the Sciences 的五轮手稿写作审查：去冗余、主动语态、句子结构、关键词一致性、数据引用完整性 | Skill | 2026-04-04 |
| **[Research Paper Writing Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills)** | ML/CV/NLP 论文各章节写作指导，覆盖 Abstract、Introduction、Method、Experiments、Conclusion | Skill | 2026-04-23 |
| **[LaTeX arXiv Paper Writer](https://github.com/renocrypt/latex-arxiv-SKILL)** | Issue 驱动的 IEEEtran 双栏 LaTeX 工作流，生成 arXiv ML/AI 综述论文并验证 BibTeX 引文 | Skill | 2025-12-29 |
| **[PPT Master](https://github.com/hugohe3/ppt-master)** | 演示文稿生成项目，适合 AI 生成、润色和组织 PPT 内容 | 项目 / PPT 工作流 | 2026-06-04 |
| **[Nature Skills](https://github.com/Yuan1z0825/nature-skills.git)** | 面向 Nature / 高影响力期刊科研产出的 Skills 套件，覆盖写作、润色、审稿、引用、全文 reader、论文转 PPT、数据可用性和论文转专利 | Skill 套件 | 2026-06-20 |

### 自主研究与实验系统

面向“Agent 自己提出、执行、比较、回写实验结果”的系统，通常不是单一 SKILL.md，而是研究自动化环境或协作框架。

| Repo | 重点能力 | 形式 | 最近同步 |
|---|---|---|---|
| **[autoresearch](https://github.com/karpathy/autoresearch)** | 给 AI Agent 一个迷你 LLM 训练环境：修改训练代码、固定 5 分钟训练、比对 `val_bpb`、保留或回滚 | 实验环境 | 2026-03-25 |
| **[OpenResearch](https://github.com/openResearch1/openresearch)** | 以“声明-证据”原子图谱为核心，AI 围绕 claim 生成实验、执行、回收结果并回写图谱 | 研究协作系统 | 2026-05-29 |
| **[OpenHuman](https://github.com/tinyhumansai/openhuman)** | tinyhumansai 开放 AI human / agent 交互项目，可作为拟人化 Agent 和应用构建参考 | Agent 应用参考 | 2026-06-05 |

### 搜索、信息获取与知识源

面向实时网页搜索、URL 内容读取、RSS、深度研究报告等外部信息获取能力。

| Repo | 重点能力 | 形式 | 最近同步 |
|---|---|---|---|
| **[UniFuncs Agent Skills](https://github.com/UniFuncs/skills)** | 实时网页搜索、URL 内容读取（PDF/Word/Excel/PPTX）、多源交叉验证深度搜索和深度研究报告生成 | Skill 套件 | 2026-05-27 |
| **[Folo CLI Skill](https://github.com/RSSNext/Folo)** | Folo RSS 阅读器 CLI 技能，支持订阅管理、时间线阅读、未读处理、收藏操作、OPML 导入导出 | Skill / CLI | 2026-06-06 |
| **[QMD](https://github.com/tobi/qmd)** | 本地文档、知识库、会议记录搜索引擎，组合 BM25、向量语义搜索和 LLM rerank，并提供 CLI 与 MCP server | CLI / 本地搜索 | 待初始化 |

### Agent 开发、运行时与行为规范

面向 Skill 工程化、Agent 运行时、Claude Code 行为约束和可移植性。

| Repo | 重点能力 | 形式 | 最近同步 |
|---|---|---|---|
| **[SkVM](https://github.com/SJTU-IPADS/SkVM)** | LLM Agent Skill 编译运行时，对 Skill 做 Profiling、AOT 编译和 JIT 优化，使其跨模型和 harness 运行 | 运行时 / 研究系统 | 2026-06-06 |
| **[Karpathy-Inspired Claude Code Guidelines](https://github.com/forrestchang/andrej-karpathy-skills)** | 以单一 CLAUDE.md 改善 Claude Code 行为：先思后码、简洁优先、外科修改、目标驱动 | 行为规范 / Claude Code Plugin | 2026-04-20 |
| **[Conductor](https://github.com/Jinghao67/conductor)** | 长周期 AI 工作的上下文卫生与交互式分支编排：干净 master、可交互分支、调度室和脏解释 sidecar | Skill / Claude Code Plugin | 待初始化 |
| **[Matt Pocock Skills](https://github.com/mattpocock/skills)** | 面向真实软件工程的 Agent Skill 套件：需求追问、PRD/issue 拆分、TDD、诊断、架构改进和代码库上下文整理 | Skill 套件 / 工程工作流 | 待初始化 |

### 演示、HTML 与可视化产物

面向 PPT、HTML、Web 展示和 AI 生成前端产物的生成或评估。

| Repo | 重点能力 | 形式 | 最近同步 |
|---|---|---|---|
| **[歸藏 Magazine Web PPT Skill](https://github.com/op7418/guizang-ppt-skill)** | 生成电子杂志风横向翻页单文件 HTML PPT，含 WebGL 背景、主题色和多种页面布局 | Skill | 2026-06-02 |
| **[HTML Anything](https://github.com/nexu-io/html-anything)** | AI Agent HTML 生成参考项目，用于把需求转化为可交付 HTML 页面、组件或单文件产物 | 前端生成参考 | 2026-06-02 |
| **[HTML Effectiveness](https://github.com/anthropics/html-effectiveness)** | Anthropic HTML 产物效果评估项目，用于评估 AI 生成 HTML 页面的质量、任务完成度与展示有效性 | 评估基准 | 2026-05-15 |

### 综合合集与外部索引

跨学科或跨任务的 Skills 集合，适合用作发现入口，而不是直接选定单一工作流。

| Repo | 重点能力 | 形式 | 最近同步 |
|---|---|---|---|
| **[Awesome Scientific Skills](https://github.com/InternScience/Awesome-Scientific-Skills)** | 面向自然科学研究者的开放 Agent Skills 精选合集，涵盖生信、化学信息、文献检索、科学写作、统计分析等 | 外部合集 | 2026-05-26 |
| **[Awesome Agent Skills for Empirical Research](https://github.com/brycewang-stanford/Awesome-Agent-Skills-for-Empirical-Research)** | CoPaper.AI × Stanford REAP 维护的实证研究 Skills 大全，收录大量经验研究工作流 | 外部合集 | 2026-06-05 |

---

## 维护方式

结构化元数据以 `registry.yaml` 为准；`README.md` 负责面向人类浏览的分类和选型说明。

### 添加完整上游 repo

1. 在项目根目录 clone 或添加子模块，目录名应与 `registry.yaml` 的 `local_path` 一致。
2. 在 `registry.yaml` 的 `repos:` 列表末尾新增条目，包含 `name`、`display_name`、`description`、`repo`、`local_path`、`categories`、`updated_at: ''`、`last_commit: ''`、`changelog: []`。
3. 在 `README.md` 对应分类表格追加一行，最近同步填 `待初始化`。
4. 运行同步脚本初始化 `updated_at`、`last_commit` 和 `changelog`。

```powershell
.venv\Scripts\python.exe sync.py --apply --repo <name>
```

### 添加只保存总结的外部 repo

当只需要索引外部 repo，而不需要把完整源码纳入本项目时：

1. 创建 `<local_path>/README.md`，只写来源链接、类型、摘要和使用提示。
2. 不 clone 上游 repo，不创建 `.git`，不复制上游源码、资源或大文件。
3. 在 `registry.yaml` 添加同名条目；`updated_at`、`last_commit`、`changelog` 初始留空。
4. 在 `README.md` 对应分类表格追加摘要行，最近同步填 `待初始化`。
5. 验证 `<local_path>/.git` 不存在，确认只纳入总结文档。

### 同步各 repo 的最新更新

`sync.py` 会对每个 git repo 运行 `git pull --ff-only`，再根据 `last_commit` 或 `updated_at` 追加 changelog；对有 `skill_source` 的 repo（如 Folo）通过 SHA-256 检测远程内容变化。默认仅预览，`--apply` 才写入 `registry.yaml` 和 `README.md`。

```powershell
# 预览会做什么（默认）
.venv\Scripts\python.exe sync.py

# 实际写入 registry.yaml 和 README.md
.venv\Scripts\python.exe sync.py --apply

# 只同步某个 repo
.venv\Scripts\python.exe sync.py --apply --repo claude-scholar
```

---

## 目录结构

```text
Awesome-SKILLs/
├── README.md                           # 本文件：分类浏览与快速选型
├── registry.yaml                       # 结构化元数据，供脚本和 AI 查询
├── requirements.txt                    # Python 依赖
├── sync.py                             # git pull + SHA-256 检测，同步 registry 和 README
└── .claude/
    ├── .env.example                    # API key 示例，不含真实密钥
    └── skills/registry-manage/         # 本仓库 registry 管理 Skill
```
