import numpy as np

a = np.array(
    [
        [0.49, 0.97, 0.53, 0.05],
        [0.33, 0.65, 0.62, 0.51],
        [1.00, 0.38, 0.61, 0.45],
        [0.74, 0.27, 0.64, 0.17],
        [0.36, 0.17, 0.96, 0.12]
    ]
)

b = np.array(
    [
        [0.79, 0.32, 0.68, 0.90, 0.77],
        [0.18, 0.39, 0.12, 0.93, 0.09],
        [0.87, 0.42, 0.60, 0.71, 0.12],
        [0.45, 0.55, 0.40, 0.78, 0.81]
    ]
)

print(np.dot(a, b))