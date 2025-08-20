import math

a = float(input("Distance from the Planet in AU:"))
M = float(input("Mass of the star (Sun = 1): "))
T = math.sqrt(a**3 / M)

print("Orbital Period is:", T, "Years")
