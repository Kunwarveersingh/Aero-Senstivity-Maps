# Project instructions

## Shared context and working preferences

- Read `docs/SPEC.md` and relevant notes in `docs/handoffs/` when starting work.
  Use `README.md` for the project overview. Review recent commits and local
  changes, summarize the current state and open questions, and choose the
  session's task with the collaborator before starting new work.
- At the start of each new session, ask the user's preferred name. An explicit
  introduction in that session satisfies this requirement. Never infer identity
  from workspace paths or account names. Confirm placeholder names before use.
- Label individual research directions and handoff contributions with confirmed
  names; keep shared decisions separate. Ask about the collaborator's research
  focus and current task when setting up a new collaborator, then request other
  details only as needed.
- Both collaborators are MATLAB beginners. Explain concepts in plain language,
  introduce technical terms as needed, and explain the reasoning behind equations
  and implementation choices.
- Work through one topic at a time and keep explanations manageable.
- Distinguish what is necessary for the initial project, useful but can wait,
  and entirely optional. Discuss scope expansion before proceeding.
- Separate agreed decisions, proposals, assumptions, and unresolved questions.
  Flag conflicting requirements rather than silently replacing them.
- Do not invent missing project details or present unvalidated results as findings.
- Develop the project point by point with the collaborators. Keep current project
  status in `docs/SPEC.md` and handoffs rather than treating it as a permanent rule.
- Maintain `docs/REPORT.md` as the project's thesis-style narrative. Ask focused
  questions about missing reasoning, including decisions researched outside the
  coding assistants. Capture attribution, rationale, evidence, and decision status.
  Mark unanswered sections "To be documented"; never invent completed work.
- Do not assume that reference-only parameters change geometry or physics, that
  Python runs as a native STAR-CCM+ macro, or that the existing CFD template has
  any particular configuration. Follow the inspection requirements in `docs/SPEC.md`.

## File organization

- Keep the project root tidy. Do not create files there unless required
  by the agreed project structure.
- Put temporary scripts, debugging output, intermediate data, and draft
  figures in `work/<task-name>/`.
- Reuse existing code and documentation before creating new files.
- Do not create duplicate scripts with names such as `final_v2` or `fixed_new`.
- Never modify or delete original files in `data/raw/`.
- Put reviewed deliverables in `results/<study-name>/`.
- Before finishing, remove only disposable files you created for this task.
  Preserve anything needed to reproduce results.
- Never delete another collaborator's files or unrelated work.
- Summarize which files were created, changed, and retained.
