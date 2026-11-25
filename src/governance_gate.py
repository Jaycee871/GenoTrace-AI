"""Minimal GenoTrace-AI governance gate.

This prototype validates required governance fields and flags obvious
interpretation risks. It is not a clinical decision system.
"""

from __future__ import annotations

from typing import Any, Dict, List


REQUIRED_FIELDS = {
    "claim_id",
    "claim",
    "evidence_type",
    "source",
    "population",
    "causal_status",
    "allowed_interpretation",
    "forbidden_interpretation",
    "limitations",
}

CAUSAL_TERMS = (
    "causes",
    "cause",
    "caused by",
    "leads to",
    "results in",
    "will develop",
    "will get",
)


def validate_evidence_unit(unit: Dict[str, Any]) -> List[str]:
    """Return schema-level governance warnings."""
    warnings: List[str] = []

    missing = sorted(REQUIRED_FIELDS - unit.keys())
    if missing:
        warnings.append("missing_required_fields:" + ",".join(missing))

    if unit.get("causal_status") == "ASSOCIATIONAL" and not unit.get(
        "forbidden_interpretation"
    ):
        warnings.append("association_without_causal_boundary")

    if not unit.get("limitations"):
        warnings.append("limitations_missing")

    if not unit.get("population"):
        warnings.append("population_boundary_missing")

    return warnings


def check_interpretation(unit: Dict[str, Any], generated_text: str) -> List[str]:
    """Flag simple governance violations in generated interpretation text."""
    flags = validate_evidence_unit(unit)
    text = generated_text.lower()

    if unit.get("causal_status") == "ASSOCIATIONAL":
        if any(term in text for term in CAUSAL_TERMS):
            flags.append("possible_causal_overreach")

    for forbidden in unit.get("forbidden_interpretation", []):
        if forbidden.lower() in text:
            flags.append("explicit_forbidden_interpretation")

    return sorted(set(flags))
