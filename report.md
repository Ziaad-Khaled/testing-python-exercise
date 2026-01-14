# Step 2

Added assertions to ensure input parameters are floats. The code failed because the default values for temperature were integers (300, 700) instead of floats (300.0, 700.0).

```
Traceback (most recent call last):
  File "diffusion2d.py", line 146, in <module>
    main()
  File "diffusion2d.py", line 116, in main
    DiffusionSolver.initialize_physical_parameters()
  File "diffusion2d.py", line 54, in initialize_physical_parameters
    assert isinstance(T_cold, float), 'T_cold should be a float'
AssertionError: T_cold should be a float
```

# Step 4: Verification

Introduced a bug in `initialize_domain`: `self.nx = int(h / dx)` instead of `int(w / dx)`.
The test `test_initialize_domain` failed as expected with `assert 20 == 40`.
This confirms the test correctly catches errors in domain initialization.

# Step 4: Verification (Unittest)

Refactored tests to use `unittest` and `setUp`. Re-introduced the same bug in `initialize_domain`.
The test `test_initialize_domain` failed again as expected:
```
FAILED tests/unit/test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_domain - AssertionError: 20 != 40
```
This confirms the refactored test suite is correctly constructed.

# Step 5: Integration Tests

Implemented integration tests in `tests/integration/test_diffusion2d.py`.
- `test_initialize_physical_parameters`: Verifies `dt` is computed correctly when `initialize_domain` and `initialize_physical_parameters` are called together.
- `test_set_initial_condition`: Verifies the initial condition array `u` matches expected values computed manually.

Both tests passed.

# Step 5: Verification (Integration Tests)

Introduced bug in `initialize_physical_parameters` (wrong formula: `dx2 * dy2` instead of `dx2 + dy2`).
The test `test_initialize_physical_parameters` failed as expected.
This confirms the integration tests correctly catch errors.
