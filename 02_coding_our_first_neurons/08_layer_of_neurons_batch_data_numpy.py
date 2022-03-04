import numpy as np

inputs = [
    [1.0, 2.0, 3.0, 2.5], 
    [2.0, 5.0, -1.0, 2.0], 
    [-1.5, 2.7, 3.3, -0.8]
]
weights = [
    [0.2, 0.8, -0.5, 1.0], 
    [0.5, -0.91, 0.26, -0.5], 
    [-0.26, -0.27, 0.17, 0.87]
]

biases = [2.0, 3.0, 0.5]

# Is necessary to transpose because the shapes are (3, 4) and (3,4), and we need to be (3, 4) and (4, 3)
outputs = np.dot(inputs, np.array(weights).T) + biases

print(outputs)