# Thesis

## Topic: Quantum Oracle Synthesis on varied basis

## Stage 1

### Background

- Using the varied basis for Oracle Synthesis
- Oracle synthesis should be considered as the combination of Encoded Basis (e.g. Angle encoding--$\otimes^{(N-2)/2}*{j=0}cos(x*{2j+1})\ket{0}+e^{ix2j}sin(x_{2j+1})\ket{1}$) and General Basis (e.g. Orthogonal Z-basis {$\ket{0},\ket{1}$}, Orthogonal X-basis {$\ket{+},\ket{-}$} ), also shown as the figure follows
  - ![](C:\Users\14767\AppData\Roaming\Typora\typora-user-images\image-20240506161928267.png)

### Problem Description

- One big problem with topic 1 is that Grover's algorithm depends on the use of entanglement in the diffusion filter (as well as quantum superposition). It is not clear how entanglement can be accomplished with amplitude (or angle) encoded. A new method for performing inversion about the mean would need to be created if angle- or amplitude-encoding is used for the oracle.

### Basis Tutorial

- Basic Info

  - | Encoding Patern     | Encoding                                                     | Req. qubits |
    | ------------------- | ------------------------------------------------------------ | ----------- |
    | Basic QROM          | $\sum^{n-1}_{j=0}\ket{a_j}\ket{x_j},a_j  \in \mathbb{Z}^n_2, x_j \in \mathbb{Z}^m_2$ |             |
    | Angle QROM          | $\sum^{(n-2)/2}_{j=0}\ket{a_j}(cos(x_{2j+1})\ket{0}+e^{ix_{2j}}sin(x_{2j+1})\ket{1}),a_j  \in \mathbb{Z}^n_2, x_j \in \mathbb{Z}^m_2$ |             |
    | Improved Angle QROM | $\sum^{(n-2)/2}_{j=0}\ket{a_j}(cos(S_j)\ket{0}+e^{iE_j}sin(S_j)\ket{1}),a_j  \in \mathbb{Z}^n_2, S_j \in [0,2\pi), E_j \in [0,2\pi)$ |             |
    | QUAM Encoding       | $\sum^{n-1}_{j=0}\frac{1}{\sqrt{n}}\ket{x_j},x_j \in \mathbb{Z}^m_2$ |             |
    | QRAM Encoding       | $\sum^{n-1}_{j=0}\frac{1}{\sqrt{n}}\ket{a_j}\ket{x_j},a_j  \in \mathbb{Z}^n_2, x_j \in \mathbb{Z}^m_2$ |             |
    | Amplitude Encoding  | $\sum^{n-1}_{j=0}x_j\ket{a_j},a_j  \in \mathbb{Z}^n_2,x_j \in \mathbb{Z}^m_2$ |             |

- Basic QROM

### Testing method

- Grover's Algorithm
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