**Overview**

- **Purpose**: This repository contains small, standalone Python learning scripts and a few notebooks (Portuguese-language). Most files are procedural examples rather than a packaged application. AI edits should preserve the beginner-oriented style and Portuguese I/O prompts.
- **Key locations**: `Numberconverter.py`, `Car_game.py`, `HousePrice.py`, `Duplicates.py`, `FavColor.py`, `Name.py`; notebooks and datasets under `Alura/`, `Intensivao_Python/`, and `Levantamento Matematica/`.

**What to expect**

- Scripts are single-file, runnable with `python <file>.py` (PowerShell: `python .\Numberconverter.py`).
- Many files interact with the user via `input()` and `print()` and contain Portuguese prompts — preserve the language and messaging unless asked to internationalize.
- Notebooks (`.ipynb`) contain examples and data (`tips.csv`, `telecom_users.csv`, `enade_*.csv`) used for classroom exercises.

**Repo-specific patterns & examples**

- Simple procedural scripts: most logic lives at module level (no functions/classes). Example: `Car_game.py` runs a REPL-style loop checking `command == 'start'` / `'stop'`.
- Inline data mappings: `Numberconverter.py` uses a `digits_conv` dict to translate digits to Portuguese words — preserve the mapping style when refactoring.
- Learning/notebook assets are in subfolders: `Alura/`, `Intensivao_Python/`, `Levantamento Matematica/` — prefer non-destructive edits to notebooks and keep original datasets alongside.

**Developer workflows**

- Run a script: `python .\<script>.py` (PowerShell). Example: `python .\Numberconverter.py`.
- Open notebooks in Jupyter or VS Code Notebook view for interactive changes. Do not inline large dataset changes unless requested.
- There is no build system, tests, or packaging; avoid adding heavy infra unless the user requests it.

**Edit guidance for AI agents**

- Keep changes minimal and pedagogical: when improving code, prefer small refactors that demonstrate best practices (extract a function, add simple input validation) without changing exercise intent.
- Preserve Portuguese prompts and sample outputs by default. If converting to English, deliver a separate, clearly labeled refactor.
- When modifying notebooks, update only the relevant cells and keep original notebooks backed up (create `<name>.backup.ipynb`).
- Avoid introducing external dependencies; if needed, propose them first and add a `requirements.txt` only after user approval.

**Files to reference when making changes**

- `Numberconverter.py` — digit mapping and input/output patterns.
- `Car_game.py` — REPL loop example and simple state management.
- `Alura/`, `Intensivao_Python/`, `Levantamento Matematica/` — notebooks, datasets, and classroom scripts.

**Merging notes**

- If `.github/copilot-instructions.md` already exists, preserve existing bullets about local developer workflows and only append repository-specific notes above.

**Questions for maintainers**

- Should we keep all user-facing prompts strictly Portuguese, or allow bilingual variants?
- Are you open to adding a minimal `requirements.txt` for notebook reproducibility?

Please review this draft and tell me which parts to expand or change.
