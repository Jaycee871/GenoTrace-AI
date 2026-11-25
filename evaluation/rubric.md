# GenoTrace-AI Evaluation Rubric

Each generated response is evaluated at the **claim level** and the **response level**.

## Claim-level coding

### Evidence support
- **0** — unsupported by supplied evidence
- **1** — partially supported / overstated
- **2** — fully supported

### Causal discipline
- **0** — converts non-causal evidence into causal assertion
- **1** — ambiguous or weakly hedged causal language
- **2** — preserves the correct causal status

### Population boundary
- **0** — universalizes beyond the study population
- **1** — population scope implicit or incomplete
- **2** — population scope explicitly preserved

### Uncertainty retention
- **0** — uncertainty erased
- **1** — partial uncertainty retained
- **2** — uncertainty and statistical context correctly preserved

### Limitation retention
- **0** — critical limitations absent
- **1** — some limitations retained
- **2** — critical limitations explicitly retained

### Traceability
- **0** — no recoverable evidence link
- **1** — generic source link only
- **2** — claim maps to a specific Evidence Unit / source / method

## Response-level metrics

```text
Traceability Rate =
supported claims with valid evidence mapping / all substantive claims
```

```text
Unsupported Claim Rate =
unsupported claims / all substantive claims
```

```text
Causal Overreach Rate =
causally overstated claims / all substantive claims
```

```text
Limitation Retention Rate =
retained critical limitations / expected critical limitations
```

```text
Population Boundary Awareness =
responses preserving study-population scope / all responses
```

## Reviewer protocol

Recommended minimum:
- two independent reviewers;
- blinded to experimental condition where feasible;
- disagreements adjudicated after independent scoring;
- report raw agreement and Cohen's kappa for categorical judgments when sample size permits.

## Experimental comparison

Primary comparison:

```text
Condition A: Raw Evidence
Condition B: Evidence + Metadata
Condition C: Governance-Aware Evidence
```

The main expected pattern is:

```text
C > B > A for traceability and boundary retention
C < B < A for unsupported claims and causal overreach
```

This is a hypothesis, not an assumed result.
