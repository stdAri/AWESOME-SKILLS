# Awesome-SKILLs Registry 管理 Skill

管理 `D:\Project\Awesome-SKILLs` 的 repo 索引：添加、删除、同步和维护根 README 展示页。

---

## 触发条件

用户说“添加 repo / 新增 skill / 加入某个仓库”“删除 repo / 移除某个仓库”“更新所有 repo / 同步 registry”时，加载此 skill。

---

## 当前仓库策略

本仓库是 **索引仓库**，不是外部 skills/research repo 的源码镜像。

### GitHub 上允许提交的内容

- 根 `README.md`
- `registry.yaml`
- `requirements.txt`
- `scripts/`：本仓库维护脚本
- `.claude/skills/registry-manage/`：本仓库管理 Skill
- `.claude/.env.example`：示例配置，不含真实密钥
- `CLAUDE.md`、`AGENTS.md` 等本仓库说明文件

### GitHub 上不要提交的内容

- 外部完整上游 repo 目录，例如 `academic-research-skills/`、`Auto-claude-code-research-in-sleep/`、`SkVM/`、`openresearch/`、`skills/` 等
- 外部摘要目录，例如 `html-anything/`、`html-effectiveness/`、`openhuman/`、`ppt-master/`、`folo/`
- 任何 `.git` 子仓库、gitlink、submodule 记录
- `.claude/.env`、`.venv/`、`.omc/`、`.agents/` 等本地状态或密钥

外部 repo 可以在本地存在，用于读取、评估和同步元数据，但必须由 `.gitignore` 忽略，不能提交到外层 Git 仓库。

---

## 前置知识

### 三种索引类型

| 类型 | 特征 | sync.py 行为 | 是否提交 local_path 目录 |
|---|---|---|---|
| **本地 git clone** | `local_path/.git` 存在，`registry.yaml` 无 `skill_source` | `git pull --ff-only` + `git log <last_commit>..HEAD` 更新 `updated_at`、`last_commit`、`changelog` | 否，只提交 registry/README 更新 |
| **skill_source** | 有远程 SKILL.md URL，通常无 git clone | 下载远程 SKILL.md 并 SHA-256 对比；如本地目录被忽略，只用于本地缓存 | 否 |
| **外部索引条目** | 无本地 clone，或只想记录 repo | `sync.py` 跳过，保持 `updated_at: ''` / README `待初始化` | 否 |

### registry.yaml entry schema

```yaml
- name: <唯一标识符，通常与 local_path 一致>
  display_name: <展示名称>
  description: <一句话功能描述，中文，尽量简洁>
  repo: https://github.com/<owner>/<repo>
  local_path: <相对于仓库根目录的本地路径>
  skill_source: <可选，远程 SKILL.md URL，仅 skill_source 类型填写>
  categories:
    - <分类标签>
  updated_at: ''
  last_commit: ''
  changelog: []
```

说明：
- `updated_at`、`last_commit`、`changelog` 由 `sync.py --apply` 维护；新增条目初始留空。
- 对没有本地 clone 的外部索引条目，不要手动伪造 `last_commit`。
- `skill_source` 类型可以不写 `last_commit`。

### 有效分类标签

`academic-research` · `autonomous-research` · `ml-training` · `scientific-writing` · `search` · `information-retrieval` · `rss` · `coding`

### README.md 当前表格格式

根 README 使用“快速选型 + 分类索引”的新结构，表格列为：

```markdown
| Repo | 重点能力 | 形式 | 来源 | 最近同步 |
|---|---|---|---|---|
| **[<display_name>](<local_path>/)** | <重点能力> | <形式> | [<owner>/<repo>](https://github.com/<owner>/<repo>) | 待初始化 |
```

常用 section：

- `### 学术研究流水线`
- `### 论文阅读、推导与文献处理`
- `### 科学写作与投稿产出`
- `### 自主研究与实验系统`
- `### 搜索、信息获取与知识源`
- `### Agent 开发、运行时与行为规范`
- `### 演示、HTML 与可视化产物`
- `### 综合合集与外部索引`

README 的 `最近同步` 只放日期或 `待初始化`，不要把 changelog 塞进表格单元格。详细更新记录只保存在 `registry.yaml`。

---

## 操作流程

### 添加本地 git clone 类型 repo

用于需要长期跟踪上游更新的 repo。

**Step 1 — 本地 clone**

```powershell
cd D:\Project\Awesome-SKILLs
git clone <repo-url> <local_path>
```

不要使用 `git submodule add`。本仓库不提交外部 repo，也不维护 submodule。

**Step 2 — 确认 `.gitignore` 忽略该目录**

确认 `.gitignore` 包含：

```gitignore
<local_path>/
```

如果没有，先添加。这样外部 repo 只用于本地同步，不会出现在 GitHub 文件列表中。

**Step 3 — 收集元数据**

若用户未提供，读取上游 README 或 repo 描述提炼：

- `display_name`
- `description`
- `categories`
- README 表格中的 `重点能力`
- README 表格中的 `形式`，例如 `Skill`、`Skill 套件`、`研究协作系统`、`前端生成参考`、`外部合集`

