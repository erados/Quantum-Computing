# Quantum-Computing
My study of QC with cirq.

# Two Qubits Teleportation
![2-큐빗 순간이동 실행결과](https://github.com/erados/Quantum-Computing/blob/main/two_qubits_teleportation.png)
1-큐빗 순간이동을 채널만 늘린 것이다. 1-큐빗 순간이동은 EPR 쌍을 공유하고 메시지와 엘리스의 큐비트를 벨 측정(CNOT-H)하여 이루어진다.

# Deutsch's Algorithm
![도이치 알고리즘 회로](https://github.com/erados/Quantum-Computing/blob/main/Deutsch%20algorithm%20circuit.svg)
![도이치 알고리즘 결과 분포](https://github.com/erados/Quantum-Computing/blob/main/Deutsch%20algorithm%20distribution.svg)

도이치 알고리즘은 ![](https://latex.codecogs.com/svg.latex?f:{0,1}\rightarrow{0,1})가 상수 함수인지 균형 함수(출력이 0과 1일 경우의 수가 같음)인지 판단하는 알고리즘이다.

고전 컴퓨팅으로는 2회의 쿼리를 보내야하지만 양자 컴퓨팅으로는 1회의 쿼리만 보내면 된다.

상수 함수의 유니타리 행렬을 ![](https://latex.codecogs.com/svg.latex?U_f%20|x>|->%20=%20(-1)^{f(X)}|x>|->) 로 설정하면

![](https://latex.codecogs.com/svg.latex?Q_1) 에 대해 ![](https://latex.codecogs.com/svg.latex?I,%20-I,%20Z,%20-Z)(상수/상수/균형/균형),

![](https://latex.codecogs.com/svg.latex?Q_0) 에 대해 ![](https://latex.codecogs.com/svg.latex?I,%20X,%20CNOT(Q_1,%20Q_0),%20CNOT(Q_1,%20Q_0)&X) 를 수행하게된다.

따라서 ![](https://latex.codecogs.com/svg.latex?Q_1) 의 양쪽에 ![](https://latex.codecogs.com/svg.latex?H)를 추가하면 

![](https://latex.codecogs.com/svg.latex?Q_1) 에 대해 ![](https://latex.codecogs.com/svg.latex?I,%20-I,%20X,%20-X) 가 되어 

상수함수는 입력이 그대로 나오고 균형함수는 입력이 반전되어 나오게 된다.
