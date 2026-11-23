# Style guide, part 1: rules for the whole paper

General writing, flow, conciseness, and rigor rules for any scientific paper. Each paper keeps its own vocabulary, notation, scope, section plan, and worked examples in a paper-specific file (start from `paper-template.md`). The paper-specific file overrides this one where they conflict. The writing-agent workflow is in `agent-workflow.md` (part 3).

Rules marked *(house style)* are choices rather than universal good practice. Keep, change, or drop them in your paper-specific file.

Last updated 2026-11-23.

## 1. Rules for the whole paper

### 1.1 Flow, structure, and paragraphs

1. **Clear paragraph arcs:** Open each paragraph with a topic sentence that states its main point. Consecutive paragraphs should build a clear narrative progression, with explicit logical links between them rather than isolated blocks of facts.
2. **Given-to-new chaining:** Place familiar or already-introduced information near the start of a sentence and new information at the end. Avoid resetting the grammatical subject abruptly from one sentence to the next.
3. **Vary sentence length and connect related ideas:** Do not write long runs of uniform, short declarative sentences. Combine closely linked ideas (especially a claim and its immediate condition, cause, or contrast) using clear subordination (`because`, `although`, `while`, `whereas`, `when`, `since`, `so that`). Reserve short sentences for topic sentences, emphasis, and key takeaways.
4. **Use explicit transitions:** Signal logical relationships with plain connectives (`however`, `therefore`, `consequently`, `in contrast`, `similarly`, `for this reason`) instead of stacking bare assertions like an unbulleted list.
5. **Fix unclear passages by restructuring, not padding:** When a passage is unclear, identify the root cause (buried logic, missing motivation, or jargon) and rewrite it cleanly. Never bolt on extra explanatory sentences when a tighter rewrite will solve the problem.
6. **Define terms positively:** Define a concept by what it is, at its first appearance, rather than by what it is not.

### 1.2 Conciseness and section length

1. **State global scope once:** Establish paper-wide conventions and scope once at the start of the relevant section (for example, conventions in the methods section and benchmark defaults in the results section). Restate scope only in standalone locations (abstract, formal theorems, captions) or where a specific result deviates from the default.
2. **Explain mathematics and methods, not source code or lab logistics:** Never transcribe code control flow line by line into prose. Omit software boilerplate such as input type validation, Boolean checks, environment-variable parsing, exception classes, tie-breaking minutiae, and internal helper names. Those details belong in repository documentation, docstrings, or protocols, not in a journal paper.
3. **Choose the right medium:** Present multi-step procedures as compact numbered algorithms or pseudocode, group numerical tolerances and constants into summary tables, and let figures and tables carry raw numbers. Prose should state the mechanism, trend, or comparison rather than reading tables aloud row by row.
4. **Depth targets by section:** Each paper fixes its section plan and depth targets in its paper-specific file. In general:
   - **Abstract:** Within the journal's word limit, containing only reproduced numbers.
   - **Introduction:** Motivation, concise literature positioning, and a brief summary of contributions. Avoid repeating detailed method mechanics.
   - **Method:** Conceptual and mathematical core: what the method does and why it works. Keep low-level heuristics and tolerance tables in an appendix.
   - **Results:** Focus prose on trends, key head-to-head takeaways, and regimes of validity. Put exhaustive parameter sweeps and per-instance breakdowns in appendices.
   - **Discussion:** Synthesis of main findings, explicit limitations, trade-offs, and open questions. Do not re-summarize every section.
   - **Appendices:** Clean, self-contained proofs without repeating main-text intuition; compact algorithm specifications and tolerance tables (no code-to-prose narration); experimental protocols, reproducibility instructions, and extended data tables.
5. **Tightening pass:** Before finalizing any section, check whether (a) consecutive choppy sentences can merge into one smooth sentence, (b) a paragraph merely duplicates a table or an earlier section, or (c) an implementation detail can be cut without hurting rigor or reproducibility.

### 1.3 Punctuation and mechanics

