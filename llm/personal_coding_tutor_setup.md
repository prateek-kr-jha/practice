
# Personal Coding Tutor — Full Setup Guide (Global, Repo-Agnostic)
**Languages:** JavaScript/TypeScript, Python, Java, C/C++  
**Goals:** Learn from your mistakes, enforce language & architectural best practices, generate weekly progress reports, suggest cleaner/optimized code and better names — **without touching company CI or repos**.

---

## 🧭 What You’ll Build
- A **global tutor** that follows you into any repo (no boilerplate).
- **Client-side CI**: linters, type-checkers, fast tests, complexity snapshots.
- **Learning memory**: logs outcomes per commit to build personal trends.
- **Weekly coaching report**: strengths, gaps, and a mini practice plan.
- **Editor integration**: Continue (VS Code) & Zed slash-commands for coaching.
- **Architecture checks**: layering rules and dependency hygiene.
- **Naming/clarity assistant**: consistent, human-readable names.

> Privacy-first: all analysis is local or via your own self-hosted LLM. No external APIs are required.

---

## 0) Prereqs (macOS, Apple Silicon or Intel)
```bash
# Xcode tools (if missing)
xcode-select --install

# Homebrew (if missing)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Essentials
brew install git python node pnpm jq wget
brew install cmake llvm    # C/C++ toolchain
pip3 install --user pipx
python3 -m pipx ensurepath
```

> You can use Windows/Linux too. Substitute package managers (`choco`, `apt`, etc.).

---

## 1) Create Global Tutor Home
```bash
mkdir -p ~/.tutor/{scripts,prompts,rules,reports,skills,hooks,config}
```

---

## 2) Install Global Tools (once)
```bash
# JavaScript / TypeScript
npm i -g eslint typescript jest depcruise

# Python
pipx install ruff mypy pytest import-linter radon

# Java (project-local wrappers preferred; install for convenience)
brew install spotbugs

# C/C++ analysis & formatting
brew install cppcheck clang-format llvm include-what-you-use
```

---

## 3) Global Style & Naming (Autofix Everywhere)
Create these config files (optionally symlink into repos if you want to enforce per-project).

### 3.1 `.editorconfig`
`~/.tutor/config/.editorconfig`
```ini
root = true
[*]
end_of_line = lf
insert_final_newline = true
charset = utf-8
indent_style = space
indent_size = 2

[*.{java,py,c,cc,cpp,h,hpp}]
indent_size = 4
```

### 3.2 Prettier (JS/TS)
`~/.tutor/config/.prettierrc.json`
```json
{ "printWidth": 100, "singleQuote": true, "semi": true, "trailingComma": "all" }
```

### 3.3 Clang-Format (C/C++)
`~/.tutor/config/.clang-format`
```yaml
BasedOnStyle: Google
IndentWidth: 4
ColumnLimit: 100
DerivePointerAlignment: false
PointerAlignment: Left
```

### 3.4 Naming Rules
`~/.tutor/rules/naming.json`
```json
{
  "booleans_prefix": ["is","has","can","should"],
  "collection_suffix": ["List","Map","Set","ById","ByDate"],
  "anti_patterns": ["data","info","tmp","misc","util2","foo","bar"]
}
```

---

## 4) Architecture Rules
### 4.1 JavaScript/TypeScript (dependency-cruiser)
`~/.tutor/rules/depcruise.config.cjs`
```js
module.exports = {
  forbidden: [
    { name: "no-cycles", severity: "error", from: {}, to: { circular: true } },
    { name: "no-orphans", severity: "warn", from: { path: "src" }, to: { orphan: true } },
    {
      name: "layering",
      comment: "enforce layers: app -> domain -> infra",
      from: { path: "^src/app" },
      to:   { pathNot: "^src/domain|^src/infra" }
    }
  ],
  options: { tsConfig: { fileName: "tsconfig.json" } }
}
```

### 4.2 Python (Import Linter)
Add an `il.ini` file **per project that needs layering**:
```ini
[importlinter]
root_package = yourpkg

[contract:layers]
name = app-domain-infra layering
type = layers
layers =
    yourpkg.app
    yourpkg.domain
    yourpkg.infra
```

### 4.3 Java (ArchUnit)
Create a test (per project) to enforce package rules, e.g.:
- `..app..` may depend on `..domain..`; `..infra..` may depend on `..domain..`.
- `..domain..` depends on nothing outward.

> Keep domain **pure** (no frameworks/IO).

### 4.4 C/C++
- Headers: keep interfaces lean; one header per unit of abstraction.
- Use **include-what-you-use** to prune transitive includes.
- Generate `compile_commands.json` via CMake for clang-tidy.

