import numpy as np
import matplotlib.pyplot as plt
import qiskit
from qiskit.circuit import Parameter
import qiskit_aer

# Create a parameterized quantum circuit
theta = Parameter('θ')
qc = qiskit.QuantumCircuit(2)

qc.h(0)
qc.cry(theta, 0, 1)
qc.measure_all()

# Activate the GPU capability
backend = qiskit_aer.AerSimulator(
    method="statevector",
    device="GPU",
    cuStateVec_enable=True,
)

theta_values = np.linspace(0, 2 * np.pi, 50)

# Run the circuit for different values of theta to plot it
counts_list = []
for theta_value in theta_values:
    bound_circuit = qc.assign_parameters({theta: theta_value})
    transpiled_circuit = qiskit.transpile(bound_circuit, backend)
    
    # Run simulation
    job = backend.run(transpiled_circuit, shots=1000)
    result = job.result()

    # Store counts
    counts = result.get_counts()
    counts_list.append(counts)

# Analyze results and save the plot:

probabilities_00 = []
probabilities_11 = []

for counts in counts_list:
    total_counts = sum(counts.values())
    probabilities_00.append(counts.get('00', 0) / total_counts)
    probabilities_11.append(counts.get('11', 0) / total_counts)

print("Probabilities for |00> : \n", probabilities_00)
print("Probabilities for |01> : \n", probabilities_11)
print("Total counts: \n", total_counts)
print("Counts: \n", counts)

plt.figure(figsize=(10, 6))
plt.plot(theta_values, probabilities_00, label='P(|00⟩)', marker='o')
plt.plot(theta_values, probabilities_11, label='P(|01⟩)', marker='s')
plt.title("Probabilities vs Parameter θ")
plt.xlabel("θ (radians)")
plt.ylabel("Probability")
plt.legend()
plt.grid()

plt.savefig("plot.png")

print("Plot saved as 'plot.png'")
