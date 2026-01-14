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
