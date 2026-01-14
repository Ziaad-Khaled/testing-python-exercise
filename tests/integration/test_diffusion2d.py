"""
Tests for functionality checks in class SolveDiffusion2D
"""

import numpy as np
from diffusion2d import SolveDiffusion2D


def test_initialize_physical_parameters():
    """
    Checks that dt is computed correctly when initialize_domain
    and initialize_physical_parameters are called together.
    """
    solver = SolveDiffusion2D()
    
    # Integration: call initialize_domain first
    w = 10.
    h = 10.
    dx = 0.5
    dy = 0.5
    solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)
    
    # Call initialize_physical_parameters
    d = 2.
    T_cold = 100.
    T_hot = 500.
    solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot=T_hot)
    
    # Manual calculation of expected dt
    # dt = dx2 * dy2 / (2 * D * (dx2 + dy2))
    # dx2 = 0.25, dy2 = 0.25
    # dt = 0.0625 / (2 * 2 * 0.5) = 0.0625 / 2 = 0.03125
    expected_dt = 0.03125
    
    assert np.isclose(solver.dt, expected_dt)


def test_set_initial_condition():
    """
    Checks that the initial condition u is computed correctly
    when all setup functions are called together.
    """
    solver = SolveDiffusion2D()
    
    # Integration: call setup functions
    w = 10.
    h = 10.
    dx = 1.
    dy = 1.
    solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)
    solver.initialize_physical_parameters(d=4., T_cold=300., T_hot=700.)
    
    # Call set_initial_condition
    u = solver.set_initial_condition()
    
    # Manual calculation of expected u
    nx = int(w / dx)
    ny = int(h / dy)
    expected_u = 300. * np.ones((nx, ny))
    
    # Circle of radius r=2 centered at (cx=5, cy=5)
    r, cx, cy = 2, 5, 5
    r2 = r ** 2
    for i in range(nx):
        for j in range(ny):
            p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
            if p2 < r2:
                expected_u[i, j] = 700.
    
    np.testing.assert_array_equal(u, expected_u)
