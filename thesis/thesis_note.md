# Thesis

## Topic: Quantum Oracle Synthesis on varied basis

## Stage 1

### Background

- Using the varied basis for Oracle Synthesis
- Oracle synthesis should be considered as the combination of Encoded Basis (e.g. Angle encoding--$\otimes^{(N-2)/2}_{j=0}cos(x*{2j+1})\ket{0}+e^{ix2j}sin(x_{2j+1})\ket{1}$) and General Basis (e.g. Orthogonal Z-basis {$\ket{0},\ket{1}$}, Orthogonal X-basis {$\ket{+},\ket{-}$} ), also shown as the figure follows
  - ![](C:\Users\14767\AppData\Roaming\Typora\typora-user-images\image-20240506161928267.png)

### Problem Description

- One big problem with topic 1 is that Grover's algorithm depends on the use of entanglement in the diffusion filter (as well as quantum superposition). It is not clear how entanglement can be accomplished with amplitude (or angle) encoded. A new method for performing inversion about the mean would need to be created if angle- or amplitude-encoding is used for the oracle.

### Basis Tutorial

- Basic Info (from source paper)

  - | Encoding Patern         | Encoding                                                     | Req. qubits      |
    | ----------------------- | ------------------------------------------------------------ | ---------------- |
    | Basis Encoding [1]      | $x=(b_{m-1},b_{m-2},...,b_0),x \in \mathbb{Z}_2^m,b_j \in \mathbb{Z}_2 \rarr \ket{x}=\ket{b_{m-1}b_{m-2}...b_0}$ | l = m            |
    | Angle Encoding          | $x\in [0,2\pi) \rarr \otimes_{j=0}^{(N-2)/2}cos(x_{2j+1})\ket{0}+e^{ix_{2j}}sin(x_{2j+1})\ket{1}$(Dense Encoding) [1]<br />$x \rarr \otimes_{j=0}^{N-1}cos(x_j)\ket{0}+sin(x_j)\ket{1}$(General Encoding)[4] | 1 per data point |
    | Amplitude Encoding [4]  | $x \rarr \sum_{i=0}^{n-1}x_i\ket{i}$, where $\sum|x_i|^2=1$  | l = log(n)       |
    | Basic QROM [1]          | $\{\vec{a},\vec{x}\},a_j  \in \mathbb{Z}^n_2, x_j \in \mathbb{Z}^m_2\rarr \ket{\psi_x}=\sum^{n-1}_{j=0}\ket{a_j}\ket{x_j}$ |                  |
    | Angle QROM [1]          | $\{\vec{a},\vec{x}\},a_j  \in \mathbb{Z}^n_2, x_j \in [0,2\pi) \rarr \sum^{(n-2)/2}_{j=0}\ket{a_j}(cos(x_{2j+1})\ket{0}+e^{ix_{2j}}sin(x_{2j+1})\ket{1})$ |                  |
    | Improved Angle QROM [1] | $\{\vec{a},\vec{x}\},a_j  \in \mathbb{Z}^n_2, S_j \in [0,2\pi), E_j \in [0,2\pi) \rarr \sum^{N-1}_{j=0}\ket{a_j}(cos(S_j)\ket{0}+e^{iE_j}sin(S_j)\ket{1})$ |                  |
    | QuAM Encoding [4]       | $\sum^{n-1}_{i=0}\frac{1}{\sqrt{n}}\ket{x_i},x_i \in \mathbb{Z}^m_2$ | l                |
    | QRAM Encoding [4]       | $\sum^{n-1}_{j=0}\frac{1}{\sqrt{n}}\ket{a_j}\ket{x_j},a_j  \in \mathbb{Z}^n_2, x_j \in \mathbb{Z}^m_2$ | log(n) + l       |

- Basic Encoding

- Angle Encoding

- Amplitude Encoding

  - Context
    - A numerical input data vector $[x_0,...,x_{n-1}]^T$ must be encoded for an algorithm.

  - Solution 
    - Use amplitudes to encode the data. As the squared moduli of the amplitudes of a quantum state must sum up to 1, the input vector needs to be normalized to length 1. This is illustrated in Fig. 5 for a 2-dimensional input vector that contains 2 data points. To associate each amplitude with a component of the input vector, the dimension of the vector must be equal to a power of 2 because the vector space of an $n$ qubit register has dimension $2^n$. If this is not the case, the input vector can be padded with additional zeros to increase the dimension of it. Using a suitable state preparation routine (see Known Uses), the input vector is encoded in the amplitudes of the quantum state as follows: 
    
      - $$
        \ket{\psi}=\sum^{n-1}_{i=0}x_i\ket{i}
        $$
    
        
    
    - As the amplitudes depend on the data, the process of encoding the data (but not the encoding itself) is often referred to as arbitrary state preparation.
    
      - ![image-20240701201507306](C:\Users\14767\AppData\Roaming\Typora\typora-user-images\image-20240701201507306.png)
    
  - Result

    - A data input vector of length $l$ can be represented by $[log_2(l)]$ qubits - this is indeed a very compact representation. For an arbitrary state represented by $n$ qubits (which represents $2^n$ data values), it is known that at least $\frac{1}{n}2^n$ parallel operations are needed []

- Basic QROM

- Angle QROM

- Improved Angle QROM

