"""
TIFC-V3.4: Emergent Thalamocortical Gating via PAC and Landauer Cost
Author: Alejandro Vaquero Barriero (2026)
"""
import numpy as np
kB = 1.380649e-23
T = 310.0
LANDAUER = kB * T * np.log(2)

def generate_signals(n=5000, fs=500):
    t = np.arange(n)/fs
    theta_freq = 6.0
    gamma_freq = 80.0
    theta_phase = np.angle(np.exp(1j*2*np.pi*theta_freq*t))
    pac_strength = 0.8
    gamma_amp = 1.0 + pac_strength * (np.sin(theta_phase) + 1)/2
    gamma = gamma_amp * np.sin(2*np.pi*gamma_freq*t)
    return t, theta_phase, gamma_amp

def modulation_index(theta_phase, gamma_amp, n_bins=18):
    bins = np.linspace(-np.pi, np.pi, n_bins+1)
    digitized = np.digitize(theta_phase, bins) - 1
    mean_amp_per_bin = np.array([np.mean(gamma_amp[digitized==b]) if np.any(digitized==b) else 0 for b in range(n_bins)])
    prob = mean_amp_per_bin / (np.sum(mean_amp_per_bin)+1e-12)
    H = -np.sum(prob * np.log(prob + 1e-12))
    MI = (np.log(n_bins) - H) / np.log(n_bins)
    return MI

def main():
    t, theta_phase, gamma_amp = generate_signals()
    MI = modulation_index(theta_phase, gamma_amp)
    bits = 10 * (1 - MI) + 1
    cost = bits * LANDAUER
    p_gate = 1/(1+np.exp((cost - 1e-21)/(1e-22)))
    print(f"MI: {MI:.4f}, Cost: {cost:.3e} J, p_gate: {p_gate:.3f}")

if __name__ == "__main__":
    main()
