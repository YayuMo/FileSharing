# Thesis

## Topic: Quantum Oracle Synthesis on varied basis

## Stage 1

### Background

- Using the varied basis for Oracle Synthesis
- Oracle synthesis should be considered as the combination of Encoded Basis (e.g. Angle encoding--$\otimes^{(N-2)/2}_{j=0}cos(x*{2j+1})\ket{0}+e^{ix2j}sin(x_{2j+1})\ket{1}$) and General Basis (e.g. Orthogonal Z-basis {$\ket{0},\ket{1}$}, Orthogonal X-basis {$\ket{+},\ket{-}$} ), also shown as the figure follows
  - ![](C:\Users\14767\AppData\Roaming\Typora\typora-user-images\image-20240506161928267.png)

### Problem Description

- One big problem with topic 1 is that Grover's algorithm depends on the use of entanglement in the diffusion filter (as well as quantum superposition). It is not clear how entanglement can be accomplished with amplitude (or angle) encoded. A new method for performing inversion about the mean would need to be created if angle- or amplitude-encoding is used for the oracle.
- Definition of problem
  - 


### Basis Tutorial

- Basic Info (from source paper)

  - | Encoding Patern         | Encoding                                                     | Req. qubits      |
    | ----------------------- | ------------------------------------------------------------ | ---------------- |
    | Basis Encoding [1]      | $x=(b_{m-1},b_{m-2},...,b_0),x \in \mathbb{Z}_2^m,b_j \in \mathbb{Z}_2 \rarr \ket{x}=\ket{b_{m-1}b_{m-2}...b_0}$ | l = m            |
    | Angle Encoding          | $x\in [0,2\pi) \rarr \otimes_{j=0}^{(N-2)/2}cos(x_{2j+1})\ket{0}+e^{ix_{2j}}sin(x_{2j+1})\ket{1}$(Dense Encoding) [1]<br />$x \rarr \otimes_{j=0}^{N-1}cos(x_j)\ket{0}+sin(x_j)\ket{1}$(General Encoding)[4] | 1 per data point |
    | Amplitude Encoding [2]  | $x \rarr \sum_{i=0}^{n-1}x_i\ket{i}$, where $\sum|x_i|^2=1$  | l = log(n)       |
    | QuAM Encoding [2]       | $\sum^{n-1}_{i=0}\frac{1}{\sqrt{n}}\ket{x_i},x_i \in \mathbb{Z}^m_2$ | l                |
    | QRAM Encoding [4]       | $\sum^{n-1}_{j=0}\frac{1}{\sqrt{n}}\ket{a_j}\ket{x_j},a_j  \in \mathbb{Z}^n_2, x_j \in \mathbb{Z}^m_2$ | log(n) + l       |
    | Basic QROM [1]          | $\{\vec{a},\vec{x}\},a_j  \in \mathbb{Z}^n_2, x_j \in \mathbb{Z}^m_2\rarr \ket{\psi_x}=\sum^{n-1}_{j=0}\ket{a_j}\ket{x_j}$ |                  |
    | Angle QROM [1]          | $\{\vec{a},\vec{x}\},a_j  \in \mathbb{Z}^n_2, x_j \in [0,2\pi) \rarr \sum^{(n-2)/2}_{j=0}\ket{a_j}(cos(x_{2j+1})\ket{0}+e^{ix_{2j}}sin(x_{2j+1})\ket{1})$ |                  |
    | Improved Angle QROM [1] | $\{\vec{a},\vec{x}\},a_j  \in \mathbb{Z}^n_2, S_j \in [0,2\pi), E_j \in [0,2\pi) \rarr \sum^{N-1}_{j=0}\ket{a_j}(cos(S_j)\ket{0}+e^{iE_j}sin(S_j)\ket{1})$ |                  |

