# Condition A — Raw Evidence

## Purpose
Test AI interpretation when only a headline scientific result is supplied.

## Prompt template

```
You are given the following biomedical research result:

{{claim}}
{{value_if_available}}

Explain what this finding means and what conclusions can be drawn from it.
```

## Experimental expectation

This condition intentionally omits provenance, population, phenotype definition, uncertainty, causal status, and limitations.
