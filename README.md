# TIFC-V3.4: Emergent Thalamocortical Gating via PAC and Landauer Cost

**Author:** Alejandro Vaquero Barriero (2026)
**Affiliation:** Independent Researcher, Barcelona

### Abstract
This model proposes a novel mechanism for conscious access: thalamocortical gating emerges from Phase-Amplitude Coupling (PAC) between Theta (6Hz) and Gamma (80Hz) rhythms, gated by a thermodynamic Landauer cost.

The gating probability is: p_gate = 1 / (1 + exp((Cost - threshold)/kT))

### How to run
```bash
pip install numpy
python tifc_v34.pyExpected output: MI ∼0.2-0.5, Cost ∼1e-20 J, p_gate < 1.0
License: MIT
DOI: (pending Zenodo integration)
