import numpy as np
n = 10  
a = np.random.rand(n)
b = np.random.rand(n)
mean_a = np.mean(a)
mean_b = np.mean(b)
cov = np.mean((a - mean_a) * (b - mean_b))
std_a = np.std(a)
std_b = np.std(b)
corr = cov / (std_a * std_b)
print("Vector a:", a)
print("Vector b:", b)
print("Correlation between Vector a and Vector b:", corr)


