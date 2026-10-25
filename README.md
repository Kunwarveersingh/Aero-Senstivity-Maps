# FSAE Aerodynamic Sensitivity Mapping

A collaborative university project developing **MATLAB** code to generate aerodynamic performance and sensitivity maps for a Formula SAE car using **STAR-CCM+** CFD results, with **Python** for export automation and data processing and **CSV** files connecting the results to MATLAB.

The project investigates how vehicle attitude and setup affect downforce, drag, and aerodynamic balance.

> Status: Project introduction agreed. Detailed planning and implementation have not started. See [docs/SPEC.md](docs/SPEC.md) for the agreed scope and unresolved questions.

## Agreed Introduction

Start with straight-line operating conditions, particularly front and rear ride-height effects. Keep the simulation count as low as reasonably possible while retaining enough evidence to support conclusions. Cornering-related conditions will be considered later.

The intended sequence is **theory → CAD → simulation**. Around the simulation phase, develop export/data-processing automation and initial MATLAB code in parallel with CFD work, improving MATLAB code as results become available. This sequence is not a finalized workflow or timeline.

Initially, geometry changes in CAD, geometry updates in STAR-CCM+, and corresponding STAR-CCM+ parameter updates will be manual. Distinguish **simulation-driving parameters**, which control the simulation through actual model connections, from **reference-only parameters**, which describe a case for export and MATLAB. Changing a reference-only parameter does not imply a change to geometry or physics.

Inspect the existing STAR-CCM+ template together before deciding on changes. Confirm the supported automation mechanism for the team's STAR-CCM+ version before implementation: Python automation is intended, but native Python macro support is not assumed. CSV exports should contain relevant case parameters and aerodynamic results; the schema remains undecided.

The sections below retain earlier objectives and technical ideas for discussion. Candidate variables beyond the initial scope, output lists, validation details, workflow steps, and milestones are **proposals**, not agreed research decisions. Discuss scope expansion before adopting them.

## Objectives

- Organize CFD results into a consistent, traceable dataset.
- Generate aerodynamic maps across selected operating conditions.
- Calculate how aerodynamic outputs change with individual input variables.
- Identify operating regions with strong aerodynamic sensitivity.
- Document assumptions, data quality, and validation results.

## Earlier Workflow Proposal (Not Finalized)

This proposed data flow is retained for discussion; the intended development sequence is described above.

```text
Define parameter study
        |
        v
STAR-CCM+
Run CFD cases and export results
        |
        v
Python
Collect, validate, and standardize data
        |
        v
MATLAB
Build maps, calculate sensitivities, and export figures
        |
        v
Review and validation
```

### STAR-CCM+

- Define geometry, physics, boundary conditions, and parameter values.
- Run the selected operating conditions.
- Export forces, moments, reference quantities, and convergence information.
- Preserve case identifiers and simulation settings.

Simulation automation will be added where supported and documented.

### Python

- Support export automation through a mechanism confirmed for the installed STAR-CCM+ version.
- Collect STAR-CCM+ exports.
- Validate required fields and identify missing or duplicate cases.
- Standardize units, names, and data structure.
- Flag cases that do not meet agreed quality criteria.
- Export a consolidated dataset for MATLAB.

### MATLAB

- Import the validated dataset.
- Generate aerodynamic performance maps.
- Calculate sensitivities using documented numerical methods.
- Visualize parameter interactions and data coverage.
- Export reproducible figures and result tables.

## Candidate Input Variables

| Variable | Description |
|---|---|
| Front ride height | Front reference-point height above the ground |
| Rear ride height | Rear reference-point height above the ground |
| Roll angle | Vehicle rotation about the longitudinal axis |
| Yaw angle | Relative angle between the vehicle and incoming flow |
| Steering angle | Steering input using an agreed wheel-angle convention |
| Vehicle speed | Freestream speed |
| Wing settings | Selected aerodynamic configuration parameters |

The agreed initial focus is front and rear ride height under straight-line conditions. Other variables are retained as candidates for later discussion, not additions to the initial scope.

Reference points, units, and positive directions must be defined before generating cases. Pitch and rake must remain consistent with the ride-height definitions.

## Aerodynamic Outputs

- Total downforce
- Drag
- Front and rear equivalent aerodynamic loads
- Aerodynamic balance
- Aerodynamic force coefficients
- Downforce-to-drag ratio

The method used to calculate equivalent axle loads and aerodynamic balance will be documented.

## Performance Maps and Sensitivity Maps

**Performance maps** show an aerodynamic output across operating conditions, such as downforce versus front and rear ride height.

**Sensitivity maps** show the rate at which an output changes with an input, such as:

- Change in downforce per millimetre of front ride height
- Change in drag per degree of yaw
- Change in aerodynamic balance per degree of roll

