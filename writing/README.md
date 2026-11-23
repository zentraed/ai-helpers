# Writing guides

Style guides for writing scientific papers with the help of AI writing agents. They are written so that a person or an agent can follow them directly.

## Files

| File | Part | What it holds |
| --- | --- | --- |
| `general-rules.md` | 1 | Rules for any paper: flow, conciseness, punctuation, word choice, claims and evidence, notation, citations, figures. |
| `paper-template.md` | 2 | A blank paper-specific file: glossary, notation, scope, section plan, examples, and your own workflow. |
| `agent-workflow.md` | 3 | The two-pass editing workflow for writing agents, with field-neutral before-and-after examples. |
| `organization-template.md` | — | A blank paper-organization file: what the paper argues, settled decisions, layout, which run backs each claim, and the figure and table inventory. |

## How to use them

1. Copy `paper-template.md` into a folder named for your paper, as `<paper>/paper-specific-rules.md`, and fill it in. Optionally copy `organization-template.md` there as `<paper>/paper-organization.md`: the style file says how the paper is written, and the organization file says what it contains.
2. Point agents at that file only. It tells them to read `general-rules.md` and `agent-workflow.md` as well.
3. Keep the folder layout. The paper file finds the general files at `../general-rules.md` and `../agent-workflow.md`.

**Which file wins:** where the paper-specific file and a general file disagree, the paper-specific file wins. For example, the general rules say "within the journal's word limit" and a paper file can set "150 to 200 words".

**House style:** rules marked *(house style)* in `general-rules.md` are choices, not universal good practice (no em dashes, American spelling, `\cref`, a list of banned subjective praise words such as "powerful" and "novel"). Say in your paper file which ones you keep, change, or drop.

**Your own setup:** the "Author workflow preferences" sections of `general-rules.md` (Section 1.9) and `agent-workflow.md` (Section 3.4) are templates for where your PDFs live, how your bibliography is managed, and who reviews commits. Fill them in, or record your answers in the matching section of your paper file (Section 2.8).

## Sharing

`general-rules.md`, `agent-workflow.md`, `paper-template.md`, `organization-template.md`, and this README are meant to be shared. A filled-in paper-specific or organization file often describes unpublished work (its terminology, internal function names, and results). Check it before sharing it with anyone outside the project.
