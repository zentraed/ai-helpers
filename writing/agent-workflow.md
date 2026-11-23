# Style guide, part 3: writing-agent workflow

Instructions for writing agents. General rules are in `general-rules.md` (part 1). Each paper's vocabulary, conventions, and worked examples are in its paper-specific file (start from `paper-template.md`), which overrides the general files where they conflict.

Last updated 2026-11-23.

## 3. Writing-agent workflow

### 3.1 Two-pass editing process

Every draft or revision goes through two explicit passes rather than editing sentences in isolation:

1. **Pass 1 (Truth, notation, and citation audit):** Verify every factual claim, numerical value, theorem precondition, and citation against its recorded source (the code, the release data or result files named in the paper-specific file, and the local copies of cited works; see Section 3.4, Author workflow preferences). Flag any unverified statement rather than smoothing it over.
2. **Pass 2 (Flow, terminology, and conciseness pass):** Read the full section continuously to:
   - Smooth transitions between sentences and paragraphs (given-to-new chaining, varied sentence lengths, explicit connectives).
   - Replace every avoided or coined term using the paper's glossary.
   - Cut duplicated scope statements, table narrations, and code-level boilerplate.

### 3.2 Repository and collaboration rules

1. Agree on section structure, notation changes, and new subsections before drafting.
2. When reusing verified text from another file, copy it verbatim before applying agreed edits.
3. State each convention once, in the section the paper-specific file names, and reference it afterward.

### 3.3 Before-and-after examples

These examples are field-neutral. Each paper-specific file adds examples drawn from that paper's own text.

**Example 1: Fixing choppy flow (Discussion)**

- *Avoid (staccato, disconnected):*
  > Three limits apply. The model assumes a constant temperature. The data come from one site. The fit uses only ten years of records.
- *Prefer (connected, still concise):*
  > Three limitations bound these conclusions. First, the model assumes a constant temperature, so it does not capture seasonal effects. Second, all data come from a single site, which limits how far the trends generalize. Finally, the fit covers only ten years of records, too short to separate slow drift from decade-scale variability.

**Example 2: Explaining the method instead of narrating code (Methods)**

- *Avoid (code narration + internal names):*
  > Call `load_batch` on each file and skip it if the flag is false. Then loop over the rows and run `fix_drift` unless the value is NaN. Keep the best run by `score` and break ties by the smaller index.
- *Prefer (method + standard terms):*
  > Each measurement batch is corrected for instrument drift by subtracting a linear baseline fitted to its reference samples, and missing values are excluded. Among repeated runs we report the one with the lowest residual error.

**Example 3: Stating the status and scope of a result (Results)**

- *Avoid (hedged, scope unclear):*
  > The method appears to work well and seems to beat the baseline in most cases.
- *Prefer (status, scope, and count):*
  > Across 200 randomly drawn test instances, the method gives a lower error than the baseline in 187 of 200 cases. This is a measured result for problem sizes up to $n = 64$; we prove no bound for larger $n$.

### 3.4 Author workflow preferences (template)

Fill in for your own setup, or record your choices in Section 2.8 (Author workflow preferences) of the paper-specific file.

1. **Local copies of cited works:** `<folder holding the PDFs, and whether agents may open the reference manager's app>`.
2. **Commits and review:** `<where edits are committed, the commit-message policy (e.g., whether AI co-author lines are allowed), and who reviews and pushes>`.
