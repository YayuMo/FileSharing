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
from thesis.grover_test import initQC, buildRev, grover_oracle, simulate

# get simulator
SIM = Aer.get_backend('qasm_simulator')

# VQC based softmax
def softmaxVQC(args):
    vec = args["data"]
    arr = np.zeros(len(vec),dtype = np.complex_)
    sum = 0
    for item in vec:
        sum += cmath.e ** item
    for i in range(len(vec)):
        arr[i] = cmath.sqrt(cmath.e ** vec[i] / sum)
    return arr

# VQC based ReLU
def reluVQC(args):
    vec = args["data"]
    n = len(args["markedState"])
    arr = np.zeros(len(vec))
    for i in range(len(vec)):
        if vec[i] > 0:
            arr[i] = 1 / math.sqrt(n)
        else:
            arr[i] = 0
    return arr

# VQC based Sigmoid
def sigmoidVQC(args):
    vec = args["data"]
    arr = np.zeros(len(vec),dtype = np.complex_)
    for i in range(len(vec)):
        arr[i] = 100 / (1 + cmath.sqrt(cmath.e ** (-vec[i])))
    args["data"] = arr
    return softmaxVQC(args)

# measurement
def measurement(n, statevector):
    qc = QuantumCircuit(n, n)
    qc.initialize(statevector.data)
    qc.measure_all()

    return qc

# build circuit
def composeCircuit(n, oracle, marked_state, func):
    qc = QuantumCircuit(n, n)
    initial = initQC(n)
    rev = buildRev(n)
    qc = qc.compose(initial)
    qc = qc.compose(oracle)
    qc = qc.compose(rev)
    statevector = Statevector.from_instruction(qc)
    args = {}
    args["markedState"] = marked_state
    args["data"] = statevector.data
    statevector = Statevector(func(args))
    print(sigmoidVQC(args))
    return statevector

# set func as param
def perform_action(func, arg):
    return func(arg)

if __name__ == '__main__':
    marked_states = ["110", "011"]
    oracle = grover_oracle(marked_states)
    statevector = composeCircuit(3, oracle, marked_states, sigmoidVQC)
    qc = measurement(3, statevector)
    simulate(qc, 100000, SIM)
    print(statevector)
