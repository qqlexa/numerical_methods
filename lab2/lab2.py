import numpy as np
print("Included!")

A = np.array([[20, 10], [17, 22]])
B = np.array([350, 500])
X = np.linalg.solve(A,B)

print(X)
