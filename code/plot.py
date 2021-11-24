import matplotlib.pyplot as plt
import non_linear_function as nlf
import numpy as np
import sys

def plot_distribution(data_point, func):
    plt.plot(data_point, func)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.show()


if __name__ == '__main__':
     function = str(sys.argv[1])
     function = function.lower()
     x = np.linspace(-10, 10, 100)
     functions = nlf.non_linear_function(x)
     if (function == "sigmoid"):
         plot_distribution(x, functions.Sigmoid())
     elif (function == "relu"):
         plot_distribution(x, functions.ReLU())
     elif (function == "tanh"):
         plot_distribution(x, functions.tanh())
         
