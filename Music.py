__author__ = 'adamlind'

import pysynth
from Markov import Markov

class Music:
    def __init__(self):
        self._prevNote = None
        self._markov = Markov(["a", "a#", "b", "c", "c#", "d", "d#", "e", "f", "f#", "g", "g#"])
        self._times = Markov([1,2,4,8,16])

    def add(self, fNote):
        #connect path from previous note to next note
        #multiple connections increases weight
        if(self._prevNote is None):
            self._prevNote = fNote
            return
        iNote = self._prevNote
        self._markov.add(iNote[0], fNote[0])
        self._times.add(iNote[1], fNote[1])
        self._prevNote = fNote

    def nextNote(self, iNote):
        return [self._markov.nextVal(iNote[0]), self._times.nextVal(iNote[1])]