1. **Dashes and colons** *(house style)*: No em dashes. Avoid colons in the middle of a sentence; a colon may introduce a displayed equation, list, or formal definition. Use semicolons sparingly (only to join two tightly coupled independent clauses or separate complex list items), relying primarily on commas with conjunctions and subordinate clauses for smooth syntax.
2. **Spelling** *(house style)*: American English (color, behavior, toward, program, catalog, afterward, modeling).
3. **Author citations:** Cite a single author by surname ("Smith") and a group as "Smith et al." In LaTeX, write `et al.\ ` when the sentence continues, and avoid ending a sentence on "et al." so no double period appears.
4. **Cross-references** *(house style, LaTeX)*: Use `\cref` and `\Cref` for every internal reference.
5. **Links** *(house style)*: No `\href` or raw DOI links in body text; DOIs belong in the bibliography.

### 1.4 Word choice and anti-jargon rules

1. **No hedging:** Avoid "may suggest", "appears to", "somewhat", and "arguably". State the result together with its condition.
2. **No subjective praise words** *(house style word list)*: Avoid "powerful", "elegant", "straightforward", "hallmark", "remarkable", "striking", and "novel".
3. **Standard terminology only:** Use the established terms of the field (see the paper's glossary). Never invent metaphors, codebase nicknames, or AI-coined labels.
4. **Never leak internal jargon into prose:** Translate codebase identifiers, lab shorthand, and nicknames into standard scientific English. The paper-specific file lists the terms to translate.
5. **One concept, one name:** Use the same term consistently across text, equations, captions, and figure axes. Do not introduce a new label for a concept used only once.
6. **Unpack noun stacks:** Replace dense modifier chains with clear prepositional phrases (for example, "sample-batch drift correction factor" becomes "the factor that corrects drift between sample batches").

### 1.5 Claims and evidence

1. **Sentence-level accuracy:** Every sentence must be factually true as written.
2. **Explicit status of results:** Clearly distinguish what is proved, what is computed or measured, and what is fitted. A result proved under stated assumptions and a result measured over a sample of instances are different kinds of statements and must be worded accordingly.
3. **Unambiguous scope:** Ensure the reader knows the setting and parameter range of every bound, measurement, or benchmark (stated once for a section or table, and repeated only in standalone statements or exceptions).
4. **Numerical checks:** Name the method and tolerances needed for reproducibility, omitting incidental implementation minutiae.
5. **Counts:** Report success or comparison counts as "$k$ of $N$".
6. **Prior work:** Verify every claim about prior work against the original paper. State what each method achieves and its assumptions before noting its limitations.
7. **Bounds vs. fits:** Call a computed upper bound an upper bound. Call a fitted trend a fit and report its domain.
8. **No unproved thresholds:** Do not claim a mathematical threshold in any parameter without a theorem; report empirical transitions as observed behavior.
9. **Reproduced numbers only:** Do not cite historical or unverified values. Every reported number must come from a recorded source (a tagged code revision, a data release, or a dated lab record) named in the paper-specific file.
10. **Verified claims only:** State novelty only where supported by the literature comparison, and state journal requirements only after checking the target journal's current policy.

### 1.6 Notation

1. Define every symbol where it first appears. In LaTeX, keep shared macros in the preamble.
2. State each convention (ordering, indexing, normalization, units) once and reference it afterward.

### 1.7 Citations

1. Cite the peer-reviewed published version by DOI; cite a preprint only when no published version exists.
2. Keep a local copy of every cited work and check claims against it (Section 1.9, Author workflow preferences, says where the copies live). Never invent a DOI.
3. Cite both the paper that originated a result and the specific source of any quoted number or statement.

### 1.8 Figures, tables, and captions

1. The main text states the finding or trend shown by a figure or table; it does not narrate the figure or recite table entries row by row.
2. Every caption defines all symbols, colors, markers, and abbreviations it uses, and must be understandable without the surrounding text.
3. Axis labels, legends, and table headers must use the exact standardized terms from the paper's glossary.
4. Tables and displayed equations do not substitute for explanatory paragraphs.
5. Every data figure or table records what is needed to reproduce it (the source revision or dataset, and any random seed or instrument settings) in the caption or table notes.

### 1.9 Author workflow preferences (template)

Fill in for your own setup, or record your choices in Section 2.8 (Author workflow preferences) of the paper-specific file.

1. **Bibliography source:** `<where the .bib file comes from, e.g., synced from a reference manager>`. State whether agents may edit it by hand.
2. **Local copies of cited works:** `<folder holding the PDFs>`. State whether agents may use the reference manager's app or must read the folder directly.
3. **Missing sources:** `<who to tell, and what to give them, e.g., the plaintext DOI>`.
