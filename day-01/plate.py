import math

def plate_mass(length_mm, width_mm, thickness_mm, hole_diameter_mm, density_g_cm3=7.85):
    plate_volume = length_mm * width_mm * thickness_mm
    hole_volume = math.pi * (hole_diameter_mm / 2) ** 2 * thickness_mm
    volume_cm3 = (plate_volume - hole_volume) / 1000
    return volume_cm3 * density_g_cm3 / 1000  # kilograms

print(round(plate_mass(100, 50, 10, 20), 3))
print(round(plate_mass(200, 100, 5, 30), 3))
print(round(plate_mass(200, 100, 5, 30, 2.75), 4))

def cylinder_mass(diameter_mm, length_mm, density_g_cm3=7.85):
    radius_mm =  diameter_mm / 2
    volume_mm3 = math.pi * radius_mm ** 2 * length_mm
    volume_cm3 = volume_mm3 / 1000
    return volume_cm3 * density_g_cm3 / 1000

print(round(cylinder_mass(20, 100), 3))
