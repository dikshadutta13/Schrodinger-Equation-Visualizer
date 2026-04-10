import numpy as np
import matplotlib.pyplot as plt

# INPUTS
L = float(input("Enter length of box (L): "))
n = int(input("Enter quantum number (n): "))

# x values
x = np.linspace(0, L, 1000)

# Wave function ψ(x)
psi = np.sqrt(2 / L) * np.sin(n * np.pi * x / L)

# Probability density ψ²(x)
probability = psi ** 2

# Plot Wave Function
plt.figure()
plt.plot(x, psi)
plt.title(f"Wave Function ψ(x) for n={n}")
plt.xlabel("x")
plt.ylabel("ψ(x)")
plt.grid()

# Save image
plt.savefig("images/psi_graph.png")

# Plot Probability Density
plt.figure()
plt.plot(x, probability)
plt.title(f"Probability Density ψ²(x) for n={n}")
plt.xlabel("x")
plt.ylabel("ψ²(x)")
plt.grid()

# Save image
plt.savefig("images/probability_graph.png")

plt.show()
