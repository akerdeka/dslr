import sys
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

class MachineLearning:

    np.set_printoptions(threshold=sys.maxsize)

    @staticmethod
    def Initialisation(X):
        W = np.random.randn(X.shape[1], 1)
        b = np.random.randn(1)
        return (W, b)

    @staticmethod
    def Model(X, W, b):
        Z = X.dot(W) + b
        e = np.exp(-Z)
        A = 1 / (1 + e)
        return (A)

    @staticmethod
    def LogLoss(A, y):
        return (1 / len(y) * np.sum(-y * np.log(A) - (1 - y) * np.log(1 - A)))

    @staticmethod
    def Gradients(A, X, y):
        dW = 1 / len(y) * np.dot(X.T, A - y)
        db = 1 / len(y) * np.sum(A - y)
        return (dW, db)

    @staticmethod
    def Update(dW, db, W, b, learning_rate):
        W = W - learning_rate * dW
        b = b - learning_rate * db
        return (W, b)

    @staticmethod
    def Predict(X, W, b):
        A = MachineLearning.Model(X, W, b)
        return A

    @staticmethod
    def Artificial_neuron(X, y, learning_rate = 1, nb_iter = 1000):
        W, b = MachineLearning.Initialisation(X)

        Loss = []

        for i in range(nb_iter):
            A = MachineLearning.Model(X, W, b)
            Loss.append(MachineLearning.LogLoss(A, y))
            dW, db = MachineLearning.Gradients(A, X, y)
            W, b = MachineLearning.Update(dW, db, W, b, learning_rate)

        plt.plot(Loss)
        plt.savefig("images/log_loss.png")

        return (W, b)

