# Project specification: Phase 1 scope and open proposals

## Status and purpose

Initial literature review and scope discussions have begun. Detailed study design
remains open; no project implementation or simulation results are established here.
This document separates agreed requirements from proposals. The two collaborators
will develop the project one topic at a time and agree on the detailed workflow
and timeline together.

This university project for Strohm und Söhne e.V. Noris Racing at Technische
Hochschule Nürnberg Georg Simon Ohm will develop MATLAB code to generate aerodynamic
performance and sensitivity maps for an FSAE car using STAR-CCM+ CFD results.
The shared GitHub repository will hold code, methodology, research decisions,
validation evidence, and progress notes so either collaborator can understand
and continue the other's work. They use Codex and Claude Code with shared
instructions in `AGENTS.md`.

## Agreed initial scope

- Phase 1 is a straight-line proof of concept with front and rear ride height as
  the only varied inputs. Demonstrate the CFD → CSV → MATLAB workflow and assess
  its efficiency before adding complexity. Other operating settings are not
  additional swept variables; their values remain to be agreed.
- Keep the simulation count as low as reasonably possible while retaining
  enough evidence to support conclusions. No simulation count is selected.
- Consider cornering-related conditions later; they are outside the initial scope.
- Distinguish necessary initial work, useful work that can wait, and entirely
  optional work as each stage is discussed. Discuss scope changes before adoption.

## Proposed responsibilities and development sequence

The earlier intended sequence was theory → CAD → simulation. Kunwar now proposes
preparing CAD alongside theoretical research because he expects CAD preparation
to take longer. This revision and the responsibility split remain proposals for
discussion with the collaborator; neither is a finalized workflow.

| Collaborator | Proposed focus | Identity status |
|---|---|---|
| Kunwar | CAD preparation/editing, CFD setup and simulations, Python automation/data processing | Confirmed name |
| Collaborator | Theory, evidence requirements, simulation counts, variables and values | Advaith is a placeholder; ask for confirmation |
| Both | Learn and develop MATLAB code together | Shared intention |

The expectation is that research will identify suitable values by the time CAD
is ready; this is not a deadline. The proposed case-generation approach is to
manually adjust front/rear ride heights, export and save a separate STEP (`.stp`)
geometry per selected combination, and import and simulate cases one by one.

Around the simulation phase, develop export/data-processing automation and
initial MATLAB code in parallel with the CFD work. Improve the MATLAB code as
simulation results become available.

This is the intended sequence, not a finalized workflow or timeline.

## Simulation-count proposals — no justification selected

| Proposal | All front/rear combinations |
|---|---|
| 3 front values × 3 rear values | 9 |
| 5 front values × 5 rear values | 25 |

These are discussion options without supporting reasoning yet, not agreed case
counts. They assume every front/rear combination is included and exclude any
additional validation or repeat simulations. Actual heights, ranges, selection
criteria, and total simulation effort remain undecided. Thesis case counts are
not evidence that either option is sufficient for this car.

## Intended tool roles and data exchange

- **STAR-CCM+:** perform CFD simulations and provide aerodynamic results and
  relevant case information.
- **Python:** support export automation and data processing. The supported
  automation mechanism must be confirmed for the team's STAR-CCM+ version;
  native Python macro support is not assumed.
- **CSV:** connect STAR-CCM+ results to MATLAB, carrying relevant case parameters
  and aerodynamic results. The detailed schema remains undecided.
- **MATLAB:** generate aerodynamic performance and sensitivity maps, with code
  refined as results become available. Numerical methods remain undecided.

## Manual geometry changes and parameter meaning

Initially, geometry will be changed manually in CAD, updated in STAR-CCM+, and
any required simulation-driving STAR-CCM+ parameters updated manually. The earlier
intention to also enter reference values manually is now under review: Kunwar
wants to avoid duplicating ride-height metadata where it has no simulation role.

**Simulation-driving parameters** control the simulation through their actual
connections to the model or physics. Those connections must be inspected.

**Reference-only parameters** record information describing a case for export
and subsequent MATLAB use. Changing them does not imply a change to geometry,
physics, or the simulated case. Keep this distinction explicit in documentation
and eventual data exports; classify actual parameters after inspecting the template.

Options under discussion are ride heights encoded in simulation filenames or a
companion text/CSV file. The assistant proposed an authoritative case-information
CSV read by Python and joined with exported results; this is not selected.
Descriptive filenames could be a convenience, but neither a metadata file nor a
filename changes or verifies geometry or replaces a simulation-driving parameter.
Naming, units, case matching, and the schema remain undecided.

## Inspection required before implementation

At the simulation stage, the collaborators will provide their existing
STAR-CCM+ template for joint inspection before deciding whether it needs changes.
Its current configuration is unknown and must not be assumed.

Inspect the installed STAR-CCM+ version and supported automation mechanism
before implementing automation. Python automation is intended, but its exact
integration with STAR-CCM+ is unresolved.

## Decisions still open

The detailed workflow and timeline, parameter definitions and ranges, simulation
count and case selection, output definitions, CSV schema, numerical methods,
validation criteria, software versions and dependencies, template changes, and
automation mechanism remain undecided. No equations, simulation matrix, or
implementation choices are established by these discussions. Confirm the
collaborator's identity, proposed responsibilities, and parallel preparation
approach before treating them as shared commitments.

The README retains earlier candidate variables, outputs, validation ideas, and
milestones as proposals for future discussion. They are not additional agreed
research requirements or authorization to expand the initial scope.

## Project narrative and evidence

Maintain [the project report](REPORT.md) for future team members. Explain both
what was done and why, including CAD constraints, simplifications, case selection,
and decisions researched outside Codex or Claude Code. Ask focused questions as
each topic is reached; record contributor, rationale, sources/evidence, and status.
Unanswered sections remain "To be documented". Literature findings, proposed
methods, and validated results for this car must remain distinct.

Kunwar requested a Microsoft Word report with a simple academic layout for
potential professional sharing. Its title is general to the whole project:
"Aerodynamic Performance and Sensitivity Mapping for a Formula Student Car";
the cover must not be tied to the current Phase 1 task. Keep its working-report
status explicit while research and results remain incomplete.

The current documentation workflow uses `docs/REPORT.md` as the source and
`results/project-documentation/build_report.py` to generate
`results/project-documentation/Formula_Student_Aerodynamic_Mapping_Report.docx`.
The generator uses Python's standard library and supports the report's current
Markdown structure; it is not a general Markdown converter. Regeneration replaces
the Word copy, so preserve substantive edits in the Markdown source. Review the
cover date/status in the generator and check the rendered layout before sharing.
This documentation addition does not change the research scope or establish a
CFD, data-processing, or MATLAB implementation.
