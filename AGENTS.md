# Project instructions

## Shared context and working preferences

- At the start of each new session, before reviewing files or summarizing, ask
  the user's preferred name and wait for the answer. An explicit introduction in
  that session satisfies this requirement. Never infer identity from workspace
  paths or account names. Confirm placeholder names before use.
- Once the name is known, read `docs/SPEC.md`, `README.md`, and the notes in
  `docs/handoffs/`. Identify that collaborator's most recent handoff and previous
  task, and the other collaborator's recent work. Review recent commits and local
  changes, summarize the current state, the user's previous task, and open
  questions, and choose the session's task with the collaborator before starting
  new work. Record the session collaborator's confirmed name at the top of each
  handoff so their previous task can be found.
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

## Session closeout and Git instructions

- When the user asks to "Finish this working session and prepare a handoff for
  my collaborator", complete the requested review and documentation updates,
  then include exact copy-and-paste Ubuntu commands for the user to commit and
  push. Do not commit or push on their behalf.
- Tailor commands to the actual repository path, verified branch, and exact
  intended files for that session. Use explicit paths in `git add`, never a
  blanket `git add .`. Exclude raw data, credentials, temporary files, and
  unrelated changes; inspect existing staged changes before giving instructions.
- Provide steps to check status and branch, stage the intended files, review the
  staged file list and diff, run `git diff --cached --check`, commit with a complete
  quoted message describing the work, integrate the intended remote branch with
  `git pull --rebase`, push normally, and verify final status and commit.
- Tell the user to run commands one at a time and stop if any command fails or
  reports conflicts. Never recommend force-pushing. If remote changes are
  integrated, identify relevant checks to rerun before pushing. Explain expected
  intentionally untracked files and how to exit Git's viewer with `Q`.
- If the branch or remote is unexpected, explain the discrepancy before providing
  push commands; do not silently switch branches or change remotes.