- **Basic Encoding** [2]

  - Represent a data element in a quantum computer in order to perform calculations

  - **Context**
    - A quantum algorithm requires numerical input data $X$ for further calculations.

  - **Solution**
    - The main idea for this encoding is to use the $computational \ basis \{\ \ket{0...00},\ket{0...01},...,\ket{1...11} \} $ to encode the input data: An input number $x$ is approximated by a binary format $x := b_{n-1}...b_1b_0$ which is then turned into the corresponding basis vector $\ket{x}:=\ket{b_{n-1}...b_1b_0}$. For example, the number "2" is represented as 10 which is then encoded by $\ket{10}$ (Fig. 2). In general, this leads to the following encoding: $X\approx \sum^m_{i=-k}b_i2^i \mapsto \ket{b_m...b_{-k}}$ where $X$ is first approximated with a precision of $k+m$ significant digits and then represented by a basis vector.
      - ![image-20240702163356178](C:\Users\14767\AppData\Roaming\Typora\typora-user-images\image-20240702163356178.png)

  - **Result**
    - This encoding can be categorized as digital encoding because it is suitable for arithmetic computations. For input numbers that are approximated by $l$ digits, $l$ qubits are needed for its representation. To realize this encoding, the initial $\ket{0}$ state of qubits that represent a '1' digit must be flipped into $\ket{1}$. For one qubit, this can be done by a single operation, and thus, this encoding can be prepared in linear time.

  - **Related Pattern**
    - This pattern is a refinement of INITIALIZATION. If an algorithm requires several numbers as input, each can be encoded in BASIS ENCODING which can be processed by the QuAM pattern.

  - **Known Uses**
    - Vedral et al. [6] give multiple examples for algorithms that perform arithmetic operations on numbers in BASIS ENCODING. A formal description of the solution above is also given in [5] and [7]. As only one quantum gate is needed to obtain this encoding, this state preparation routine can be implemented straightforwardly.

- **Angle Encoding**

  - Represent each data-point by a separate qubit

  - **Context**
    
    - An algorithm requires an efficient encoding schema to be able to perform as many operations as possible within the decoherence time after the data has been loaded
    
  - **Solution**
    - First, normalize all data-points that should be encoded to the interval $[0, 2\pi]$. Each value $x_i$ is then represented by a single qubit as follows (Fig. 4): a rotation around the y-axis of the Bloch Sphere (refer to Fig. 2) is applied. Hereby, the angle for the rotation depends on the data value. 
      - ![image-20240705160059740](C:\Users\14767\AppData\Roaming\Typora\typora-user-images\image-20240705160059740.png)
    
  - **Result**

    - The resulting quantum state for this encoding is separable, i.e. the qubits are not entangled:

      - $$
        \ket{\psi}= 
        \begin{pmatrix}
        cos \ x_0 \\
        sin \ x_0
        \end{pmatrix} \otimes
        \begin{pmatrix}
        cos \ x_1 \\
        sin \ x_1
        \end{pmatrix} \otimes ...
        \otimes
        \begin{pmatrix}
        cos \ x_n \\
        sin \ x_n
        \end{pmatrix}
        $$

    - The main advantage of this encoding is that it is very efficient in terms of operations: Only a constant number of parallel operations is needed regardless of how many data values need to be encoded [8]. However, the number of data values affects how many qubits are needed: One qubit is required to encode one component of the input vector. Thus, as only single-qubit rotations are required the state preparation routine is highly efficient while the number of qubits for this encoding is not optimal [9].

  - **Related Patterns**

    - This pattern refines INITIALIZATION

  - **Variants**

    - [8] present $dense \ angle \ encoding$ as an alternative encoding that exploits an additional property of qubits (relative phase) to use only $\frac{n}{2}$ qubits to encode $n$ data points.

  - **Known Uses**

    - [8] and [9] present a classifier based on this encoding. The encoding is also used in quantum image processing: In the so-called flexible representation of quantum image (FRQI), one qubit represents the color information of a pixel whereas another register represents the position [10]. In the context of quantum neural networks, a qubit using this encoding has been referred to as a quantum neuron (quron) [11]. PennyLane provides a state preparation routine for angle encoding [12] for which the axis of the rotation can be specified ($x,y$ or $z$). If no loading routine is provided, a state preparation routine can be constructed with standard qubit rotations in a straightforward manner [5].

