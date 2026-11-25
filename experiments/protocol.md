# A/B/C Experiment Protocol

## Objective

Evaluate whether governance-aware evidence representation improves AI interpretation of biomedical evidence.

## Experimental unit

One source-derived Evidence Unit under one prompt condition.

Current catalog:
- 34 Evidence Units
- 3 conditions
- 102 deterministic prompt instances per model

## Conditions

### A — Raw evidence
Headline result only.

### B — Evidence + ordinary metadata
Adds evidence type, estimate, CI, P value, method, population, and source.

### C — Governance-aware evidence
Adds causal status, governance risk, interpretation boundary, population constraint, and critical limitation.

## Independent variable

Evidence-governance condition: A, B, or C.

## Primary dependent variables

- Evidence support score
- Causal discipline score
- Population-boundary score
- Uncertainty-retention score
- Limitation-retention score
- Traceability score
- Causal-overreach flag
- Unsupported-claim flag

## Model logging requirements

Every run must record:
- provider;
- model name;
- model/version identifier where available;
- date;
- temperature;
- top-p or equivalent;
- system prompt;
- user prompt hash;
- response;
- response hash.

## Run policy

For a single-model study:
1. use the same model/version for all 102 prompts;
2. keep generation settings constant;
3. do not expose condition labels to the model beyond prompt content;
4. randomize execution order;
5. preserve raw outputs unchanged.

For a multi-model extension, treat model identity as a second factor.

## Human evaluation

Recommended:
- two independent reviewers;
- reviewers blinded to condition where feasible;
- score with `evaluation/rubric.md`;
- resolve disagreements only after independent scoring;
- report agreement statistics.

## Analysis plan

Primary analysis:
- compare A vs B vs C on mean rubric scores;
- compare causal-overreach and unsupported-claim rates;
- report results overall and stratified by governance risk.

Risk strata currently include:
- causal overreach;
- population overgeneralization;
- genetic determinism;
- gene-causality overreach;
- clinical escalation;
- significance inflation;
- replication overstatement;
- sex-difference overreach;
- subgroup overreach;
- drug-repurposing overreach.

## Interpretation constraint

Condition C is expected to perform better, but this is a hypothesis. The experiment must retain null or contrary findings without post-hoc relabeling of success criteria.
