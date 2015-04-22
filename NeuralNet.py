__author__ = 'adamlind'


import random
import math

#sigmoid function allows for backward propogation

alpha = 0
noisemax = 0
nodes = 0
size = 0
outputweight = []
hiddenweight = [[]]


def sigmoid(x):
    return 1/(1+math.exp(-x))

class NeuralNet:
    #constructor
    def __init__(self):
        #alpha is a learning rate (0->1)
        #small alphas can get stuck on local minima and take longer to train
        #large alphas train faster but can go over the solution
        aplha = 0.05
        #magnitude of initial weight values, ranged uniformly from +-moisemax/2
        noisemax = 0.4
        #saving the size for later, number of inputs and hidden nodes
        size = nodes
        #instantiate the output weights
        for i in range(0,nodes+1):
            outputweight[i] = random.random()*noisemax - noisemax/2
        #hidden weight 2D array
        for i in range(0,nodes):
            for j in range(0,nodes+1):
                hiddenweight[i][j] = random.random()*noisemax - noisemax/2

    #returns a binary guess with binary inputs
    def getPrediction(inputs):
        hidden = []
        for i in range(0,size):
            #used for summing dot products
            sum1 = 0
            for j in range(0,size):
                #make the value positive or negative
                sum1 += (-1 if (inputs[j]==0) else 1) * hiddenweight[i][j]
            #add the bias weight * 1
            sum1 += hiddenweight[i][size]
            #sigmoid it
            hidden[i] = sigmoid(sum1)
        #now do this for outputs
        sum2 = 0
        for i in range(0,size):
            sum2 += hidden[i] * outputweight[i]
        sum2 += outputweight[size]
        #return result of sigmoid rounded to 0 or 1
        return 1 if (sigmoid(sum2) >= 0.5) else 0

    #same as the getPrediction function without rounding
    #use this when you want to compare two outputs to have a more trustworthy prediction
    def getRawPrediction(inputs):
        hidden = []
        for i in range(0,size):
            #used for summing dot products
            sum1 = 0
            for j in range(0,size):
                #make the value positive or negative
                sum1 += (-1 if (inputs[j]==0) else 1) * hiddenweight[i][j]
            #add the bias weight * 1
            sum1 += hiddenweight[i][size]
            #sigmoid it
            hidden[i] = sigmoid(sum1)
            #now do this for outputs
            sum2 = 0
            for i in range(0,size):
                sum2 += hidden[i] * outputweight[i]
            sum2 += outputweight[size]
            #return unrounded result
            return sigmoid(sum2)

    #method for training your net based on sample inputs
    #calculation similar to previous methods
    def trainNet(inputs,desired):
        hidden = []
        for i in range(0,size):
            #used for summing dot products
            sum1 = 0
            for j in range(0,size):
                #make the value positive or negative
                sum1 += (-1 if (inputs[j]==0) else 1) * hiddenweight[i][j]
            #add the bias weight * 1
            sum1 += hiddenweight[i][size]
            #sigmoid it
            hidden[i] = sigmoid(sum1)
        #now do this for outputs
        sum2 = 0
        for i in range(0,size):
            sum2 += hidden[i] * outputweight[i]
        sum2 += outputweight[size]
        #save the prediction
        prediction = sigmoid(sum2)

        #and now it's time to train

        #find the error then multiply by the derivative of the output with respect to the hidden output
        #derivative of sigmoid is x*(1-x)
        error = (desired - prediction) * (prediction * (1 - prediction))

        hiddenerror = []
        #for the hidden nodes
        for i in range(0,size):
            #find node error then multiply by derivative of hidden output with respect to hidden input
            hiddenerror[i] = hidden[i] * (1-hidden[i]) * outputweight[i] * error
            #adjust hidden node -> output weight, then multiply by learning rate
            outputweight[i] += error * hidden[i] * alpha

        #now do the bias
        outputweight[size] += error * hidden[i] * alpha

        #train inputs of hidden nodes
        for i in range(0,size):
            for j in range(0,size):
                #node error to adjust weight
                hiddenweight[i][j] += alpha * hiddenerror[i] * (-1 if (inputs[i]==0) else 1)
            #and for the bias
            hiddenweight[i][size] += alpha * hiddenerror[i]

        #return boolean of whether prediction matached desired
        return True if ((1 if (prediction >= 0.5) else 0) == desired) else False