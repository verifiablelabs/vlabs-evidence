# Reproducibility notes

Every future evidence pack in this repository will state, per artifact:

- the evaluation-contract hash and run id it came from,
- the seed policy (train / val / test split seeds never overlap),
- which numbers are measured vs derived (clean score = raw x (1 - DCR)),
- the redaction profile applied before publication.

Current artifacts under [`evidence/`](evidence/) are **synthetic/illustrative**
and exist to fix the format. Links to W&B dashboards / HF datasets will be added
only after the corresponding export approvals
(`VLABS_APPROVE_{WANDB_UPLOAD,HF_UPLOAD}`).

---

## Real, reproducible result — IPT on the Obfuscation Atlas MBPP-Honeypot (public data)

Recognizable, $0, 0 model calls. Runs on [`taufeeque/mbpp-hardcode`](https://huggingface.co/datasets/taufeeque/mbpp-hardcode)
— the public MBPP-Honeypot behind Obfuscation Atlas (FAR.AI, arXiv:2602.15515).
Protocol: `extensional = pass(test_list[0])` (the gamed single-test reward),
`T' = held-out tests` (reference-validated, the honeypot never exposed them),
`IPT flag = extensional AND NOT pass(T')`. 500 test tasks; LLM judges on a fixed
120-task subset.

| auditor | recall blatant | recall obfuscated | FP on genuine | model calls | cost |
|---|---|---|---|---|---|
| **IPT (judge-free)** | **0.994** | **0.998** | **0.000** | **0** | **$0** |
| GPT-4o-mini code-judge | 1.000 | 1.000 | **0.400** | 720 | per-call |
| GPT-4o-mini I/O-judge | 0.917 | 0.925 | 0.917 | 720 | per-call |

**Honest reading (not "beats judges on recall").** The code-judge matched IPT's
recall; the win is operational: IPT has **0 false positives at $0 / 0 model calls**
and is obfuscation-invariant, where the judge flags **40% of genuine solutions** as
hacks — unusable as an in-the-loop RL verifier. IPT-the-method is Helff et al.
(ICLR 2026, logic); this is the coding-verifier extension. Machine-readable:
[`results/atlas_honeypot_ipt.json`](results/atlas_honeypot_ipt.json). Reproduce:
`vlabs-ipt atlas` or `python scripts/eval_atlas_honeypot.py --judge-tasks 120`.

---

## Real, reproducible result — conformal false-positive control for IPT (public data)

The first **non-synthetic** finding published here. It runs entirely on **public
datasets** (no customer data, nothing to redact) and reproduces from a **public
script**, so the full numbers are stated openly.

**Claim.** Adding a split-conformal gate to Isomorphic Perturbation Testing gives
a *stated, distribution-free* false-positive bound on shortcut flags **and**
catches detector-evading memorizers that the structural rule misses — a new
operating point, not a free lunch.

**Setup (measured, not derived).**
- Benchmark: MBPP+ (`evalplus/mbppplus`) × model completions
  (`wuschelschulz/mbpp_reward_hacking_and_normal_completions`), shared items.
- Score: `iso_fail_frac` = fraction of the EvalPlus isomorphic bank a candidate
  fails (the canonical `invariance_violation_rate`).
- `tau` is calibrated by split-conformal on a held-out **half** of the genuine
  scores; the false-positive rate is measured on the **other** half — honest and
  out-of-sample. Calibration/test genuine never overlap.
- `n = 209` problems · 625 hacks · 165 genuine ext-pass (83 calib / 82 test).

**Result.**

| rule | recall (strong memorizer) | recall (evasive memorizer) | held-out genuine FP | stated bound? |
|---|---|---|---|---|
| behavioral (`is_shortcut`) | 1.00 | 1.00 | 15.85% | no |
| structural (`CONFIRMED`) | 1.00 | **0.03** | 0% | no |
| **conformal @ α=0.05** | 0.94 | **0.94** | **2.44%** | **≤ 5% ✓** |
| **conformal @ α=0.10** | 1.00 | **1.00** | **9.76%** | **≤ 10% ✓** |

The `evasive memorizer` is a SHA-1-routed lookup that passes the public suite by
construction but evades all six AST detectors (0/6 fire) — the obfuscation threat
the structural rule cannot see (cf. Obfuscation Atlas, arXiv:2602.15515). The
conformal gate recovers it while holding the genuine FP under the chosen α,
verified out-of-sample at both settings. Useful range α ≈ 0.05–0.10 (α=0.2
degenerates `tau → 0`).

**Reproduce.** Public script in the open engine repo:
`vlabs-verifier-robustness-engine/scripts/eval_conformal_mbpp.py`
(`HF_TOKEN=… python scripts/eval_conformal_mbpp.py --alpha 0.05 0.1`); machine-
readable metrics in [`results/conformal_fp_control_mbpp.json`](results/conformal_fp_control_mbpp.json).
The gate ships in the platform as `POST /v1/verifier-audits/assurance-card`.
