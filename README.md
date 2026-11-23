# ai-helpers

Markdown guides for doing scientific programming and writing with AI agents. Each file is written so that a person can read it and an agent can follow it directly.

## Contents

| Folder | What it holds |
| --- | --- |
| [`writing/`](writing/) | Style guides for writing scientific papers with AI writing agents: general rules for any paper, a two-pass agent editing workflow, and blank templates for a paper's own rules and organization. |
| [`orchestration/`](orchestration/) | `AGENTS.md.template`, an agent-instructions file for a Python research project (environments, commit and push rules, cluster jobs, and how to launch Agy, Codex, and Claude Code jobs), and `generate_agents.py`, which fills it in from a params file. |

## Getting started

**Writing guides**

1. Read [`writing/README.md`](writing/README.md) for how the guides fit together.
2. Copy `writing/paper-template.md` (and optionally `writing/organization-template.md`) into a folder named for your paper, and fill it in.
3. Point your writing agent at the filled-in paper file. It tells the agent which general guides to read as well.

**Agent instructions**

1. Copy `orchestration/agents.params.example` to `<name>.params` and fill in your project, paths, identity, and remotes.
2. Generate the file:

   ```bash
   python3 orchestration/generate_agents.py --params-file orchestration/<name>.params -o /path/to/repo/AGENTS.md
   ```

   The script stops if any placeholder is left without a value, and it overwrites an existing file only with `--force`.
3. Replace the examples in the sections marked `EDIT` with your project's own rules.

## Conventions

- The guides are plain Markdown and do not depend on any particular agent or editor.
- Rules marked *(house style)* are choices, not universal good practice; keep, change, or drop them in your paper file.
- Filled-in parameter files (`*.params`) are gitignored, so local paths and personal details stay out of the repository.
