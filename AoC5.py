import re
import string
import numpy as np 
input = open("D5P1.txt").read()
#input = open("PracData.txt").read()
input = re.split("", input)

input = np.array(input)

def reaction(input):
    alphabet = list(string.ascii_lowercase)
    value = True
    while (value == True):
        value = False
        for letter in alphabet:
            locations = np.where(input == letter)[0]
            for loc in locations:
                if (letter.upper() == input[loc + 1]):
                    input = np.delete(input, loc + 1)
                    input = np. delete(input, loc)
                    value = True
                    break
                elif (letter.upper() == input[loc - 1] and (loc - 1 > 0)):
                    input = np.delete(input, loc)
                    input = np.delete(input, loc - 1)
                    value = True
                    break
    size = input.shape 
    f = open("outputData.txt", "w+")
    for item in input:
        f.write(item)
    f.close()
    return(size[0] - 2)

size = reaction(input)
print("The answer is %d" % size)
