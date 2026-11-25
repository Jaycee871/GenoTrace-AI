# Condition B — Evidence + Metadata

## Purpose
Test whether ordinary scientific metadata improves interpretation.

## Prompt template

```
Interpret the following biomedical result:

Claim: {{claim}}
Evidence type: {{evidence_type}}
Value: {{value}}
95% CI: {{confidence_interval}}
P value: {{p_value}}
Method: {{method}}
Population: {{population}}
Source: {{source}}

Explain the result, its likely meaning, and its main limitations.
```
