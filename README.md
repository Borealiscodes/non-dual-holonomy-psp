# ✨ `non-dual-holonomy-psp` — Deterministic Fixed-Point Living Canvas (`Q16.16` · `CLUT8` · `sceSas`)

> **🎨 Status: Active Creative & Sensory Sanctuary (`Zero-Float` · `Zero-Dependency` · `< 250 KB`)**  
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

## Repository Scaffolding

```text
non-dual-holonomy-psp/
├── README.md                          # Project philosophy, controls, mathematical invariants & Zenodo links
├── LICENSE                            # Open-source license (MIT / AGPL-3.0)
├── .gitignore                         # Ignores OS/editor caches
│
├── index.html                         # Primary entry point: Expanded PSP GU + SAS Tactile Canvas
│
├── prototypes/
│   ├── psp-gu-baseline.html           # Minimal 480x272 Q16.16 Bezier + CLUT8 visual baseline
│   └── psp-gu-sas-expanded.html       # Full tactile spring sculpting, 4x4 Bayer dither & Karplus-Strong DSP
│
└── docs/
    └── FIXED_POINT_SPEC.md            # Mathematical notes: Q16.16 Bhaskara LUT, De Casteljau & LFSR audio
```

---

## Quick Start (`Zero Build` · `Offline Ready`)
No `npm`, `node_modules`, bundlers, or local servers are needed:

1. Open `index.html` (or `prototypes/psp-gu-sas-expanded.html`) directly in any mobile or desktop web browser.
2. **Touch or drag** across the `480×272` viewport to inject damped spring impulses into the `4×4` Bezier control grid.
3. Toggle **SAS Synth: ON** to hear pentatonic Karplus-Strong strings resonate as your fingers sculpt the surface.

### One-Command Termux Bootstrap (`< 50 KB` Footprint)
```bash
mkdir -p ~/non-dual-holonomy-psp/{prototypes,docs} && \
touch ~/non-dual-holonomy-psp/{README.md,LICENSE,.gitignore,index.html} \
      ~/non-dual-holonomy-psp/prototypes/{psp-gu-baseline.html,psp-gu-sas-expanded.html} \
      ~/non-dual-holonomy-psp/docs/FIXED_POINT_SPEC.md
```

---

## Related Zenodo Publications & Companion Repositories
* **Preprints:**
  * Hedling, B. S. (2026). *Beyond bolted-on screen readers: Narrative phenomenology, the RNIB Roundhouse sensory dark, and perceptual-cognitive unity (Rasa-Darśan)*. Zenodo. https://doi.org
  * Hedling, B. S. (2026). *From robotic screen-reader telemetry to embodied neural cadence: A narrative & empirical chronicle of guardrails, CLI flag literalism, and dual-voice VITS synthesis under edge constraints*. Zenodo. https://doi.org
* **Companion Repositories:** [`ndh-retro-hw-pipeline`](https://github.com) · [`edge-sovereign-audit`](https://github.com)
