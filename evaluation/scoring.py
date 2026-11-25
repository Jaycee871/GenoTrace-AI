"""Aggregate manually coded GenoTrace-AI experiment results."""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path


SCORE_FIELDS = (
    "evidence_support",
    "causal_discipline",
    "population_boundary",
    "uncertainty_retention",
    "limitation_retention",
    "traceability",
)


def summarize(path: Path) -> dict[str, dict[str, float]]:
    rows = list(csv.DictReader(path.open(encoding="utf-8", newline="")))
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[row["condition"]].append(row)

    output: dict[str, dict[str, float]] = {}
    for condition, items in grouped.items():
        summary: dict[str, float] = {"n": float(len(items))}
        for field in SCORE_FIELDS:
            values = [float(x[field]) for x in items if x.get(field) not in ("", None)]
            summary[f"mean_{field}"] = sum(values) / len(values) if values else float("nan")

        causal_flags = [int(x["causal_overreach_flag"]) for x in items if x.get("causal_overreach_flag") != ""]
        unsupported_flags = [int(x["unsupported_claim_flag"]) for x in items if x.get("unsupported_claim_flag") != ""]
        summary["causal_overreach_rate"] = (
            sum(causal_flags) / len(causal_flags) if causal_flags else float("nan")
        )
        summary["unsupported_claim_rate"] = (
            sum(unsupported_flags) / len(unsupported_flags) if unsupported_flags else float("nan")
        )
        output[condition] = summary

    return output
