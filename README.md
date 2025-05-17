# Quantum Error Correction Simulation

> **Motivation:**  
> Quantum error correction (QEC) is essential for building fault-tolerant quantum computers. This project simulates and compares the performance of two 5-qubit codes under realistic noise.

## 🚀 Project Overview

- **Codes Simulated:**  
  - 5-qubit Surface Code  
  - 5-qubit Shor Code  

- **Noise Model:**  
  - Depolarizing noise at 0 %, 1 %, 2 %, 3 %, and 5 % per gate

- **Key Deliverables:**  
  1. Python scripts using Qiskit  
  2. Plot of logical error rate vs. noise rate (`results/qec_plot.png`)  
  3. Short analysis in `REPORT.md`

## 📂 Repository Structure
QEC/
├── code/
│ ├── simulate_surface.py
│ └── simulate_shor.py
├── results/
│ └── qec_plot.png
├── README.md
└── proposal.pdf



