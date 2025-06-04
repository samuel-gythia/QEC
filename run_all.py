#!/usr/bin/env python3
"""
Run all QEC simulations and generate plots
Simple script to execute the full analysis pipeline
"""

import subprocess
import sys

def run_simulation(script_name, description):
    """Run a simulation script and handle any errors"""
    print(f"\n{'-'*50}")
    print(f"Running {description}...")
    print(f"{'-'*50}")
    
    try:
        result = subprocess.run([sys.executable, f"code/{script_name}"], 
                              capture_output=False, check=True)
        print(f"✓ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error running {description}: {e}")
        return False

if __name__ == "__main__":
    print("Quantum Error Correction Simulation Pipeline")
    print("=" * 50)
    
    # Run simulations
    success = True
    success &= run_simulation("simulate_surface.py", "Surface Code Simulation")
    success &= run_simulation("simulate_shor.py", "Shor Code Simulation") 
    success &= run_simulation("plot_comparison.py", "Generating Comparison Plot")
    
    print(f"\n{'='*50}")
    if success:
        print("✓ All simulations completed successfully!")
        print("Check results/qec_plot.png for the comparison plot")
        print("See REPORT.md for detailed analysis")
    else:
        print("✗ Some simulations failed. Check output above.")
    print(f"{'='*50}")
