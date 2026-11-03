import math

def plate_mass(length_mm, width_mm, thickness_mm, hole_diameter_mm, density_g_cm3=7.85):
    plate_volume = length_mm * width_mm * thickness_mm
    hole_volume = math.pi * (hole_diameter_mm / 2) ** 2 * thickness_mm
    volume_cm3 = (plate_volume - hole_volume) / 1000
    return volume_cm3 * density_g_cm3 / 1000  # kilograms

def cylinder_mass(diameter_mm, length_mm, density_g_cm3=7.85):
    radius_mm = diameter_mm / 2
    volume_mm3 = math.pi * radius_mm ** 2 * length_mm
    return volume_mm3 / 1000 * density_g_cm3 / 1000

print("\nThickness Sweep ")
# Sweep 1: thickness
thicknesses = [5, 10, 15, 20]
for t in thicknesses:
    mass = plate_mass(100, 50, t, 20)
    print(f"Thickness {t} mm -> {mass:.3f} kg")

print("\nHole Diameter Sweep ")
# Task-1
holedia = [10, 20, 30, 40]
for d in holedia:
    mass = plate_mass(100, 50, 10, d)
    print(f"Hole Diameter {d} mm -> {mass:.3f} kg")

print("\nMaterials Comaprison ")    
# materials dictionary loop
materials = {"steel": 7.85, "aluminum": 2.70, "titanium": 4.51, "copper": 8.96}
for name, density in materials.items():
    print(name, round(plate_mass(100, 50, 10, 20, density), 3))

print("\nunder 0.5 kg check")
thicknesses = [5, 10, 15, 20]
for t in thicknesses:
    mass = plate_mass(100, 50, t, 20)
    if mass < 0.5:
        print(f"Thickness {t} mm -> {mass:.3f} kg")
    else:
        print(f"Thickness {t} mm -> too heavy({mass:.3f}) kg")