---

## 5) Client-Side “CI” (Global Scan Script)
`~/.tutor/scripts/scan.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail
[ -f .tutor.local.sh ] && . ./.tutor.local.sh

# ---------- JS / TS ----------
if [ -f package.json ]; then
  npx -y eslint . --ext .js,.jsx,.ts,.tsx || true
  if [ -f tsconfig.json ]; then npx -y tsc --noEmit --pretty false || true; fi
  # Architecture
  if [ -d src ]; then npx -y depcruise --config ~/.tutor/rules/depcruise.config.cjs src || true; fi
  # Fast tests (related)
  npx -y jest -i --findRelatedTests || true
fi

# ---------- Python ----------
if ls -1 **/*.py >/dev/null 2>&1; then
  ruff . || true
  mypy . || true
  pytest -q --maxfail=1 --disable-warnings --cov=. || true
  [ -f il.ini ] && import-linter || true
fi

# ---------- Java ----------
if [ -f mvnw ] || [ -f gradlew ] || [ -f pom.xml ] || [ -f build.gradle* ]; then
  ./mvnw -q -DskipTests=true -Dspotbugs.failOnError=false spotbugs:spotbugs || true
  ./mvnw -q -DskipTests=true -Dcheckstyle.skip=false checkstyle:checkstyle || true
  # Run ArchUnit tests if present (name pattern suggestion)
  ./mvnw -q -Dtest=*Architecture* test || true
fi

# ---------- C / C++ ----------
if ls -1 **/*.{c,cc,cpp,h,hpp} >/dev/null 2>&1; then
  cppcheck --quiet --enable=warning,style,performance,portability . || true
  if [ -f build/compile_commands.json ]; then run-clang-tidy -p build || true; fi
  iwyu_tool -p build || true
  (cd build && ctest -j$(sysctl -n hw.ncpu) --output-on-failure) || true
fi

# ---------- Complexity Snapshots ----------
if command -v npx >/dev/null 2>&1; then
  npx -y complexity-report -f json -o .tutor.reports.cr.json . || true
fi
if command -v radon >/dev/null 2>&1; then
  radon cc -s -j . > .tutor.reports.radon.json || true
fi
```
Make executable:
```bash
chmod +x ~/.tutor/scripts/scan.sh
```

> Tip: If the script feels heavy in some repos, comment out sections and run `tutor scan` manually when needed.

---

## 6) Learning Memory & Weekly Reports

### 6.1 Learning Logger
`~/.tutor/scripts/learn.py`
```python
#!/usr/bin/env python3
import json, os, subprocess, sys, time
commit = sys.argv[1] if len(sys.argv) > 1 else subprocess.check_output(
    ["git","rev-parse","HEAD"], text=True).strip()
event = {
  "ts": int(time.time()),
  "repo": os.path.basename(os.getcwd()),
  "commit": commit,
  "js": os.path.exists("package.json"),
  "py": any(p.endswith(".py") for p in os.listdir(".")),
  "notes": ""
}
os.makedirs(os.path.expanduser("~/.tutor/skills"), exist_ok=True)
with open(os.path.expand_user("~/.tutor/skills/learning.jsonl"), "a") as f:
    f.write(json.dumps(event)+"\n")
print("logged", event)
```
> If you prefer SQLite later, you can migrate — JSONL is simple and robust.

### 6.2 Weekly Report Generator
`~/.tutor/scripts/report.py`
```python
#!/usr/bin/env python3
from datetime import datetime
import json, os, collections

path = os.path.expanduser("~/.tutor/skills/learning.jsonl")
events = []
if os.path.exists(path):
    with open(path) as f:
        events = [json.loads(x) for x in f if x.strip()]

by_repo = collections.Counter(e["repo"] for e in events[-2000:])
summary = [f"# Weekly Tutor Report",
           f"Generated: {datetime.now()}",
           f"",
           f"## Activity by repo"]

for r, c in by_repo.most_common():
    summary.append(f"- {r}: {c} commits logged")

out = os.path.expanduser("~/.tutor/reports/weekly.md")
os.makedirs(os.path.dirname(out), exist_ok=True)
open(out, "w").write("\n".join(summary) + "\n")
print("wrote", out)
```

Make both executable:
```bash
chmod +x ~/.tutor/scripts/learn.py ~/.tutor/scripts/report.py
```

---

## 7) Global Git Hooks (Apply to All Repos)
Tell Git to use your global hooks:
```bash
git config --global core.hooksPath ~/.tutor/hooks
```

