# Handoff: session-start rule, confirmed names, and aero-map learning

Date: 2026-10-26. Session collaborator: Advaith (confirmed).

## Changes and decisions

- `AGENTS.md` (lasting rule, requested by Advaith): at the start of each session
  the assistant must ask the user's preferred name and wait for the answer
  before reviewing files or summarizing. It then reads SPEC, README, and
  handoffs, identifies that collaborator's previous task and the other
  collaborator's recent work, and includes the user's previous task in its
  summary. Each handoff must record the session collaborator's confirmed name.
  `CLAUDE.md` still imports `AGENTS.md`.
- Advaith confirmed their name. "Advaith" is no longer a placeholder in
  `docs/SPEC.md` and `docs/REPORT.md`. The README wording about placeholders
  was updated to match.
- `docs/SPEC.md` records Advaith's chosen research direction: a ground-up
  understanding of aero maps (components, variables, parameters, building and
  interpreting performance and sensitivity maps). Advaith has not yet confirmed
  or declined the full responsibility split that Kunwar proposed.
- Regenerated the Word report from `docs/REPORT.md` so it no longer contains
  the placeholder wording. Cover date and status were unchanged and still
  accurate.

No research scope, methodology, case count, or implementation decision changed.

## Findings

- No earlier handoff was recorded under Advaith's name; this was Advaith's
  first recorded session.
- The thesis PDFs listed in the report references (`docs/pdfs/`) are not
  present in Advaith's checkout. They were never committed. Advaith needs
  copies from Kunwar to check the literature summary.

## Learning work (chat only, not written into the report)

The assistant summarized Kunwar's earlier decisions and their stated reasons.
It then proposed a learning roadmap for aero maps:

1. What an aero map is (covered)
2. Forces, moments, and coefficients, and sign conventions
3. Aero balance and centre of pressure
4. Vehicle attitude: ride height, pitch, rake, heave
5. Ground effect
6. Sampling and case count
7. Fitting and interpolation
8. Sensitivity calculation

Using the maps for setup and lap simulation, plus the cornering variables, can
wait. Lesson 1 covered:

- drag, downforce, and pitching moment
- the force equation ½ρv²AC and why coefficients are used
- why ride height changes on track
- the definitions of aero maps and sensitivity maps

Lesson content was general textbook-level explanation, not sourced from the
theses and not a finding for our car. Advaith has not decided whether learning
notes should go into `docs/REPORT.md` §2. Nothing was added there.

## Assumptions

- The session's chat explanations are background only and must be supported by
  cited sources before going into the report.
- Remote state is unverified: no fetch was performed in this session.

## Checks and results

- `git diff --check`: passed.
- Reviewed the full diff of every changed file for consistency and scope.
- Local Markdown links in the changed files resolve.
- `CLAUDE.md` still contains `@AGENTS.md` and is unchanged.
- Word report regenerated with
  `python3 results/project-documentation/build_report.py`. The DOCX ZIP and XML
  parts parse, and the placeholder sentence is absent.

Not tested:

- opening or checking the visual layout of the Word file in Word or LibreOffice
- the commit, pull, and push commands
- the current remote state

No CAD, CFD, Python processing, or MATLAB work exists to test.

## Unresolved questions and next steps

1. Advaith: get the thesis PDFs from Kunwar.
2. Advaith: continue with Lesson 2 (forces, moments, coefficients, sign
   conventions). Decide whether to record sourced learning notes in REPORT §2.
3. Advaith: confirm or adjust the proposed responsibility split.
4. Both: the ride-height definition (reference points, units, positive
   direction, pitch/rake) is still the suggested next study-design topic.
5. Everything listed as open in SPEC remains open.

## Exact commit scope

Modified:

- `AGENTS.md`
- `README.md`
- `docs/SPEC.md`
- `docs/REPORT.md`
- `results/project-documentation/Formula_Student_Aerodynamic_Mapping_Report.docx`

Created:

- `docs/handoffs/2026-10-26-advaith-session-start-and-aeromap-learning.md`

No temporary files were created, and no cleanup was needed. No raw data or
credentials are involved.
