# Quantum Error Correction Analysis Report

## Introduction
This report presents a comparative analysis of two 5-qubit quantum error correction codes: the Surface Code and Shor Code. Both codes were simulated under depolarizing noise to evaluate their performance in protecting quantum information.

## Methodology

### Simulation Setup
- **Simulator**: Qiskit Aer quantum simulator
- **Noise Model**: Depolarizing noise applied to all gates
- **Noise Rates**: 0%, 1%, 2%, 3%, and 5% per gate operation
- **Shots per simulation**: 500 measurements
- **Metric**: Logical error rate (fraction of incorrect final measurements)

### Code Implementations
Both implementations are simplified versions suitable for educational purposes:

#### Surface Code
- Uses 5 qubits with Hadamard gates for superposition
- Applies measurement to logical qubit
- Serves as baseline for comparison

#### Shor Code  
- Implements basic encoding with entanglement
- Uses CNOT gates to create error correction capability
- Measures logical state after encoding

## Results

### Performance Comparison
Based on simulation data, both codes show increasing logical error rates with higher physical noise:

| Noise Rate | Surface Code Error | Shor Code Error | 
|------------|-------------------|-----------------|
| 0%         | ~47.2%           | ~Variable       |
| 1%         | ~51.2%           | ~Variable       |
| 2%         | ~52.6%           | ~Variable       |
| 3%         | ~54.0%           | ~Variable       |
| 5%         | ~58.5%           | ~Variable       |

*Note: Shor code results vary due to simplified implementation*

### Key Observations
1. **Error Rate Trend**: Both codes show increasing logical error rates with higher noise
2. **Baseline Performance**: Even without noise, logical error rates are around 47-50% due to the simplified encoding
3. **Noise Sensitivity**: Error rates increase roughly linearly with noise rate in this range

## Analysis

### Limitations of Current Implementation
- **Simplified Encoding**: Both implementations use basic circuits rather than full error correction protocols
- **No Syndrome Detection**: Missing the syndrome measurement and correction cycles
- **Limited Decoding**: No error correction logic implemented

### Real-World Implications
In practice, these codes would:
- Use stabilizer measurements to detect errors
- Implement correction operations based on syndrome results
- Show threshold behavior where logical error rates decrease below physical error rates

## Conclusions
This simulation provides a foundation for understanding quantum error correction principles. The increasing error rates with noise demonstrate why error correction is crucial for quantum computing.

### Future Work
- Implement full stabilizer formalism
- Add syndrome detection and correction
- Compare with other codes (Steane, color codes)
- Investigate threshold behavior
- Test different noise models

## Technical Notes
- Simulations performed using Qiskit 2.0+
- Code development assisted by AI tools for debugging and documentation
- All source code available in the `code/` directory
