import numpy as np
import qiskit
from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_distribution
from qiskit.circuit.library import GroverOperator, MCMT, ZGate
from qiskit.quantum_info import Operator
import math
import cmath
from qiskit_ibm_runtime import SamplerV2 as Sampler
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

# get simulator
SIM = Aer.get_backend('qasm_simulator')

# build superposition
def initQC(n):
    # params: n -- num of qubits
    qc = QuantumCircuit(n, n)

    for i in range(n):
        qc.h(i)
    qc.barrier() # differentiate area

    return qc

# build Grover's Oracle
def grover_oracle(marked_states):
    """Build a Grover oracle for multiple marked states

    Here we assume all input marked states have the same number of bits

    Parameters:
        marked_states (str or list): Marked states of oracle

    Returns:
        QuantumCircuit: Quantum circuit representing Grover oracle
    """
    if not isinstance(marked_states, list):
        marked_states = [marked_states]
    # Compute the number of qubits in circuit
    num_qubits = len(marked_states[0])

    qc = QuantumCircuit(num_qubits)
    # Mark each target state in the input list
    for target in marked_states:
        # Flip target bit-string to match Qiskit bit-ordering
        rev_target = target[::-1]
        # Find the indices of all the '0' elements in bit-string
        zero_inds = [ind for ind in range(num_qubits) if rev_target.startswith("0", ind)]
        # Add a multi-controlled Z-gate with pre- and post-applied X-gates (open-controls)
        # where the target bit-string has a '0' entry
        qc.x(zero_inds)
        qc.compose(MCMT(ZGate(), num_qubits - 1, 1), inplace=True)
        qc.x(zero_inds)
    return qc

# build ReverseGate
def buildRev(n):
    # params: n -- num of qubits
    qc = QuantumCircuit(n, n)
    qcIndex = list(range(n))
    mat = np.zeros((2**n, 2**n))
    np.fill_diagonal(mat, -1)
    RevGate = Operator(mat)
    qc.append(RevGate, qcIndex)
    return qc

# build replaced IaM
def buildReIaM(statevector):
    n = len(statevector)
    qubits = int(math.log(n, 2))
    qc = QuantumCircuit(qubits, qubits)
    qcIndex = list(range(qubits))
    sum = 1
    mat = np.zeros((n, n), dtype=np.complex_)
    for item in statevector:
        sum *= cmath.exp(1j * item)
    for i in range(n):
        mat[i,i]=cmath.exp(1j * statevector[i]) / sum
    mat[3,3] = 1
    IaMGate = Operator(mat)
    qc.append(IaMGate, qcIndex)
    return qc

# combine all together
def composeCircuit(n, oracle):
    qc = QuantumCircuit(n, n)
    initial = initQC(n)
    rev = buildRev(n)
    qc = qc.compose(initial)
    qc = qc.compose(oracle)
    qc = qc.compose(rev)
    state = Statevector.from_instruction(qc)
    IaM = buildReIaM(state.data)
    qc = qc.compose(IaM)
    qc.measure_all()
    qc.draw(output='mpl')
    plt.show()
    return qc

# simulate
def simulate(qc, shots, backend):
    sampler = Sampler(backend=backend)
    sampler.options.default_shots = shots
    result = sampler.run([qc]).result()
    # print(result)
    dist = result[0].data.meas.get_counts()
    plot_distribution(dist)
    plt.show()


if __name__ == '__main__':
    marked_states = ["011"]
    oracle = grover_oracle(marked_states)
    qc = composeCircuit(3, oracle)
    # state = Statevector.from_instruction(qc)
    # print(state)
    simulate(qc, 1000, SIM)