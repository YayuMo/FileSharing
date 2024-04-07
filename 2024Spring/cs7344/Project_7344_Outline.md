# Project_7344_Outline

Traditional Network Structure with quantum protocols

## Subject (5 Questions)

- What type of network ?
  - Network based on several quantum protocols
- Purpose of your network
  - To apply the basic principle of quantum mechanism in traditional network structure
  - To utilize the benefits of entanglement
  - To build a highly secure network
- Physical layer
  - Entanglement Generator

- Datalink protocol? Why?
  - Swapping Protocol

- Any modification? Why?
- Software
  - For experiments 
    - Python
    - Qiskit
  - For network structure
    - Cisco Packet Tracer
  - For paper
    - Overleaf


## Paper Collection

- Designing a Quantum Network Protocol
  - Kozlowski et al. [1]
- One Layer Demonstration of Quantum Internet on the IBM Q System
  - Medhi et al. [2]

## Background

In this section, brief information about basic quantum notations, quantum gates, Bell States.

- Quantum Notations

  - Quantum Computation usually apply linear algebra as its computational logic.

  - The mathematical form of quantum computation is usually written in Dirac Notations. $|·\rangle$. In most circumstances, to represent the quantum state unit of a single qubit, the computational basis is introduced. The most general basis is $\{|0\rangle,|1\rangle\}$, which in explicit form are

  - $$
    |0\rangle =\left[\begin{matrix}
    	1 \\
    	0
    \end{matrix}\right],
    |1\rangle = \left[\begin{matrix}
            0 \\
            1
    \end{matrix}\right]
    $$

  - The single qubit could also be the combination of computational basis with the probability amplitude $\alpha$ and $\beta$, which is denoted as 

  - $$
    |\psi\rangle=\alpha|0\rangle+\beta|1\rangle
    $$

  - also could be written as the state vector

  - $$
    |\psi\rangle = \left[\begin{matrix}
            \alpha \\
            \beta
    \end{matrix}\right]
    $$

- Quantum Gates

  - The quantum circuits are usually the combination of several quantum gates and measurements. The basic quantum gates included in the model are introduced in the following:
  - ![image-20240405214212588](C:\Users\14767\AppData\Roaming\Typora\typora-user-images\image-20240405214212588.png)
  - Hadamard Gate and Controlled X(Not) gate
  - ![image-20240405214401396](C:\Users\14767\AppData\Roaming\Typora\typora-user-images\image-20240405214401396.png)

- Bell State

  - Also called EPR pairs, which is the most simple example of quantum entanglement state, and the Dirac form could be represented as followings

    - $$
      |\Phi^+\rangle = \frac{|00\rangle+|11\rangle}{\sqrt{2}} \\
      |\Phi^-\rangle = \frac{|00\rangle-|11\rangle}{\sqrt{2}} \\
      |\Psi^+\rangle = \frac{|01\rangle+|10\rangle}{\sqrt{2}} \\
      |\Psi^-\rangle = \frac{|01\rangle-|10\rangle}{\sqrt{2}} \\
      $$

    - 

  - Bell State could be be generated through the circuit diagram below

    - ![image-20240406123157151](C:\Users\14767\AppData\Roaming\Typora\typora-user-images\image-20240406123157151.png)

  - Bell State measurement

    - The bell state measurement are used for collapse the bell state to basic state $\{|0\rangle,|1\rangle\}$
    - ![image-20240406173903851](C:\Users\14767\AppData\Roaming\Typora\typora-user-images\image-20240406173903851.png)

- Quantum Repeaters

  - The basic thought of Quantum Repeater is to build the entanglements in 2 pairs and then apply a bell state measurements between the 2 pairs

## Brief Introduction about our method

