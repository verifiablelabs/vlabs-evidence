# Reproducibility notes

Every future evidence pack in this repository will state, per artifact:

- the evaluation-contract hash and run id it came from,
- the seed policy (train / val / test split seeds never overlap),
- which numbers are measured vs derived (clean score = raw x (1 - DCR)),
- the redaction profile applied before publication.

Current artifacts are **synthetic/illustrative** and exist to fix the format.
Links to W&B dashboards / HF datasets will be added only after the
corresponding export approvals (`VLABS_APPROVE_{WANDB_UPLOAD,HF_UPLOAD}`).