- Quantum Associative Memory (QuAM) Encoding [3]

  - Context

    - A quantum algorithm requires multiple numerical values X as input for further calculations

  - Solution

    - Use a quantum associative memory (QuAM) to prepare a superposition of basis encoded values in the same qubit register. In Fig. 3, this is illustrated for the 3 values $x_1$, $x_2$ and $x_3$ in binary format. Note that the resulting encoding is an equally weighted superposition of the basis encoded values, i.e., all amplitude are of the same magnitude.

      - $$
        \begin{matrix} x_0 \\ x_1 \\ x_2  \end{matrix}
        \begin{bmatrix} 0 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 1 & 1\end{bmatrix}
        \rarr 
        \begin{matrix} \frac{1}{\sqrt{3}} \\ \frac{1}{\sqrt{3}} \\ \frac{1}{\sqrt{3}}  \end{matrix}
        \begin{matrix} |0 & 1 & 0\rangle + \\ |1 & 1 & 0\rangle+ \\ |0 & 1 & 1\rangle \quad \end{matrix}
        $$

      - ![image-20240701190439486](C:\Users\14767\AppData\Roaming\Typora\typora-user-images\image-20240701190439486.png)

        - Fig. 3. Resulting Encoding. Each data value represented by a row on the left is encoded in BASIS ENCODING and an amplitude of $\frac{1}{\sqrt{n}}$

    - To load the data, the register of the quantum associative memory is in superposition of 2 states, a processing and a memory branch. (Fig. 4). Both branches have a load and a storage part. An additional element is first prepared into the load part of both branches (step 1). Next, the processing branch is split in such a manner, that the new element gets a proper amplitude (step 2) such that it can be stored by bringing it into superposition with the already added elements (step 3). Finally, an UNCOMPUTE cleans the both branches to be ready for the next iteration. 

      - **![image-20240701191019374](C:\Users\14767\AppData\Roaming\Typora\typora-user-images\image-20240701191019374.png)**
        - Fig. 4. Illustration of the state preparation routine. In each iteration, an element is loaded and brought into superposition with the already stored elements.

  - Result

    - The resulting encoding is a digital encoding and therefore suitable for arithmetic computations. For input $n$ numbers that are approximated by $l$ digits, $l$ qubits are needed for this representation. Each of the $n$ encoded input values is represented by a basis vector with an amplitude of $\frac{1}{\sqrt{n}}$. All other $2^l-n$ amplitudes of the register are zero - in our example, $\ket{000}$, $\ket{001}$, $\ket{100}$, $\ket{101}$, and $\ket{111}$. The amplitude vector is therefore often sparse for this encoding.

  - Related Pattern

    - This pattern refines INITIALIZATION and makes use of UNCOMPUTE. UNIFORM SUPERPOSITION creates a superposition of all computational basis states. Each of the computational basis states also represents a value in BASIS ENCODING.

  - Known Uses

    - The presented state preparation routine based on [5] can be used whenever multiple data values need to be represented in BASIS ENCODING. Shor's algorithm [6] for the factorization of prime numbers, a quantum version of the Fourier transform [7], and Grover's algorithm [8] for unstructured search rely on this encoding. Various algorithms extend or use Grover's algorithm and therefore also make use of this encoding.  

- QRAM Encoding


### Testing method

- Grover's Searching Algorithm
  - 
- Inversion of Mean
  - 
- Softmax replacement of IoM

  - Standard softmax equation

    - $$
      \sigma(\hat{z})_i=\frac{e^{z_i}}{\sum^n_{j=1}e^{z_j}}
      $$
    - $\sigma:\mathbb{R}^n \rarr (0,1)^n $, where $n \ge 1$, takes a vector $\hat{z}=(z_1,...,z_n) \in \mathbb{R}^n$
- Approximate Circuit for method
  - ![image-20240621154955368](C:\Users\14767\AppData\Roaming\Typora\typora-user-images\image-20240621154955368.png)
  - $U_f$ represents Grover's Oracle
  - $U_{IaM}$ represents the replacement of Inversion about Mean, could be softmax or other method

### References

[1] Sinha A, Henderson E R, Henderson J M, et al. Automated quantum memory compilation with improved dynamic range[C]//2022 IEEE/ACM Third International Workshop on Quantum Computing Software (QCS). IEEE, 2022: 22-35.

[2] Weigold M, Barzen J, Leymann F, et al. Data encoding patterns for quantum computing[C]//Proceedings of the 27th Conference on Pattern Languages of Programs. 2020: 1-11.

[3] Weigold M, Barzen J, Leymann F, et al. Expanding data encoding patterns for quantum algorithms[C]//2021 IEEE 18th International Conference on Software Architecture Companion (ICSA-C). IEEE, 2021: 95-101.

[4] Weigold M, Barzen J, Leymann F, et al. Encoding patterns for quantum algorithms[J]. IET Quantum Communication, 2021, 2(4): 141-152.

[5] Ventura D, Martinez T. Quantum associative memory[J]. Information sciences, 2000, 124(1-4): 273-296.

[6] Shor P W. Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer[J]. SIAM review, 1999, 41(2): 303-332.v

[7] Coppersmith D. An approximate Fourier transform useful in quantum factoring[J]. arXiv preprint quant-ph/0201067, 2002.

[8] Grover L K. A fast quantum mechanical algorithm for database search[C]//Proceedings of the twenty-eighth annual ACM symposium on Theory of computing. 1996: 212-219.