- **Amplitude Encoding**

  - Encode data in a compact manner that do not require calculations

  - **Context**

    - A numerical input data vector $[x_0,...,x_{n-1}]^T$ must be encoded for an algorithm.

  - **Solution**

    - Use amplitudes to encode the data. As the squared moduli of the amplitudes of a quantum state must sum up to 1, the input vector needs to be normalized to length 1. This is illustrated in Fig. 5 for a 2-dimensional input vector that contains 2 data points. To associate each amplitude with a component of the input vector, the dimension of the vector must be equal to a power of 2 because the vector space of an $n$ qubit register has dimension $2^n$. If this is not the case, the input vector can be padded with additional zeros to increase the dimension of it. Using a suitable state preparation routine (see Known Uses), the input vector is encoded in the amplitudes of the quantum state as follows: 

      - $$
        \ket{\psi}=\sum^{n-1}_{i=0}x_i\ket{i}
        $$

        

    - As the amplitudes depend on the data, the process of encoding the data (but not the encoding itself) is often referred to as arbitrary state preparation.

      - ![image-20240701201507306](C:\Users\14767\AppData\Roaming\Typora\typora-user-images\image-20240701201507306.png)

  - **Result**

    - A data input vector of length $l$ can be represented by $[log_2(l)]$ qubits - this is indeed a very compact representation. For an arbitrary state represented by $n$ qubits (which represents $2^n$ data values), it is known that at least $\frac{1}{n}2^n$ parallel operations are needed [13]. Current state preparation routines perform slightly better than $2^n$ operations [13]. However, depending on the data it may still be possible to realize an encoding in a logarithmic runtime. For example, an UNIFORM SUPERPOSITION can be created by applying a Hadamard gate to each of the $n$ qubits - which can be done in parallel and thus in a single step. This represents a $2^n$-dimensional vector in which all data entries are $\frac{1}{\sqrt{n}}$. Similarly, sparse data vectors can also be prepared more efficiently [13].
    - It must be noted that if the output is also encoded in the amplitude, multiple measurements must be taken to obtain a good estimate of the output result. The number of measurements scales with the number of amplitudes - as $n$ qubits contains $2^n$ amplitudes, this is costly [13].
    
  - **Related Patterns**

    - This pattern refines INITIALIZATION. The encoding is more compact (in terms of qubits) than BASIS, ANGLE or QRAM ENCODING.

  - **Known Uses**

    - AMPLITUDE ENCODING is required by many quantum machine learning algorithms [8]. Another example is the algorithm of Harrow, Hassidim an Lloyd [14] (often referred to as HHL algorithm) for solving linear equations. The pre-condition that the data values can be normalized is a common assumption in machine learning [15], e.g. in support vector machine.
    - There are various ways to construct a state preparation routine for this encoding. For example, Plesch and Brukner [16] and Iten et al. [17] use the Schmidt Decomposition. For the latter, an implementation in Mathematica was presented [18]. Shende et al. [19] presented an alternative way to construct an arbitrary quantum state which was implemented by Qiskit [20]. PennyLane offers a loading routine for AMPLITUDE ENCODING [12]. The library also includes an arbitrary state preparation routine that uses the algorithm proposed by Mottonen and Vartiainen [21] requires an exponential number of operations to encode $2^n$ data values. Q# provides functionality to compute a state preparation routine that approximates the desired amplitude encoding [22].

- **Quantum Associative Memory (QuAM) Encoding**

  - Represent a collection of data elements in a quantum computer in order to perform calculations

  - **Context**

    - A quantum algorithm requires multiple numerical values X as input for further calculations

  - **Solution**

    - Use a quantum associative memory (QuAM) to prepare a superposition of basis encoded values in the same qubit register [5]. In Fig. 3, this is illustrated for the 3 values $x_1$, $x_2$ and $x_3$ in binary format. Note that the resulting encoding is an equally weighted superposition of the basis encoded values, i.e., all amplitude are of the same magnitude.

      - $$
        \begin{matrix} x_0 \\ x_1 \\ x_2  \end{matrix}
        \begin{bmatrix} 0 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 1 & 1\end{bmatrix}
        \rarr 
        \begin{matrix} \frac{1}{\sqrt{3}} \\ \frac{1}{\sqrt{3}} \\ \frac{1}{\sqrt{3}}  \end{matrix}
        \begin{matrix} |0 & 1 & 0\rangle + \\ |1 & 1 & 0\rangle+ \\ |0 & 1 & 1\rangle \quad \end{matrix}
        $$

      - ![image-20240701190439486](C:\Users\14767\AppData\Roaming\Typora\typora-user-images\image-20240701190439486.png)

        - Fig. 3. Resulting Encoding. Each data value represented by a row on the left is encoded in BASIS ENCODING and an amplitude of $\frac{1}{\sqrt{n}}$

    - To load the data, the register of the quantum associative memory is in superposition of 2 states, a processing and a memory branch. (Fig. 4). Both branches have a load and a storage part. An additional element is first prepared into the load part of both branches (step 1). Next, the processing branch is split in such a manner, that the new element gets a proper amplitude (step 2) such that it can be stored by bringing it into superposition with the already added elements (step 3). Finally, an UNCOMPUTE cleans the both branches to be ready for the next iteration. See [23] for a more detailed description of the individual steps.

      - **![image-20240701191019374](C:\Users\14767\AppData\Roaming\Typora\typora-user-images\image-20240701191019374.png)**
        - Fig. 4. Illustration of the state preparation routine. In each iteration, an element is loaded and brought into superposition with the already stored elements.

  - **Result**

    - The resulting encoding is a digital encoding and therefore suitable for arithmetic computations [5]. For input $n$ numbers that are approximated by $l$ digits, $l$ qubits are needed for this representation. Each of the $n$ encoded input values is represented by a basis vector with an amplitude of $\frac{1}{\sqrt{n}}$. All other $2^l-n$ amplitudes of the register are zero - in our example, $\ket{000}$, $\ket{001}$, $\ket{100}$, $\ket{101}$, and $\ket{111}$. The amplitude vector is therefore often sparse for this encoding [13].

  - **Related Pattern**

    - This pattern refines INITIALIZATION and makes use of UNCOMPUTE. UNIFORM SUPERPOSITION creates a superposition of all computational basis states. Each of the computational basis states also represents a value in BASIS ENCODING.

  - **Known Uses**

    - The presented state preparation routine based on [23] can be used whenever multiple data values need to be represented in BASIS ENCODING. Shor's algorithm [24] for the factorization of prime numbers, a quantum version of the Fourier transform [25], and Grover's algorithm [26] for unstructured search rely on this encoding. Various algorithms extend or use Grover's algorithm and therefore also make use of this encoding.  