- Swapping Protocol applied as transportation protocol in data link layer
  - We are focusing on the Fig. 1 and Fig. 3 in article[2], and also found some regular pattern.
  - Regular Pattern
    - The difference between circuit constructed by even numbers and odd numbers are the requirements of Controlled-Z gate. For even numbers, Controlled-Z gate could be ignored, and for odd numbers, the Controlled-Z couldn't be ignored.
      - The 8-qubit repeater diagram are as followings:
        - ![image-20240404161742860](C:\Users\14767\AppData\Roaming\Typora\typora-user-images\image-20240404161742860.png)

      - The 3-qubit repeater diagram are as followings:
        - ![image-20240406183434523](C:\Users\14767\AppData\Roaming\Typora\typora-user-images\image-20240406183434523.png)

    - The number of repeaters during the route has a specific regulation
      - For even number qubit, the number of repeaters must be n*4m, where n is the even number of qubits(n=4,6,8,10...), and m=1,2,3,4...
      - For odd number qubit, the number of repeaters must be n*2m, where n is the odd number of qubits(n=3,5,7,9...), and m=1,2,3,4...

  - Security teleportation
    - According to the regulation above, suppose Alice is transmitting information to Bob through 8-qubit pattern, which requires at least 32 repeaters. And after swapping for 32 repeaters, the information Bob receives would be the same as the Alice send.
    - In our hypothesis, if we measure the quantum state during the middle transfer nodes (for example, after 15 repeaters), it would randomly collapse to the distribution of different basic state stream, which would significantly improve the security during transmission.
    - ![image-20240407153734735](C:\Users\14767\AppData\Roaming\Typora\typora-user-images\image-20240407153734735.png)
    
  - Advantage
    - Could be worked as large distance teleportation (such as WAN).
    - High Security during the transfer nodes.
  
- Encoding Packet Generating Method
  - BB84 Encryption Protocol (We are still working on it)


## Preliminary Experiments

- Regular Pattern experiments

  - According to the diagram, we did experiments on 3-qubits and 8-qubits.
  - We can tell from the experiment result that the the effectiveness of even and odd number qubits pattern has been verified.
  - The experiment result of 8-qubits is:
    - ![image-20240404161903564](C:\Users\14767\AppData\Roaming\Typora\typora-user-images\image-20240404161903564.png)

  - The experiment result of 3-qubits is:
    - ![image-20240406180044010](C:\Users\14767\AppData\Roaming\Typora\typora-user-images\image-20240406180044010.png)

