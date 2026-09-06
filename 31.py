import numpy as np

arr = np.array([10, 25, 30, 45, 60])

mask = arr > 30
print("Mask:", mask)

filtered = arr[mask]
print("Filtered elements:", filtered)
