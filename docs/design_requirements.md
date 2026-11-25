# Design Requirements

These requirements synthesize the initial literature review and the BPD case-study needs.

## DR1 — Evidence provenance must be explicit

Every governed biomedical claim must be traceable to a source evidence object, analytical method, and transformation path.

**Rationale:** provenance supports transparency, accountability, reproducibility, and responsible AI.

## DR2 — Claim-level governance must be first-class

The system must represent a scientific claim as an explicit object rather than treating generated text as an unstructured endpoint.

Each claim should have:
- claim ID,
- evidence type,
- source,
- value/estimate,
- uncertainty,
- population,
- phenotype definition,
- causal status.

## DR3 — Causal boundaries must be machine-readable

The artifact must distinguish:
- ASSOCIATIONAL,
- PREDICTIVE,
- DESCRIPTIVE,
- CAUSAL,
- UNKNOWN.

For non-causal evidence, explicit forbidden interpretations should be stored.

## DR4 — Population scope must persist through interpretation

Evidence derived from a restricted population must not be silently universalized.

Example:
`European ancestry GWAS` must remain visible in AI interpretation and audit records.

## DR5 — Phenotype semantics must remain visible

Equivalent labels from heterogeneous ascertainment processes must not automatically be treated as semantically identical.

Example:
`BPD = 1` may originate from:
- DSM-based clinical diagnosis,
- ICD-coded biobank phenotype,
- self-reported diagnosis.

## DR6 — Uncertainty and limitations must survive summarization

AI interpretation must preserve critical uncertainty and limitations, including:
- confidence intervals,
- statistical context,
- comorbidity,
- phenotype overlap,
- diagnostic misclassification,
- ancestry limitations,
- non-causal evidence status.

## DR7 — Provenance must cover entities, activities, and agents

The implementation should align with the basic logic of W3C PROV:

- **Entity:** source dataset, paper, evidence unit, generated claim.
- **Activity:** GWAS, meta-analysis, LDSC, PheWAS, AI interpretation, governance validation.
- **Agent:** researcher, software tool, model, reviewer.

## DR8 — Auditability must be measurable

A reviewer should be able to reconstruct:
1. which evidence supported a claim,
2. which method produced the evidence,
3. which population and phenotype definitions applied,
4. what causal boundary applied,
5. what limitations were present,
6. whether the final AI statement crossed any boundary.

## DR9 — Governance effectiveness must be empirically evaluated

The framework should not stop at architecture.

The A/B/C study will compare:
- raw evidence,
- evidence + ordinary metadata,
- governance-aware evidence.

Primary outcomes:
- traceability,
- unsupported claim rate,
- causal overreach,
- limitation retention,
- population-boundary awareness,
- auditability.

## DR10 — Governance overhead should remain inspectable

The system should record the cost of governance in:
- additional metadata fields,
- processing time,
- review effort,
- token/response overhead where relevant.

This enables future analysis of the trade-off between governance completeness and operational burden.
