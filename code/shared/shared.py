from datetime import datetime
from qiskit.visualization import *
from qiskit.tools.jupyter import *
from ibm_quantum_widgets import *
from qiskit.providers.aer import QasmSimulator
from qiskit import transpile


def timeit(func):
    def wrapper_function(*args, **kwargs):
        s = datetime.now()
        func(*args, **kwargs)
        print(f"\n==> Time taken: {(datetime.now() - s).microseconds} microseconds")

    return wrapper_function


@timeit
def run(func, simulator=QasmSimulator(), sim_shots=1024, verbose=False, draw=True):
    circuit = func()
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=sim_shots)
    result = job.result()
    if verbose:
        print(f"\nResults: {result}")
    print("\nCount:", result.get_counts(compiled_circuit))
    if draw:
        print(circuit.draw())
