import numpy as np
from qiskit import QuantumCircuit, transpile, assemble
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram
from qiskit_aer import Aer

# 定义给定的状态向量
statevector = Statevector([0.0691902 - 0.34671706j, 0.0691902 - 0.34671706j,
                           0.0691902 - 0.34671706j, -0.27784168 + 0.21864126j,
                           0.0691902 - 0.34671706j, 0.0691902 - 0.34671706j,
                           0.0691902 - 0.34671706j, 0.0691902 - 0.34671706j])

# 创建量子电路并初始化状态
qc = QuantumCircuit(3)
qc.initialize(statevector.data, [0, 1, 2])

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
