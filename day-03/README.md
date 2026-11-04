# Day 3: Input Validation and Tests

Makes the mass functions safe to use and proves they are correct, the way real engineering code is written.

## What it does

- `plate_mass` and `cylinder_mass` reject bad inputs with `raise ValueError(...)`:
  - Non-positive dimensions
  - A hole that does not fit inside the plate
  - A non-positive density
- `assert` tests confirm known results:
  - Steel plate (100 × 50 × 10 mm, 20 mm hole): 0.368 kg
  - Aluminum plate (same size, density 2.70): 0.127 kg
  - Steel rod (20 mm diameter, 100 mm long): 0.247 kg
- `try` / `except` blocks catch bad inputs and print a clear message instead of crashing.

## Run it

```bash
python3 day-03/validation.py
```

Expected output:

```
All tests passed
Caught error: Hole must fit inside the plate
Caught error: Dimensions must be positive
Caught error: Density must be positive
```

## What I learned

- Raising errors with `raise ValueError` for invalid input
- Writing tests with `assert` and checking results against hand calculations
- Handling errors with `try` / `except`
- Keeping the same default density (steel, 7.85) across functions so they behave consistently
- Testing one problem at a time so each error message is clear

## Next steps

- Report every invalid input at once, with its name and value
- Read part dimensions from a file instead of typing them in
