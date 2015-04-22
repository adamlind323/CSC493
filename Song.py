__author__ = 'adamlind'

import pysynth
from Music import Music

musicMarkov = Music()

musicMarkov.add(["c", 4]) #Row
musicMarkov.add(["c", 4]) #row
musicMarkov.add(["c", 4]) #row
musicMarkov.add(["d", 8]) #your
musicMarkov.add(["e", 4]) #boat
musicMarkov.add(["e", 4]) #gent-
musicMarkov.add(["d", 8]) #-ly
musicMarkov.add(["e", 4]) #down
musicMarkov.add(["f", 8]) #the
musicMarkov.add(["g", 2]) #stream
musicMarkov.add(["c", 8]) #mer-
musicMarkov.add(["c", 8]) #-ri-
musicMarkov.add(["c", 8]) #-ly
musicMarkov.add(["g", 8]) #mer-
musicMarkov.add(["g", 8]) #-ri-
musicMarkov.add(["g", 8]) #-ly
musicMarkov.add(["e", 8]) #mer-
musicMarkov.add(["e", 8]) #-ri-
musicMarkov.add(["e", 8]) #-ly
musicMarkov.add(["c", 8]) #mer-
musicMarkov.add(["c", 8]) #-ri-
musicMarkov.add(["c", 8]) #-ly
musicMarkov.add(["g", 4]) #life
musicMarkov.add(["f", 8]) #is
musicMarkov.add(["e", 4]) #but
musicMarkov.add(["d", 8]) #a
musicMarkov.add(["c", 2]) #dream!

markovSong = []
selNote = ["c", 4]
for i in range(0,100):
    print selNote[0] + ", " + str(selNote[1])
    selNote = musicMarkov.nextNote(selNote)
    markovSong.append(selNote)

pysynth.make_wav(markovSong, fn = "song.wav")