Each sensitivity calculation must state:

- The output and input being compared
- Units and sign conventions
- Which other variables are held fixed
- The differentiation or fitting method
- Any normalization applied

Interpolation and extrapolation must be identified explicitly. Unsupported regions must not be presented as validated CFD results.

## Repository Structure

```text
.
├── AGENTS.md               Shared instructions for coding assistants
├── CLAUDE.md               Imports shared instructions for Claude Code
├── README.md               Project overview and setup
├── docs/
│   ├── SPEC.md             Requirements and agreed conventions
│   ├── methodology.md      Mapping and sensitivity methods
│   └── handoffs/           Task progress and collaboration notes
├── starccm/
│   ├── macros/             Simulation automation, where applicable
│   └── export_templates/   Export definitions and examples
├── python/
│   ├── src/                Data-processing code
│   └── tests/              Data-processing tests
├── matlab/
│   ├── src/                Mapping and sensitivity functions
│   ├── tests/              Numerical and software tests
│   └── examples/           Reproducible demonstrations
├── data/
│   ├── sample/             Small shared example datasets
│   ├── raw/                Original CFD exports
│   └── processed/          Validated datasets
└── results/
    └── <study-name>/       Reviewed deliverables for a study
```

This structure is a proposal; directories will be created only when needed and agreed. Temporary scripts, debugging output, intermediate data, and draft figures belong in `work/<task-name>/`. Reviewed deliverables belong in `results/<study-name>/`, following `AGENTS.md`.

## Data Management

- Preserve raw exports without modification.
- Assign every simulation a unique case identifier.
- Record input parameters, units, reference quantities, and configuration.
- Link processed results to their source cases.
- Keep small sample datasets in Git.
- Store large simulation files separately and document how to access them.
- Exclude local paths, credentials, and temporary files from version control.

## Validation

Before accepting results:

- Check units, coordinate systems, and force signs.
- Review simulation convergence and mesh sensitivity.
- Check parameter coverage and missing cases.
- Validate processing against known exports.
- Compare numerical sensitivities with a known analytical example.
- Examine sensitivity to differentiation step size or fitting choices.
- Validate interpolation using held-out cases where feasible.
- Record limitations and regions requiring additional simulations.

Agreement between coding assistants is not a substitute for numerical or physical validation.

## Software Requirements

Exact versions and dependencies will be recorded during setup.

| Software | Purpose | Version |
|---|---|---|
| STAR-CCM+ | CFD simulation and export | TBD |
| Python | Export automation and data processing | TBD |
| MATLAB | Mapping, numerical analysis, and visualization | TBD |
| Git | Version control | Team-supported version |

Required Python packages and MATLAB toolboxes will be documented once selected.

## Getting Started

For now, read `README.md`, `docs/SPEC.md`, `AGENTS.md`, and relevant notes in `docs/handoffs/`. Detailed planning and implementation have not started; choose the first topic together. The setup steps below are retained for future use, and no executable sample workflow is established yet.

1. Clone the repository.
2. Read `docs/SPEC.md` for agreed definitions and requirements.
3. Install the documented dependencies.
4. Run the sample-data workflow.
5. Validate the sample results before processing a full CFD study.

Executable setup and run commands will be added as the implementation becomes available.

## Collaboration

This university project is developed by two collaborators using Codex and Claude Code. The shared repository holds code, methodology, research decisions, validation evidence, and progress notes so either collaborator can understand and continue the other's work.

Both collaborators are MATLAB beginners. Explain concepts in plain language, one topic at a time, including the reasoning behind equations and implementation choices. Distinguish necessary initial work, useful work that can wait, and optional work. Separate agreed decisions, proposals, assumptions, and unresolved questions; do not invent missing details or treat unvalidated results as established findings.

Retained collaboration guidance:

- Maintain common instructions in `AGENTS.md`.
- Import those instructions from `CLAUDE.md` using `@AGENTS.md`.
- Assign each task to one owner.
- Work in separate branches and local copies.
- Agree on data formats and function interfaces before parallel implementation.
- Use pull requests for review before merging into `main`.
- Record decisions, tests, limitations, and next steps in task handoff notes.
- Clearly distinguish tests that were run from checks that remain unverified.

## Earlier Milestone Proposals (Not an Agreed Plan)

- [ ] Define the first parameter study and aerodynamic outputs
- [ ] Agree on units, sign conventions, and reference quantities
- [ ] Specify the STAR-CCM+ export format
- [ ] Create a small sample dataset
- [ ] Implement Python data collection and validation
- [ ] Generate the first MATLAB performance maps
- [ ] Implement and validate sensitivity calculations
- [ ] Run an end-to-end demonstration
- [ ] Document findings and limitations

## License

To be selected by the project owners.
