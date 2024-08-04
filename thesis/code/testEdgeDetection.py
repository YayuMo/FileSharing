import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import json
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import clear_output
from qiskit import QuantumCircuit
from qiskit.circuit import ParameterVector
from qiskit.circuit.library import ZFeatureMap
from qiskit.quantum_info import SparsePauliOp, Statevector

from parameters import PARAMS

def conv_circuit(params):
    target = QuantumCircuit(2)
    target.rz(-np.pi / 2, 1)
    target.cx(1, 0)
    target.rz(params[0], 0)
    target.ry(params[1], 1)
    target.cx(0, 1)
    target.ry(params[2], 1)
    target.cx(1, 0)
    target.rz(np.pi / 2, 0)
    return target

def conv_layer(num_qubits, param_prefix):
    qc = QuantumCircuit(num_qubits, name="Convolutional Layer")
    qubits = list(range(num_qubits))
    param_index = 0
    params = ParameterVector(param_prefix, length=num_qubits * 3)
    for q1, q2 in zip(qubits[0::2], qubits[1::2]):
        qc = qc.compose(conv_circuit(params[param_index : (param_index + 3)]), [q1, q2])
        qc.barrier()
        param_index += 3
    for q1, q2 in zip(qubits[1::2], qubits[2::2] + [0]):
        qc = qc.compose(conv_circuit(params[param_index : (param_index + 3)]), [q1, q2])
        qc.barrier()
        param_index += 3

    qc_inst = qc.to_instruction()

    qc = QuantumCircuit(num_qubits)
    qc.append(qc_inst, qubits)
    return qc

def countSqrSum(arr):
    sqrsum = 0
    for item in arr:
        sqrsum += np.power(item, 2)
    return sqrsum

def image2StateVectorArr(path):
    # read image
    img = Image.open(path)
    # resize image
    resized_img = img.resize((32, 32))
    # convert to gray
    gray = resized_img.convert('L')
    # convert to ndarray
    img_array = np.array(gray).reshape(-1)
    sqrsum = countSqrSum(img_array)
    statevector = Statevector(1 / np.sqrt(sqrsum) * np.array(img_array))
    return statevector,sqrsum

def StateVector2image(statevector, sqrsum):
    arr = np.sqrt(sqrsum) * np.array(statevector)
    arr_list = arr.reshape(32, 32)
    img = Image.fromarray(np.array(arr_list))
    return img



def composeCircuit(statevector, n):
    qc = QuantumCircuit(n, n)
    qc.initialize(statevector)
    # qc.compose(feature_map)
    qc = qc.compose(conv_layer(n,"c1"))
    # Bind parameter c1[0] with a specific value

    qc.draw(output='mpl')
    plt.show()

    qc = qc.assign_parameters(PARAMS)
    vec = Statevector.from_instruction(qc)
    return vec.data.real


if __name__ == '__main__':
    statevector,sqrsum = image2StateVectorArr('../img/I08.png')
    vec = composeCircuit(statevector, 10)
    img = StateVector2image(vec, sqrsum)
    plt.imshow(img)
    plt.show()