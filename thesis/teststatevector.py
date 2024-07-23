from matplotlib import pyplot as plt
from qiskit import QuantumCircuit, transpile, assemble
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram
from qiskit_aer import Aer

from thesis.grover_test import grover_oracle, composeCircuit

if __name__ == '__main__':
    marked_states = ["011"]
    oracle = grover_oracle(marked_states)
    qc = composeCircuit(3, oracle)
    state = Statevector.from_instruction(qc)

    # 创建量子电路并初始化状态
    qc = QuantumCircuit(3)
    qc.initialize(state.data, [0, 1, 2])

    # 添加测量操作
    qc.measure_all()

    # 使用Qiskit Aer模拟器
    simulator = Aer.get_backend('qasm_simulator')

    # 编译和运行电路
    compiled_circuit = transpile(qc, simulator)
    qobj = assemble(compiled_circuit)
    result = simulator.run(qobj).result()

    # 获取测量结果
    counts = result.get_counts()

    # 打印测量结果
    print("测量结果:", counts)

    # 可视化测量结果
    plot_histogram(counts)

    plt.show()