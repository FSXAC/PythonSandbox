# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 16:26:45 2016

NEURAL NETWORK TESTING V0

@author: Muchen
"""

#TODO CURRENTLY THE DATA AND PARAMETERS ARE HARD CODED - MAKE VARIABLE

#Imports
import numpy as np

class Neural_Network(object):
    def __init__(self, inSize, hideSize, outSize):
        #Define hyper-parameters
        self.inputSize = inSize;
        self.hiddenSize = hideSize;
        self.outputSize = outSize;        
        
        #Weights [W1, W2, ...]
        self.WEIGHTS = [np.random.randn(self.inputSize, self.hiddenSize),
                        np.random.randn(self.hiddenSize, self.outputSize)]
                        
    
    def forward(self, X):
        """Forward Propagation where X is a (m x n) matrix and m is
        the number of training examples and n is the number of units
        """
        #Propagation through the neural network
        #TODO: VECTORIZATION
        # INPUT LAYER - Matrix multiple, then use activation function
        self.z2 = np.dot(X, self.WEIGHT[0])
        self.a2 = self.sigmoid(self.z2)
        
        # HIDDEN LAYER
        self.z3 = np.dot(self.a2, self.WEIGHTS[1])
        prediction = self.sigmoid(self.z3)
        
        # return OUTPUT LAYER
        return prediction

    def sigmoid(self, z):
        #Apply sigmoid activation function
        return 1 / (1 + np.exp(-z));

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
        
main()