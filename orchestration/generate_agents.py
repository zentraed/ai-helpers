#!/usr/bin/env python3
"""Generate AGENTS.md from AGENTS.md.template by filling in project details.

Placeholders in the template look like {{NAME}}. Values come from a params
file (KEY=VALUE lines, '#' comments allowed) and/or command-line flags; flags
win. Every placeholder in the template must receive a value.

Keep filled-in params files out of git (*.params is ignored); see
agents.params.example for the full list of keys. After generating, fill in
the sections the template marks "EDIT" by hand.

Examples:
    python3 generate_agents.py --params-file my.params -o ../../my-project/AGENTS.md
    python3 generate_agents.py --params-file my.params --git-email me@example.com -o -
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

PARAMS = {
    # Project
    "PROJECT_NAME": "short project name, also used in /tmp log names (e.g. mylib)",
    "PROJECT_DIR": "main repository, relative to where agents start (e.g. ../mylib)",
    "PYTHON_VERSION": "minimum Python version (e.g. 3.12)",
    "DEV_ENV": "minimal development conda env (e.g. mylib)",
    "DEV_ENV_FILE": "its environment file (e.g. environment.yml)",
    "TEST_ENV": "test/benchmark conda env (e.g. mylib-bench)",
    "TEST_ENV_FILE": "its environment file (e.g. environment-bench.yml)",
    "TEST_PYTHON": "python in the test env (e.g. /opt/conda/envs/mylib-bench/bin/python)",
    "TEST_COMMAND": "full test command (e.g. conda run -n mylib-bench python -m pytest)",
    "MAX_CORES": "core limit for benchmarks (e.g. 4)",
    # Cluster
    "CLUSTER_JOBS_DIR": "cluster job scripts repo (e.g. ../clusterjobs/mylib)",
    "CLUSTER_NAME": "HPC cluster name (e.g. University)",
    "OWNER_NAME": "person who deletes cluster files and cuts releases (e.g. Alex)",
    # Identity and remotes
    "GIT_EMAIL": "required author/committer email (e.g. 12345+user@users.noreply.github.com)",
    "FORBIDDEN_EMAIL": "personal email that must never appear in commits",
    "PUBLIC_REPO_URL": "public 'origin' repo (e.g. github.com/user/mylib)",
    "PRIVATE_REPO_URL": "private repo (e.g. github.com/user/mylib-private)",
    # Tools
    "AGY_BIN": "agy executable (e.g. ~/.local/bin/agy)",
    "CODEX_BIN": "codex executable (e.g. /opt/homebrew/bin/codex)",
    "NPM_PREFIX": "global npm prefix (e.g. /opt/homebrew)",
}

PLACEHOLDER = re.compile(r"\{\{([A-Z0-9_]+)\}\}")


def flag(key: str) -> str:
    return "--" + key.lower().replace("_", "-")


def read_params_file(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for lineno, raw in enumerate(path.read_text().splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            sys.exit(f"{path}:{lineno}: expected KEY=VALUE, got {raw!r}")
        key, value = (s.strip() for s in line.split("=", 1))
        values[key] = value.strip("'\"")
    return values


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("-t", "--template", type=Path, default=HERE / "AGENTS.md.template")
    ap.add_argument("-o", "--output", type=Path, default=Path("AGENTS.md"),
                    help="output file ('-' for stdout; default: ./AGENTS.md)")
    ap.add_argument("--params-file", type=Path, help="KEY=VALUE file")
    ap.add_argument("--force", action="store_true", help="overwrite an existing output")
    for key, help_text in PARAMS.items():
        ap.add_argument(flag(key), dest=key, help=help_text)
    args = ap.parse_args()

    values = read_params_file(args.params_file) if args.params_file else {}
    values.update({k: getattr(args, k) for k in PARAMS if getattr(args, k) is not None})

    template = args.template.read_text()
    needed = set(PLACEHOLDER.findall(template))
    missing = sorted(needed - values.keys())
    if missing:
        sys.exit(f"missing values for: {', '.join(missing)} "
                 f"({', '.join(flag(k) for k in missing)})")
    unknown = sorted(values.keys() - needed)
    if unknown:
        print(f"warning: unused parameters: {', '.join(unknown)}", file=sys.stderr)

    result = PLACEHOLDER.sub(lambda m: values[m.group(1)], template)

    if str(args.output) == "-":
        sys.stdout.write(result)
        return
    if args.output.exists() and not args.force:
        sys.exit(f"{args.output} exists; pass --force to overwrite")
    args.output.write_text(result)
    print(f"wrote {args.output}; now fill in the EDIT sections", file=sys.stderr)


if __name__ == "__main__":
    main()
