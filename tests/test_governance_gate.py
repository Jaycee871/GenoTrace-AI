from src.governance_gate import check_interpretation, validate_evidence_unit


UNIT = {
    "claim_id": "BPD_GC_001",
    "claim": "BPD showed a strong positive genetic correlation with PTSD.",
    "evidence_type": "genetic_correlation",
    "source": "Nature Genetics 2026",
    "population": "European ancestry GWAS",
    "causal_status": "ASSOCIATIONAL",
    "allowed_interpretation": [
        "BPD and PTSD show substantial shared common genetic effects."
    ],
    "forbidden_interpretation": [
        "PTSD causes BPD.",
        "BPD causes PTSD.",
        "A person with PTSD will develop BPD.",
    ],
    "limitations": [
        "Genetic correlation does not establish causal direction."
    ],
}


def test_valid_unit_has_no_schema_warnings():
    assert validate_evidence_unit(UNIT) == []


def test_association_statement_passes():
    text = "BPD and PTSD show substantial shared genetic liability."
    assert check_interpretation(UNIT, text) == []


def test_causal_overreach_is_flagged():
    text = "PTSD causes BPD."
    flags = check_interpretation(UNIT, text)
    assert "possible_causal_overreach" in flags
    assert "explicit_forbidden_interpretation" in flags
