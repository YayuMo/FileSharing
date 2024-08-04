# Report I for the thesis

## Problem Definition

- It is uncertain how entanglement can be accomplished with encoded basis
- A new method for the same functionality of Inversion about Mean should be created
- For varied basis, the definition of oracle synthesis could be given specific results and and input, then converge the state vector of input to the output vector. 
  - For example, in amplitude encoding, the definition could be described below
  - Suppose we have a input state vector $\ket{\psi}=\frac{1}{\sqrt{3}}\ket{00}+\frac{1}{\sqrt{3}}\ket{01}+\frac{1}{\sqrt{3}}\ket{10}= [\frac{1}{\sqrt{3}} \ \frac{1}{\sqrt{3}} \ \frac{1}{\sqrt{3}} \ 0]^T$, and a result state vector $U_f\ket{\psi}= \frac{1}{\sqrt{29}}(2\ket{00}+3\ket{01}+4\ket{10}) = [\frac{2}{\sqrt{29}} \ \frac{3}{\sqrt{29}} \ \frac{4}{\sqrt{29}} \ 0]^T$. The approximated circuit could be drawn as follows:
    - ![image-20240718161926637](C:\Users\14767\AppData\Roaming\Typora\typora-user-images\image-20240718161926637.png)
    - The function of $U_f$ could be the convergence from $\ket{input}$ to $\ket{output}$

## Tutorial for several quantum basis

- **Basis Encoding**

  - $$
    x=(b_{n-1},b_{n-2},...,b_0),x \in \mathbb{Z}_2^n,b_j \in \mathbb{Z}_2 \rarr \ket{x}=\ket{b_{n-1}b_{n-2}...b_0}
    $$

  - **Brief Intro**

    - Represent a data element in a quantum computer in order to perform calculations.

  - **Advantage**

    - Straightforward

    - Could be applied in performing calculations

    - Easy to construct, since only one quantum gate (Pauli-X) is needed to obtain the encoding

  - **Storage**

    - Basis Encoding usually doesn't take storage into consideration, but every qubit could be mapped to classical bits accordingly, which is a perfect way to store the qubits. 

  - **Num of Qubit Required**

    - n = l
    - the number of qubit $n$ is exactly the same as data length $l$.

  - **Use Cases**

    - Arithmetic calculations

  - **Noise Model**

    - Bit Flip. It could happen when one or more qubits are interfered by environments to flip $\ket{0}$ to $\ket{1}$ or $\ket{1}$ to $\ket{0}$.

  - **Limitations**

    - Since the number of qubits depends on the data length, which basically requires more qubits to represent data.

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

      - 1 qubit could encode 2 data points ($x_{2j},x_{2j+1}$)

      - 

    - **Storage**

    - **Num of Qubit Required**

      - 1 each 2 data point

    - **Use Cases**
    
    - **Noise Model**
    
    - **Limitations**
    
    - **Examples**

- **Amplitude Encoding**

  - $$
    x \rarr \sum_{i=0}^{n-1}c_i\ket{i},c_i= \frac{x_i}{\sqrt{\sum x_i^2}}
    $$

  - **Brief Intro**

    - Encode data in a compact manner according to its original value.
    - The coefficient $c_i$ represents the value of the data (e.g. pixel value in images), and the $i$ represents the index of data (e.g. pixel position in images)

  - **Advantage**

  - **Storage**

  - **Num of Qubit Required**

    - $n = log_2(l)$
    - $n$ qubits could represent $2^n$ data values.

  - **Use Cases**

  - **Noise Model**

  - **Limitations**

  - **Examples**

    - $$
      x=[2 \ 3 \ 4]^T \rarr \ket{x}=\frac{1}{\sqrt{29}}(2\ket{00}+3\ket{01}+4\ket{10})
      $$

- **Quantum Associative Memory (QuAM) Encoding**

  - $$
    \sum^{n-1}_{i=0}\frac{1}{\sqrt{n}}\ket{x_i},x_i \in \mathbb{Z}^n_2
    $$

  - **Brief Intro**

    - Represent a collection of data elements in a quantum computer in order to perform calculations

  - **Advantage**

  - **Storage**

  - **Num of Qubit Required**

    - $n = size(x_i)$

  - **Use Cases**

  - **Noise Model**

  - **Limitations**

  - **Examples**

    - $$
      \begin{matrix} x_0 \\ x_1 \\ x_2  \end{matrix}
      \begin{bmatrix} 0 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 1 & 1\end{bmatrix}
      \rarr 
      \begin{matrix} \frac{1}{\sqrt{3}} \\ \frac{1}{\sqrt{3}} \\ \frac{1}{\sqrt{3}}  \end{matrix}
      \begin{matrix} |0 & 1 & 0\rangle + \\ |1 & 1 & 0\rangle+ \\ |0 & 1 & 1\rangle \quad \end{matrix}
      $$
    
    - 

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

