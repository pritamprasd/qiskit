from qiskit import QuantumCircuit
from shared import run


def circuit_1():
    circuit = QuantumCircuit(2, 2)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.measure([0, 1], [0, 1])
    return circuit


if __name__ == "__main__":
    run(circuit_1)
