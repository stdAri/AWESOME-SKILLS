#!/usr/bin/env python3
"""
同步各 repo 的最新状态，更新 registry.yaml 和 README.md

两种 repo 类型：
  - git repo   : 通过 git log 获取新提交，追加到 changelog 列表
  - skill_source: 通过 HTTP 下载对比 SHA-256，有变化则更新本地 SKILL.md 并追加 changelog

用法:
    python scripts/sync.py               # 默认仅预览，不修改任何文件
    python scripts/sync.py --apply        # 实际写入 registry.yaml / README.md
    python scripts/sync.py --repo folo    # 只同步指定 repo（仍默认预览）
    python scripts/sync.py --apply --repo folo
"""

import argparse
import hashlib
import re
import subprocess
from datetime import date
from pathlib import Path

import requests
from ruamel.yaml import YAML

# ── 路径 ─────────────────────────────────────────────────────────────────────
REPO_ROOT = Path(__file__).parent.parent
REGISTRY  = REPO_ROOT / "registry.yaml"
README    = REPO_ROOT / "README.md"

yaml = YAML()
yaml.preserve_quotes = True
yaml.width = 4096  # 避免长字符串被折行


# ── YAML 读写（ruamel 保留注释和格式） ────────────────────────────────────────
def load_registry(path: Path):
    with path.open(encoding="utf-8") as f:
        return yaml.load(f)


def save_registry(doc, path: Path) -> None:
    with path.open("w", encoding="utf-8") as f:
        yaml.dump(doc, f)


# ── Git 工具 ─────────────────────────────────────────────────────────────────
def _git(repo_path: Path, *args: str) -> list[str]:
    result = subprocess.run(
        ["git", "-C", str(repo_path)] + list(args),
        capture_output=True, text=True, encoding="utf-8", errors="replace"
    )
    if result.returncode != 0:
        return []
    return [l for l in result.stdout.splitlines() if l.strip()]


def get_latest_date(repo_path: Path) -> str | None:
    lines = _git(repo_path, "log", "-1", "--format=%ci")
    return lines[0].split()[0] if lines else None  # YYYY-MM-DD


def get_head_hash(repo_path: Path) -> str | None:
    """返回当前 HEAD 的完整 40 字符 hash，失败返回 None。"""
    lines = _git(repo_path, "rev-parse", "HEAD")
    return lines[0].strip() if lines else None


def get_new_commits(repo_path: Path, since: str) -> list[str]:
    """获取新提交 subject 列表。

    since 可以是：
      - 40 字符 git commit hash：使用 `git log <hash>..HEAD`（精确，无重复）
      - YYYY-MM-DD 日期字符串：使用 `--after=<date>`（兼容旧数据）
    """
    if re.match(r'^[0-9a-f]{40}$', since):
        lines = _git(repo_path, "log", f"{since}..HEAD", "--format=%s")
    else:
        lines = _git(repo_path, "log", f"--after={since}", "--format=%s")
    return [
        l for l in lines
        if not re.match(r"^Merge (pull request|branch)", l)
    ]


# ── skill_source 工具 ─────────────────────────────────────────────────────────
def fetch_url(url: str) -> bytes | None:
    try:
        r = requests.get(url, timeout=20)
        r.raise_for_status()
        return r.content
    except Exception as e:
        print(f"    [WARN] 拉取失败: {e}")
        return None


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def get_local_hash(skill_md: Path) -> str | None:
    if not skill_md.exists():
        return None
    return sha256(skill_md.read_bytes())


# ── changelog 条目追加（newest-first） ────────────────────────────────────────
def prepend_changelog(entry: dict, new_date: str, summary: str) -> None:
    """在 entry['changelog'] 列表头部插入新记录，并更新 updated_at（写入字符串）。"""
    from ruamel.yaml.comments import CommentedSeq
    if "changelog" not in entry or entry["changelog"] is None:
        entry["changelog"] = CommentedSeq()
    entry["changelog"].insert(0, f"{new_date}  {summary}")
    entry["updated_at"] = new_date  # ruamel.yaml 接受字符串，不会再转 date


# ── README.md 更新（替换表格行中的日期·描述字段，分条 <br>· 格式） ───────────
def update_readme_entry(readme_text: str, local_path: str,
                        new_date: str, new_summary: str) -> str:
    escaped = re.escape(local_path)
    # 兼容旧格式（「date · summary」）、新格式（「date<br>· item」）及初始化占位符（「待初始化」）
    pattern = re.compile(
        rf"(\*\*\[[^\]]+\]\({escaped}[^)]*\)\*\*[^\r\n]*\|\s*)"
        rf"(?:\d{{4}}-\d{{2}}-\d{{2}}[^|\r\n]+|（待初始化）)"
        rf"(\s*\|)"
    )
    items = [s.strip() for s in new_summary.split("；") if s.strip()]
    cell = new_date + "".join(f"<br>· {item}" for item in items)
    return pattern.sub(rf"\g<1>{cell}\g<2>", readme_text)


