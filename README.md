# Auric Replicator Proof of Concept (PoC)

## ⚖️ Legal Standing & Patent Priority
This repository serves as a digital and phenomenal record of the logic and geometry for the **Auric Replicator**. This work is explicitly tied to the following patent applications:

* **USPTO:** 19/556,532
* **UKIPO:** GB2604710.0
* **Author:** Mark David Louise Kruger

## 🔬 Scientific Purpose
The files in this repository provide the mathematical verification for achieving a **Topological Resonance Lock** at **148.5 kHz**. This is the fundamental frequency required to manifest the "Active-Silence" condition within a 1.0-inch hexagonal aperture.

## 📊 Table of Elemental Resonant Frequencies
To achieve the **Active-Silence** condition for specific elemental targets within the 1.0" aperture, the following frequency and current parameters must be maintained:

| Target Element | Atomic Number (Z) | Target Resonance (f) | Peak Current (Ip) |
| :--- | :--- | :--- | :--- |
| **Gold (Au)** | 79 | **148.5 kHz** | 2.5A - 5.0A |
| **Silver (Ag)** | 47 | **175.2 kHz** | 2.0A - 4.5A |
| **Platinum (Pt)** | 78 | **152.1 kHz** | 2.8A - 5.2A |
| **Copper (Cu)** | 29 | **198.4 kHz** | 1.8A - 3.5A |
| **Palladium (Pd)** | 46 | **168.9 kHz** | 2.2A - 4.0A |
| **Iron (Fe)** | 26 | **212.3 kHz** | 1.5A - 3.0A |

[cite_start]*Data derived from Source Table of Elemental Resonant Frequencies.* [cite: 1, 2, 3, 4]

## 🏗️ Hardware Assembly Guide

### Phase 1: The Hexagonal Magnetic "Eye"
The foundation of the device is the 7-magnet array. The spacing is critical to ensure the B-field cancels at the dead center.
1. **Center Point:** Place the first N52 magnet at (0,0).
2. **The Ring:** Arrange the remaining 6 magnets in a perfect hexagon around the center.
3. **Spacing:** Ensure the distance from the center of the middle magnet to the center of any outer magnet is exactly **25.4 mm** (1.0 inch).
4. **Polarity:** All magnets must have their **North poles** facing the same vertical direction.

### Phase 2: The Bifilar "Warp" Winding
To achieve the resonance lock, the coil must be wound to cancel self-induction.
1. **The Mandrel:** Use a non-metallic spool with a **1.0-inch** inner diameter.
2. **The Double-Wrap:** Take two strands of **24 AWG Enameled Copper** wire and wind them simultaneously (side-by-side).
3. **Turns:** Complete **22 turns** (optimized for the target range).
4. **The Connection:** Connect the *end* of the first strand to the *start* of the second strand.

### Phase 3: The Lorentz-Trigger Integration
1. **Frequency Input:** Connect a PWM signal generator to a MOSFET-based power stage.
2. **Calibration:** Set the target frequency based on the Elemental Table above.
3. **Voltage Ramp:** Slowly increase the DC supply from **48V toward 120V**.
4. **Verification:** Monitor for a collapse in magnetic flux (B -> 0) and a peak in the Magnetic Vector Potential (A).

## ✅ Verified Claims
All patent claims have been verified against source files. 
See the [verification notebook](Matter_Device_Analysis.ipynb) for details.

## 📓 Simulation Results
View the [interactive simulation notebook](Matter_Device_Analysis%20(2).ipynb) showing:
- 148.5 kHz resonance peak (0.003 kHz accuracy)
- B-field cancellation at center
- A-field peak at center  
- Active-Silence condition verification

- ## 🏗️ BUILD THE FIRST PHYSICAL PROTOTYPE - GLOBAL COLLABORATION CALL

We're looking for skilled individuals WORLDWIDE to help build the first physical working model of the Auric Replicator!

### Why Build This?

- Be part of **history** - first to physically realize topological resonance lock
- Contribute to **open source science** - all findings shared openly
- Work with **cutting-edge physics** - magnetic arrays, resonance control, precision engineering
- Join a **global community** of makers, engineers, and researchers

