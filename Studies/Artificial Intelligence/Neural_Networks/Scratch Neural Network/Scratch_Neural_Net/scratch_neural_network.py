import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import clear_output


class Scratch_Neural_Network:
    def __init__(self, m, n) -> None:
        self.m = m
        self.n = n


    def __init_params(self):
        w1 = np.random.rand(10, 784) - 0.5
        b1 = np.random.rand(10, 1) - 0.5
        w2 = np.random.rand(10, 10) - 0.5
        b2 = np.random.rand(10, 1) - 0.5
        return w1, b1, w2, b2


    def __ReLU(self, z):
        return np.maximum(z, 0)


    def __softmax(self, z):
        return np.exp(z) / sum(np.exp(z))


    def __forward_propagation(self, w1, b1, w2, b2, x):
        z1 = w1.dot(x) + b1
        a1 = self.__ReLU(z1)
        z2 = w2.dot(a1) + b2
        a2 = self.__softmax(z2)
        return z1, a1, z2, a2


    def __derivate_ReLU(self, z):
        return z > 0


    def __one_hot(self, y):
        one_hot_y = np.zeros((y.size, y.max() + 1))
        one_hot_y[np.arange(y.size), y] = 1
        one_hot_y = one_hot_y.T
        return one_hot_y


    def __back_propagation(self, z1, a1, z2, a2, w2, x, y):
        # m = y.size
        one_hot_y = self.__one_hot(y)
        dz2 = a2 - one_hot_y
        dw2 = 1 / self.m * dz2.dot(a1.T)
        db2 = 1 / self.m * np.sum(dz2) 
        dz1 = w2.T.dot(dz2) * self.__derivate_ReLU(z1)
        dw1 = 1 / self.m * dz1.dot(x.T)
        db1 = 1 / self.m * np.sum(dz1)
        return dw1, db1, dw2, db2


    def __update_params(self, w1,b1,w2,b2,dw1,db1,dw2,db2,alpha):
        w1 = w1 - alpha * dw1
        b1 = b1 - alpha * db1
        w2 = w2 - alpha * dw2
        b2 = b2 - alpha * db2
        return w1, b1, w2, b2
        

    def __get_predictions(self, a2):
        return np.argmax(a2, 0)


    def __accuracy_ratio(self, predictions, y):
        print(predictions)
        return np.sum(predictions == y) / y.size


    def train(self, x, y, iterations, alpha):
        w1, b1, w2, b2 = self.__init_params()
        for i in range(iterations + 1):
            z1, a1, z2, a2 = self.__forward_propagation(w1, b1, w2, b2, x)
            dw1, db1, dw2, db2 = self.__back_propagation(z1, a1, z2, a2, w2, x, y)
            w1, b1, w2, b2 = self.__update_params(w1,b1,w2,b2,dw1,db1,dw2,db2,alpha)

            progress = i / iterations
            arrow = '=' * int(round(progress * iterations) - 1)
            spaces = ' ' * (iterations - len(arrow))

            if i % 10 == 0:
                print(f"Iteration {i} \r[{arrow}{spaces}] {progress*100:.2f}% Complete")
                print(f"Acc {self.__accuracy_ratio(self.__get_predictions(a2), y):.2%}")
            
                clear_output(wait = True)

        return w1, b1, w2, b2


    def predict(self, X, W1, b1, W2, b2):
        _, _, _, A2 = self.__forward_propagation(W1, b1, W2, b2, X)
        predictions = self.__get_predictions(A2)
        return predictions


