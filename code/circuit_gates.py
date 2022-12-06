from qiskit import QuantumCircuit
from shared import run


def circuit_NOT_gate():
    qc = QuantumCircuit(3, 3)
    qc.x([0, 1])  # Perform X-gates on qubits 0 & 1
    qc.measure([0, 1, 2], [0, 1, 2])
    return qc


def circuit_XOR_gate(x_bit=0, y_bit=0):
    qc = QuantumCircuit(3, 1)
    if x_bit:
        qc.x(0)
    if y_bit:
        qc.x(1)
    qc.cx(0, 2)
    qc.cx(1, 2)
    qc.measure(2, 0)
    return qc


if __name__ == "__main__":
    run(circuit_XOR_gate)