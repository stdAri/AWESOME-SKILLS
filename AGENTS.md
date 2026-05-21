# AIResearch

本项目是 Codex AI Research Skill 的汇总追踪仓库。目的是集中收集、对比和管理各类与 Codex 学术研究能力相关的开源项目和技能（skills）。

**本项目不直接执行研究任务。** 具体的研究工作在其他项目目录下进行，本目录仅作为索引、评估和参考。

## 目录结构

```
AIResearch/
├── academic-research-skills/   # 学术研究技能集（论文搜索、审稿、文献综述流水线）
├── Auto-Codex-research-in-sleep/  # 自动化研究技能（OpenAlex、Semantic Scholar、Gemini、Exa 等多源检索）
├── autoresearch/               # AI 自动化科研项目（Python ML 训练/分析）
├── Codex-scholar/             # Codex Scholar 插件（commands、hooks、skills、MCP 集成）
├── sciwrite/                   # 科学写作技能
├── skills/                     # 通用技能合集
├── openalex_api_documentation.md  # OpenAlex API 参考文档
└── requirements.txt            # Python 依赖
```

子目录分两类：
- 完整上游仓库 clone：子目录自身包含 `.git`，用于跟踪上游更新。
- 摘要索引目录：只保留本项目写的 `README.md` 总结，不 vendor 上游代码或完整 repo 内容。

## 使用方式

- 在本目录下浏览、对比各子项目的功能和实现
- 实际使用某个技能时，进入对应子目录或在目标研究项目中引用/安装
- API 密钥配置见 `.Codex/.env.example`

## Repo 管理流程

本项目的结构化索引由 `registry.yaml` 维护，展示页由根 `README.md` 维护。添加或更新 repo 时遵循以下规则。

### 添加完整上游 repo

1. 在项目根目录 clone 或添加子模块，目录名应与 `registry.yaml` 的 `local_path` 一致。
2. 在 `registry.yaml` 的 `repos:` 列表末尾新增条目，包含 `name`、`display_name`、`description`、`repo`、`local_path`、`categories`、`updated_at: ''`、`last_commit: ''`、`changelog: []`。
3. 在根 `README.md` 对应分类表格追加一行，最近更新填 `（待初始化）`。
4. 运行 `.venv\Scripts\python.exe scripts\sync.py --apply --repo <name>` 初始化 `updated_at`、`last_commit` 和 `changelog`。

### 添加只保存总结的外部 repo

当用户要求“只上传总结文档，不上传具体 repo”或不需要本地跟踪完整代码时：

1. 创建 `<local_path>/README.md`，只写来源链接、类型、摘要和使用提示。
2. 不 clone 上游 repo，不创建 `.git`，不复制上游源码、资源或大文件。
3. 在 `registry.yaml` 添加同名条目，但不手动填写 `last_commit`；`updated_at` 和 `changelog` 初始留空。
4. 在根 `README.md` 对应分类表格追加摘要行，最近更新填 `（待初始化）`。
5. 验证 `<local_path>/.git` 不存在，确认只纳入总结文档。

### 更新已有 repo

- 对完整上游仓库：先确认工作区干净，再在各子仓库执行 `git pull --ff-only`；不要用会产生 merge commit 的 pull。
- 更新索引摘要：运行 `.venv\Scripts\python.exe scripts\sync.py --apply`，或用 `--repo <name>` 更新单个条目。
- 对摘要索引目录：只更新本地 `README.md` 总结和根索引，不把完整上游 repo 拉入本项目。
- 完成前至少验证：`registry.yaml` 可解析、根 `README.md` 有对应行、摘要目录没有 `.git`。