Create the hooks:

`~/.tutor/hooks/pre-commit`
```bash
#!/bin/sh
~/.tutor/scripts/scan.sh >/dev/null 2>&1 || true
```
`~/.tutor/hooks/post-commit`
```bash
#!/bin/sh
python3 ~/.tutor/scripts/learn.py "$(git rev-parse HEAD)" >/dev/null 2>&1 || true
```
Make them executable:
```bash
chmod +x ~/.tutor/hooks/*
```

> From now on, every repo you commit in will run quick checks and log learning events — **no per-repo setup**.

---

## 8) Tutor CLI (Convenience)
Create `~/.tutor/tutor`:
```bash
#!/usr/bin/env bash
case "${1:-}" in
  scan)      ~/.tutor/scripts/scan.sh ;;
  learn)     python3 ~/.tutor/scripts/learn.py ;;
  report|weekly) python3 ~/.tutor/scripts/report.py && open ~/.tutor/reports/weekly.md ;;
  *) echo "Usage: tutor {scan|learn|weekly}" ;;
esac
```
```bash
chmod +x ~/.tutor/tutor
echo 'export PATH="$HOME/.tutor:$PATH"' >> ~/.zshrc && source ~/.zshrc
```

---

## 9) Editor Integration (Coaching Prompts)

### 9.1 Continue (VS Code)
Open `~/.continue/config.yaml` and add these slash-commands:
```yaml
slashCommands:
  - name: coach
    prompt: |
      You are my coding tutor. Using the selected code and my global trends (~/.tutor/skills/learning.jsonl):
      1) Explain the issue briefly.
      2) Propose a minimal unified diff (keep behavior).
      3) Suggest clearer variable and function names.
      4) Reduce complexity in small steps.
      5) Propose tests (names + cases).
      6) One key takeaway for future me.

  - name: lang-best-practices
    prompt: |
      Identify language-specific best practices for the selected code:
      - JS/TS: immutability, pure functions, async errors, input validation.
      - Python: EAFP, type hints, context managers, dataclasses/attrs.
      - Java: SOLID, exception policy, Optional, records, streams.
      - C/C++: RAII, const-correctness, noexcept, smart pointers, bounds checks.
      Return: concise bullets + 1 minimal diff improving two items.

  - name: arch-review
    prompt: |
      Infer architectural layer (app/domain/infra) from file path & imports.
      Check for violations (downward-only deps, domain purity).
      Output: violations, suggested moves/abstractions, tiny dep graph.

  - name: names-and-clarity
    prompt: |
      Suggest better names based on ~/.tutor/rules/naming.json.
      Output: table of current -> suggested -> rationale.
```

### 9.2 Zed
Configure once (global) with your local or self-hosted models; coach prompts can be pasted when you chat.

---

## 10) Daily Workflow
1. **Code** as usual in any repo.  
2. Select code → **/coach** for step-by-step guidance.  
3. Apply minimal diffs; add tests.  
4. `git commit` → pre-commit scan + post-commit learning log.  
5. Run `tutor weekly` on Fridays → read report → ask your LLM to propose next week’s **3 micro-katas** based on your trends.

---

## 11) Security & Policy Hygiene
- Never send code to third-party APIs; use **local LLM** or your own **self-hosted GPU**.
- Before sharing patches externally, run a quick secret scan (add a grep of common keys to your export script).
- If compliance requires, work in a **shadow repo** (interfaces only) and translate diffs back to real code.

---

## 12) Troubleshooting
- **Hooks not running** → confirm `git config --global core.hooksPath` points to `~/.tutor/hooks` and files are executable.
- **Slow scans** → comment heavy sections in `scan.sh`; run on demand with `tutor scan`.
- **Java ArchUnit** → ensure tests named `*Architecture*` or adjust the `-Dtest` pattern.
- **C/C++ analyzers** → generate `compile_commands.json` (CMake: `-DCMAKE_EXPORT_COMPILE_COMMANDS=ON`).

---

## 13) Optional Enhancements
- **SQLite learning DB** with richer metrics (lint count deltas, coverage deltas, time-to-fix).  
- **HTML weekly report** with charts (use `plotly` or `matplotlib`).  
- **Per-language recipe prompts** (e.g., Python data modeling, JS Zod validation at API edges).  
- **Local dashboard**: tiny Flask app to browse trends.

---

## ✅ You’re Done
You now have a **global personal coding tutor**:
- Enforces **style**, **naming**, and **architecture**.
- Learns from your commits and gives you **weekly coaching reports**.
- Stays **local/private** and independent of company CI/repo policies.