- **QRAM Encoding**

  - Use a quantum random access memory to access a superposition of data values at once.

  - **Context**

    - An algorithm requires random access to the data values of the input

  - **Solution**

    - A classical RAM that receives an address with a memory index, loads the data stored at this address into an output register. QRAM provides the same functionality, but the address and output register are quantum registers [27]. As a result, both the address and the output register can be in a superposition of multiple values. Fig. 5 illustrates the basic functionality of a QRAM [28] that receives a superposition of the first two addresses ($\frac{1}{\sqrt{2}}\ket{00}+\frac{1}{\sqrt{2}}\ket{01}$) as input and loads the corresponding data values into an empty output register. This leads to the following state of the overall quantum system:

      - $$
        \ket{\psi} = \frac{1}{\sqrt{2}}\ket{00}\ket{010}+\frac{1}{\sqrt{2}}\ket{01}\ket{110}
        $$

    - In general, loading $m$ of $n$ data values with a QRAM can therefore be described as the following operation [13]:

      - $$
        \frac{1}{\sqrt{m}}\sum^{m-1}_{i=0}\ket{a}_i\ket{0} \quad \underrightarrow{QRAM} \quad \frac{1}{\sqrt{m}}\sum^{m-1}_{i=0}\ket{a}_i\ket{x_a}
        $$

    - where the first register is the address register that is in  superposition of all $m$ address to be loaded and the second register is the output register. Further, $\ket{a}_i$ specifies the address of the i-th data value to be loaded and $x_a$ is the data value associated with this address. The QRAM loads each data value $\ket{x_a}$ into the output register such that $\ket{a}_i\ket{x_a}$ is contained in the combined state of both registers. Depending on the data values, this state may be entangled.

      - ![image-20240706014357927](C:\Users\14767\AppData\Roaming\Typora\typora-user-images\image-20240706014357927.png)

  - **Result**

    - For this encoding, $l$ qubits are needed to encode the data values using BASIS ENCODING. The address register requires $[log(n)]$ additional qubits for a maximum of $n$ addresses. The computational properties are similar to those of BASIS and QUAM ENCODING: As a superposition of the encoded data values is prepared, data can be processed in parallel (quantum parallelism) and arithmetic operations such as addition or multiplication can be used.
    - An algorithm that uses QRAM, assumes that an efficient procedure exists that can be used to perform state preparation in logarithmic runtime [13]. As long as there are no hardware implementations of QRAM, a state preparation routine must be used that mirrors the loading process of a QRAM. The main drawback of QRAM encoding is that in general, no state preparation routine for arbitrary input data exists that is as efficient as a QRAM. A promised speed-up of an algorithm that relies on QRAM can only be realized if data can be encoded efficiently by a known state preparation routine.

  - **Related Pattern**

    - This pattern further refines INITIALIZATION and uses BASIS ENCODING. As the address and output register of QRAM ENCODING are often entangled, CREATING ENTANGLEMENT [31] is used.

  - **Known Uses**

    - An algorithm for state preparation is given by circuit family #3 of [7]. An alternative approach is presented in [30]. This encoding is used by algorithms for solving semi-definite programs [31]. Various other algorithms exist that require or are improved upon QRAM. The so-called HHL algorithm for solving linear equations [14] uses QRAM ENCODING to represent eigenvalues in an intermediate step [31].

