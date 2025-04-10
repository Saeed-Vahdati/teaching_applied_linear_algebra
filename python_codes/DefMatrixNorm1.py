import numpy as np
A = np.array([[1, -2, 3],
              [4,  0, -1],
              [-2, 1, 5]])
num_samples = 1000
approx_norm_1 = 0
for _ in range(num_samples):
    v = np.random.randn(A.shape[1])  
    v /= np.linalg.norm(v, 1)  
    norm_ratio = np.linalg.norm(A @ v, 1)  
    approx_norm_1 = max(approx_norm_1, norm_ratio) 

print(f"Approximate Norm 1: {approx_norm_1}")