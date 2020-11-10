import cirq
import random

def make_circuit(ranX, ranY, ranX2, ranY2):
	
	msg = [cirq.LineQubit(1),cirq.LineQubit(2)]
	alice = [cirq.LineQubit(3),cirq.LineQubit(4)]
	bob = [cirq.LineQubit(5),cirq.LineQubit(6)]


	circuit = cirq.Circuit()
	circuit.append([cirq.X(msg[0])**ranX, cirq.Y(msg[0])**ranY, cirq.X(msg[1])**ranX2, cirq.Y(msg[1])**ranY2])
	circuit.append([cirq.H(alice[0]), cirq.H(alice[1])])
	circuit.append([cirq.CNOT(alice[0], bob[0]), cirq.CNOT(alice[1], bob[1])])

	circuit.append([cirq.CNOT(msg[0], alice[0]), cirq.CNOT(msg[1], alice[1])])
	circuit.append([cirq.H(msg[0]), cirq.H(msg[1])])

	circuit.append([cirq.measure(msg[0],msg[1],alice[0],alice[1])])

	circuit.append([cirq.CX(alice[0], bob[0])])
	circuit.append([cirq.CX(alice[1], bob[1])])

	circuit.append([cirq.CZ(msg[0], bob[0])])
	circuit.append([cirq.CZ(msg[1], bob[1])])


	print(circuit)

	return circuit

def main():
	ranX = random.random() 
	ranY = random.random() 
	ranX2 = random.random() 
	ranY2 = random.random()
	
	circuit = make_circuit(ranX, ranY, ranX2, ranY2)

	msg = [cirq.LineQubit(7),cirq.LineQubit(8)]
	
	sim = cirq.Simulator()
	a = cirq.Circuit()
	a.append([cirq.X(msg[0])**ranX, cirq.Y(msg[0])**ranY, cirq.X(msg[1])**ranX2, cirq.Y(msg[1])**ranY2])
	message = sim.simulate(a)
	received = sim.simulate(circuit)

	print("앨리스의 큐비트")
	b0X, b0Y, b0Z = cirq.bloch_vector_from_state_vector(message.final_state,0)
	print("\nx: ",round(b0X, 3),"y: ",round(b0Y, 3),"z: ",round(b0Z, 3),)
	b0X, b0Y, b0Z = cirq.bloch_vector_from_state_vector(message.final_state,1)
	print("\nx: ",round(b0X, 3),"y: ",round(b0Y, 3),"z: ",round(b0Z, 3),)
	print(message)

	print("\n\n전송된 큐비트")
	b0X, b0Y, b0Z = cirq.bloch_vector_from_state_vector(received.final_state,4)
	print("\nx: ",round(b0X, 3),"y: ",round(b0Y, 3),"z: ",round(b0Z, 3))
	b0X, b0Y, b0Z = cirq.bloch_vector_from_state_vector(received.final_state,5)
	print("\nx: ",round(b0X, 3),"y: ",round(b0Y, 3),"z: ",round(b0Z, 3))
	print(received)

if __name__ == '__main__':
	main()

