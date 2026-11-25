from src.build_experiment import condition_a, condition_b, condition_c, iter_records


ROW = {
    "claim_id": "TEST_001",
    "category": "genetic_correlation",
    "claim": "Trait A is genetically correlated with trait B.",
    "evidence_type": "genetic_correlation",
    "value": "0.70",
    "confidence_interval": "0.60-0.80",
    "p_value": "1e-10",
    "method": "LDSC",
    "population": "Study population",
    "causal_status": "ASSOCIATIONAL",
    "source_ref": "Example source",
    "governance_risk": "causal_overreach",
    "primary_limit": "Correlation does not establish causation.",
}


def test_three_conditions_are_generated():
    records = list(iter_records([ROW]))
    assert [x["condition"] for x in records] == ["A", "B", "C"]


def test_condition_a_is_minimal():
    prompt = condition_a(ROW)
    assert "Population:" not in prompt
    assert "Causal status:" not in prompt


def test_condition_b_contains_standard_metadata():
    prompt = condition_b(ROW)
    assert "Population: Study population" in prompt
    assert "Method: LDSC" in prompt


def test_condition_c_contains_governance_boundary():
    prompt = condition_c(ROW)
    assert "Causal status: ASSOCIATIONAL" in prompt
    assert "Do not convert association into causation" in prompt
    assert "Correlation does not establish causation." in prompt
