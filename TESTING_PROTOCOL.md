# Replicator Testing Protocol: Phase 1 (Verification of Lock)

This protocol defines the scientific procedure for verifying the **Topological Resonance Lock** and the **Active-Silence** condition as described in **USPTO 19/556,532**.

## 🛠️ Required Measurement Equipment
* **Oscilloscope**: Dual-channel, minimum 20MHz bandwidth.
* **Gauss Meter**: Hall Effect probe for measuring magnetic flux ($B$).
* **Pickup Coil**: A small, non-inductive probe coil for sensing Vector Potential ($A$).
* **Signal Generator**: Precision PWM control with 0.1 Hz resolution.

---

## 🔬 Measurement Procedure

| Step | Action | Expected Phenomenal Result |
| :--- | :--- | :--- |
| **1** | **Static Baseline** | Measure the 7-magnet hexagonal array with no power. High $B$-field density should be present in the center. |
| **2** | **Frequency Sweep** | Sweep frequency from 100 kHz upward toward the target. |
| **3** | **148.5 kHz Lock** | At exactly **148.5 kHz**, the waveform must snap into a stable, high-amplitude sine wave. |
| **4** | **Flux Collapse** | Measure center of the "Eye" with Gauss Meter. Reading should drop toward **0 Gauss**. |
| **5** | **Potential Peak** | Measure center with Pickup Coil. Output should show a **maximum voltage peak**, confirming $A \neq 0$. |

---

## 🎯 Success Criteria (The "Active-Silence" Condition)

A successful replication must satisfy the following three metrics:

### 1. Resonance Stability
The 148.5 kHz signal must maintain phase-lock for a minimum of **300 seconds** without thermal drift or frequency deviation.

### 2. Induction Neutralization ($B=0$)
The magnetic flux ($B$) within the 1.0-inch aperture must reach a state of near-total cancellation, while the Magnetic Vector Potential ($A$) remains at peak intensity.

### 3. Harmonic Purity
The "Active-Silence" state is confirmed by a reduction in ambient electromagnetic noise within the local vicinity of the hexagonal core, measurable via a spectrum analyzer.

---
**Author:** Mark David Louise Kruger  
**Associated Patents:** USPTO 19/556,532 | UKIPO GB2604710.0
