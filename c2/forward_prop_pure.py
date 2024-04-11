import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# Input data
x = np.array([200.0, 17.0])

# Layer 1 Unit/Neuron 1
w1_1 = np.array([1, 2])
b1_1 = np.array([-1])
z1_1 = np.dot(w1_1, x) + b1_1
a1_1 = sigmoid(z1_1)

# Layer 1 Unit/Neuron 2
w1_2 = np.array([-3, 4])
b1_2 = np.array([1])
z1_2 = np.dot(w1_2, x) + b1_2
a1_2 = sigmoid(z1_2)

# Layer 1 Unit/Neuron 3
w1_3 = np.array([5, -6])
b1_3 = np.array([2])
z1_3 = np.dot(w1_3, x) + b1_3
a1_3 = sigmoid(z1_3)

# Output of Layer 1 (Input of Layer 2)
a1 = np.array([a1_1, a1_2, a1_3])

# Layer 2 Unit/Neuron 1
w2_1 = np.array([-7, 8, 9])
b2_1 = np.array([3])
z2_1 = np.dot(w2_1, a1) + b2_1
a2_1 = sigmoid(z2_1)

# Output of Layer 2
a2 = np.array([a2_1])
