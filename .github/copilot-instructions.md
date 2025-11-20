<!-- Auto-generated guidance for AI coding agents working on this repo. -->

# Copilot / AI Agent Instructions — ML_PROJECT

Summary
- This repository is currently a minimal ML project skeleton. Root files: `README.md`, `requirements.txt`, `setup.py`. A `venv/` directory exists. Implementation code, tests, and CI configuration are not present in this commit.

Quick Start (what an agent should do first)
- Read `README.md`, `requirements.txt`, and `setup.py` to confirm assumptions; both `requirements.txt` and `setup.py` are empty today.
- Check for a `venv/` directory. On Windows PowerShell, activate if present:

  ```powershell
  .\venv\Scripts\Activate.ps1
  python -m pip install --upgrade pip
  python -m pip install -r requirements.txt
  ```

- If `requirements.txt` is empty, ask the repository owner before adding or installing packages.

Repository-specific patterns and constraints
- No `src/` or package directory detected — expect code to be added at project root or under a new package directory. Do not move files without explicit approval.
- No `tests/` directory present. If adding tests, use `pytest` and place tests under `tests/`.
- `venv/` is present in the repo. Avoid editing or replacing it unless instructed; prefer creating local virtual environments instead of committing venv contents.

Developer workflows (discoverable)
- Packaging: `setup.py` exists but is currently empty. If you add packaging metadata, use `pip install -e .` or `python setup.py develop` for local installs.
- Testing and CI: No CI configuration found. When adding CI, reference standard GitHub Actions in `.github/workflows/`.

When editing or adding files
- Preserve the minimal README and note any changes in it when they affect usage.
- When adding dependencies, update `requirements.txt` and include an explanation in `README.md`.
- Keep changes minimal and easy to review; this repo appears to be an initial skeleton and the maintainer likely expects incremental additions.

Where to look next (examples)
- `README.md` — current project summary (one line).
- `requirements.txt` — dependency manifest (currently empty).
- `setup.py` — packaging entry (currently empty).
- `venv/` — committed virtual environment; treat cautiously.

Merge guidance
- If `.github/copilot-instructions.md` already exists, preserve any maintainer-written notes and merge new, repo-discoverable facts only. Do not overwrite non-empty sections without a clear rationale.

If something is missing
- This repo lacks implementation, tests, and CI; before making large design changes (adding package layout, adding heavy dependencies), ask the repo owner for intent and preferred structure.

Questions for maintainers (agents should surface these as PR questions)
- Should `venv/` be removed from source control and added to `.gitignore`?
- Do you prefer a `src/` layout for packages or top-level modules?
- Are there target Python versions or deployment targets we should follow?

— End of auto-generated guidance —
