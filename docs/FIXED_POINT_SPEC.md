# `FIXED_POINT_SPEC.md` — Deterministic `Q16.16` Arithmetic, `CLUT8` Rasterization & Integer `sceSas` DSP Specification

**Repository:** `non-dual-holonomy-psp`  
**Document:** `docs/FIXED_POINT_SPEC.md`  
**Target Architecture:** Platform-Agnostic Zero-Float Runtime (`ARM64` Edge / Retro Console `480×272` EDRAM Model)

---

## Author & Human Context Disclaimer
> **Pacing, Sovereignty, and Self-Kindness Note:** As a neurodivergent human rights defender facing institutional duress, transnational repression, academic exclusion, and the denial of grants to explore this technology, **I owe myself the kindness of returning to this project strictly on my own terms.** This mathematical specification documents the integer invariants of *Non Dual Holonomy* as a peaceful creative reference—never a deadline or obligation. Touch, play, rest, and step away whenever your nervous system and curiosity choose.

---

## 1. Number Representation (`Q16.16` Signed Fixed-Point)

All spatial coordinates, Bezier parameters, rotation matrices, and tactile spring states are represented in **signed 32-bit `Q16.16` fixed-point format** ($x_{\text{Q16}} \in \mathbb{Z}_{32}$), encoding a real value $x \in [-32768.0,\; 32767.999985]$ as:

$$x_{\text{Q16}} = \left\lfloor x \cdot 2^{16} \right\rfloor = \left\lfloor 65536 \cdot x \right\rfloor$$

### 1.1 Exact Multiplication (`mulQ16`)
To prevent intermediate 32-bit overflow during multiplication of two `Q16.16` operands $a_{\text{Q16}}, b_{\text{Q16}}$, products are promoted to 64-bit signed integers (`BigInt` in JavaScript, `int64_t` in C/Rust) prior to arithmetic right-shift:

$$\text{mulQ16}(a, b) = \left( (a \times_{64} b) \gg 16 \right) \bmod 2^{32}$$

This guarantees **bit-exact determinism** across `ARM64`, `x86_64`, and browser runtimes, eliminating IEEE-754 floating-point rounding drift.

---

## 2. 1024-Brad Integer Bhaskara Sine Lookup Table (`SIN_LUT`)

Angles are discretized into **1024 binary radians (`brads`)** per full revolution ($2\pi \text{ rad} \equiv 1024 \text{ brads}$), allowing modular angle wrapping via a single bitwise `AND` (`theta & 1023`).

For the first quadrant $i \in \{0, 1, \dots, 256\}$ corresponding to $x = \frac{9000 \cdot i}{256}$ (degrees $\times 100$), $\sin(x)$ is synthesized purely in integer arithmetic via **Bhaskara I’s 7th-century rational approximation**:

$$\sin_{\text{Q16}}(i) = \left\lfloor \frac{4 \cdot x(18000 - x) \cdot 65536}{405000000 - x(18000 - x)} \right\rfloor$$

Symmetry identities populate the remaining three quadrants without transcendental functions:
* $\sin_{\text{Q16}}(512 - i) = \sin_{\text{Q16}}(i)$
* $\sin_{\text{Q16}}(512 + i) = -\sin_{\text{Q16}}(i)$
* $\sin_{\text{Q16}}((1024 - i) \bmod 1024) = -\sin_{\text{Q16}}(i)$
* $\cos_{\text{Q16}}(\theta) = \sin_{\text{Q16}}((\theta + 256) \bmod 1024)$

Maximum approximation error across all 1024 entries is $< 0.0016$ ($< 105\text{ LSBs}$ in `Q16.16`).

---

## 3. Bicubic Bezier Patch Tessellation (`De Casteljau` in `Q16.16`)

Given a $4 \times 4$ control grid $\mathbf{P} = \{P_{r,c}\}_{r,c \in \{0..3\}}$ in `Q16.16`, the surface point $S(u, v)$ for normalized parameters $u, v \in [0, 65536]$ is evaluated via two passes of **integer De Casteljau subdivision**:

1. **Cubic Curve Kernel (`evalCubicBezierQ16`):** For control scalars $(p_0, p_1, p_2, p_3)$ and parameter $t \in [0, 65536]$, let $\bar{t} = 65536 - t$:
   $$\begin{aligned}
   a_0 &= \text{mulQ16}(p_0, \bar{t}) + \text{mulQ16}(p_1, t) \\
   a_1 &= \text{mulQ16}(p_1, \bar{t}) + \text{mulQ16}(p_2, t) \\
   a_2 &= \text{mulQ16}(p_2, \bar{t}) + \text{mulQ16}(p_3, t) \\
   b_0 &= \text{mulQ16}(a_0, \bar{t}) + \text{mulQ16}(a_1, t) \\
   b_1 &= \text{mulQ16}(a_1, \bar{t}) + \text{mulQ16}(a_2, t) \\
   B(p_0..p_3; t) &= \text{mulQ16}(b_0, \bar{t}) + \text{mulQ16}(b_1, t)
   \end{aligned}$$
