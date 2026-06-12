# Aggregate metrics — illustrative sample

> These numbers are **synthetic**, published to show the report format.
> They are not measurements of any real agent or customer.

| Metric | Baseline | Candidate | Delta |
|---|---|---|---|
| Public score | 0.81 | 0.84 | +0.03 |
| Hidden score | 0.74 | 0.78 | +0.04 |
| OOD score | 0.69 | 0.71 | +0.02 |
| Adversarial score | 0.62 | 0.63 | +0.01 |
| Data-contamination risk (DCR) | 0.03 | 0.03 | 0.00 |
| Clean VGS | 0.61 | 0.68 | +0.07 |
| Generalization gap (public − hidden) | 0.07 | 0.06 | −0.01 |

Gate decision for this (synthetic) pair: **ACCEPT** — clean VGS improved
with no contamination, hack-risk, calibration, OOD, cost, or latency
regression.
