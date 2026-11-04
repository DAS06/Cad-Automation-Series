import math

def plate_mass(length_mm, width_mm, thickness_mm, hole_diameter_mm, density_g_cm3=7.85):
    if min(length_mm, width_mm, thickness_mm) <= 0:
        raise ValueError("Dimensions must be positive")
    if hole_diameter_mm < 0 or hole_diameter_mm >= min(length_mm, width_mm):
        raise ValueError("Hole must fit inside the plate")
    plate_volume = length_mm * width_mm * thickness_mm
    hole_volume = math.pi * (hole_diameter_mm / 2) ** 2 * thickness_mm
    return (plate_volume - hole_volume) / 1000 * density_g_cm3 / 1000

def cylinder_mass(diameter_mm, length_mm, density_g_cm3=7.85):
    if diameter_mm <= 0 or length_mm <= 0:
        raise ValueError("Dimensions must be positive")
    if density_g_cm3 <=0:
        raise ValueError("Density must be positive")
    radius_mm = diameter_mm / 2
    return math.pi * radius_mm ** 2 * length_mm / 1000 * density_g_cm3 / 1000

# Tests: these fail loudly if a result is wrong
assert round(plate_mass(100, 50, 10, 20), 3) == 0.368 #Steel
# Task-1 testing aluminium density =2.70
assert round(plate_mass(100, 50, 10, 20, 2.70), 3) == 0.127 #Aluminium
assert round(cylinder_mass(20, 100), 3) == 0.247
print("All tests passed")

# Catch a bad input instead of crashing
try:
    plate_mass(100, 50, 10, 60)
except ValueError as e:
    print("Caught error:", e)
# Task-2 testing -ve thickness
try:
    plate_mass(100, 50, -2, 20)
except ValueError as e:
    print("Caught error:", e)
# Task-3 testing -ve density
try:
    cylinder_mass(20, 100, -1)
except ValueError as e:
    print("Caught error:", e)
