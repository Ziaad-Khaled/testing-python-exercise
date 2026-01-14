"""
Tests for functions in class SolveDiffusion2D
"""

import unittest
import numpy as np
from diffusion2d import SolveDiffusion2D


class TestDiffusion2D(unittest.TestCase):
    def setUp(self):
        self.solver = SolveDiffusion2D()

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        w = 20.
        h = 10.
        dx = 0.5
        dy = 2.
        self.solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)
        
        self.assertEqual(self.solver.w, w)
        self.assertEqual(self.solver.h, h)
        self.assertEqual(self.solver.dx, dx)
        self.assertEqual(self.solver.dy, dy)
        self.assertEqual(self.solver.nx, 40)
        self.assertEqual(self.solver.ny, 5)

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_physical_parameters
        """
        self.solver.dx = 0.2
        self.solver.dy = 0.2
        d = 5.
        T_cold = 200.
        T_hot = 600.
        self.solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot=T_hot)
        
        self.assertEqual(self.solver.D, d)
        self.assertEqual(self.solver.T_cold, T_cold)
        self.assertEqual(self.solver.T_hot, T_hot)
        
        # Expected dt = dx2 * dy2 / (2 * D * (dx2 + dy2))
        # dx2 = 0.04, dy2 = 0.04
        # dt = 0.0016 / (2 * 5 * 0.08) = 0.0016 / 0.8 = 0.002
        self.assertAlmostEqual(self.solver.dt, 0.002)

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.set_initial_condition
        """
        self.solver.initialize_domain(w=10., h=10., dx=1., dy=1.)
        self.solver.initialize_physical_parameters(d=4., T_cold=300., T_hot=700.)
        
        u = self.solver.set_initial_condition()
        
        # Check shape
        self.assertEqual(u.shape, (10, 10))
        
        # Check T_cold outside (0, 0) -> (0-5)^2 + (0-5)^2 = 50 > 4
        self.assertEqual(u[0, 0], 300.)
        
        # Check T_hot inside (5, 5) -> (5-5)^2 + (5-5)^2 = 0 < 4
        # Index corresponding to x=5, y=5. 
        # i * dx = x => i = 5/1 = 5
        # j * dy = y => j = 5/1 = 5
        self.assertEqual(u[5, 5], 700.)
