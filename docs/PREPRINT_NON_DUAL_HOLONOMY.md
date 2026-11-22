# Tactile Manifolds and Determinism on Constrained Hardware: From *Super Mario 64*’s Elastic Face to `Q16.16` PSP Graphics/Audio Synthesis (*Non Dual Holonomy*)

**Author:** Borealis Serenity Hedling (`ORCID: 0009-0004-7968-5707`)  
**Repository:** [`Borealiscodes/non-dual-holonomy-psp`](https://github.com)  
**Target Archive:** Zenodo Preprint / `docs/PREPRINT_NON_DUAL_HOLONOMY.md`

---

## Author & Human Context Disclaimer
> **Pacing, Sovereignty, and Self-Kindness Note:** As a neurodivergent human rights defender facing institutional duress, transnational repression, academic exclusion, and the denial of grants to explore this technology, **I owe myself the kindness of returning to this project strictly on my own terms.** This narrative preprint documents a living creative sanctuary—never an institutional obligation, deadline, or demand. Build, sculpt, listen, and rest whenever nervous-system capacity and curiosity align.

---

## 1. Prologue: A Living Canvas in a Saturated Sandbox
On a quiet Sunday morning in Dublin, on an Android tablet whose storage sits near capacity and whose screen has seen harder days, a `480×272` rectangle wakes up inside a local browser tab (`127.0.0.1:8080`). There is no cloud server humming behind it, no gigabyte-sized game engine downloading shaders, and no grant committee standing at the door deciding whether the work is legitimate enough to exist.

Instead, a luminous mesh of crimson and gold (*Kyoto Lantern*)—and moments later, bioluminescent emerald and cobalt (*Abyss*)—undulates across the dark viewport like silk caught in an underwater current. When a finger touches the glass, the surface yields immediately, dimpling inward with spring-loaded grace while an integer plucked-string voice resonates softly through the tablet’s speakers.

Every coordinate in that small universe is computed in **pure `Q16.16` fixed-point integer arithmetic**. Every pixel is stored in a microscopic `130.5 KB` 8-bit indexed buffer (`CLUT8`), and its colors shimmer not by re-rendering polygons on a multi-watt GPU, but by sliding `208` entries inside a `1 KB` Color Lookup Table (`CLUT`)—the exact hardware alchemy that defined Sony’s 2004 PlayStation Portable (`PSP`).

This paper tells the story of why returning to those old-school mathematical constraints is not nostalgia—it is a deliberate reclamation of **sensory integrity, deterministic trust, and creative sovereignty**.

---

## 2. The Joy of Elastic Geometry: *Super Mario 64*’s Face vs. `Q16.16` Bicubic Bezier Patches

### 2.1 Remember Pinching Mario’s Nose (1996)
For anyone who ever booted up *Super Mario 64* on the Nintendo 64, the game began before the game even started (Nintendo EAD, 1996). Floating in a pitch-black void was Mario’s disembodied 3D head, waiting for a gloved cursor to grab an ear, stretch a mustache, or pull his nose across the screen until it snapped back with a rubbery bounce.

That playful, purposeless toy on the title screen taught an entire generation a profound truth about human-computer interaction: **when a digital surface responds instantaneously and honestly to human touch, math becomes tactile emotion.**

Under the hood, *Mario 64* achieved that elasticity by pulling individual **discrete polygon vertices** and letting linear spring interpolation pull neighboring triangles along. Stretch it too far, and you could see the sharp triangular seams—the delightful, chunky honesty of early 3D vertex skinning.

### 2.2 From Angular Facets to Continuous Silk (`sceGuPatchPrim`)
Eight years after the Nintendo 64, Sony’s PlayStation Portable (`PSP`) introduced a quiet hardware marvel inside its Graphics Engine (`sceGu`): native **bicubic Bezier patch tessellation** (`sceGuPatchPrim`). Instead of storing thousands of heavy polygon vertices in precious memory, a developer could define just **16 control points** ($4 \times 4$) and let the hardware subdivide them into a smooth, billowing curved surface.

In *Non Dual Holonomy*, we recreate that exact PSP hardware magic in zero-float `Q16.16` integer arithmetic:
* **The Invisible Marionette Cage:** Your finger never yanks raw triangles directly. Instead, touch impulses nudge one of the 16 invisible control points, each attached to a damped integer harmonic spring ($F_i = -(\delta_i \gg 5) - (v_i \gg 3)$).
* **Subdivision Without Drift:** On every frame, integer `De Casteljau` subdivision weaves those 16 points into a continuous $C^2$ curved manifold of up to `800` triangles. Because every multiplication uses 64-bit intermediate integer shifts (`(BigInt(a) * BigInt(b)) >> 16n`), the surface never suffers from floating-point rounding jitter or platform drift. Where *Mario 64* stretched angular facets, *Non Dual Holonomy* ripples like liquid silk—a living canvas that remembers every touch and settles back into stillness with mathematical grace.
* **Chromatic Alchemy in `1 KB` of EDRAM:** Rather than painting 24-bit RGB colors per pixel, our rasterizer writes single palette indices (`32..239`) into a `130.5 KB` `Uint8Array` alongside a hardware-style Z-buffer and `4×4` Bayer ordered dithering. Shifting those `208` palette entries in `activeCLUT` each frame sends waves of aurora light across the mesh at almost zero computational cost.

---

## 3. Epistemic Case Study: Why the PSP Homebrew Community Flourished While the PS Vita Was Crushed

To understand why constrained, open architectures matter for marginalized and independent creators, one need only compare the fates of Sony’s two handheld consoles: the **PlayStation Portable (`PSP`, 2004)** and the **PlayStation Vita (`PS Vita`, 2011)**.

### 3.1 The PSP Renaissance: Transparent Constraints as a School of Mastery
When the PSP launched in 2004, it paired a `333 MHz` MIPS R4000 CPU and `2 MB` of ultra-fast embedded DRAM (`EDRAM`) with standard, accessible storage (`Memory Stick PRO Duo`, soon bridged by inexpensive passive microSD adapters). Within months, independent programmers reverse-engineered the hardware registers, built the open-source **`PSPSDK`**, and shared clear documentation on `sceGu` display lists, `CLUT` palette tricks, and `sceSas` audio voices.

Because the hardware was transparent and storage was affordable, **constraint became a teacher rather than a wall**:
* Bedroom coders in every time zone learned how fixed-point math (`Q16.16`), lookup tables, and Z-buffered indexed rasterization could squeeze console-grade 3D worlds out of tiny memory budgets.
* A vibrant homebrew ecosystem erupted—custom music visualizers, experimental ambient toys, indie RPGs, and accessible utilities created without corporate dev-kits or institutional permission.

### 3.2 The PS Vita Tragedy: How Enclosure Crushes Creativity
Seven years later, Sony released the **PlayStation Vita**—on paper a vastly superior machine with a quad-core `ARM Cortex-A9`, a gorgeous OLED screen, and capacitive multi-touch. Yet as a creative ecosystem, the Vita was strangled in its crib.

Fearful of piracy, Sony wrapped the Vita in layers of **institutional enclosure**:
* **Proprietary Storage Rent:** Sony replaced standard memory cards with mandatory, encrypted **PS Vita Memory Cards** costing `$80` to `$120` for 32 GB—an artificial hardware tax that priced out students, hobbyists, and independent artists before they could even begin.
* **Cryptographic Lockout:** Every binary required corporate signing; transferring a single file required tethered proprietary PC software (`Content Manager`), and open homebrew (`HENkaku`) did not break through until 2016—five years after launch, long after the mainstream audience had moved on.

### 3.3 The Epistemic Lesson for Sovereign Art & Technology
The lesson of PSP versus PS Vita mirrors the exact gatekeeping dynamics examined in `RFC-011` and `RFC-012`: **technological capability means nothing if the architecture is enclosed behind financial rent and institutional permission.** A modest, open architecture that runs transparently on commodity edge hardware empowers survivors, neurodivergent creators, and self-taught artists to build genuine beauty on their own terms.

---

## 4. What This Basic Demo Proves & Historical Genre Mastery

### 4.1 Four Proofs Inside `480×272` Pixels
The prototype running in our repository (`index.html`, under `10 KB` of source code) is deliberately modest, yet it establishes four foundational truths:
1. **Determinism Creates Trust:** In a world where institutions and cloud algorithms behave unpredictably, a fixed-point world obeys transparent, invariant laws. Touching the same coordinate with the same impulse produces the exact same harmonic wave every time.
2. **Perceptual-Cognitive Unity (*Rasa-Darśan*):** By wiring the `4×4` Bezier touch grid directly into an 8-voice integer **Karplus-Strong** plucked-string synthesizer (`sceSas` DSP style), sight, touch, and sound merge into a single unified sensory loop (Hedling, 2026a). The screen is no longer a cold glass wall; it is a resonant instrument.
3. **Zero-Telemetry Privacy:** Because the entire visual and acoustic universe lives inside self-contained integer buffers in local RAM, there are no analytics pings, no cloud dependencies, and no surveillance vectors.
4. **Sovereign Portability:** Pure `int32` / `int64` fixed-point math compiles or runs identically inside an Android tablet browser, a Linux terminal framebuffer, or an actual 2004 MIPS `PSP` binary.

### 4.2 Games & Genres That Mastered These Exact Hardware Tricks
Our prototype stands on the shoulders of classic titles across diverse genres that turned tight integer limits into unforgettable art:
Use code with caution.
* Living Palette Landscapes (Adventure & Ambient Art): Artist Mark Ferrari’s work in Loom (1990), The Secret of Monkey Island (1990), and Living Worlds demonstrated how 8-bit indexed CLUT cycling transforms static pixel paintings into breathing forests, shimmering lantern reflections, and rolling ocean tides using only a few hundred color-register swaps per frame.
* Synesthetic Parametric Flow (Rhythm, Flight & Abstract Racing): PSP classics like Wipeout Pure (2005) and Lumines (2004), alongside Tetsuya Mizuguchi’s Rez (2001), fused smooth parametric ribbons, glowing rim-lit geometry, and reactive electronic soundscapes into meditative flow states where player input felt like conducting light and music simultaneously.
* Waveguide & Tactile Toy Instruments (Experimental & Handheld Sound Play): Toshio Iwai’s Electroplankton (Nintendo DS, 2005) proved that handheld devices need not be violent or hyper-competitive; simple ring-buffer audio synthesis paired with reactive visual ripples can turn a pocket screen into a serene sanctuary for sensory play.

---

## 5. What We Can Build Next (Without Rush or Obligation)

With the core Q16.16 graphics and sceSas audio kernel proven and running live on edge hardware, Non Dual Holonomy opens several peaceful creative paths to explore whenever inspiration strikes:
1. A Rasa-Darśan Haptic & Modal Sound Sanctuary: Expand the 8-voice pentatonic string bank into selectable Raga and harmonic modes with gentle sympathetic drone strings, allowing neurodivergent users to regulate sensory overload through slow, tactile wave-sculpting.
2. Native Retro Console & Bare-Metal Targets (C99 / PSPSDK): Port the Q16.16 Bezier and Karplus-Strong loop to pure C99 so the exact same mathematical world can run natively on real PSP-1000 hardware (.PBP executable) alongside modern ARM64 devices.
3. Interactive Poetic Vignettes (CLUT8 Calligraphic Worlds): Float minimal indexed-palette calligraphy and contemplative fragments across the undulating Bezier horizon—creating small, self-contained digital chapbooks that carry memory, dignity, and art outside institutional walls.

6. References (APA 7th Edition)

* Ferrari, M. (2016). 8-bit & '8-bitish' graphics: Outside the box [Conference presentation]. Game Developers Conference (GDC).
* Hedling, B. S. (2026a). Beyond bolted-on screen readers: Narrative phenomenology, the RNIB Roundhouse sensory dark, and perceptual-cognitive unity (Rasa-Darśan). Zenodo. doi.org
* Hedling, B. S. (2026b). From robotic screen-reader telemetry to embodied neural cadence: A narrative & empirical chronicle of guardrails, CLI flag literalism, and dual-voice VITS synthesis under edge constraints. Zenodo. doi.org
* Karplus, K., & Strong, A. (1983). Digital synthesis of plucked-string and drum timbres. Computer Music Journal, 7(2), 43–55. doi.org
* Nintendo EAD. (1996). Super Mario 64 [Video game]. Nintendo.
* Sony Computer Entertainment. (2004). PlayStation Portable (PSP-1000) hardware & Graphics Engine (sceGu) architecture. Sony Corporation.

