# Quantum-Computing
My study of QC with cirq.

# Two Qubits Teleportation
![2-큐빗 순간이동 실행결과](https://github.com/erados/Quantum-Computing/blob/main/two_qubits_teleportation.png)
1-큐빗 순간이동을 채널만 늘린 것이다. 1-큐빗 순간이동은 EPR 쌍을 공유하고 메시지와 엘리스의 큐비트를 벨 측정(CNOT-H)하여 이루어진다.

# Deutsch's Algorithm
![도이치 알고리즘 회로](https://github.com/erados/Quantum-Computing/blob/main/Deutsch%20algorithm%20circuit.svg)
![도이치 알고리즘 결과 분포](https://github.com/erados/Quantum-Computing/blob/main/Deutsch%20algorithm%20distribution.svg)
도이치 알고리즘은 1비트 입력 1비트 출력을 하는 함수 f(x)가 상수 함수인지 균형 함수(출력이 0과 1일 경우의 수가 같음)인지 판단하는 알고리즘이다.
고전 컴퓨팅으로는 2회의 쿼리를 보내야하지만 양자 컴퓨팅으로는 1회의 쿼리만 보내면 된다.
상수 함수의 유니타리 행렬을 U_f |x>|-> = (-1)^{f(X)}|x>|-> 로 설정하면 Q_1 에 대해 I, -I, Z, -Z(상수함수/상수함수/균형함수/균형함수), Q_0에 대해 I, X, CNOT(Q_1, Q_0), CNOT(Q_1, Q_0) X 를 수행하게된다. 따라서 Q_1 의 양쪽에 H를 추가하면 Q_1 에 대해 I, -I, X, -X 가 되어 상수함수는 입력이 그대로 나오고 균형함수는 입력이 반전되어 나오게 된다.
