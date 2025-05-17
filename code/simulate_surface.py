# Simulate a simple 5-qubit surface code under depolarizing noise using Qiskit
from qiskit import QuantumCircuit, execute
from qiskit_aer import Aer
from qiskit_aer.noise import NoiseModel, depolarizing_error

# Build a placeholder 5-qubit surface code circuit
# TODO: Replace with actual 5-qubit surface code logic for real QEC simulation
# For now, applies Hadamard gates to all qubits and measures the first qubit

def build_surface_code():
    qc = QuantumCircuit(5, 1)
    qc.h(range(5))  # Put all qubits into superposition
    qc.measure(0, 0)  # Measure only the first qubit
    return qc

# Run the simulation for a given depolarizing noise rate
# Returns the logical error rate (fraction of shots where outcome is '1')
def run_simulation(noise_rate):
    noise = NoiseModel()
    err = depolarizing_error(noise_rate, 1)
    # Apply depolarizing error to all single-qubit and two-qubit gates
    noise.add_all_qubit_quantum_error(err, ['u3', 'cx'])
    sim = Aer.get_backend('qasm_simulator')
    qc = build_surface_code()
    # Run the circuit with noise for 500 shots
    result = execute(qc, sim, noise_model=noise, shots=500).result()
    counts = result.get_counts()
    # Logical error: measured '1' on the first qubit
    error_rate = counts.get('1', 0) / 500
    return error_rate

if __name__ == '__main__':
    # Example: test for three noise rates
    rates = [0.0, 0.01, 0.02]
    errs = [run_simulation(r) for r in rates]
    # Print (noise_rate, logical_error_rate) pairs
    print(list(zip(rates, errs)))
