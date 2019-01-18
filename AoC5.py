import re
import string
import numpy as np 
from functools import partial
from operator import ne

input = open("D5P1.txt").read()
#input = open("PracData.txt").read()
input = re.split("", input)

def reaction(input):
    input = np.array(input)
    alphabet = list(string.ascii_lowercase)
    value = True
    while (value == True):
        value = False
        for letter in alphabet:
            locations = np.where(input == letter)[0]
            locations = sorted(locations, reverse = True)
            for loc in locations:
                if (letter.upper() == input[loc + 1]):
                    input = np.delete(input, loc + 1)
                    input = np. delete(input, loc)
                    value = True
                elif (letter.upper() == input[loc - 1] and (loc - 1 > 0)):
                    input = np.delete(input, loc)
                    input = np.delete(input, loc - 1)
                    value = True
    size = input.shape 
    return(size[0] - 2)

def removeLetters(input):
    totLength = 0
    alphabet = list(string.ascii_lowercase)
    for letter in alphabet:
        removeLower = list(filter(partial(ne, letter), input))
        removeUpper = list(filter(partial(ne, letter.upper()), removeLower))
        locLength = reaction(removeUpper)
        if (locLength < totLength or totLength == 0):
            totLength = locLength
    return(totLength)


size = reaction(input)
print("The answer to part 1 is %d" % size)
finalSize = removeLetters(input)
print("The answer to part 2 is %d" % finalSize)
