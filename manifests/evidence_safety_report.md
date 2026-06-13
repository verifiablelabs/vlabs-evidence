# Evidence safety report — HF/W&B dry-run

Generated locally. **No upload performed.** Approval flags VLABS_APPROVE_HF_UPLOAD / VLABS_APPROVE_WANDB_UPLOAD are not set; all exporters returned `uploaded=false, dry_run=true`.

## Scan results (over the exact upload candidate set)

| Check | Result |
|---|---|
| secret | CLEAN |
| leakage | CLEAN |
| forbidden_claims | CLEAN |
| hidden_eval_gold | CLEAN (note¹) |
| evidence_validator | PASS |
| docs_claims | PASS |
| synthetic_markers | PASS |

¹ The only matches were the manifest safety-flags  and  — redaction metadata asserting *absence*, not content. No hidden-eval/gold-answer/raw-trace content is present.

## Export-guard negative tests (assert_public_export_safe)
- hidden_eval → REFUSED · gold_answer → REFUSED · raw_trace → REFUSED · secret → REFUSED
- classification RESTRICTED → REFUSED · SECRET → REFUSED

## Upload candidate set
### Hugging Face (dataset)
- LICENSE
- aggregate_metrics_sample.md
- hf_upload_manifest.json
- reproducibility-notes.md
- sample_assurance_card_redacted.json

### Weights & Biases (artifacts)
- wandb_upload_manifest.json

## Never uploaded (refused by policy / not in set)
- hidden evals, gold answers, raw/customer traces, secrets/API keys
- private anti-hack traps, scenario-compiler/contamination-firewall internals
- private eval-vault contents, private engine source
