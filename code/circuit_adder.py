from qiskit import QuantumCircuit
from shared import run

def circuit_half_adder(x_bit=1, y_bit=1):
    qc = QuantumCircuit(4, 2)
    if x_bit:
        qc.x(0)
    if y_bit:
        qc.x(1)
    qc.cx(0, 2)
    qc.cx(1, 2)
    qc.ccx(0, 1, 3)

    qc.measure(2, 0)
    qc.measure(3, 1)
    return qc


if __name__ == "__main__":
    run(circuit_half_adder)