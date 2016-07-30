# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 16:26:45 2016

NEURAL NETWORK TESTING V0

@author: Muchen
"""

"""
TODO CURRENTLY THE DATA AND PARAMETERS ARE HARD CODED - MAKE VARIABLE
"""

#Imports
import numpy as np

class Neural_Network(object):
    def __init__(self, inSize, hideSize, outSize):
        #Define hyper-parameters
        self.inputSize = inSize;
        self.hiddenSize = hideSize;
        self.outputSize = outSize;        
        
        #Weights [W1, W2, ...]
        """
        TODO: NEED VECTORIZE
        """
        self.WEIGHTS = [np.random.randn(self.inputSize, self.hiddenSize),
                        np.random.randn(self.hiddenSize, self.outputSize)]
                        
    
    def forward(self, X):
        """Forward Propagation where X is a (m x n) matrix and m is
        the number of training examples and n is the number of units
        """
        #Propagation through the neural network
        """
        TODO: NEED VECTORIZATION
        """
        # INPUT LAYER - Matrix multiple, then use activation function
        self.z2 = np.dot(X, self.WEIGHTS[0])
        self.a2 = self.sigmoid(self.z2)
        
        # HIDDEN LAYER
        self.z3 = np.dot(self.a2, self.WEIGHTS[1])
        prediction = self.sigmoid(self.z3)
        
        # return OUTPUT LAYER
        return prediction

    def sigmoid(self, z):
        #Apply sigmoid activation function
        return 1 / (1 + np.exp(-z));
        
    def sigmoidPrime(self, z):
        #Derivative of the sigmoid function with respect to z
        return np.exp(-z)/((1 + np.exp(-z)) ** 2)
        
    def costFunction(self, X, y):
        #Calculate the cost function given the formula
        return sum((y - self.forward(X)) ** 2)
        
    def costFunctionPrime(self, X, y):
        #Derivative of the cost function with respect to weight
        gradient = []
        
        #Get hypothesis
        prediction = self.forward(X)
        
        #Use prediction in the back propagation through output -> hidden
        delta3 = np.multiply(-(y - prediction), self.sigmoidPrime(self.z3))
        gradient.append(np.dot(self.a2.T, delta3))
        
        #Backpropagate through hidden -> input
        delta2 = np.dot(delta3, self.WEIGHTS[1].T) * self.sigmoidPrime(self.z2)
        gradient.append(np.dot(X.T, delta2))
        
        #Stacking for a deeper network
        """
        TODO: MORE RESEARCH REQUIRED - INACCURATE
        delta_(i) = np.dot(delta_(i+1), weight_(i).T) * sigmoidPrime(z_(i))
        gradient_(i) = np.dot(X.T, delta_(i))
        """
        
        return gradient

#==============================================
def main():
    #Main program
    
    #Get X matrix and y vector
    XData = [[69, 72, 82],
         [81, 88, 80],
         [94, 90, 84]]
        
    yData = [[63], [74], [83]]
    
    X = np.array(XData, dtype = float)
    y = np.array(yData, dtype = float)
    
    #Normalize the inputs and outputs
    X = X / np.amax(X, axis = 0)
    y = y / 100
    
    #Establish other working variables
    m = len(X)
    n = len(X[0])
    
    brain = Neural_Network(n, 4, 1)
    
    print(brain.forward(X))
    print("===")
    print(y)
    
        
main()