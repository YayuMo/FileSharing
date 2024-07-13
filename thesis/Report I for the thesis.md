# Report I for the thesis

## Problem Definition



## Tutorial for several quantum basis

- **Basis Encoding**

  - $$
    x=(b_{n-1},b_{n-2},...,b_0),x \in \mathbb{Z}_2^n,b_j \in \mathbb{Z}_2 \rarr \ket{x}=\ket{b_{n-1}b_{n-2}...b_0}
    $$

  - **Brief Intro**

    - Represent a data element in a quantum computer in order to perform calculations.

  - **Advantage**

    - Straightforward

    - Could be applied in perform calculation

    - Easy to construct, since only one quantum gate (Pauli-X) is needed to obtain the encoding

  - **Storage**

    - Basis Encoding usually doesn't take storage into consideration, but

  - **Num of Qubit Required**

    - n = l
    - the number of qubit $n$ is exactly the same as data length $l$.

  - **Use Cases**

    - Arithmetic calculations

  - **Noise Model**

    - Bit Flip. It could happen when one or more qubits are interfered by environments to flip $\ket{0}$ to $\ket{1}$ or $\ket{1}$ to $\ket{0}$

  - **Limitations**

    - Since the number of qubits depends on the data length, 

  - **Examples**

    - $$
      \quad \quad \quad b_1b_0 \rarr \ket{q_1q_0} \\3(D) = 11(B) \rarr \ket{11}
      $$

- **Angle Encoding**

  - **General Encoding**

    - $$
      x \in [0,2\pi) \rarr \otimes_{j=0}^{N-1}cos(x_j)\ket{0}+sin(x_j)\ket{1}
      $$

    - **Brief Intro**

      - Represent each data-point by a separate qubit.

    - **Advantage**

    - **Storage**

    - **Num of Qubit Required**

      - 1 per data point

    - **Use Cases**

    - **Noise Model**

    - **Limitations**

    - **Examples**

  - **Dense Encoding**

    - $$
      x\in [0,2\pi) \rarr \otimes_{j=0}^{(N-2)/2}cos(x_{2j+1})\ket{0}+e^{ix_{2j}}sin(x_{2j+1})\ket{1}
      $$

    - **Brief Intro**

      - An alternative encoding that exploits an additional property of qubits (relative phase) to use only $\frac{n}{2}$ qubits to encode $n$ data points.

    - **Advantage**

    - **Storage**

    - **Num of Qubit Required**

      - 1 each 2 data point

    - **Use Cases**

    - **Noise Model**

    - **Limitations**
    
    - **Examples**

- **Amplitude Encoding**

  - $$
    x, \sum |x_i|^2=1 \rarr \sum_{i=0}^{n-1}x_i\ket{i}
    $$

  - **Brief Intro**

    - Encode data in a compact manner that do not require calculations.

  - **Advantage**

  - **Storage**

  - **Num of Qubit Required**

    - $n = log_2(l)$
    - $n$ qubits could represent $2^n$ data values.

  - **Use Cases**

  - **Noise Model**

  - **Limitations**

  - **Examples**

- **Quantum Associative Memory (QuAM) Encoding**

  - $$
    \sum^{n-1}_{i=0}\frac{1}{\sqrt{n}}\ket{x_i},x_i \in \mathbb{Z}^n_2
    $$

  - **Brief Intro**

    - Represent a collection of data elements in a quantum computer in order to perform calculations

  - **Advantage**

  - **Storage**

  - **Num of Qubit Required**

    - l = n

  - **Use Cases**

  - **Noise Model**

  - **Limitations**

  - **Examples**

- **Quantum Random Access Memory (QRAM) Encoding**

  - $$
    \{ \vec{a},\vec{x} \} \rarr \sum^{n-1}_{j=0}\frac{1}{\sqrt{n}}\ket{a_j}\ket{x_j},a_j  \in \mathbb{Z}^n_2, x_j \in \mathbb{Z}^m_2
    $$

  - **Brief Intro**

    - Use a quantum random access memory to access a superposition of data values at once.

  - **Advantage**

  - **Storage**

  - **Num of Qubit Required**

  - **Use Cases**

  - **Noise Model**

  - **Limitations**

  - **Examples**

- **Quantum Read-Only Memory (QROM) Encoding**

  - $$
    \{\vec{a},\vec{x}\},a_j  \in \mathbb{Z}^n_2, x_j \in \mathbb{Z}^m_2\rarr \ket{\psi_x}=\sum^{n-1}_{j=0}\ket{a_j}\ket{x_j}
    $$

  - **Brief Intro**

    - .

  - **Advantage**

  - **Storage**

  - **Num of Qubit Required**

  - **Use Cases**

  - **Noise Model**

  - **Limitations**

  - **Examples**

- **Angle QROM**

  - $$
    \{\vec{a},\vec{x}\},a_j  \in \mathbb{Z}^n_2, x_j \in [0,2\pi) \rarr \sum^{(n-2)/2}_{j=0}\ket{a_j}(cos(x_{2j+1})\ket{0}+e^{ix_{2j}}sin(x_{2j+1})\ket{1})
    $$

  - **Brief Intro**

    - .

  - **Advantage**

  - **Storage**

  - **Num of Qubit Required**

  - **Use Cases**

  - **Noise Model**

  - **Limitations**

  - **Examples**

- **Improved Angle QROM**

  - $$
    \{\vec{a},\vec{x}\},a_j  \in \mathbb{Z}^n_2, S_j \in [0,2\pi), E_j \in [0,2\pi) \rarr \sum^{N-1}_{j=0}\ket{a_j}(cos(S_j)\ket{0}+e^{iE_j}sin(S_j)\ket{1})
    $$

  - **Brief Intro**

    - .

  - **Advantage**

  - **Storage**

  - **Num of Qubit Required**

  - **Use Cases**

  - **Noise Model**

  - **Limitations**

  - **Examples**


## Trial to apply an alternative method in Grover's algorithm

- SoftMax
- Sigmoid
- ReLU


$$
UU^\dagger = U^\dagger U = I \\
U^{-1} = U^\dagger
$$