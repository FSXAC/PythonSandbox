# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 16:26:45 2016

NEURAL NETWORK TESTING V0

@author: Muchen
"""

#Imports
import numpy as np

class Neural_Network(object):
    def __init__(self, inputSize, hiddenSize, outputSize):
        #Define hyper-parameters
        self.inputLayerSize = inputSize;
        self.outputLayerSize = outputSize;
        self.hiddenLayerSize = hiddenSize;
    
    def forward(self, X):
        """Forward Propagation where X is a (m x n) matrix and m is
        the number of training examples and n is the number of units
        """
        #Propagation through the neural network

    def sigmoid(self, z):
        #Apply sigmoid activation function
        return 1/(1+np.exp(-z));

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
    
    NN = Neural_Network(n, 4, 1)
    for i in range(-10, 10):
        print(NN.sigmoid(i))
        
main()