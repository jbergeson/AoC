import numpy as np
import matplotlib.pyplot as plt
import itertools 
data = np.genfromtxt("D1P1.txt", dtype = int)
## Practice data sets:
#data = np.genfromtxt("PracData.txt", dtype = int)
#data = [7, 7, -2, -7, -4]
#data = [1, -2, 3, 4, 5, 6, -8, -2, 3, 4, 1, -9, -1, 8, -5]
n = 5  # number of times to repeat data set
data = list(data)
data = n * data
def getSums(data):
    newFreq = list(itertools.accumulate(data))
    myLength = len(data)
    zeroBase = myLength - 1
    last = newFreq[zeroBase]
    print("The last is: %d" % last)
    return(newFreq)

def getAns(data):
    newFreq = getSums(data)
    myList = []
    for x in newFreq:
        if x in myList: break
        else:
            myList.append(x)
    print("The final answer is: %d" %x)
getAns(data)
