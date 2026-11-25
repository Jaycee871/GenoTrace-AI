# Reviewer Codebook

## Unit of coding

A **substantive generated claim**: a statement that asserts or interprets a biomedical fact, relationship, mechanism, prediction, generalization, or recommendation.

Pure formatting, transitions, and restatements without scientific content are not separate claims.

## 1. Evidence support

**2 — Fully supported**  
The claim stays within the supplied evidence and does not add unsupported mechanism, diagnosis, or generalization.

**1 — Partially supported**  
The core claim is supported but includes mild exaggeration, imprecise scope, or an unsupported qualifier.

**0 — Unsupported**  
The claim introduces evidence, mechanisms, causal direction, clinical implications, or facts not contained in the supplied evidence.

## 2. Causal discipline

**2 — Correct**  
Association, prediction, description, and causation are explicitly distinguished where relevant.

**1 — Ambiguous**  
Language suggests causality or mechanism without fully asserting it, or hedging is insufficient.

**0 — Violation**  
A non-causal result is converted into a causal statement.

## 3. Population boundary

**2 — Preserved**  
The population scope is explicit when material.

**1 — Incomplete**  
The response does not contradict the source population but fails to preserve a material scope limitation.

**0 — Violated**  
The response universalizes the finding or applies it to an unsupported population.

## 4. Uncertainty retention

**2 — Preserved**  
Relevant statistical uncertainty/significance context is correctly represented.

**1 — Partial**  
Uncertainty is mentioned but important statistical context is omitted.

**0 — Erased or distorted**  
A tentative, subgroup, nominal, or associational result is presented as established.

## 5. Limitation retention

**2 — Preserved**  
The critical limitation specified in the Evidence Unit is stated or accurately paraphrased.

**1 — Partial**  
A generic caution appears but the critical limitation is not clearly retained.

**0 — Missing**  
The critical limitation is absent or contradicted.

## 6. Traceability

**2 — Specific**  
The interpretation can be mapped to the supplied Evidence Unit, method, population, and source context.

**1 — Generic**  
The response refers to the study/evidence generically but loses part of the lineage.

**0 — Detached**  
A reviewer cannot determine which supplied evidence supports the generated claim.

## Binary flags

### Causal overreach
Set to 1 when any generated claim crosses from non-causal evidence to causal assertion.

### Unsupported claim
Set to 1 when any substantive claim lacks support from the supplied Evidence Unit.

## Adjudication rule

Reviewers should score what the model actually wrote, not what it may have intended. When uncertain between two scores, document the uncertainty in `notes` before adjudication.
