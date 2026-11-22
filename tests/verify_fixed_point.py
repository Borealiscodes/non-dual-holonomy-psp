import math
import unittest

SHIFT = 16
ONE = 1 << SHIFT


def mul_q16(a: int, b: int) -> int:
    res = ((a * b) >> SHIFT) & 0xFFFFFFFF
    return res - 0x100000000 if res & 0x80000000 else res


def build_sin_lut() -> list[int]:
    lut = [0 for _ in range(1024)]
    for i in range(257):
        x = (i * 9000) // 256
        term = x * (18000 - x)
        val = (4 * term * 65536) // (405000000 - term)
        lut[i] = val
        lut[512 - i] = val
        lut[512 + i] = -val
        lut[(1024 - i) & 1023] = -val
    return lut


def eval_cubic_bezier_q16(p0: int, p1: int, p2: int, p3: int, t_q16: int) -> int:
    inv_t = ONE - t_q16
    a0 = mul_q16(p0, inv_t) + mul_q16(p1, t_q16)
    a1 = mul_q16(p1, inv_t) + mul_q16(p2, t_q16)
    a2 = mul_q16(p2, inv_t) + mul_q16(p3, t_q16)
    b0 = mul_q16(a0, inv_t) + mul_q16(a1, t_q16)
    b1 = mul_q16(a1, inv_t) + mul_q16(a2, t_q16)
    return mul_q16(b0, inv_t) + mul_q16(b1, t_q16)


class TestFixedPointInvariants(unittest.TestCase):
    def test_mul_q16_exactness(self):
        half = ONE >> 1
        self.assertEqual(mul_q16(ONE, ONE), ONE)
        self.assertEqual(mul_q16(half, half), ONE >> 2)
        self.assertEqual(mul_q16(-ONE, half), -half)

    def test_bhaskara_sin_lut_accuracy_and_symmetry(self):
        lut = build_sin_lut()
        self.assertEqual(lut[0], 0)
        self.assertEqual(lut[256], ONE)
        self.assertEqual(lut[512], 0)
        self.assertEqual(lut[768], -ONE)

        for brad in range(1024):
            approx = lut[brad] / ONE
            exact = math.sin(2.0 * math.pi * brad / 1024.0)
            self.assertLess(abs(approx - exact), 0.002)

    def test_de_casteljau_endpoints_and_midpoint(self):
        p0, p1, p2, p3 = 0, ONE, ONE, 0
        self.assertEqual(eval_cubic_bezier_q16(p0, p1, p2, p3, 0), 0)
        self.assertEqual(eval_cubic_bezier_q16(p0, p1, p2, p3, ONE), 0)
        self.assertEqual(eval_cubic_bezier_q16(p0, p1, p2, p3, ONE >> 1), (3 * ONE) >> 2)

    def test_galois_lfsr_maximal_period(self):
        state = 0xACE1
        seen = set()
        for _ in range(65535):
            seen.add(state)
            bit = ((state >> 0) ^ (state >> 2) ^ (state >> 3) ^ (state >> 5)) & 1
            state = (state >> 1) | (bit << 15)
        self.assertEqual(len(seen), 65535)
        self.assertEqual(state, 0xACE1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
