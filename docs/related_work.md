# Related Work

GenoTrace-AI is positioned at the intersection of **data provenance**, **trustworthy AI**, **biomedical informatics**, and **clinical decision support**.

## Data provenance for responsible AI

Werder, Ramesh, and Zhang define data provenance as a record of the origins and processing of data and connect provenance to fairness, accountability, transparency, and explainability (FATE). Their work is especially relevant to GenoTrace-AI because it appears in *ACM Transactions on Management Information Systems* and frames provenance as an organizational and technical mechanism for responsible AI.

- Werder K, Ramesh B, Zhang R. *Establishing Data Provenance for Responsible Artificial Intelligence Systems*. ACM TMIS. 2022. https://doi.org/10.1145/3503488

## Biomedical provenance

Gierend et al. reviewed biomedical provenance approaches and identified recurring requirements including integrity, reproducibility, traceability, interoperability, security, scalability, and trust. The review highlights W3C PROV and Open Provenance Model as common reference models, while also noting unresolved issues of granularity, completeness, semantic heterogeneity, and validation.

- Gierend K, et al. *Provenance Information for Biomedical Data and Workflows: Scoping Review*. JMIR. 2024. https://doi.org/10.2196/51297

## Traceability for trustworthy AI

Mora-Cantallops et al. argue that traceability requires a complete account of data, processes, artifacts, agents, and decisions across an AI lifecycle. Their review also identifies weak support for narrative context and decision rationale in existing tooling.

- Mora-Cantallops M, et al. *Traceability for Trustworthy AI: A Review of Models and Tools*. Big Data and Cognitive Computing. 2021. https://doi.org/10.3390/BDCC5020020

## Governance of AI in healthcare

Reddy et al. propose a governance model centered on fairness, transparency, trustworthiness, and accountability across approval, introduction, deployment, monitoring, and retirement.

- Reddy S, Allan S, Coghlan S, Cooper P. *A governance model for the application of AI in health care*. JAMIA. 2020. https://doi.org/10.1093/jamia/ocz192

## Auditable clinical AI

Alu and Oluwadare propose a conceptual architecture for source-verified clinical decision support using provenance metadata, claim-level evidence linking, retrieval, citation verification, and audit logging.

- Alu F, Oluwadare S. *An auditable and source-verified framework for clinical AI decision support: integrating retrieval-augmented generation with data provenance*. Frontiers in Artificial Intelligence. 2026. https://doi.org/10.3389/frai.2026.1737532

## Correlation, causation, and design science

Zipperling et al. use Design Science Research to derive clinician-facing requirements for causal machine-learning decision support. Their work reinforces the need to distinguish association from causal inference, communicate uncertainty, expose assumptions, and link conclusions to verifiable evidence.

- Zipperling D, et al. *Integrating Causal Machine Learning into Clinical Decision Support Systems: Insights from Literature and Practice*. 2026. https://doi.org/10.48550/arXiv.2603.24448

## Research gap addressed by GenoTrace-AI

Existing work largely traces:

```text
Data → Process → Model → Output
```

GenoTrace-AI extends the governance target to:

```text
Data → Process → Evidence → Claim → AI Interpretation → Decision
```

The proposed novelty is **claim-level evidence governance**.

A claim is treated as a governed object carrying:

- source provenance,
- phenotype definition,
- population scope,
- uncertainty,
- causal status,
- allowed interpretation,
- forbidden interpretation,
- limitations,
- audit trail.

The empirical question is whether this additional governance layer improves AI interpretation quality compared with raw evidence or ordinary metadata alone.