- The  security teleportation experiment result (4-qubits):

  - In the experiments of security teleportation, we set varied numbers of repeaters to work as the measurements in different middle nodes to verify the effectiveness of security teleportation.

  - <div><table frame=void>
    	<tr>
            <td>
                <div>
                <center>
            	<img src="C:\Users\14767\PycharmProjects\FileSharing\2024Spring\cs7344\image\02.png"
                     alt="2Repeaters"
                     height="120"/>
            	<br>
            	2 Repeaters
            	</center>
                </div></td>    
         	<td><div><center>
        		<img src="C:\Users\14767\PycharmProjects\FileSharing\2024Spring\cs7344\image\04.png"
                     alt="4Repeaters"
                     height="120"/>
        		<br>
        		4 Repeaters
            </center></div></td>
            <td><div><center>
        		<img src="C:\Users\14767\PycharmProjects\FileSharing\2024Spring\cs7344\image\06.png"
                     alt="6Repeaters"
                     height="120"/>
        		<br>
        		6 Repeaters
            </center></div></td>
            <td><div><center>
        		<img src="C:\Users\14767\PycharmProjects\FileSharing\2024Spring\cs7344\image\08.png"
                     alt="8Repeaters"
                     height="120"/>
        		<br>
        		8 Repeaters
            </center></div></td>
    	</tr>	
    	<tr>
            <td>
                <div>
                <center>
            	<img src="C:\Users\14767\PycharmProjects\FileSharing\2024Spring\cs7344\image\10.png"
                     alt="10Repeaters"
                     height="120"/>
            	<br>
            	10 Repeaters
            	</center>
                </div></td>    
         	<td><div><center>
        		<img src="C:\Users\14767\PycharmProjects\FileSharing\2024Spring\cs7344\image\12.png"
                     alt="12Repeaters"
                     height="120"/>
        		<br>
        		12 Repeaters
            </center></div></td>
            <td><div><center>
        		<img src="C:\Users\14767\PycharmProjects\FileSharing\2024Spring\cs7344\image\14.png"
                     alt="14Repeaters"
                     height="120"/>
        		<br>
        		14 Repeaters
            </center></div></td>
            <td><div><center>
        		<img src="C:\Users\14767\PycharmProjects\FileSharing\2024Spring\cs7344\image\16.png"
                     alt="16Repeaters"
                     height="120"/>
        		<br>
        		16 Repeaters
            </center></div></td>
    	</tr>
        	<tr>
            <td>
                <div>
                <center>
            	<img src="C:\Users\14767\PycharmProjects\FileSharing\2024Spring\cs7344\image\18.png"
                     alt="18Repeaters"
                     height="120"/>
            	<br>
            	18 Repeaters
            	</center>
                </div></td>    
         	<td><div><center>
        		<img src="C:\Users\14767\PycharmProjects\FileSharing\2024Spring\cs7344\image\20.png"
                     alt="20Repeaters"
                     height="120"/>
        		<br>
        		20 Repeaters
            </center></div></td>
            <td><div><center>
        		<img src="C:\Users\14767\PycharmProjects\FileSharing\2024Spring\cs7344\image\22.png"
                     alt="22Repeaters"
                     height="120"/>
        		<br>
        		22 Repeaters
            </center></div></td>
            <td><div><center>
        		<img src="C:\Users\14767\PycharmProjects\FileSharing\2024Spring\cs7344\image\24.png"
                     alt="24Repeaters"
                     height="120"/>
        		<br>
        		24 Repeaters
            </center></div></td>
    	</tr>
        	<tr>
            <td>
                <div>
                <center>
            	<img src="C:\Users\14767\PycharmProjects\FileSharing\2024Spring\cs7344\image\26.png"
                     alt="26Repeaters"
                     height="120"/>
            	<br>
            	26 Repeaters
            	</center>
                </div></td>    
         	<td><div><center>
        		<img src="C:\Users\14767\PycharmProjects\FileSharing\2024Spring\cs7344\image\28.png"
                     alt="28Repeaters"
                     height="120"/>
        		<br>
        		28 Repeaters
            </center></div></td>
            <td><div><center>
        		<img src="C:\Users\14767\PycharmProjects\FileSharing\2024Spring\cs7344\image\30.png"
                     alt="30Repeaters"
                     height="120"/>
        		<br>
        		30 Repeaters
            </center></div></td>
            <td><div><center>
        		<img src="C:\Users\14767\PycharmProjects\FileSharing\2024Spring\cs7344\image\32.png"
                     alt="32Repeaters"
                     height="120"/>
        		<br>
        		32 Repeaters
            </center></div></td>
    	</tr>
    </table></div>

  - In the histograms above, we can tell the 16 and 32 repeaters could transmit the correct qubit stream, and other numbers would collapse to random distribution by measurements.


## Team work

- Haojing Zhai (hzhai@mail.smu.edu)
  - Writing most part of paper
- Yayu Mo (yayum@mail.smu.edu)
  - Algorithm
  - Experiment

- Liping Tang (lipingt@mail.smu.edu)
  - Literature collection and indexing
  - Related works


## Our next work

- doing further study on the Controlled-Z, trying to figure out in what circumstances would the Controlled-Z work.
- trying to add some promotion in the protocol.
- focusing on the packeting process, add some encryption method (such as BB84 protocol) in the packet generations.

## Reference

[1] Kozlowski W, Dahlberg A, Wehner S. Designing a quantum network protocol[C]//Proceedings of the 16th international conference on emerging networking experiments and technologies. 2020: 1-16.

[2] Medhi V N, Deka V N, Behera B K, et al. One Layer Demonstration of Quantum Internet on the IBM Q System[J].