import numpy as np
from method import gauss

print("Included!")

student_id = "12648067"
# g = int(student_id[-1])  # 7
# k = int(student_id[-2])  # 6

# eq1 = [[g + 1, g + 2, g + 3], [2 * (g + 1), g + 6, g - 5], [3 * (g + 1), g, -3]]
# eqAd = [k, k + 1, k + 2]

# A = np.array([[20, 10], [17, 22]])
# A = np.array(eq1)
# B = np.array([350, 500])
# B = np.array(eqAd)
# X = np.linalg.solve(A, B)

print(X)
# [0.34294872 0.07692308 0.25641026]
eq = [[1, 3, 0], [0, 3, 0], [1, 3, 0]]
eqAd = [1, 2, 3]
x = gauss.solve(eq, eqAd)
print(x)

