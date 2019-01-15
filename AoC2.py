import numpy as np 
data = open("D2P1.txt").read().split()
#data = open("PracData.txt").read().split()

def checksum(data):
    i = 0
    twoCt = 0
    threeCt = 0
    for a in data:
        two = 0
        three = 0
        for x in data[i]:
            line = data[i]
            ct = line.count(x)
            if (ct == 2):
                two = 1
            elif (ct == 3):
                three = 1
            line = line.replace(x, "")
            print(type(line))
        twoCt += two
        threeCt += three
        i += 1
    return(twoCt, threeCt)


def getLetters(data):
    row = data[1]
    length = len(row)
    i = 0   #counts rows for myRow
    for myRow in data:  #iterates through myRows
        j = 0   #counts rows for otherRow
        for x in data:  #iterates through rows to check against
            otherRow = data[j]
            k = 0   #counts letters in a row
            check = 0
            for myLetter in myRow:  #iterates through letter sequence
                if (myLetter != otherRow[k]):
                    if (check == 0):
                        check = 1
                    else: break
                elif (check <= 1 and k == (length - 1) and myRow != otherRow):
                        print(myRow, otherRow)
                k += 1
            j += 1
        i += 1

getLetters(data)