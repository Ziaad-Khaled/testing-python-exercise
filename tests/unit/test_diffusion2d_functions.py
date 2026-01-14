"""
Tests for functions in class SolveDiffusion2D
"""

import numpy as np
from diffusion2d import SolveDiffusion2D


def test_initialize_domain():
    """
    Check function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    w = 20.
    h = 10.
    dx = 0.5
    dy = 2.
    solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)
    
    assert solver.w == w
    assert solver.h == h
    assert solver.dx == dx
    assert solver.dy == dy
    assert solver.nx == 40
    assert solver.ny == 5


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_physical_parameters
    """
    solver = SolveDiffusion2D()
    solver.dx = 0.2
    solver.dy = 0.2
    d = 5.
    T_cold = 200.
    T_hot = 600.
    solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot=T_hot)
    
    assert solver.D == d
    assert solver.T_cold == T_cold
    assert solver.T_hot == T_hot
    
    # Expected dt = dx2 * dy2 / (2 * D * (dx2 + dy2))
    # dx2 = 0.04, dy2 = 0.04
    # dt = 0.0016 / (2 * 5 * 0.08) = 0.0016 / 0.8 = 0.002
    # Using np.isclose for float comparison
    assert np.isclose(solver.dt, 0.002)


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.set_initial_condition
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(w=10., h=10., dx=1., dy=1.)
    solver.initialize_physical_parameters(d=4., T_cold=300., T_hot=700.)
    
    u = solver.set_initial_condition()
    
    # Check shape
    assert u.shape == (10, 10)
    
    # Check T_cold outside (0, 0) -> (0-5)^2 + (0-5)^2 = 50 > 4
    assert u[0, 0] == 300.
    
    # Check T_hot inside (5, 5) -> (5-5)^2 + (5-5)^2 = 0 < 4
    assert u[5, 5] == 700.
