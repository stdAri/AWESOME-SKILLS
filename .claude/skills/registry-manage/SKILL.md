# Awesome-SKILLs Registry 管理 Skill

管理 `d:\Project\Awesome-SKILLs` 的 repo 索引：添加、删除、初始化同步。

---

## 触发条件

用户说"添加 repo / 新增 skill / 加入某个仓库"或"删除 repo / 移除某个仓库"时，加载此 skill。

---

## 前置知识

### 两种 repo 类型

| 类型 | 特征 | sync.py 行为 |
|------|------|-------------|
| **git repo** | 有本地 clone，`registry.yaml` 无 `skill_source` 字段 | `git pull` + `git log <hash>..HEAD` 检测新提交 |
| **skill_source** | 无 git clone，只有一个远程 SKILL.md URL | 下载后 SHA-256 对比，有变化则覆盖本地文件 |

### registry.yaml entry 完整 schema

```yaml
- name: <唯一标识符，与 local_path 目录名一致>
  display_name: <展示名称>
  description: <一句话功能描述（中文，≤60字）>
  repo: https://github.com/<owner>/<repo>
  local_path: <相对于仓库根目录的路径>
  skill_source: <可选，远程 SKILL.md URL>    # 仅 skill_source 类型填写
  categories:
    - <分类标签>                               # 见下方有效标签列表
  updated_at: ''                               # sync.py 自动维护，初始留空
  last_commit: ''                              # sync.py 自动维护（git repo 类型）
  changelog: []                                # sync.py 自动维护
```

### 有效分类标签

`academic-research` · `autonomous-research` · `ml-training` · `scientific-writing` · `search` · `information-retrieval` · `rss` · `coding`

### README.md 表格行格式

```markdown
| **[<display_name>](<local_path>/)** | <description> | `<skill1>` · `<skill2>` | [<owner>/<repo>](https://github.com/<owner>/<repo>) | （待初始化） |
```

表格位于对应分类 section 下（`## 学术研究全流程` / `## AI 自动研究` / `## 科学写作` / `## 通用搜索与信息获取`）。  
若分类不存在，在末尾 `---` 分隔线前新建 section：
```markdown
## <分类名>

| Repo | 描述 | 包含 Skills | 来源 | 最近更新 |
|------|------|-------------|------|----------|
```

---

## 操作流程

### 添加 git repo

**Step 1 — 克隆**（由用户自行完成，或代为执行）
```powershell
cd d:\Project\Awesome-SKILLs
git clone <repo-url> <local_path>
# 若希望保持上游同步，也可用子模块：
# git submodule add <repo-url> <local_path>
```

**Step 2 — 收集元数据**（若用户未提供则询问）
- `display_name`：展示名称
- `description`：一句话功能描述（可从 repo README 首段提炼，≤60字中文）
- `categories`：从有效标签中选择
- 包含哪些 Skills（用于 README 表格"包含 Skills"列）

**Step 3 — 追加 registry.yaml entry**

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

**Step 4 — 追加 README.md 表格行**

在对应分类表格末尾添加一行，"最近更新"填 `（待初始化）`。

**Step 5 — 初始化同步**（写入 `last_commit` + `updated_at` + 初始 changelog）
```powershell
cd d:\Project\Awesome-SKILLs
.venv\Scripts\python.exe scripts\sync.py --apply --repo <name>
```

---

### 添加 skill_source repo（仅远程 SKILL.md，无 git clone）

**Step 1 — 验证 URL 可访问**
```powershell
curl -I <skill_source_url>
```

**Step 2 — 追加 registry.yaml entry**（无 `last_commit` 字段）
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

**Step 3 — 追加 README.md 表格行**（同上）

**Step 4 — 初始化**（首次下载 SKILL.md）
```powershell
.venv\Scripts\python.exe scripts\sync.py --apply --repo <name>
```

---

### 删除 repo

> ⚠️ 删除操作不可逆，执行前需用户确认。

**Step 1 — 从 `registry.yaml` 删除对应 entry 块**

**Step 2 — 从 `README.md` 删除对应表格行**

**Step 3 — 可选：删除本地目录**（询问用户）
```powershell
# 普通 clone：
Remove-Item -Recurse -Force d:\Project\Awesome-SKILLs\<local_path>

# git submodule：
git submodule deinit -f <local_path>
git rm <local_path>
Remove-Item -Recurse -Force .git\modules\<local_path>
```

---

## 执行原则

- 修改 `registry.yaml` 前先 `read_file` 读取当前内容，避免破坏 YAML 结构
- 修改 `README.md` 前先确认目标分类 section 存在
- `updated_at`、`last_commit`、`changelog` **不手动填写**，交由 `sync.py --apply` 自动初始化
- 操作完成后提示用户运行 `sync.py --apply --repo <name>` 验证