2. **Tensor-Product Surface Evaluation:** Evaluate four row curves at $u$ to obtain intermediate column control points $C_r = B(P_{r,0..3}; u)$, then evaluate $S(u, v) = B(C_{0..3}; v)$.

---

## 4. Tactile Harmonic Spring Field (Stylus / Touch Coupling)

Each control point $i \in \{0, \dots, 15\}$ maintains an integer displacement $\delta_i \in \mathbb{Z}_{32}$ and velocity $v_i \in \mathbb{Z}_{32}$ updated once per frame via a **damped integer Hooke’s law integrator** (bit-shift stiffness $k = 2^{-5}$, damping $d = 2^{-3}$):

$$F_i = -(\delta_i \gg 5) - (v_i \gg 3), \qquad v_i \leftarrow v_i + F_i, \qquad \delta_i \leftarrow \delta_i + v_i$$

Because both stiffness and damping are power-of-two arithmetic right-shifts, the manifold is unconditionally stable and returns smoothly to equilibrium without floating-point denormals or energy drift.

---

## 5. `480×272` EDRAM Buffer, `4×4` Bayer Dither & `CLUT8` Cycling

### 5.1 Memory Layout (`131.5 KB` Total State)
* **Indexed Color Buffer (`indexBuf`):** $480 \times 272 \times 1\text{ byte} = 130,560\text{ bytes}$ (`Uint8Array`).
* **Depth Z-Buffer (`zBuf`):** $480 \times 272$ integer depth values (`Int32Array`).
* **Color Lookup Table (`activeCLUT`):** $256 \times 4\text{ bytes} = 1,024\text{ bytes}$ (`0xAABBGGRR`):
  * Indices `0..31`: Background sky gradient ramp.
  * Indices `32..239`: 208-entry cyclable iridescent manifold ramp.
  * Indices `240..255`: Patch-edge specular rim highlight ramp.

### 5.2 Sub-Index `4×4` Ordered Dithering
During scanline rasterization at pixel $(x, y)$, the interpolated `Q16.16` palette coordinate $c_{\text{Q16}}$ is perturbed by a zero-mean `4×4` Bayer matrix $M_{(y \bmod 4), (x \bmod 4)} \in [-8, +7]$ shifted left by 12 bits ($\pm 0.5$ palette index):

$$\text{idx}(x, y) = \text{clamp}_{[32, 239]}\Big( \big(c_{\text{Q16}} + ((M_{y \bmod 4, x \bmod 4} - 8) \ll 12)\big) \gg 16 \Big)$$

### 5.3 Zero-Overdraw CLUT Rotation
Color animation slides indices `32..239` modulo $208$ each frame:

$$\text{CLUT}_{\text{active}}[32 + i] = \text{CLUT}_{\text{base}}\big[32 + ((i + \Delta_{\text{tick}}) \bmod 208)\big], \quad i \in \{0..207\}$$

This transforms the entire frame's luminescence in $208$ integer memory copies without re-rasterizing geometry.

---

## 6. Deterministic Integer Karplus-Strong `sceSas` Voice Synthesis

Audio synthesis runs at $f_s = 22,050\text{ Hz}$ using 8 polyphonic ring buffers tuned to a pentatonic harmonic series ($L_v \in \{100, 89, 75, 67, 56, 50, 44, 37\}$ samples, corresponding to $\approx 220.5\text{ Hz}$ through $595.9\text{ Hz}$).

1. **16-Bit Galois LFSR Excitation:** On touch impulse, the delay line is filled using a deterministic maximal-period Linear Feedback Shift Register (polynomial $x^{16} + x^{14} + x^{13} + x^{11} + 1$, seed `0xACE1`):
   $$\text{bit} = ((s \gg 0) \oplus (s \gg 2) \oplus (s \gg 3) \oplus (s \gg 5)) \mathbin{\&} 1, \qquad s \leftarrow (s \gg 1) \mid (\text{bit} \ll 15)$$
2. **Integer Two-Point Low-Pass Decay:** Each sample step updates ring-buffer element $y[n]$ with fixed-point damping factor $\frac{253}{512} \approx 0.49414$:
   $$y[n] \leftarrow \big((y[n] + y[(n + 1) \bmod L_v]) \times 253\big) \gg 9$$

---

## 7. References (APA 7th Edition)

* Bayer, B. E. (1973). *An optimum method for two-level rendition of continuous-tone pictures* (IEEE International Conference on Communications, Vol. 1, pp. 26-11–26-15). IEEE.
* Bhaskara I. (c. 629 CE / 1976). *Mahābhāskarīya* (K. S. Shukla, Ed. & Trans.). Department of Mathematics and Astronomy, Lucknow University.
* Karplus, K., & Strong, A. (1983). Digital synthesis of plucked-string and drum timbres. *Computer Music Journal*, *7*(2), 43–55. https://doi.org
* Yates, R. (2009). *Fixed-point arithmetic: An introduction*. Digital Signal Labs.
