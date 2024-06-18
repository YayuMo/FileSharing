# Thesis Topics Proposal

## 1. Quantum Oracle Synthesis on varied bases

- Basic Backgrounds

  - Using the varied basis for a More General Oracle Synthesis (Not only for QROM)

  - Oracle synthesis should be considered as the combination of Encoded Basis (e.g. Angle encoding--$\otimes^{(N-2)/2}_{j=0}cos(x_{2j+1})\ket{0}+e^{ix2j}sin(x_{2j+1})\ket{1}$) and General Basis (e.g. Orthogonal Z-basis {$\ket{0},\ket{1}$}, Orthogonal X-basis {$\ket{+},\ket{-}$} ), also shown as the figure follows

    - ![image-20240506161928267](C:\Users\14767\AppData\Roaming\Typora\typora-user-images\image-20240506161928267.png)

  - Focus on Improved Angle Encoding basis [1] or more complicated basis[2], possible basis are shown in the following table

    - | Encoding Patern     | Encoding                                                     |
      | ------------------- | ------------------------------------------------------------ |
      | Basic QROM          | $\sum^{n-1}_{j=0}\ket{a_j}\ket{x_j},a_j  \in \mathbb{Z}^n_2, x_j \in \mathbb{Z}^m_2$ |
      | Angle QROM          | $\sum^{(n-2)/2}_{j=0}\ket{a_j}(cos(x_{2j+1})\ket{0}+e^{ix_{2j}}sin(x_{2j+1})\ket{1}),a_j  \in \mathbb{Z}^n_2, x_j \in \mathbb{Z}^m_2$ |
      | Improved Angle QROM | $\sum^{(n-2)/2}_{j=0}\ket{a_j}(cos(S_j)\ket{0}+e^{iE_j}sin(S_j)\ket{1}),a_j  \in \mathbb{Z}^n_2, S_j \in [0,2\pi), E_j \in [0,2\pi)$ |
      | QUAM Encoding       | $\sum^{n-1}_{j=0}\frac{1}{\sqrt{n}}\ket{x_j},x_j \in \mathbb{Z}^m_2$ |
      | QRAM Encoding       | $\sum^{n-1}_{j=0}\frac{1}{\sqrt{n}}\ket{a_j}\ket{x_j},a_j  \in \mathbb{Z}^n_2, x_j \in \mathbb{Z}^m_2$ |
      | Amplitude Encoding  | $\sum^{n-1}_{j=0}x_j\ket{a_j},a_j  \in \mathbb{Z}^n_2,x_j \in \mathbb{Z}^m_2$ |

    - I didn't look at too many encoding bases, but there are more bases in different areas, like quantum images. 

- Challenges

  - Extent the QROM synthesis to more general ones.
  - The method should synthesize the QC to combinations of Pauli-X gates, Controlled-X gates, or Toffoli gates (ESOP[3] for Basic-QROM), as well as Controlled Rotation gates or general rotation gates (rotation-based synthesis [4] for Angle-QROM).
  - One big problem with topic 1 is that Grover's algorithm depends on the use of entanglement in the diffusion filter (as well as quantum superposition). It is not clear how entanglement can be accomplished with amplitude (or angle) encoded. A new method for performing inversion about the mean would need to be created if angle- or amplitude-encoding is used for the oracle.

- References

  - [1] Sinha A, Henderson E R, Henderson J M, et al. Automated quantum memory compilation with improved dynamic range[C]//2022 IEEE/ACM Third International Workshop on Quantum Computing Software (QCS). IEEE, 2022: 22-35.
  - [2] Weigold M, Barzen J, Leymann F, et al. Encoding patterns for quantum algorithms[J]. IET Quantum Communication, 2021, 2(4): 141-152.
  - [3] Fazel K, Thornton M A, Rice J E. ESOP-based Toffoli gate cascade generation[C]//2007 IEEE Pacific Rim Conference on Communications, Computers and Signal Processing. IEEE, 2007: 206-209.
  - [4] Abdollahi A, Saeedi M, Pedram M. Reversible logic synthesis by quantum rotation gates[J]. arXiv preprint arXiv:1302.5382, 2013.

## 2. Quantum Image Representation on varied bases

- Basic Backgrounds

  - Several bases are applied to represent different color spaces, shown as table below.

  - | Image representation | Quantum State                                                | Basis                 |
    | -------------------- | ------------------------------------------------------------ | --------------------- |
    | FRQI [1]             | $\ket{f}=\frac{1}{2^m}\sum^{2^{2m}-1}_{k=0}(cos\theta_k\ket{0}+sin\theta_k\ket{1})\ket{k}$ | Angle                 |
    | NEQR [1]             | $\ket{f}=\frac{1}{2^m}\sum^{2^{2m}-1}_{k=0}\ket{f(k)}\ket{k}$ | basis of qubits       |
    | OPIE [1]             | $\ket{f}=\sum^{2^{2m}-1}_{k=0}c_k\ket{k}$                    | probability amplitude |
    | FTQR [2]             | $f_{n,m} \rightarrow T[f_{n,m}]=e^{i\alpha f_{n,m}},\\ \ket{\hat{f}}=\frac{1}{\sqrt{NM}}\sum^{M-1}_{m=0}\sum^{N-1}_{n=0}T[r_{n,m}\ket{n,m}]$ |                       |
    |                      |                                                              |                       |

  - Other Basis could be applied to image representation, such as the QROM or QRAM basis series mentioned in the last topic.

  - Several compression and encryption methods could be applied to quantum image representations using varied bases.

  - The image processing techniques also significantly affect image representations, specifically the impact of ML approach combined with image representations[3]. 

