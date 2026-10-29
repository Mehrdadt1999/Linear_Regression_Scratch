import math
import numpy as np

class LinearRegression:
    def __init__(self, x_train: np.array, y_train: np.array):
        self.bias = 0
        self.weight = 0
        self.x_train = x_train
        self.y_train = y_train

    def cal_yhat(self):
        y_hats = (self.x_train * self.weight) + self.bias
        return y_hats

    def cal_MSE(self):
        squared_error_sum = 0
        y_hats = self.cal_yhat()
        squared_error_sum = np.sum((y_hats - self.y_train) ** 2)
        return squared_error_sum / (2 * np.size(self.y_train))

    def gradient_descent(self, lr):
        y_hats = self.cal_yhat
        dw = np.dot((y_hats - self.y_train), np.transpose(self.x_train))
        db = np.sum(y_hats - self.y_train)
        
        

    def train(self):
        mse = self.cal_MSE(self.x_train, self.y_train)
        print(mse)


        


    def predict(self):
        pass
