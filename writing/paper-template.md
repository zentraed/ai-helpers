# Style guide, part 2: paper-specific rules (<paper short name>)

Copy this file into a folder named for your paper (for example `my-paper/paper-specific-rules.md`), fill in each section, and delete any section that does not apply.

<One sentence: the paper, the target journal, and the source files these rules apply to.>

**This file is the entry point for this paper's style guide.** Read all three parts:

1. `../general-rules.md` (part 1): general writing, flow, and rigor rules.
2. `../agent-workflow.md` (part 3): the two-pass editing workflow.
3. This file (part 2): rules for this paper. Where this file and the general files differ, this file wins. <State which *(house style)* rules from part 1 you keep, change, or drop.>

Last updated <YYYY-MM-DD>.

## 2. Paper-specific rules

### 2.1 Journal and format

1. Document class or template: <name>. Verify against the journal's current template before submission.
2. Abstract: <word limit>, containing only reproduced numbers.
3. Source of record for every number: <tagged code revision, data release, or dated lab record>.
4. Remove all draft macros (<list them>) before submission.

### 2.2 Standardized vocabulary

Follow this glossary strictly across text, appendices, tables, and figure labels. If a term is in the "Avoid" column, replace it.

| Preferred term | Avoid / retired | Definition and usage |
| --- | --- | --- |
| <term> | <synonyms, nicknames, code names> | <definition, and when to use it> |

<Add any rules about individual words that need more than a table row, such as banned words and their replacements.>

### 2.3 Notation

1. **Macros:** <shared LaTeX macros and what they stand for>.
2. **Conventions:** <ordering, indexing, normalization, units; and the section of the paper where each is stated once>.
3. **Symbols:** <each main symbol, its meaning, and where it is first defined>.

### 2.4 Scope statements

1. <The setting every main result applies to, and where the paper states it.>
2. <Any comparison that must be labeled conditional.>

### 2.5 Section plan and depth targets

1. **Where scope is stated once:** <section for conventions; section for experimental or benchmark defaults>.
2. **Depth targets by section:**
   - **Abstract:** <limit>.
   - **Section 1 (<name>):** <what it covers>.
   - **Section 2 (<name>):** <what it covers>.
   - **Appendices:** <what each appendix holds>.

### 2.6 Prose, claims, and figures for this paper

1. **Internal jargon to translate:** <code identifiers, lab shorthand, nicknames>.
2. **Scope of each result:** <the parameters every bound or measurement must state>.
3. **Figure and table records:** <the fields every data figure or table records>.

### 2.7 Before-and-after examples for writing agents

**Example 1: <what it fixes> (<section>)**

- *Avoid:*
  > <a real sentence or passage from a draft of this paper>
- *Prefer:*
  > <the rewrite>

### 2.8 Author workflow preferences

These fill in the templates in Section 1.9 (Author workflow preferences) of `../general-rules.md` and Section 3.4 (Author workflow preferences) of `../agent-workflow.md`.

1. **Bibliography:** <where the .bib file comes from, and whether agents may edit it>.
2. **Local copies of cited works:** <folder, and whether agents may open the reference manager's app>.
3. **Missing sources:** <who to tell, and what to give them>.
4. **Pass 1 sources:** <the code, data, and result files claims are checked against>.
5. **Commits and review:** <where edits are committed, commit-message policy, who reviews and pushes>.
