# Schrödinger Equation Visualizer  
## Particle in a One-Dimensional Box (Computational Chemistry Project)

---

## Overview
This project is a Python-based visualization of the wave function and probability density of a particle confined in a one-dimensional box using the principles of quantum mechanics.

It demonstrates how quantum particles behave differently from classical particles by showing that their position is described by a probability distribution rather than a definite path.

---

## Objective
- To computationally solve the Schrödinger equation for a particle in a 1D box  
- To visualize the wave function ψ(x)  
- To visualize the probability density ψ²(x)  
- To understand quantum confinement and quantization  

---

## Theory

### Schrödinger Equation
In quantum mechanics, the behavior of a particle is described by the Schrödinger equation. For a particle confined in a one-dimensional box of length **L**, the allowed wave functions are:
ψₙ(x) = √(2/L) sin(nπx/L


Where:
- n = quantum number (n = 1, 2, 3, ...)
- L = length of the box
- x = position inside the box

---

### Boundary Conditions
- ψ(0) = 0  
- ψ(L) = 0  

This means the particle cannot exist at the walls of the box.

---

### Probability Density
The probability of finding the particle at a position x is given by:
P(x) = ψ²(x)

---

### Key Observations
- The particle does not have a fixed position  
- Higher quantum number → higher energy states  
- Number of nodes = n − 1  
- Probability distribution changes with energy level  

---

## Features
- Computes wave function ψ(x)
- Computes probability density ψ²(x)
- Supports different quantum numbers (n)
- Generates graphical outputs
- Saves graphs as image files

---

## Technologies Used
- Python  
- NumPy  
- Matplotlib  

---

## Installation

1. Install Python (if not already installed)

2. Install required libraries: pip install numpy matplotlib

---

## How to Run

1. Clone or download the repository  
2. Open terminal in the project folder  
3. Run the script: python sourcecode.py


4. Enter inputs:
- Length of box (L)
- Quantum number (n)

---

## Output

The program generates:

- Wave Function Graph (ψ vs x)  
- Probability Density Graph (ψ² vs x)  

Graphs are saved in the `images/` folder.

---

## Sample Inputs

| L | n | Description |
|---|---|------------|
| 1 | 1 | Ground state |
| 1 | 2 | First excited state |
| 1 | 3 | Higher energy state |

---

## Expected Results

- Graph starts and ends at zero  
- Number of peaks = n  
- Number of nodes = n − 1  
- Probability density is always positive  

---

## Project Structure
schrodinger-visualizer/
│
├── sourcecode.py
├── README.md
├── statement.md
│
├── images/
│ ├── psi_graph.png
│ ├── probability_graph.png


---

## Applications
- Understanding quantum mechanics concepts  
- Educational visualization tool  
- Basis for advanced quantum simulations  

---

## Future Improvements
- Add energy level calculations  
- 3D visualization  
- GUI using Tkinter  
- Support for other quantum systems  

---

## Conclusion
This project demonstrates the quantum mechanical behavior of a particle in a confined system. It highlights the probabilistic nature of quantum mechanics through graphical visualization.

---



