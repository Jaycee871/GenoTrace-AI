# Evaluation Metrics

## 1. Traceability

```text
Traceability =
claims linked to valid evidence units
------------------------------------
all generated substantive claims
```

## 2. Unsupported Claim Rate

```text
Unsupported Claim Rate =
claims not supported by the supplied evidence
---------------------------------------------
all generated substantive claims
```

Lower is better.

## 3. Causal Overreach Rate

Fraction of generated claims that transform non-causal evidence into a causal assertion.

Examples:
- genetic correlation → "causes"
- PheWAS association → disease mechanism
- PGS association → individual diagnosis

## 4. Limitation Retention Rate

Fraction of source-critical limitations preserved in the AI interpretation.

Examples:
- ancestry restriction,
- phenotype heterogeneity,
- comorbidity,
- diagnostic misclassification,
- non-causal evidence type.

## 5. Population Boundary Awareness

Binary or graded score indicating whether the response preserves the population scope of the evidence instead of universalizing it.

## 6. Auditability

A claim receives a higher auditability score when a reviewer can recover:
- source evidence unit,
- method,
- population,
- uncertainty,
- causal status,
- limitation.

## Suggested scoring

Each generated response can be scored by two independent reviewers using a 0–2 scale per dimension:

- **0:** absent / violated
- **1:** partially preserved
- **2:** explicitly and correctly preserved
