from unittest import TestCase

import monte_carlo


class TestMonteCarlo(TestCase):
    def test_integral_1(self):
        # Tests a triangle
        area = monte_carlo.integral_1(lambda x, y: y <= x, x_from=0, x_to=1, y_min=0, y_max=1)
        self.assertAlmostEqual(0.5, area, delta=0.05)

    def test_integral_2(self):
        # Tests a triangle
        area = monte_carlo.integral_2(lambda x: x, x_from=0, x_to=1)
        self.assertAlmostEqual(0.5, area, delta=0.05)

    def test_pi(self):
        # Tests a triangle
        area = monte_carlo.calc_pi()
        self.assertAlmostEqual(3.1415, area, delta=0.05)
