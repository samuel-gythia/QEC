# **# 🧬 Quantum Error Correction Simulation**
**# 🧠 Motivation:**
  Quantum error correction (QEC) is a foundational requirement for fault-tolerant quantum computation. As quantum hardware becomes increasingly viable, simulating QEC codes helps us evaluate and understand their behavior under noise—an essential step toward scalable quantum systems.

**# 🚀 Project Overview:**
  This project simulates the performance of two well-known 5-qubit error correction codes using Qiskit, under varying levels of depolarizing noise.

**# > Codes Simulated:**

  🧱 5-Qubit Surface Code

  🧩 5-Qubit Shor Code

**# Noise Model:**
  Depolarizing noise rates of 0%, 1%, 2%, 3%, and 5% per gate.

**# Key Outcomes:**

  1. Python simulations using Qiskit

  2. Logical error rate plots vs. noise rate (results/qec_plot.png)

  3. Basic comparative analysis of both codes in REPORT.md

**#📊 Results Preview:**
<img src="results/qec_plot.png" alt="Logical Error Rate vs Noise" width="500"/>


**# 📁 Project Structure**

    ```
    QEC/
    ├── code/
    │   ├── simulate_surface.py    
    # Surface code simulation scripts
    │   └── simulate_shor.py       
    # Shor code simulation scripts
    ├── results/
    │   └── qec_plot.png           
    # Logical error rate vs. noise plot
    ├── REPORT.md                  
    # Comparative analysis and findings
    ├── proposal.pdf               
    # Project proposal and objectives
    └── README.md                  
    # Project overview (this file)
    ```
    - **code/**: Contains Python scripts for simulating the 5-qubit Surface and Shor codes using Qiskit.
    - **results/**: Stores output plots and data generated from simulations.
    - **REPORT.md**: Provides a detailed comparative analysis of the codes' performance.
    - **proposal.pdf**: Outlines the initial project motivation, goals, and methodology.
    - **README.md**: Offers a comprehensive introduction and guide to the project.

**# 📌 Notes:**
  This project is an early-stage research prototype and can be extended further with stabilizer formalism, different noise models, or circuit optimization techniques.

**Contributions and feedback are welcome!**



