# vlabs-evidence

Redacted evidence artifacts from the Verifiable Labs clean promotion gate:
sample assurance cards, aggregate metrics, and sanitized export manifests.

> Verifiable Labs builds clean feedback and promotion gates for increasingly general AI agents.

**Everything currently in this repository is illustrative** — synthetic
numbers published to show the *shape* of the evidence, not real customer
results. Real (consented, redacted) evidence packs will be added here as
they are produced, and will be clearly labeled.

What is never published, here or anywhere: hidden evaluation content, gold
answers, anti-hack detection details, raw traces, customer data, secrets,
private anti-hack traps, or private engine internals.

## Contents

- [`evidence/sample_assurance_card_redacted.json`](evidence/sample_assurance_card_redacted.json)
- [`evidence/aggregate_metrics_sample.md`](evidence/aggregate_metrics_sample.md)
- [`reproducibility-notes.md`](reproducibility-notes.md)
- [`manifests/`](manifests/) — sanitized HF/W&B export manifests (below)

## Sanitized evidence manifests

`manifests/` holds the **sanitized export manifests** used to publish public
evidence to Hugging Face and Weights & Biases:

- [`manifests/hf_upload_manifest.json`](manifests/hf_upload_manifest.json)
- [`manifests/wandb_upload_manifest.json`](manifests/wandb_upload_manifest.json)
- [`manifests/evidence_safety_report.md`](manifests/evidence_safety_report.md)

The artifacts they reference are **synthetic / redacted**. They contain
**no** hidden evals, gold answers, raw traces, customer data, secrets,
private anti-hack traps, or private engine internals — every record is
routed through the platform's `assert_public_export_safe` policy gate, which
refuses any such content and any `restricted`/`secret` classification.

HF and W&B uploads are **gated by explicit approval flags**
(`VLABS_APPROVE_HF_UPLOAD=1`, `VLABS_APPROVE_WANDB_UPLOAD=1`); the exporters
are dry-run by default and never touch the network without them.

## Install the SDK

```bash
pip install "vlabs-sdk==0.0.2"
```

## Formal scope

Selected mathematical properties behind the contamination-resistant promotion gate are machine-verified in Lean 4. The implementation is property-tested against the formal specification.