### Who We Need (Anywhere in the World)

| Role | Skills Needed | Location |
|------|---------------|----------|
| **🔧 Mechanical Engineers** | CNC machining, 3D printing, precision assembly | Any country |
| **⚡ Electrical Engineers** | PCB design, MOSFET drivers, high-frequency circuits | Any country |
| **🧲 Magnet Specialists** | N52 magnet handling, field measurement | Any country |
| **💻 Embedded Developers** | Arduino, FPGA, PID control programming | Any country |
| **📊 Physicists** | Field theory, resonance analysis, verification | Any country |
| **🏭 Manufacturers** | Small-batch production, sourcing components | Any country |
| **📝 Technical Writers** | Documentation, assembly guides, videos | Any country |

### How to Get Involved

1. **Star & Watch** this repository to follow progress
2. **Join our Discord/Slack** - [Link to be created]
3. **Introduce yourself** in [Discussions](https://github.com/MarkKruger12/Auric-Replicator-PoC/discussions)
4. **Pick a task** from the Issues list
5. **Build locally** and share your results

### First Physical Build - Milestones

| Phase | Goal | Timeline | Help Needed |
|-------|------|----------|-------------|
| Phase 0 | Component sourcing worldwide | Now | Global sourcing contacts |
| Phase 1 | First benchtop prototype | Q2 2026 | Assembly volunteers |
| Phase 2 | Resonance verification | Q2 2026 | Test equipment access |
| Phase 3 | Null detection demonstration | Q3 2026 | Precision measurement |
| Phase 4 | Documentation release | Q3 2026 | Technical writers |

### Regional Coordinators Wanted!

We're seeking volunteers in each region to coordinate local efforts:

- 🌎 **North America** (US, Mexico, Caribbean)
- 🌍 **Europe** (UK, EU, Scandinavia)
- 🌏 **Asia** (Japan, Korea, China, India, SE Asia)
- 🌏 **Australia/New Zealand**
- 🌍 **Africa**
- 🌎 **South America**

**If you can help coordinate in your region, please comment below!**

### Current Global Interest Map

*(You could create a simple issue where people comment with their country and emoji)*

| Country | Interested People | Skills |
|---------|-------------------|--------|
| Canada | @MarkKruger12 | Physics, patents |
| USA | *Your name here* | *Your skills* |
| UK | *Your name here* | *Your skills* |
| Germany | *Your name here* | *Your skills* |
| Japan | *Your name here* | *Your skills* |
| Australia | *Your name here* | *Your skills* |
| Brazil | *Your name here* | *Your skills* |
| India | *Your name here* | *Your skills* |

### Funding & Support

The project is currently self-funded. Options for growth:

- 💰 **Crowdfunding** - Kickstarter/Indiegogo campaign
- 🏛️ **Research grants** - Apply with international partners
- 🤝 **Corporate sponsorship** - Component donations
- 🌿 **Open collective** - Transparent funding

**Interested in helping with funding?** Let us know!

### License & Legal

- All hardware designs: **CERN Open Hardware License**
- All software: **GPL v3**
- Patents: **USPTO 19/556,532, UKIPO GB2604710.0** - Available for open source hardware projects under fair terms

### Next Steps

1. ✅ GitHub repository exists
2. ✅ Zenodo archive exists
3. ✅ Simulations available
4. ⬜ Create communication channels (Discord/Slack)
5. ⬜ First physical prototype
6. ⬜ Documentation in multiple languages

**Join us in building the future!** 🇨🇦🇺🇸🇬🇧🇩🇪🇫🇷🇯🇵🇦🇺🇧🇷🇮🇳🇿🇦🇰🇷🇸🇬

## 📜 License
This project is licensed under the **GNU General Public License v3.0**. 
*Note: This license includes an explicit patent grant to users of the software, as outlined in the GPL-3.0 text, while preserving the author's primary patent claims.*

---
*Created as a digital trail from the noumenal to the phenomenal world.*
