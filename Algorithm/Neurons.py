import numpy as np


def sigmoid(x):
    # Our activation function : sigmoid function
    return 1 / (1 + np.exp(-x))


class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def feedforward(self, inputs):
        # Weight inputs, add bias, then use the activation function
        total = np.dot(self.weights, inputs) + self.bias  # use np.dot to implement matrix multiplication
        return sigmoid(total)


weights = np.array([0, 1])  # w1 = 0, w2 = 1
bias = 4
n = Neuron(weights, bias)

x = np.array([2, 3])
print(n.feedforward(x))  # 0.9991
