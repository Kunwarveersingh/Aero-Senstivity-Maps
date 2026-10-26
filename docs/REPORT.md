# Aerodynamic mapping for Formula Student

## Document status

Working report for Strohm und Söhne e.V. Noris Racing, Technische Hochschule
Nürnberg Georg Simon Ohm. This scaffold records the introduction and initial
literature findings; it is not a completed thesis or evidence of completed CFD.
Use [SPEC.md](SPEC.md) for decision status and [handoffs](handoffs/) for session history.
Kunwar and Advaith are confirmed contributors.

## 1. Introduction and objectives

The project aims to generate aerodynamic performance and sensitivity maps for an
FSAE car from STAR-CCM+ results. Phase 1 varies only front and rear ride height in
straight-line conditions to prove the data-to-map process and assess its efficiency.
Python is intended for export automation and processing, CSV for data exchange,
and MATLAB for maps. Cornering is a later extension.

Simulation effort should remain low while providing enough evidence for conclusions.
Neither a case count nor a validated numerical method has been selected.

## 2. Background and literature

The following findings come from relevant sections of the supplied theses, not
from results for our car. Page references are PDF page numbers, not printed pages.

| Source | Relevant finding | Limit on transfer to this project |
|---|---|---|
| Hendy [1], pp. 4–5, 17 | Uses a 6 × 6 ride-height map with separate attitude variations; reports 47 simulations overall. | Baseline roll, steer, and yaw are nonzero. This is not a straight-line setup to copy. |
| Hendy [1], pp. 13–15 | Python organizes Fluent cases and collects case information and results into CSV for subsequent use including MATLAB. | This does not establish a STAR-CCM+ automation mechanism. |
| Carreira [2], pp. 67–68 | Studies front/rear ride heights together in 35 symmetric cases; explains that changing one height changes pitch and diffuser orientation. | Its values and count do not establish adequate coverage for our car. |
| Carreira [2], pp. 77–80 | Adds 50 Latin hypercube samples for a broader five-variable model; compares polynomial models using leave-one-out cross-validation. Second order has the lowest reported error among tested orders. | A quadratic model is not thereby validated for our project. |
| Carreira [2], p. 65 | Uses Java macros in STAR-CCM+ 2020.3 and exports CSV. | Our version and supported automation still require inspection. |

Cross-validation checks predictions against observations omitted when fitting a
model. A surrogate is an approximation of CFD responses. These concepts are
research context, not selected implementation methods. Model agreement with CFD
also does not establish that CFD agrees with the physical car.

To be documented: the theory needed for our chosen outputs, conventions,
ride-height definitions, interactions, and sensitivity interpretation.

## 3. CAD preparation and constraints

To be documented: source geometry and revision, component selection,
simplifications, reference points, constraints, and ride-height adjustment method.
Manual changes and separate STEP exports are the proposed approach, not completed work.

Questions when this work is reached: Which geometry was simplified and why? How
were constraints chosen? How are the intended heights checked after export/import?
Who made each decision, and what evidence or practical limitation supported it?

## 4. CFD methodology

To be documented after inspecting the existing template: software version,
geometry import, domain, physics, boundary conditions, mesh, convergence,
reported outputs, and simulation-driving versus reference-only parameters.
Do not infer the configuration from either thesis.

## 5. Study design and simulation selection

Agreed: front and rear ride height are the only varied Phase 1 inputs.
Proposed without justification: 3 × 3 (9 combinations) or 5 × 5 (25 combinations),
excluding extra validation or repeat simulations. No option or actual values are selected.

To be documented: feasible ranges, fixed operating conditions, sampling rationale,
validation evidence, and justification for the selected total effort.
Ask what evidence supports the chosen number and distribution of cases; do not
retroactively invent a justification from the completed simulation count.

## 6. Export, data processing, and MATLAB

To be documented: confirmed automation mechanism, case identification and units,
CSV format, geometry-to-metadata checks, processing steps, mapping and sensitivity
methods, and reproducible execution instructions. Companion CSV metadata is an
assistant proposal, not an agreed interface. No code or run commands are established.

## 7. Results, validation, and limitations

To be documented when results exist: CFD quality evidence, processing checks,
map prediction errors, sensitivity checks, uncertainty, coverage, and physical
validation where available. Separate simulated points from fitted/interpolated
predictions and identify unsupported regions. No project results are claimed here.

## 8. Conclusions and future work

To be documented from evidence. Cornering is a later scope extension; detailed
optimization and extensive automation are not Phase 1 requirements.

## 9. Decision evidence and contributor record

For each substantive decision, record the question, contributor, date, status
(proposed/agreed/validated), alternatives considered, rationale, evidence/source,
and limitations. Capture research performed independently of coding assistants.
Ask one topic at a time; leave unknown answers "To be documented".

## References

1. Paul Hendy (2019), *Aero Map for Formula Student*, supplied final-year report.
   Local file: `docs/pdfs/MMS+Final+Year+Thesis+Collection+-+Aero+Map+for+Formula+Student+(Paul+Hendy+-+2019).pdf`.
2. Miguel Marques Carreira (2022), *Aerodynamic Mapping of a Formula Student
   Prototype using Numerical Simulations and On-track Validation*, master's thesis.
   Local file: `docs/pdfs/Thesis_MiguelCarreira_181564.pdf`.

The PDFs are local research material and are not included in this documentation
commit. A fresh checkout may not contain them; arrange access with the collaborators.
