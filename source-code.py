import numpy as np
import matplotlib.pyplot as plt

print("=== Thermodynamic Calculator ===")

# User Inputs
delta_H = float(input("Enter ΔH (kJ/mol): "))
delta_S = float(input("Enter ΔS (J/mol·K): "))

# Convert ΔS to kJ/mol·K
delta_S_kJ = delta_S / 1000

# Temperature range for graph
T = np.linspace(200, 1000, 100)

# Gibbs Free Energy calculation
delta_G = delta_H - T * delta_S_kJ

# Plot Graph
plt.figure()
plt.plot(T, delta_G)
plt.axhline(0)  # line where ΔG = 0
plt.xlabel("Temperature (K)")
plt.ylabel("ΔG (kJ/mol)")
plt.title("Gibbs Free Energy vs Temperature")
plt.grid()
plt.show()

# Check at room temperature (298 K)
T_room = 298
G_room = delta_H - T_room * delta_S_kJ

print(f"\nΔG at 298 K = {G_room:.2f} kJ/mol")

if G_room < 0:
    print("→ Reaction is spontaneous at room temperature")
else:
    print("→ Reaction is NOT spontaneous at room temperature")

# Calculate Transition Temperature (ΔG = 0)
if delta_S_kJ != 0:
    T_transition = delta_H / delta_S_kJ
    print(f"\nTransition Temperature (ΔG = 0): {T_transition:.2f} K")
else:
    print("\nTransition temperature cannot be calculated (ΔS = 0)")

print("\n=== End of Calculation ===")
