# Day-1 Building profile for CAD-Automation engineer 
# CAD Automation: Parametric Mass Calculator

A small Python project that calculates the mass of mechanical parts from their dimensions. It is the first step toward automating CAD and CAE workflows, where a design is driven by numbers (parameters) instead of manual changes.

## Features

- `plate_mass(length_mm, width_mm, thickness_mm, hole_diameter_mm, density_g_cm3=7.85)` returns the mass in kg of a rectangular plate with a circular hole.
- `cylinder_mass(diameter_mm, length_mm, density_g_cm3=7.85)` returns the mass in kg of a solid cylinder.

Density defaults to steel (7.85 g/cm³). Pass 2.70 for aluminum.

## How it works

1. Compute the volume of the solid shape:
   - Plate: length × width × thickness
   - Cylinder: π × radius² × length
2. For the plate, subtract the hole volume: π × (hole diameter / 2)² × thickness.
3. Convert mm³ to cm³ by dividing by 1000.
4. Multiply by density (g/cm³) to get grams, then divide by 1000 for kilograms.

## Example

```python
print(round(plate_mass(100, 50, 10, 20), 3))         # 0.368 kg (steel plate)
print(round(plate_mass(100, 50, 10, 20, 2.70), 3))   # 0.127 kg (aluminum plate)
print(round(plate_mass(200, 100, 5, 30, 2.75), 4))   # 0.2653 kg (custom density)
print(round(cylinder_mass(20, 100), 3))              # 0.247 kg (steel rod)
```

## Requirements

- Python 3 (no extra packages; uses the built-in `math` module)
  
## Run it

```bash
python3 day-01/plate.py
```

## What I learned

- Writing reusable Python functions with default arguments
- Converting units correctly (mm³ to cm³, grams to kilograms)
- Debugging: a missing `** 2` made the cylinder mass 10 times too small, which I caught by checking against a hand calculation
- Using Git and GitHub to store and share code

## Next steps

- Add input validation (no negative sizes, hole smaller than the plate)
- Add unit tests with pytest
- Generate parts through a CAD API (for example, FreeCAD's Python interface)
