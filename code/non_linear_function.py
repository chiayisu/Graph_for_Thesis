import numpy as np

class non_linear_function:
    
    def __init__(self, x):
        self.x = x
        
    def Sigmoid(self):
        sigmoid = 1/(1 + np.exp(-self.x))
        return sigmoid

    def ReLU(self):
        ReLU = np.maximum(0, self.x)
        return ReLU

    def tanh(self):
        tanh = (np.exp(self.x)-np.exp(-self.x))/(np.exp(self.x)+np.exp(-self.x))
        return tanh
