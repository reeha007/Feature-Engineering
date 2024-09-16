import numpy as np
a = np.array([2, 4, 4, 4, 5, 5, 7, 9, 6, 8])
n = len(a)
mean_value = np.sum(a) / n
variance_value = np.sum((a - mean_value) ** 2) / n
print(f"Feature Vector: {a}")
print(f"Mean: {mean_value}")
print(f"Variance: {variance_value}")
