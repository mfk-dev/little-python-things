# This is an very simple Orbital Period calculator.

import math

a = float(input("Distance from the Planet in AU:")) # Distance of planet to star (in Astronomical Units)
M = float(input("Mass of the star (Sun = 1): ")) # Mass of the star (Assuming Sun=1)
T = math.sqrt(a**3 / M)   # Kepler's Law

print("Orbital Period is:", T, "Years")


