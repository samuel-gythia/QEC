# Plot the logical error rates of both 5-qubit QEC codes under depolarizing noise
# Generates a comparison plot for the Surface Code and Shor Code performance
# Author: Learning quantum computing step by step
# Updated: June 2025

import matplotlib.pyplot as plt

# Noise rates tested (as fractions)
noise_rates = [0.0, 0.01, 0.02, 0.03, 0.05]

# Surface code results (from simulate_surface.py)
surface_errors = [0.472, 0.512, 0.526, 0.540, 0.585]

# Shor code results (from simulate_shor.py)  
shor_errors = [0.486, 0.488, 0.498, 0.516, 0.498]

# Create the comparison plot
plt.figure(figsize=(8, 6))
plt.plot(noise_rates, surface_errors, marker='o', linestyle='-', 
         color='navy', label='5-Qubit Surface Code', linewidth=2)
plt.plot(noise_rates, shor_errors, marker='s', linestyle='--', 
         color='darkred', label='5-Qubit Shor Code', linewidth=2)

plt.xlabel('Depolarizing Noise Rate', fontsize=12)
plt.ylabel('Logical Error Rate', fontsize=12)
plt.title('Quantum Error Correction Code Performance Comparison', fontsize=14)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(fontsize=11)
plt.tight_layout()

# Save with high resolution for reports
plt.savefig('results/qec_plot.png', bbox_inches='tight', dpi=300)
print('Comparison plot saved to results/qec_plot.png')

# Also show the plot if running interactively
# plt.show()  # Uncomment this line to display the plot
