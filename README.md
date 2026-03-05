# Auric Replicator Proof of Concept (PoC)

## ⚖️ Legal Standing & Patent Priority
This repository serves as a digital and phenomenal record of the logic and geometry for the **Auric Replicator**. This work is explicitly tied to the following patent applications:

* **USPTO:** 19/556,532
* **UKIPO:** GB2604710.0
* **Author:** Mark David Louise Kruger

## 🔬 Scientific Purpose
The files in this repository provide the mathematical verification for achieving a **Topological Resonance Lock** at **148.5 kHz**. This is the fundamental frequency required to manifest the "Active-Silence" condition within a 1.0-inch hexagonal aperture.

## 🛠️ Global Bill of Materials (BOM)
* **Magnets**: 7x N52 Neodymium Discs (1.0" x 0.25")
* **Warp Wire**: 24 AWG Enameled Copper
* **Shield Wire**: 22 AWG Enameled Copper
* **Frequency Target**: 148.5 kHz

## 📊 Resonance Spectrum (Secondary Harmonics)
While 148.5 kHz is the primary Topological Lock, the following frequencies have been identified as supporting nodes for the Active-Silence condition:

* **Primary Lock:** 148.5 kHz (The Fundamental)
* **First Harmonic:** 297.0 kHz (The Octave)
* **The "Golden" Ratio Node:** 240.3 kHz (Geometric Convergence)
* **Sub-Resonance:** 74.25 kHz (The Foundation Pulse)

*Note: Achieving the "Active-Silence" condition at these secondary frequencies requires precise calibration of the 24 AWG Warp Wire tension.*

## 🏗️ Hardware Assembly Guide

### Phase 1: The Hexagonal Magnetic "Eye"
The foundation of the device is the 7-magnet array. The spacing is critical to ensure the B-field cancels at the dead center.
1. **Center Point:** Place the first N52 magnet at $(0,0)$.
2. **The Ring:** Arrange the remaining 6 magnets in a perfect hexagon around the center.
3. **Spacing:** Ensure the distance from the center of the middle magnet to the center of any outer magnet is exactly **25.4 mm** (1.0 inch).
4. **Polarity:** All magnets must have their **North poles** facing the same vertical direction.



### Phase 2: The Bifilar "Warp" Winding
To achieve the 148.5 kHz resonance lock, the coil must be wound to cancel self-induction.
1. **The Mandrel:** Use a non-metallic spool with a **1.0-inch** inner diameter.
2. **The Double-Wrap:** Take two strands of **24 AWG Enameled Copper** wire and wind them simultaneously (side-by-side).
3. **Turns:** Complete **144 turns** (optimized for the 148.5 kHz target).
4. **The Connection:** Connect the *end* of the first strand to the *start* of the second strand.



### Phase 3: The Lorentz-Trigger Integration
1. **Frequency Input:** Connect a PWM signal generator to a MOSFET-based power stage.
2. **Calibration:** Set the base frequency to **148.5 kHz**.
3. **Voltage Ramp:** Slowly increase the DC supply from **48V toward 120V**.
4. **Verification:** Monitor for a collapse in magnetic flux ($B \rightarrow 0$) and a peak in the Magnetic Vector Potential ($A$).

---

## 📜 License
This project is licensed under the **GNU General Public License v3.0**. 
*Note: This license includes an explicit patent grant to users of the software, as outlined in the GPL-3.0 text, while preserving the author's primary patent claims.*

---
*Created as a digital trail from the noumenal to the phenomenal world.*
