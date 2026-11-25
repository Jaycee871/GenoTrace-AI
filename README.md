# GenoTrace-AI

**A Traceable Governance Framework from Genomic Evidence to AI Decision Support**

GenoTrace-AI is a research prototype for studying how heterogeneous biomedical evidence should be represented, traced, constrained, and audited when it is used by AI-assisted decision-support systems.

> GenoTrace-AI does **not** diagnose borderline personality disorder (BPD), predict an individual's mental-health status, or replace clinical judgment.  
> Its research target is **evidence governance**: how scientific claims change as they move from source data to statistical results, AI interpretation, and downstream decision support.

## Why this project?

Biomedical AI often receives a scientific result after several transformations:

```text
Phenotype definition
      ↓
GWAS / meta-analysis
      ↓
Locus / gene evidence
      ↓
Genetic correlation / PGS / PheWAS
      ↓
AI interpretation
      ↓
Decision support
```

At each step, provenance, uncertainty, population boundaries, phenotype definitions, and causal status may be lost. GenoTrace-AI makes those constraints explicit and machine-readable.

## Initial case study

The first case study uses the 2026 *Nature Genetics* paper:

**Genome-wide association analyses of borderline personality disorder identify 11 loci and highlight shared risk with mental and somatic disorders**  
DOI: `10.1038/s41588-026-02654-3`

The study is useful as a governance stress test because it combines clinical and biobank phenotypes, GWAS meta-analysis, gene-level evidence, polygenic scores, genetic correlations, and PheWAS results across psychiatric and somatic phenotypes.

## Core research questions

1. How can heterogeneous genomic and clinical evidence be represented in a traceable information-governance framework for AI-assisted biomedical decision support?
2. Can provenance-aware governance reduce unsupported or causally overstated AI interpretations?
3. Does explicit representation of population, phenotype, uncertainty, and causal boundaries improve auditability?

## Experimental conditions

- **Condition A — Raw evidence:** a scientific result with minimal context.
- **Condition B — Evidence + metadata:** adds method, uncertainty, source, and population metadata.
- **Condition C — Governance-aware evidence:** adds provenance, causal status, allowed/forbidden interpretations, and limitations.

## Evaluation

Primary metrics:

- Traceability
- Unsupported Claim Rate
- Causal Overreach Rate
- Limitation Retention Rate
- Population Boundary Awareness
- Auditability

## Repository structure

```text
docs/         Research design and governance framework
schema/       Machine-readable Evidence Unit schema
data/         Case-study evidence objects
prompts/      A/B/C experimental prompt conditions
src/          Minimal governance prototype
evaluation/   Metrics and evaluation rubric
paper/        Conference abstract and research notes
```

## Literature grounding

The framework is grounded in research on:

- data provenance for responsible AI (fairness, accountability, transparency, explainability);
- biomedical provenance, W3C PROV, interoperability, and reproducibility;
- traceability across data, processes, artifacts, agents, and decisions;
- healthcare AI governance across the system lifecycle;
- auditable and source-verified clinical decision support;
- causal versus associational reasoning in clinical AI.

See `docs/related_work.md` and `docs/design_requirements.md`.

## Build the A/B/C experiment

The evidence catalog currently contains **34 governance test cases**.

Generate all three experimental conditions deterministically:

```bash
python -m src.build_experiment
```

This produces **102 prompts** (34 evidence units × 3 conditions) under:

```text
experiments/generated/bpd_abc_prompts.jsonl
```

Generated experimental inputs are reproducible and can be run against one or more language models without changing the underlying evidence catalog.

The model runner is intentionally separate from the prompt builder so that model/provider/version information can be logged independently.

## Evaluation workflow

1. Generate A/B/C prompts.
2. Run the same evidence cases under each condition.
3. Store outputs with model/version metadata.
4. Blind reviewers to experimental condition where feasible.
5. Score outputs using `evaluation/rubric.md`.
6. Aggregate coded results using `evaluation/scoring.py`.

## Status

**v0.2 — literature-grounded governance architecture + 34-case BPD evidence catalog + A/B/C experiment builder**

This repository is an evolving research artifact. The initial goal is not to reproduce the full BPD GWAS, but to test whether structured evidence governance improves the reliability and auditability of AI-generated biomedical interpretations.
