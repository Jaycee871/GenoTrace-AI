# Condition C — Governance-Aware Evidence

## Purpose
Test whether explicit governance constraints reduce unsupported interpretation.

## Prompt template

```
Interpret the following structured biomedical Evidence Unit.

Claim: {{claim}}
Evidence type: {{evidence_type}}
Value: {{value}}
95% CI: {{confidence_interval}}
P value: {{p_value}}
Method: {{method}}
Population: {{population}}
Phenotype definition: {{phenotype_definition}}
Causal status: {{causal_status}}

Allowed interpretations:
{{allowed_interpretation}}

Forbidden interpretations:
{{forbidden_interpretation}}

Known limitations:
{{limitations}}

Provenance:
{{provenance}}

Produce a concise scientific interpretation.
Every substantive statement must remain inside the evidence and causal boundaries above.
Explicitly preserve population and uncertainty limitations.
```
