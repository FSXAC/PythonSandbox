# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 16:26:45 2016

NEURAL NETWORK TESTING V0

@author: Muchen
"""

"""
TODO: CURRENTLY THE DATA AND PARAMETERS ARE HARD CODED - MAKE VARIABLE
TODO: CONTINUE ON THE END OF PART 5 - FIND ERROR: GRADIENT NOT MATCHING 
      NUMERICAl RESULT
"""

#Imports
import numpy as np
from scipy import optimize

#Neural network class
class Neural_Network(object):
    def __init__(self, inSize, hideSize, outSize):
        #Define hyper-parameters
        self.inputSize = inSize;
        self.hiddenSize = hideSize;
        self.outputSize = outSize;        
        
        #Weights [W1, W2, ...] (Parameters)
        """
        TODO: NEED VECTORIZE
        """
        self.WEIGHTS = [np.ones((self.inputSize, self.hiddenSize)),
                        np.ones((self.hiddenSize, self.outputSize))]
                        
    
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
        self.prediction = self.forward(X)
        return 0.5* sum((y - self.prediction) ** 2)
        
    def costFunctionPrime(self, X, y):
        #Derivative of the cost function with respect to weight
        gradient = []
        
        #Get hypothesis
        self.prediction = self.forward(X)
        
        #Use prediction in the back propagation through output -> hidden
        delta3 = np.multiply(-(y - self.prediction), self.sigmoidPrime(self.z3))
        gradient = [np.dot(self.a2.T, delta3)] + gradient
        
        #Backpropagate through hidden -> input
        delta2 = np.dot(delta3, self.WEIGHTS[1].T) * self.sigmoidPrime(self.z2)
        gradient = [np.dot(X.T, delta2)] + gradient
        
        #Stacking for a deeper network
        """
        TODO: MORE RESEARCH REQUIRED - INACCURATE
        delta_(i) = np.dot(delta_(i+1), weight_(i).T) * sigmoidPrime(z_(i))
        gradient_(i) = np.dot(X.T, delta_(i))
        """
        
        return gradient
    
    """
    Helper functions for numerical computation
    """
    def getParams(self):
        #Returns the parameters (weights) unrolled                     
        params = np.concatenate((self.WEIGHTS[0].ravel(), 
                                 self.WEIGHTS[1].ravel()))
        return params
    
    def setParams(self, params):
        #Set the weights using a single parameter vector
        start = 0
        end = self.hiddenSize * self.inputSize
        self.WEIGHTS[0] = \
        np.reshape(params[start:end], (self.inputSize, self.hiddenSize))
        
        start = end
        end += self.hiddenSize * self.outputSize
        self.WEIGHTS[1] = \
        np.reshape(params[start:end], (self.hiddenSize, self.outputSize))
        
        
    def computeNumericalGradients(self, X, y):
        #Returns the gradient unrolled
        gradient1, gradient2 = self.costFunctionPrime(X, y)
        return np.concatenate((gradient1.ravel(), gradient2.ravel()))

#==============================================
def computeNumericalGradient(NN, X, y):
    #Computes the gradient numerically (close enough)
    paramsInitial = NN.getParams()
    numGradient = np.zeros(paramsInitial.shape)
    perturb = np.zeros(paramsInitial.shape)
    
    #epsilon for deviation
    e = 1e-4
    
    for p in range(len(paramsInitial)):
        #Set perturbation vector
        perturb[p] = e
        
        NN.setParams(paramsInitial + perturb)
        cost2 = NN.costFunction(X, y)
        
        NN.setParams(paramsInitial - perturb)
        cost1 = NN.costFunction(X, y)
        
        #Computer numerical gradient for each element
        numGradient[p] = (cost2 - cost1) / (2 * e)
        
        #Change back to 0??
        perturb[p] = 0
    
    #Reset parameters to original value
    NN.setParams(paramsInitial)
    
    return numGradient

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
    
    brain = Neural_Network(n, 3, 1)
    
    print("===NUMERICAL COMPUTATION GRADIENT")
    print(computeNumericalGradient(brain, X, y))
    print("===GRADIENT DESCENT GRADIENT")
    print(brain.computeNumericalGradients(X, y))
    
    print("close enough")
main()