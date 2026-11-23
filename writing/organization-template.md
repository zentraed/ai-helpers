# Paper organization: <paper short name>

Copy this file into your paper's folder (for example `my-paper/paper-organization.md`) and fill in each section. It is the blueprint for the paper: what it argues, how it is laid out, which run or dataset backs each claim, and which decisions are settled. It describes the target, not the to-do list. Keep open work in a separate issues file, and delete each section that does not apply.

The style rules live in the paper-specific file (`paper-specific-rules.md`, started from `paper-template.md`). This file says *what* the paper contains; that one says *how* it is written.

<Title, authors, affiliation, target journal.>

Last updated <YYYY-MM-DD> (synced to <main source file and compiled PDF>). Repository: <URL or "private">. Source of record for every number: <release tag and commit, data release, or dated lab record>, with results in <folder>. Shared defaults: <random seed, precision, instrument settings, or other settings every run uses>.

---

## 1. The paper in one paragraph (and framing priority)

<One paragraph: the problem, the gap in existing methods, the idea, and the main result stated with its condition. A reader who sees only this paragraph should know what the paper claims.>

The paper is structured around <N> prioritized contributions:

1. **<Contribution> (`<label>`):** <The claim, its conditions, and whether it is proved, computed, or measured.>
2. **<Contribution> (`<label>`):** <...>

Order the contributions by importance. The abstract, introduction, and discussion follow this order.

---

## 2. Settled decisions

Record each decision once it is made, so drafts and agents do not reopen it. For each one, give the decision, the reason, and the evidence or result that settled it.

- **<Topic, e.g., main bound or model choice>:** <Decision.> <Reason, with the theorem, run, or comparison that supports it.>
- **<Defaults and options>:** <Which settings are on by default and why; where the comparison is recorded.>
- **<Cost model or metric>:** <What is counted or measured, what is excluded, and where the excluded part is reported.>
- **<Labels for methods or conditions>:** <The exact name used in text, figures, and tables for each method, baseline, or experimental condition, and what each means.>
- **<Baselines>:** <Which prior methods are compared, which versions, and whether their results are rerun or reused.>
- **<Placement>:** <Which results go in the main text and which in appendices.>
- **<Bibliography>:** <Source of the .bib file, citation style, and version policy (published versus preprint).>

---

## 3. Manuscript layout

One row per section and subsection. "Backed by" names the runs (Section 4), appendices, or proofs that support the content, so every claim can be traced.

| Section | Label | Content | Backed by |
|---|---|---|---|
| **Abstract** | — | <Word count; the claims and numbers it leads with.> | <runs> |
| **1. Introduction** | `<label>` | <Motivation, prior work, contributions.> | <runs> |
| **2. <Method>** | `<label>` | <Subsections and the key results in each.> | <appendix> |
| — 2.1 <Subsection> | `<label>` | <...> | <...> |
| **<N>. Discussion** | `<label>` | <Synthesis, limitations, open questions.> | All |
| **Back matter** | — | <Code and data availability, contributions, acknowledgments.> | — |
| **Appendix A** | `<file or label>` | <...> | <...> |

---

## 4. Runs and data

List every run, experiment, or dataset that produces a number in the paper. Give each one an ID (R1, R2, ...) so the layout and figure tables can cite it.

All records come from <source of record>, with <shared defaults>, produced by <script, pipeline, or instrument and where it ran>.

- **R1. <Name> (`<table or figure labels>`).** <What is varied and over what range; what is recorded; the headline result.>
- **R2. <Name> (`<labels>`).** <...>

---

## 5. Figures and tables inventory

| ID | Label | Location | Asset / source | Backing run(s) |
|---|---|---|---|---|
| **Fig. 1** | `<label>` | <section> | <file path, and panels> | <R#> |
| **Table 1** | `<label>` | <section> | <what it shows> | <R#> |

<State what every data figure and table caption must record, e.g., the main parameters, metric, source revision, and seed.>

---

## 6. Editorial governance and maintenance

- **Style and vocabulary:** Follow the style guide: `paper-specific-rules.md` (glossary, notation, scope), which loads `general-rules.md` and `agent-workflow.md`.
- **Open work:** Track it in <issues file>, not here. Update this file when a decision is settled or the layout changes.
- **Pre-submission hygiene:** <Draft macros to remove, cross-reference checks, bibliography build check.>
- **Reproducibility archival:** <Where the code and data snapshot will be archived (e.g., a DOI repository) and when.>
