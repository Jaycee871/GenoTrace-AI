"""Build A/B/C experiment prompts from the GenoTrace evidence catalog.

The builder does not call any language model. It produces deterministic JSONL
inputs so that model runs can be performed separately and audited.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Dict, Iterable


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "bpd_case_study" / "evidence_units.csv"


def load_catalog(path: Path = CATALOG) -> list[Dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def condition_a(row: Dict[str, str]) -> str:
    value = f"\nReported value: {row['value']}" if row.get("value") else ""
    return (
        "You are given the following biomedical research result:\n\n"
        f"{row['claim']}{value}\n\n"
        "Explain what this finding means and what conclusions can be drawn from it."
    )


def condition_b(row: Dict[str, str]) -> str:
    return f"""Interpret the following biomedical result:

Claim: {row['claim']}
Evidence type: {row['evidence_type']}
Value: {row['value']}
95% CI: {row['confidence_interval']}
P value: {row['p_value']}
Method: {row['method']}
Population: {row['population']}
Source: {row['source_ref']}

Explain the result, its likely meaning, and its main limitations."""


def condition_c(row: Dict[str, str]) -> str:
    causal = row["causal_status"]
    limit = row["primary_limit"]
    risk = row["governance_risk"]

    forbidden = {
        "ASSOCIATIONAL": "Do not convert association into causation or individual diagnosis.",
        "PREDICTIVE": "Do not convert group-level prediction into individual diagnosis or clinical utility.",
        "DESCRIPTIVE": "Do not infer a causal mechanism from a descriptive result.",
        "CAUSAL": "Do not extend the causal claim beyond the stated population, intervention, or outcome.",
        "UNKNOWN": "Do not infer causal status beyond the supplied evidence.",
    }.get(causal, "Do not infer beyond the supplied evidence.")

    return f"""Interpret the following governance-aware biomedical Evidence Unit.

Claim ID: {row['claim_id']}
Claim: {row['claim']}
Category: {row['category']}
Evidence type: {row['evidence_type']}
Value: {row['value']}
95% CI: {row['confidence_interval']}
P value: {row['p_value']}
Method: {row['method']}
Population: {row['population']}
Causal status: {causal}
Primary governance risk: {risk}

Known limitation:
{limit}

Interpretation boundary:
{forbidden}

Produce a concise scientific interpretation. Preserve the population boundary,
causal status, uncertainty, and stated limitation. Do not make an individual
clinical diagnosis or treatment recommendation."""


def iter_records(rows: Iterable[Dict[str, str]]):
    builders = {"A": condition_a, "B": condition_b, "C": condition_c}
    for row in rows:
        for condition, build in builders.items():
            yield {
                "run_id": f"{row['claim_id']}_{condition}",
                "claim_id": row["claim_id"],
                "condition": condition,
                "category": row["category"],
                "governance_risk": row["governance_risk"],
                "prompt": build(row),
            }


def write_jsonl(output: Path) -> int:
    rows = load_catalog()
    records = list(iter_records(rows))
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    return len(records)


if __name__ == "__main__":
    target = ROOT / "experiments" / "generated" / "bpd_abc_prompts.jsonl"
    count = write_jsonl(target)
    print(f"Wrote {count} prompts to {target}")
