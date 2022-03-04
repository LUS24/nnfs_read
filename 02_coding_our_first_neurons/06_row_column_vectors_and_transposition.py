import numpy as np

a = [1, 2, 3]
b = [2, 3, 4]

row_vector_a = np.array([a])
print(row_vector_a)

# Other options to create a row vector
# np.array([[1, 2, 3]])
# np.expand_dims(np.array(a), axis=0)

column_vector_b = np.array([b]).T
print(column_vector_b)