**Step 4 — 追加 `registry.yaml` entry**

读取 `registry.yaml` 后，在 `repos:` 列表末尾追加：

```yaml
- name: <name>
  display_name: <display_name>
  description: <description>
  repo: <repo-url>
  local_path: <local_path>
  categories:
    - <category>
  updated_at: ''
  last_commit: ''
  changelog: []
```

**Step 5 — 追加根 README 表格行**

在最合适的分类 section 下追加：

```markdown
| **[<display_name>](<local_path>/)** | <重点能力> | <形式> | [<owner>/<repo>](<repo-url>) | 待初始化 |
```

如果同一 repo 适合多个分类，优先只放一个主分类；确有必要时可以在“综合合集与外部索引”等 section 重复出现，但要避免 README 过度重复。

**Step 6 — 初始化同步**

```powershell
.venv\Scripts\python.exe scripts\sync.py --apply --repo <name>
```

完成后只提交 `registry.yaml`、`README.md`、`.gitignore` 以及必要的本仓库维护文件，不提交 `<local_path>/`。

---

### 添加外部索引条目（不 clone、不创建目录）

用于只想在 Awesome-SKILLs 中记录某个 repo，但不需要本地跟踪完整代码。

**不要创建 `<local_path>/README.md`。** 旧流程中的“摘要目录”已经废弃。

**Step 1 — 收集元数据**

从用户提供信息或 GitHub README 提炼 `display_name`、`description`、`categories`、README 表格的 `重点能力` 和 `形式`。

**Step 2 — 追加 `registry.yaml` entry**

```yaml
- name: <name>
  display_name: <display_name>
  description: <description>
  repo: <repo-url>
  local_path: <local_path>
  categories:
    - <category>
  updated_at: ''
  changelog: []
```

不写 `last_commit`，除非本地确实有对应 git clone 并准备交给 `sync.py` 维护。

**Step 3 — 追加根 README 表格行**

`最近同步` 填 `待初始化`：

```markdown
| **[<display_name>](<local_path>/)** | <重点能力> | <形式> | [<owner>/<repo>](<repo-url>) | 待初始化 |
```

**Step 4 — 不运行初始化同步**

没有本地 clone 时，`sync.py` 会跳过该条目。不要为了初始化而创建空目录，否则可能被误判或污染索引。

---

### 添加 skill_source 类型 repo

用于只有远程 `SKILL.md` URL 的条目。

**Step 1 — 验证 URL 可访问**

```powershell
curl -I <skill_source_url>
```

**Step 2 — 追加 `registry.yaml` entry**

```yaml
- name: <name>
  display_name: <display_name>
  description: <description>
  repo: <官方 GitHub URL，可选>
  local_path: <local_path>
  skill_source: <remote-url>
  categories:
    - <category>
  updated_at: ''
  changelog: []
```

**Step 3 — 追加根 README 表格行**

```markdown
| **[<display_name>](<local_path>/)** | <重点能力> | <形式> | [<owner>/<repo>](<repo-url>) | 待初始化 |
```

**Step 4 — 初始化或同步**

```powershell
.venv\Scripts\python.exe scripts\sync.py --apply --repo <name>
```

注意：如果 `sync.py` 下载了 `<local_path>/SKILL.md`，该目录仍应在 `.gitignore` 中，默认不提交到 GitHub。

---

### 更新所有 repo

```powershell
.venv\Scripts\python.exe scripts\sync.py --apply
```

更新前后都要检查：

```powershell
git status --short
git diff --stat
```

期望结果：

- 可同步的本地 git clone 更新 `registry.yaml` 和 README 日期。
- 无本地 clone 的外部索引条目被 `SKIP`，保持 `待初始化`。
- 不出现新的外部目录被暂存。
- README 表格仍然只显示日期，不显示长 changelog。

---

### 删除 repo

删除索引条目和本地目录是两件事。

**Step 1 — 从 `registry.yaml` 删除对应 entry 块**

**Step 2 — 从根 `README.md` 删除对应表格行**

**Step 3 — 可选删除本地外部目录**

删除本地 clone / 缓存目录前必须确认用户意图，因为这是破坏性操作。

```powershell
Remove-Item -Recurse -Force D:\Project\Awesome-SKILLs\<local_path>
```

不要用 `git rm` 删除外部 repo 目录；正常情况下它们不应被 Git 跟踪。

---

## 执行原则

- 修改 `registry.yaml` 前先读取当前内容，避免破坏 YAML 结构。
- 修改 `README.md` 前确认目标分类 section 存在，并使用当前五列表格格式。
- 外部 repo 目录必须保持 local-only；提交前用 `git status --short --ignored` 检查。
- 若看到 `160000` mode、带箭头目录或 `adding embedded git repository` 警告，说明外部 repo 被错误提交为 gitlink，必须用 `git rm --cached <path>` 移除并加入 `.gitignore`。
- `updated_at`、`last_commit`、`changelog` 交由 `sync.py --apply` 维护，不手动伪造。
- 完成前验证 `registry.yaml` 可解析、README 行仍存在、GitHub 将只包含本仓库功能文件和根索引文件。
