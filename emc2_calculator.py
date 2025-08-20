#This program calculates the energy equivalent of a given mass using Einstein’s famous formula.

# Speed of light (m/s)
c = 299792458  

# The mass (in kilogram)
m = float(input("Enter the mass in kilograms: "))

# E = m * c^2 formula
E = m * (c ** 2)

# Result in joules
print(f"Energy: {E:.3e} Joules")