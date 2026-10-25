# Handoff: Git instructions at session closeout

Date: 2026-10-26. Collaborator: Kunwar (confirmed).

## Changes and decision

Added a lasting rule to `AGENTS.md`: when asked to finish a working session and
prepare a collaborator handoff, the assistant must also give exact Ubuntu
commands for reviewing, staging only intended files, committing, integrating
remote changes, pushing normally, and checking the result. Commands must use the
verified branch and remote, explicit file paths, and a complete quoted commit
message. Explain stopping on errors/conflicts and exiting Git's viewer with `Q`.
The assistant must not commit or push on the user's behalf.

Kunwar chose tailored instructions instead of a Git helper script. No helper was
created. This change reduces repeated requests for Git commands while retaining
file review and user control over publishing.

Created this task-specific handoff. `CLAUDE.md` still imports `AGENTS.md`.
`docs/SPEC.md`, `README.md`, and `docs/REPORT.md` are retained unchanged: there is
no new research requirement, methodology, application run command, or project
overview change. Research status and unresolved study decisions remain as recorded
in the specification and Phase 1 handoff.

## Findings and current state

The previous documentation update is committed as `af4862d`. The earlier handoff's
local-only statement is historical; at inspection, local `main` and the recorded
`origin/main` point to that commit. No fetch was performed in this closeout, so
current remote state is not independently verified.

The configured origin is `https://github.com/Kunwarveersingh/Aero-Senstivity-Maps.git`.
The index was empty at review. The supplied PDFs and their `Zone.Identifier` files
remain untracked, unchanged, and outside this commit.

## Checks and results

- Reviewed the final instruction diff and this new note for consistency and scope.
- `git diff --check`: passed for the tracked change.
- Checked whitespace in both intended files and verified the unchanged
  `CLAUDE.md` import: passed.
- Confirmed branch, remote, recent commits, and absence of existing staged changes.

Not tested: execution of commit/pull/push commands, authentication, remote conflict
resolution, or any CAD, CFD, Python, or MATLAB behaviour. This task changes only
documentation; no new application code requires testing.

## Assumptions, open questions, and next steps

Commands supplied at closeout assume the checked branch and file state have not
changed before the user runs them; the commands begin by checking status again.
If remote changes arrive, review their effect and repeat relevant checks before
pushing. Stop on errors or conflicts; never force-push.

Kunwar will review and publish the two files below in a separate Ubuntu terminal.
The collaborator can then pull the update and use the same closeout request.
No new research questions were resolved; choose the next research task together.

## Exact commit scope and preservation

- Modified: `AGENTS.md`
- Created: `docs/handoffs/2026-10-26-git-closeout-instructions.md`

No files were staged, committed, or pushed by the assistant. No temporary files
were created and no cleanup deletions were required. Preserve all unrelated files,
raw data, and local PDFs; do not add them to this documentation commit.