- Variational Quantum Algorithm (VQA) approaches [1]

  - In the original article, the procedure is shown as fig.

    - ![img](https://ars.els-cdn.com/content/image/1-s2.0-S0030401823007411-gr1_lrg.jpg)

  - The input state are required to evolve to the target state in several iterations

  - And in each iteration, the measured expectation value are going through traditional process (computing loss or gradient descending) in order to adjust the variable embedded in Variational Quantum Circuit (VQC)

  - In the original paper the expectation value measured are defined as

    - $$
      f(\theta) = \bra{0}U^\dagger(\theta)\hat{B}U(\theta)\ket{0}
      $$

  - Inspired by the VQA, my core idea is to extract the state vector and apply it in a traditional approach in order to fetch the required state

    - ![QQ_1722484352552](C:\Users\14767\AppData\Local\Temp\QQ_1722484352552.png)

  - $$
    \begin{bmatrix}
    \bra{0}f
    \end{bmatrix}
    $$

  - 

  - However, 

  - Questions about this method

    - Does the expectation value work the same as the extraction of the state vector?
    - From a physical perspective, is it possible to directly extract the state vector output by circuit?

- The primary idea is to transfer the diagonal form of the formula below to the unitary matrix

  - Suppose we have a diagonal matrix D

    - $$
      D = 
      	\begin{bmatrix} 
      	\sigma(\hat{z})_0 &  \\
      	& \sigma(\hat{z})_1 & & \\
      	&& \ddots& \\
      	&& &\sigma(\hat{z}_{n-1})
      	\end{bmatrix}
      $$

    - where $\sigma(\hat{z})$ represents the function that could implement IaM (Inversion about Mean).

  - Then transfer the $D$ to Unitary Matrix $U$ which follows the rule:

    - $$
      UU^\dagger = U^\dagger U = I \\
      U^{-1} = U^\dagger
      $$

- **Inspiration Equation**

  - **Euler's Equation**

    - $$
      e^{ix} = \cos x + i\sin x \\
      e^{i\pi}+1 = 0
      $$

  - **Taylor Expansion**

    - $$
      e^x = \sum^\infin_{n=0}\frac{x^n}{n!} = 1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+...
      $$

- **SoftMax**

  - **Formula**

    - $$
      \sigma(\hat{z})_i=\frac{e^{z_i}}{\sum^{n-1}_{j=0}e^{z_j}}
      $$

  - **Method**

    - $$
      U_f=\frac{1}{\sum^{n-1}_{j=0}e^{z_j}}
      \begin{bmatrix} 
      	e^{iz_0} &  \\
      	& e^{iz_1} & & \\
      	&& \ddots& \\
      	&& &e^{iz_n}
      \end{bmatrix}
      $$

    - What I firstly consider of was trying to build a form that is similar to 

- **Sigmoid**

  - **Formula**

    - $$
      \sigma(\hat{z})=\frac{1}{1+e^{-z_i}}
      $$

- **ReLU**

  - **Formula**

    - $$
      \sigma(\hat{z})_i=max(z_i,0) = \frac{z_i+|z_i|}{2}
      $$

    - Oracle for basis encoding could work as 

      - $$
        U_f =
        \begin{cases}
        \frac{1}{\sqrt{n}} &, z_i>0 \\
        0 &, z_i\leq0
        \end{cases}
        $$

      - where $n$ represents the number of target marked

  - **Method**

    - Firstly apply the Reverse Oracle to $U_{grover}\ket{\psi}$, the oracle has the function of reversing the sign of every element in the state vector. The transfer matrix of $U_{reverse}$ could be represented as

      - $$
        \begin{bmatrix}
        -1 & & & \\
         & -1 & & \\
         & & -1 & \\
         & & & -1
        \end{bmatrix}
        $$
        
      - and it's unitary

    - Extract the state vector and 

    - It could be applied to traditional Grover's Search, and it is not  

## Future Works

- Parameter Embedded Circuit -- Specifically, for Angle Encoding Series, can we transfer the original array (e.g. $$)into parameters and try to train the parameters to converge to a specific target vector to avoid the entanglement problem and exploit the benefits of VQA?


## References

[1] Gong L H, Pei J J, Zhang T F, et al. Quantum convolutional neural network based on variational quantum circuits[J]. Optics Communications, 2024, 550: 129993.