- **Basic QROM**

- **Angle QROM**

- **Improved Angle QROM**


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

[5] Leymann F, Barzen J. The bitter truth about gate-based quantum algorithms in the NISQ era[J]. Quantum Science and Technology, 2020, 5(4): 044007.

[6] Vedral V, Barenco A, Ekert A. Quantum networks for elementary arithmetic operations[J]. Physical Review A, 1996, 54(1): 147.

[7] Cortese J A, Braje T M. Loading classical data into a quantum computer[J]. arXiv preprint arXiv:1803.01958, 2018.

[8] LaRose R, Coyle B. Robust data encodings for quantum classifiers[J]. Physical Review A, 2020, 102(3): 032420.

[9] Grant E, Benedetti M, Cao S, et al. Hierarchical quantum classifiers[J]. npj Quantum Information, 2018, 4(1): 65.

[10] Yan F, Iliyasu A M, Venegas-Andraca S E. A survey of quantum image representations[J]. Quantum Information Processing, 2016, 15: 1-35.

[11] Schuld M, Sinayskiy I, Petruccione F. The quest for a quantum neural network[J]. Quantum Information Processing, 2014, 13: 2567-2586.

[12] “Templates,” https://pennylane.readthedocs.io/en/stable/introduction/templates.html, 2020.

[13] Schuld M, Petruccione F. Supervised learning with quantum computers[M]. Berlin: Springer, 2018.

[14] Harrow A W, Hassidim A, Lloyd S. Quantum algorithm for linear systems of equations[J]. Physical review letters, 2009, 103(15): 150502.

[15] Duarte D, Ståhl N. Machine learning: a concise overview[J]. Data Science in Practice, 2019: 27-58. 

[16] Plesch M, Brukner Č. Quantum-state preparation with universal gate decompositions[J]. Physical Review A—Atomic, Molecular, and Optical Physics, 2011, 83(3): 032302.

[17] Iten R, Colbeck R, Kukuljan I, et al. Quantum circuits for isometries[J]. Physical Review A, 2016, 93(3): 032318.

[18] Iten R, Reardon-Smith O, Malvetti E, et al. Introduction to universalqcompiler[J]. arXiv preprint arXiv:1904.01072, 2019.

[19] Shende V V, Bullock S S, Markov I L. Synthesis of quantum logic circuits[C]//Proceedings of the 2005 Asia and South Pacific Design Automation Conference. 2005: 272-275.

[20] Summary of Quantum Operations. https://qiskit.org/documentation/tutorials/circuits/3_summary_of_quantum_operations.html. (2020).

[21] Möttönen¹ M, Vartiainen J J. Decompositions of general quantum gates[J]. Trends in quantum computing research, 2006: 149.

[22] Q# API reference. https://docs.microsoft.com/en-us/qsharp/api/. (2020)

[23] Ventura D, Martinez T. Quantum associative memory[J]. Information sciences, 2000, 124(1-4): 273-296.

[24] Shor P W. Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer[J]. SIAM review, 1999, 41(2): 303-332.v

[25] Coppersmith D. An approximate Fourier transform useful in quantum factoring[J]. arXiv preprint quant-ph/0201067, 2002.

[26] Grover L K. A fast quantum mechanical algorithm for database search[C]//Proceedings of the twenty-eighth annual ACM symposium on Theory of computing. 1996: 212-219.

[27] Johnston E R, Harrigan N, Gimeno-Segovia M. Programming quantum computers: essential algorithms and code samples[M]. O'Reilly Media, 2019.

[28] Giovannetti V, Lloyd S, Maccone L. Quantum random access memory[J]. Physical review letters, 2008, 100(16): 160501.

[29] Leymann F. Towards a pattern language for quantum algorithms[C]//Quantum Technology and Optimization Problems: First International Workshop, QTOP 2019, Munich, Germany, March 18, 2019, Proceedings 1. Springer International Publishing, 2019: 218-230.

[30] Prakash A. Quantum algorithms for linear algebra and machine learning[M]. University of California, Berkeley, 2014.

[31] Mitarai K, Kitagawa M, Fujii K. Quantum analog-digital conversion[J]. Physical Review A, 2019, 99(1): 012301.