# ── 处理 git repo ──────────────────────────────────────────────────────────────
def sync_git_repo(entry: dict, local_path: Path, dry_run: bool) -> str | None:
    """先 git pull，再对比新提交，返回 summary 字符串（有更新时）或 None。"""
    # 1. 拉取上游
    pull = subprocess.run(
        ["git", "-C", str(local_path), "pull", "--ff-only", "--quiet"],
        capture_output=True, text=True
    )
    if pull.returncode != 0:
        # 非致命：可能是 detached HEAD 或无远程，打印警告后继续读本地 log
        print(f"    [WARN] {entry['name']} git pull 失败: {pull.stderr.strip()}")

    latest_date = get_latest_date(local_path)
    if not latest_date:
        print(f"  [SKIP] {entry['name']} — 无法读取 git log")
        return None

    # 优先用 last_commit hash 精确对比；无 hash 时回退到 updated_at 日期（兼容旧数据）
    last_commit = entry.get("last_commit") or ""
    since = last_commit if last_commit else (str(entry.get("updated_at", "")) if entry.get("updated_at") else "")
    head_hash = get_head_hash(local_path)

    # ── 初始化：since 为空说明是新加入的 repo ────────────────────────────────
    if not since:
        recent = _git(local_path, "log", "--format=%s", "-10")
        recent = [
            l for l in recent
            if not re.match(r"^Merge (pull request|branch)", l)
        ]
        summary = "；".join(recent[:5]) if recent else "初始收录"
        if len(recent) > 5:
            summary += f"；…（共 {len(recent)} 条）"
        print(f"\n  [INIT ] {entry['name']}")
        print(f"    updated_at : (新建)  →  {latest_date}")
        print(f"    commits    : {summary}")
        if not dry_run:
            prepend_changelog(entry, latest_date, summary)
            if head_hash:
                entry["last_commit"] = head_hash
        return summary
    # ────────────────────────────────────────────────────────────────────────

    new_commits = get_new_commits(local_path, since)

    if not new_commits:
        print(f"  [OK  ] {entry['name']} — 无新提交（最后：{latest_date}）")
        return None

    summary = "；".join(new_commits[:5]) if new_commits else "(date bump)"
    if len(new_commits) > 5:
        summary += f"；…（共 {len(new_commits)} 条）"
    print(f"\n  [UPDATE] {entry['name']}")
    print(f"    updated_at : {since}  →  {latest_date}")
    print(f"    commits    : {summary}")

    if not dry_run:
        prepend_changelog(entry, latest_date, summary)
        if head_hash:
            entry["last_commit"] = head_hash  # 记录 HEAD hash，下次精确对比

    return summary


# ── 处理 skill_source repo ────────────────────────────────────────────────────
def sync_skill_source(entry: dict, local_path: Path, dry_run: bool) -> str | None:
    """下载远程 SKILL.md，SHA-256 对比后决定是否更新。返回 summary 或 None。"""
    url = entry.get("skill_source", "")
    if not url:
        return None

    # 假设本地 SKILL.md 在 local_path/SKILL.md
    skill_md = local_path / "SKILL.md"
    remote_bytes = fetch_url(url)
    if remote_bytes is None:
        return None

    remote_hash = sha256(remote_bytes)
    local_hash  = get_local_hash(skill_md)

    if remote_hash == local_hash:
        print(f"  [OK  ] {entry['name']} — skill_source 无变化")
        return None

    today = date.today().strftime("%Y-%m-%d")
    summary = f"skill_source 内容更新（{url}）"
    print(f"\n  [UPDATE] {entry['name']}")
    print(f"    skill_source: {url}")
    print(f"    hash: {(local_hash or 'none')[:12]}  →  {remote_hash[:12]}")

    if not dry_run:
        local_path.mkdir(parents=True, exist_ok=True)
        skill_md.write_bytes(remote_bytes)
        prepend_changelog(entry, today, summary)

    return summary


# ── 主逻辑 ────────────────────────────────────────────────────────────────────
def main() -> None:
    parser = argparse.ArgumentParser(
        description="同步 registry.yaml 和 README.md（默认仅预览，加 --apply 才写文件）")
    parser.add_argument("--apply", action="store_true", help="实际写入文件（默认仅预览）")
    parser.add_argument("--repo", metavar="NAME", help="只同步指定 repo")
    args = parser.parse_args()
    dry_run = not args.apply

    today = date.today().strftime("%Y-%m-%d")
    doc   = load_registry(REGISTRY)
    readme_text = README.read_text(encoding="utf-8")
    any_changed = False

    for entry in doc["repos"]:
        name = entry["name"]
        if args.repo and name != args.repo:
            continue

        local_path = REPO_ROOT / entry["local_path"]

        # 判断类型：有 skill_source 且无 git repo → skill_source 模式
        has_skill_source = bool(entry.get("skill_source"))
        has_git = local_path.exists() and bool(get_latest_date(local_path))

        if has_skill_source and not has_git:
            summary = sync_skill_source(entry, local_path, dry_run)
        elif has_git:
            summary = sync_git_repo(entry, local_path, dry_run)
        else:
            print(f"  [SKIP] {name} — 路径不存在: {entry['local_path']}")
            continue

        if summary and not dry_run:
            new_date = entry.get("updated_at", today)
            readme_text = update_readme_entry(
                readme_text, entry["local_path"], new_date, summary
            )
            any_changed = True

    if not dry_run and any_changed:
        readme_text = re.sub(
            r"\*最后更新：\d{4}-\d{2}-\d{2}\*",
            f"*最后更新：{today}*",
            readme_text,
        )
        save_registry(doc, REGISTRY)
        README.write_text(readme_text, encoding="utf-8")
        print(f"\nregistry.yaml 和 README.md 已更新（日期：{today}）")
    elif dry_run:
        print("\n[DryRun] 预览完成，使用 --apply 写入文件")
    else:
        print("\n所有 repo 均已是最新，无需修改")


if __name__ == "__main__":
    main()
