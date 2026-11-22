# ✨ `non-dual-holonomy-psp` — Deterministic Fixed-Point Living Canvas (`Q16.16` · `CLUT8` · `sceSas`)

> **🎨 Status: Complete & Live Creative Sanctuary (`Zero-Float` · `Zero-Dependency` · `< 250 KB`)**  
> Built to run anywhere—from a constrained `ARM64` Android tablet browser to desktop—with zero external dependencies, zero floating-point drift, and zero server overhead.

---

## Author & Human Context Disclaimer
> **Pacing, Sovereignty, and Self-Kindness Note:** As a neurodivergent human rights defender facing institutional duress, transnational repression, academic exclusion, and the denial of grants to explore this technology, **I owe myself the kindness of returning to this project strictly on my own terms.** Unlike institutional systems, this fixed-point canvas is a quiet creative sanctuary—never a deadline, obligation, or demand. Touch, sculpt, listen, or step away whenever your nervous system and curiosity choose.

---

## Artistic & Architectural Philosophy (*Rasa-Darśan* & Fixed-Point Determinism)
*Non Dual Holonomy* explores old-school console hardware constraints (`PlayStation Portable sceGu / sceSas`) as a medium for **perceptual-cognitive unity** (*Rasa-Darśan*):

1. **Deterministic Living Canvas (`Q16.16` Zero-Float Math):** Every Bezier patch vertex, orbital rotation matrix, and damped touch-spring impulse runs in pure integer `Q16.16` arithmetic (1.0 = 65536). The surface responds identically and reliably to human touch on every frame without floating-point drift.
2. **Microscopic EDRAM & CLUT8 Palette Cycling (`131.5 KB`):** All 3D geometry rasterizes into a `480×272` 8-bit indexed buffer (`130.5 KB`) with a 16-bit depth Z-buffer and `4×4` Bayer ordered dithering, resolved through a live-cycling 256-entry Color Lookup Table (`1 KB`).
3. **Integer Karplus-Strong `sceSas` Voice Synthesis:** Touching or dragging across the undulating manifold plucks an 8-voice deterministic integer string synthesizer (`16-bit` Galois LFSR excitation + two-point integer averaging delay lines), uniting visual wave geometry with tactile acoustic resonance.

---

## Repository Structure

```text
non-dual-holonomy-psp/
├── README.md                                  # Master overview, controls, architecture & Zenodo DOIs
├── .gitignore                                 # Ignores Python/OS/editor caches
│
├── index.html                                 # Primary entry point: Live Q16.16 PSP GU + SAS Tactile Canvas
│
├── prototypes/
│   ├── psp-gu-baseline.html                   # Minimal 480x272 Q16.16 Bezier + CLUT8 visual baseline
│   └── psp-gu-sas-expanded.html               # Expanded tactile spring sculpting, Bayer dither & Karplus-Strong DSP
│
├── docs/
│   ├── FIXED_POINT_SPEC.md                    # Formal math spec: Q16.16 Bhaskara LUT, De Casteljau & LFSR audio
│   ├── PREPRINT_NON_DUAL_HOLONOMY.md          # Narrative preprint: Mario 64 vs. Bezier silk & PSP vs. PS Vita study
│   └── BILL_NYE_PSP_TILE_EXPLAINER.md         # Accessible science explainer tile for students & makers
│
└── tests/
    └── verify_fixed_point.py                  # Zero-dependency Python unittest verifying Q16.16 & LFSR invariants
```

---

## Quick Start (`Zero Build` · `Offline Ready`)
No `npm`, `node_modules`, bundlers, or external servers are required:

1. **Direct Browser Launch:** Open `index.html` (or `prototypes/psp-gu-baseline.html`) directly in any mobile or desktop browser.
2. **Localhost Serve (`Termux` / Desktop — Unlocks Web Audio Cleanly):**
   ```bash
   python3 -B -m http.server 8080 --bind 127.0.0.1
   ```
   Then open **`http://127.0.0`** in your browser.
3. **Interact:**
   * **Touch or drag** across the `480×272` viewport to inject damped integer spring impulses into the `4×4` Bezier control grid.
   * Switch between **Aurora**, **Kyoto**, and **Abyss** `CLUT` themes or toggle **Cycle** and **Rim** borders.
   * Tap **SAS Synth: ON** to hear 8 pentatonic Karplus-Strong waveguide strings resonate as you sculpt the manifold.

### Run Deterministic Math Verification (`0 MB` Dependencies)
```bash
python3 -B tests/verify_fixed_point.py
```

---

## Related Zenodo Publications & Companion Repositories
* **Preprints:**
  * Hedling, B. S. (2026). *Beyond bolted-on screen readers: Narrative phenomenology, the RNIB Roundhouse sensory dark, and perceptual-cognitive unity (Rasa-Darśan)*. Zenodo. https://doi.org/10.5281/zenodo.24393275 
  * Hedling, B. S. (2026). *From robotic screen-reader telemetry to embodied neural cadence: A narrative & empirical chronicle of guardrails, CLI flag literalism, and dual-voice VITS synthesis under edge constraints*. Zenodo. https://doi.org/10.5281/zenodo.24399123
* **Companion Repositories:** [`ndh-retro-hw-pipeline`](https://github.com/Borealiscodes/ndh-retro-hw-pipeline) · [`edge-sovereign-audit`](https://github.com)
