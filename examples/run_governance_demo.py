"""Run a minimal GenoTrace-AI governance demo.

Usage:
    python examples/run_governance_demo.py
"""

import json
from pathlib import Path

from src.governance_gate import check_interpretation


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE_PATH = (
    ROOT
    / "data"
    / "bpd_case_study"
    / "evidence_units"
    / "BPD_GC_001.json"
)


def main() -> None:
    unit = json.loads(EVIDENCE_PATH.read_text(encoding="utf-8"))

    interpretations = {
        "within_boundary": (
            "BPD and PTSD show substantial shared genetic liability in the "
            "studied European-ancestry GWAS; this association does not establish "
            "a causal direction."
        ),
        "causal_overreach": "PTSD causes BPD.",
    }

    for name, text in interpretations.items():
        flags = check_interpretation(unit, text)
        print(f"{name}: {text}")
        print(f"flags: {flags or ['PASS']}")
        print()


if __name__ == "__main__":
    main()