- Challenges

  - The biggest challenge could be representing images in varied color spaces such as RGB, HSV, YCbCr.
  - Due to the limitation of 2 basis state qubit ($\ket{\psi}=\alpha\ket{0}+\beta\ket{1}$), the number of pixels has to follow the rule of $N\times M=2^i$. As a consequence, the compression of images has to be specified, and the original size also should be recorded in the circuits. In addition, higher dimensional superposition qudits could also been introduced to image representation.

- References 

  - [1] Yao X W, Wang H, Liao Z, et al. Quantum image processing and its application to edge detection: Theory and experiment[J]. Physical Review X, 2017, 7(3): 031041.
  - [2] Grigoryan A M, Agaian S S. New look on quantum representation of images: Fourier transform representation[J]. Quantum Information Processing, 2020, 19(5): 148.
  - [3] Lisnichenko M, Protasov S. Quantum image representation: A review[J]. Quantum Machine Intelligence, 2023, 5(1): 2.

## 3. Quantum Image Segmentation + Reinforcement Learning

- Basic Backgrounds

  - Multi-Agent Reinforcement Learning (MARL) model in 2-D image segmentation, inspired by 3-D image model[1].

    - ![image-20240507004834351](C:\Users\14767\AppData\Roaming\Typora\typora-user-images\image-20240507004834351.png)

  - MARL in quantum [2]

    Constructed by several units below

    - State Encoder ($U_{enc}$)
      - ![image-20240507012724051](C:\Users\14767\AppData\Roaming\Typora\typora-user-images\image-20240507012724051.png)
    - Parametrized Circuit ($U_{var}$)
      - ![image-20240507021418062](C:\Users\14767\AppData\Roaming\Typora\typora-user-images\image-20240507021418062.png)
    - Variational Quantum Circuit (VQC) for Actor
      - ![image-20240507014005190](C:\Users\14767\AppData\Roaming\Typora\typora-user-images\image-20240507014005190.png)
    - VQC for Centralized Critic
      - ![image-20240507014137678](C:\Users\14767\AppData\Roaming\Typora\typora-user-images\image-20240507014137678.png)
    - Structure of QMARL framework
      - ![image-20240507014915121](C:\Users\14767\AppData\Roaming\Typora\typora-user-images\image-20240507014915121.png)

- Challenges

  - Specify the QMARL framework for the MARL 2-D image segmentation model.
  - Or combine other RL models with Quantum and apply them to the specific Image Segmentation field.
  - Optimization of the algorithm.
  - Performance compared with traditional (without quantum) and other quantum image segmentation (such as QCNN based).

- Acknowledgement

  - Inspired by MARL 3D medical image segmentation[1] and  quantum MARL[2]
  - It's a challenging topic, but since I've done a lot of work on Target Detection and Target Segmentation based on CNN, some basic ML algorithms and even single-agent MDP, this topic really fascinates me a lot.

- References
  - [1] Liao X, Li W, Xu Q, et al. Iteratively-refined interactive 3D medical image segmentation with multi-agent reinforcement learning[C]//Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2020: 9394-9402.
  - [2] Yun W J, Kwak Y, Kim J P, et al. Quantum multi-agent reinforcement learning via variational quantum circuit design[C]//2022 IEEE 42nd International Conference on Distributed Computing Systems (ICDCS). IEEE, 2022: 1332-1335.

## 4. Quantum Routing Protocol

- Basic Backgrounds
  - Entanglement Swapping Protocol has been applied to built quantum repeaters for teleportation in a long distance, but most of them are focusing on point to point teleportation (eg. 0-30, shown as diagram below). However, if we have to utilize multicast or broadcast, a routing strategy has to be taken into consideration.
    - ![70e7bb04f855fcc166a4c99a5dc094b](C:\Users\14767\OneDrive\Documents\WeChat Files\wxid_8qe5ss6t6g6j12\FileStorage\Temp\70e7bb04f855fcc166a4c99a5dc094b.png)
  - For the repeater circuits[2] that doesn't contain other Toffoli-gate or Pauli-Z gate, shown as the figure below (8 qubit repeater), it must follow specific numbers of repeaters to transfer exact the same qubit stream.
  - ![image-20240506213830794](C:\Users\14767\AppData\Roaming\Typora\typora-user-images\image-20240506213830794.png)
  - The figure below shows that if we measure at the middle node repeater, it will collapse to random distributions (also shown as the 3rd diagrams).
  - ![image-20240506211759812](C:\Users\14767\AppData\Roaming\Typora\typora-user-images\image-20240506211759812.png)
  - ![image-20240506214748658](C:\Users\14767\AppData\Roaming\Typora\typora-user-images\image-20240506214748658.png)
- Challenges
  - One or more qubits have to be added to the repeater to build a qTCP/IP-like protocol.
  - To define the IP for different quantum repeater (or router) nodes.
  - Build the protocol effectively and securely.
- Acknowledgment
  - I got inspiration from ECE/CS 8381 Homework #4 and experimented with different numbers of qubits in the repeaters.
- References
  - [1] Mastriani M. Simplified entanglement swapping protocol for the quantum Internet[J]. Scientific Reports, 2023, 13(1): 21998.
  - [2] Medhi V N, Deka V N, Behera B K, et al. One Layer Demonstration of Quantum Internet on the IBM Q System[J].





## Topic selection (For 2024.6.13 meeting)

