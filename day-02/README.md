# Day 2: Design Sweep

Runs one function many times with different parameters, the way CAD automation tests design options.

## What it does

- Sweeps plate thickness (5 to 20 mm) and hole diameter (10 to 40 mm)
- Compares materials (steel, aluminum, titanium, copper) using a dictionary
- Uses `if` and `else` to flag masses over 0.5 kg

## Run it

```bash
python3 day-02/sweep.py
```

## What I learned

- Lists, `for` loops and dictionaries
- Conditional logic with `if` and `else`
- Formatting output with f-strings