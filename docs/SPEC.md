# Project specification: agreed introduction

## Status and purpose

This document records the agreed project introduction, not a detailed plan.
Detailed planning and implementation have not started. The two collaborators
will develop the project one topic at a time and agree on the detailed workflow
and timeline together.

This university project will develop MATLAB code to generate aerodynamic
performance and sensitivity maps for an FSAE car using STAR-CCM+ CFD results.
The shared GitHub repository will hold code, methodology, research decisions,
validation evidence, and progress notes so either collaborator can understand
and continue the other's work. They use Codex and Claude Code with shared
instructions in `AGENTS.md`.

## Agreed initial scope

- Start with straight-line operating conditions, particularly front and rear
  ride-height effects.
- Keep the simulation count as low as reasonably possible while retaining
  enough evidence to support conclusions. No simulation count is selected.
- Consider cornering-related conditions later; they are outside the initial scope.
- Distinguish necessary initial work, useful work that can wait, and entirely
  optional work as each stage is discussed. Discuss scope changes before adoption.

## Intended development sequence

Understand the theory first, then prepare the CAD, then begin simulations.
Around the simulation phase, develop export/data-processing automation and
initial MATLAB code in parallel with the CFD work. Improve the MATLAB code as
simulation results become available.

This is the intended sequence, not a finalized workflow or timeline.

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
the corresponding STAR-CCM+ parameters updated manually.

**Simulation-driving parameters** control the simulation through their actual
connections to the model or physics. Those connections must be inspected.

**Reference-only parameters** record information describing a case for export
and subsequent MATLAB use. Changing them does not imply a change to geometry,
physics, or the simulated case. Keep this distinction explicit in documentation
and eventual data exports; classify actual parameters after inspecting the template.

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
implementation choices are established by this introduction.

The README retains earlier candidate variables, outputs, validation ideas, and
milestones as proposals for future discussion. They are not additional agreed
research requirements or authorization to expand the initial scope.
