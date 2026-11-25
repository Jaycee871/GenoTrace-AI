# GenoTrace Governance Framework

## Design principle

A biomedical result should not enter an AI decision-support pipeline as an isolated number. It should enter as a structured evidence object carrying its interpretation boundaries.

## Five governance layers

### 1. Data Provenance
Captures where the evidence originated.

Examples:
- clinical DSM diagnosis,
- ICD-coded EHR phenotype,
- self-reported diagnosis,
- cohort or biobank,
- source publication.

### 2. Semantic Harmonization
Captures whether superficially identical labels represent equivalent information objects.

Example:
`BPD = 1` may refer to a structured clinical diagnosis, an ICD-derived phenotype, or self-report.

### 3. Evidence Provenance
Captures the transformation chain that produced a claim.

Example:
```text
Cohort phenotype
→ GWAS
→ meta-analysis
→ LDSC
→ genetic correlation
→ AI-facing evidence object
```

### 4. AI Interpretation Governance
Specifies what an AI system may and may not infer.

Example:

**Allowed**
- BPD and PTSD show substantial shared common genetic effects.

**Forbidden**
- PTSD causes BPD.
- BPD causes PTSD.
- A person with PTSD will develop BPD.

### 5. Decision and Audit
Every AI claim should be traceable to:
- an evidence object,
- a source,
- a method,
- an uncertainty statement,
- an explicit causal status.

## Governance gate

A claim may pass only if all required governance fields are present and the proposed interpretation does not violate a forbidden causal or population-level transformation.

```text
Evidence Object
     ↓
Governance Gate
 ┌───────┴───────┐
PASS            REJECT
 ↓                ↓
AI output      Revise / flag
 ↓
Audit trail
```

## Core failure modes

1. **Causal overreach** — association rewritten as causation.
2. **Population overgeneralization** — European-ancestry evidence rewritten as universal human evidence.
3. **Phenotype flattening** — heterogeneous phenotype definitions treated as identical.
4. **Uncertainty erasure** — confidence intervals, limitations, or statistical context disappear.
5. **Source detachment** — a generated claim cannot be traced to a source evidence unit.
6. **Clinical escalation** — a research association is rewritten as an individual diagnostic recommendation.
