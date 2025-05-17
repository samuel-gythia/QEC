# Plot the logical error rate of the 5-qubit surface code under depolarizing noise
# This script generates and saves a publication-quality plot for the QEC project
# Author: "Samuel Gythia"(alias)
# Date: May 17, 2025

import matplotlib.pyplot as plt

# These are the depolarizing noise rates per gate (in percent)
rates = [0.0, 0.01, 0.02, 0.03, 0.05]
# These are the logical error rates measured from simulation 
errs = [0.472, 0.512, 0.526, 0.540, 0.585]

plt.figure(figsize=(6, 4))  # Set a nice figure size for reports
plt.plot(rates, errs, marker='o', linestyle='-', color='navy', label='Surface Code')
plt.xlabel('Depolarizing Noise Rate', fontsize=12)
plt.ylabel('Logical Error Rate', fontsize=12)
plt.title('5‑Qubit Surface Code Performance', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.savefig('results/qec_plot.png', bbox_inches='tight', dpi=300)
print('Plot saved to results/qec_plot.png')  # Results directory
