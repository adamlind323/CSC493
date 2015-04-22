__author__ = 'adamlind'

import random

class Markov:
    #constructor
    def __init__(self,listVal):
        self._addedVal = 0
        #reverse lookup
        self._revLookupVal = listVal
        self._lookupVal = {}
        #makes a key
        for i in range(0,len(listVal)):
            self._lookupVal[listVal[i]] = i
        #Initial probability adjacency matrix
        self._adjMatrix = [[0 for i in range(0,len(listVal))] for j in range(0,len(listVal))]

    def add(self,iVal,fVal):
        #makes a connection from iVal to fVal
        #repeating this will increase transition weight
        val = self._lookupVal[iVal]
        self._adjMatrix[val[iVal]][val[fVal]] += 1
        self._addedVal = self._addedVal + 1

    def nextVal(self,iVal):
        val = self._lookupVal[iVal]
        countVal = self._adjMatrix[val]
        indexVal = self.randomChoice(countVal)
        if(indexVal < 0):
            raise RuntimeError, "Non-existent value."
        else:
            return self._revLookupVal[indexVal]

    def randomChoice(self, countChoice):
        #returns a randomly chosen index
        sumCount = 0
        sC = sum(countChoice)
        countSel = random.randrange(1,sC + 1)
        for i in range(0,len(countChoice)):
            sumCount += countChoice[i]
            if(sumCount >= countSel):
                return i
        raise RuntimeError, "Unaccepted value selection."