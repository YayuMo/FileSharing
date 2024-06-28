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

- Basic Info (from source paper)

  - | Encoding Patern         | Encoding                                                     | Req. qubits      |
    | ----------------------- | ------------------------------------------------------------ | ---------------- |
    | Basis Encoding [1]      | $x=(b_{m-1},b_{m-2},...,b_0),x \in \mathbb{Z}_2^m,b_j \in \mathbb{Z}_2 \rarr \ket{x}=\ket{b_{m-1}b_{m-2}...b_0}$ | l = m            |
    | Angle Encoding          | $x\in [0,2\pi) \rarr \otimes_{j=0}^{(N-2)/2}cos(x_{2j+1})\ket{0}+e^{ix_{2j}}sin(x_{2j+1})\ket{1}$(Dense Encoding?) [1]<br />$x \rarr \otimes_{j=0}^{N-1}cos(x_j)\ket{0}+sin(x_j)\ket{1}$(General Encoding?)[2] | 1 per data point |
    | Amplitude Encoding [2]  | $x \rarr \sum_{i=0}^{n-1}x_i\ket{i}$, where $\sum|x_i|^2=1$  | l = log(n)       |
    | Basic QROM [1]          | $\{\vec{a},\vec{x}\},a_j  \in \mathbb{Z}^n_2, x_j \in \mathbb{Z}^m_2\rarr \ket{\psi_x}=\sum^{n-1}_{j=0}\ket{a_j}\ket{x_j}$ |                  |
    | Angle QROM [1]          | $\{\vec{a},\vec{x}\},a_j  \in \mathbb{Z}^n_2, x_j \in [0,2\pi) \rarr \sum^{(n-2)/2}_{j=0}\ket{a_j}(cos(x_{2j+1})\ket{0}+e^{ix_{2j}}sin(x_{2j+1})\ket{1})$ |                  |
    | Improved Angle QROM [1] | $\{\vec{a},\vec{x}\},a_j  \in \mathbb{Z}^n_2, S_j \in [0,2\pi), E_j \in [0,2\pi) \rarr \sum^{N-1}_{j=0}\ket{a_j}(cos(S_j)\ket{0}+e^{iE_j}sin(S_j)\ket{1})$ |                  |
    | QUAM Encoding [2]       | $\sum^{n-1}_{i=0}\frac{1}{\sqrt{n}}\ket{x_i},x_i \in \mathbb{Z}^m_2$ | l                |
    | QRAM Encoding [2]       | $\sum^{n-1}_{j=0}\frac{1}{\sqrt{n}}\ket{a_j}\ket{x_j},a_j  \in \mathbb{Z}^n_2, x_j \in \mathbb{Z}^m_2$ | log(n) + l       |

- Basic Encoding

- Angle Encoding

- Amplitude Encoding

- Basic QROM

- Angle QROM

- Improved Angle QROM

- QUAM Encoding

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

[2] Weigold M, Barzen J, Leymann F, et al. Encoding patterns for quantum algorithms[J]. IET Quantum Communication, 2021, 2(4): 141-152.