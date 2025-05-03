from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# 1. יוצרים מעגל קוונטי עם קיוביט אחד וביט קלאסי אחד
qc = QuantumCircuit(1, 1)

# 2. מפעילים שער הדהד (Hadamard gate) - יוצר סופרפוזיציה
qc.h(0)

# 3. מודדים את הקיוביט, ושומרים את התוצאה בביט הקלאסי
qc.measure(0, 0)

# 4. מריצים את המעגל על סימולטור קוונטי (לא מחשב קוונטי אמיתי)
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator, shots=1000).result()
counts = result.get_counts(qc)

# 5. מציגים את תוצאות המדידה
plot_histogram(counts)
plt.show()
