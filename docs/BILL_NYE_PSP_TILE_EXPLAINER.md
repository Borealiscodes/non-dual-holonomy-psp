# 🧪 BILL NYE SCIENCE TILE: How a `131.5 KB` PSP Time Machine Makes Silk & Music Out of Whole Numbers!

**Tile ID:** `NDH-TILE-PSP-01`  
**Repository:** [`Borealiscodes/non-dual-holonomy-psp`](https://github.com)  
**Target Path:** `docs/BILL_NYE_PSP_TILE_EXPLAINER.md`  
**Companion Demo:** [`index.html`](../index.html) (`480×272` · `Q16.16` Fixed-Point · `CLUT8` EDRAM · `sceSas` Integer DSP)

---

## Author & Pacing Note
> **Self-Kindness & Sovereignty Reminder:** Built to run offline on constrained edge hardware (`< 250 KB` total footprint, zero cloud dependencies) so anyone—regardless of hardware budget or institutional gatekeeping—can touch, hear, and explore deterministic interactive art on their own terms.

---

## 🎬 COLD OPEN: *“Consider the Following…”*

*(Cue upbeat synth bassline and a close-up of a spinning `480×272` glowing silk wave on a tablet screen!)*

**BILL:**  
"Whoa! Look at that shimmering ribbon of neon *Kyoto* crimson and *Abyss* emerald rippling across the screen—and listen to those plucked harp strings ringing out every time your finger touches the glass! Now, you might think you need a giant, power-hungry graphics card and a supercomputer doing billions of messy decimal calculations to pull that off.  

**WRONG!** Every single wave, shadow, and musical string in this universe is made out of **100% WHOLE NUMBERS**—and the entire screen fits inside **131.5 kilobytes** of memory. That’s smaller than a single selfie on your phone!  

*Science rules!* Let’s break down the **four retro hardware tricks** powering **Non Dual Holonomy**!"

---

## 🔬 EXPERIMENT 1: `Q16.16` Fixed-Point Math (Who Needs Decimals Anyway?!)

**THE PROBLEM:**  
Normal computers use *floating-point* numbers (`3.14159265...`) to calculate 3D curves. The catch? Floating-point math is sneaky! Across different phones, tablets, and consoles, tiny rounding errors pile up like dust bunnies under a couch—causing jitter, drift, and unpredictable glitches.

**THE `Q16.16` TRICK:**  
Instead of messy decimals, we take a plain old **32-bit whole integer** and draw an imaginary line right down the middle:
* **Top 16 bits:** The whole number part (`0` to `32,767`).
* **Bottom 16 bits:** The fraction part, measured in slices of **1 / 65,536** (`2¹⁶`)!

```text
[ 16 Bits: Whole Number ] . [ 16 Bits: 1/65,536ths of a Step ]
         1.0 in Q16.16  =  65,536
         0.5 in Q16.16  =  32,768
```

When we multiply two `Q16.16` numbers together, we briefly stretch them into a 64-bit pocket (`BigInt`), multiply, and slide (`>> 16`) right back into place!  
* **Result:** Bit-exact, rock-solid **determinism**. Touch the exact same spot with the exact same swipe on an Android tablet, a desktop browser, or a 2004 Sony PSP, and you get the **exact same wave** down to the very last bit!

---

## 🕸️ EXPERIMENT 2: The 16-Point Marionette Cage (`De Casteljau` Bezier Patches)

**THE PROBLEM:**  
Remember pinching Mario’s 3D face on the *Super Mario 64* title screen? That worked by yanking individual triangle corners—pull too hard, and the face turns into sharp, pointy origami triangles!

**THE PSP `sceGuPatchPrim` TRICK:**  
Sony’s PlayStation Portable had a secret weapon built straight into its graphics chip: **Bicubic Bezier Patches**!
1. Instead of moving 800 heavy triangles by hand, we only move **16 invisible control points** arranged in a $4 \times 4$ grid—like a marionette cage!
2. Each of those 16 points is attached to a **damped integer spring** (`F = -(offset >> 5) - (velocity >> 3)`). When your finger pokes the screen, it gives the nearest spring a gentle velocity kick.
3. Every frame, **De Casteljau’s subdivision algorithm** smoothly weaves those 16 points into **512 to 800 interlocking triangles** (`16×16` or `20×20` grid) using nothing but integer shifts and adds. That’s why the surface ripples like continuous liquid silk instead of stiff cardboard!

---

## 🎨 EXPERIMENT 3: Paint-by-Numbers Color Magic (`CLUT8` EDRAM)

**THE PROBLEM:**  
Painting every pixel on a `480×272` screen with full 32-bit True Color (`RGBA`) takes over **522 KB** per frame—and changing the lighting means recalculating every single pixel on the screen!

**THE `1 KB` CLUT TRICK:**  
Just like the PSP’s embedded DRAM (`EDRAM`), our engine plays **Paint-by-Numbers**:
* **The Index Buffer (`130.5 KB`):** Each pixel doesn’t store a color—it just stores a single badge number from **`0` to `255`** (`Uint8Array`).
  * `0..31` = Deep background twilight sky
  * `32..239` = The undulating silk wave (with **`4×4` Bayer ordered dithering** sprinkling checkerboard grain so gradients look silky-smooth!)
  * `240..255` = Crisp glowing rim-light borders
* **The Color Lookup Table (`1 KB`):** A tiny 256-slot palette (`activeCLUT`) translates those badge numbers into glowing colors right before hitting the screen.
* **Zero-Overdraw Shimmer:** To make the entire ocean of light pulse and flow, we don’t re-draw a single triangle—we just **rotate those 208 palette slots in a circle** (`208` integer swaps per frame)! Watch the thin rainbow bar beneath the screen: you can literally see the colors sliding past in real time!

---

## 🎸 EXPERIMENT 4: Plucking Virtual Strings with Integer Echoes (`sceSas` Karplus-Strong)

**THE PROBLEM:**  
Playing recorded `.WAV` or `.MP3` audio files eats up megabytes of storage and sounds identical every time you tap.

**THE KARPLUS-STRONG WAVEGUIDE TRICK:**  
To give our silk canvas a voice inspired by the PSP’s `sceSas` hardware DSP, we simulate **8 vibrating guitar/harp strings** using tiny integer ring buffers (`100` down to `37` samples long at `22,050 Hz`):
1. **The Pluck (16-bit Galois LFSR):** When your finger drags across a grid zone, a 16-bit shift-register (`0xACE1`) fills that string’s tiny buffer with a burst of deterministic integer static—just like a pick scraping a string!
2. **The Ring (Two-Point Integer Low-Pass Filter):** As the buffer loops around and around, each sample averages itself with its neighbor and multiplies by `253 / 512` (`((curr + next) * 253) >> 9`). High harsh frequencies fade away first, leaving behind a warm, woody, resonant **pentatonic pluck** that harmonizes with every ripple you sculpt!

---

## 📊 AT-A-GLANCE LAB BENCH SUMMARY

| Hardware Trick | Memory / Compute Cost | What Your Senses Experience |
| :--- | :--- | :--- |
| **`Q16.16` Fixed-Point + Bhaskara Sine LUT** | `4 KB` lookup table (`0` floats!) | Rock-solid 3D rotation & wave physics with zero jitter or drift. |
| **`4×4` Bicubic Bezier + Integer Springs** | `16` control points (`128` bytes!) | Touch-reactive liquid-silk manifold that bounces and settles smoothly. |
| **`CLUT8` EDRAM + `4×4` Bayer Dithering** | `130.5 KB` pixels + `1 KB` palette | Instant theme morphing (*Aurora*, *Kyoto*, *Abyss*) & shimmering light waves. |
| **8-Voice Integer Karplus-Strong DSP** | `< 1 KB` ring buffers | Organic pentatonic plucked strings triggered directly by touch. |

---

## 🧠 TRY THIS AT HOME! (30-Second Lab Challenge)
1. Open [`index.html`](../index.html) in any offline browser and tap **SAS Synth: ON**.
2. Toggle **Cycle: OFF** and watch the thin `256`-pixel CLUT bar below the viewport freeze—now tap **Cycle: ON** and watch how rotating just `208` numbers transforms the entire 3D surface without touching a single triangle!
3. Drag slowly from top to bottom across the silk wave to hear all **8 pentatonic waveguide strings** resonate in harmony with your touch.

> *"Now you know! It’s not magic—it’s **fixed-point math, lookup tables, and integer physics** working together in harmony. Thanks for exploring!"*
