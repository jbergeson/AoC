import numpy as np 
import re
data = open("D3P1.txt").read()
data = re.split(" @ |,|: |x|\n#", data)
data[0] = 1
data = [int(s) for s in data]

def extractData(data):
    i = 1
    j = 3
    locationL = list()
    locationT = list()
    area1 = list()
    area2 = list()
    for x in data:
        if (i > len(data)): break
        locationL.append(data[i])
        locationT.append(data[i + 1])
        area1.append(data[j])
        area2.append(data[j + 1])
        i += 5
        j += 5
    return(locationL,locationT, area1, area2)

def fillArray(locationL, locationT, area1, area2):
    blanket = np.zeros((1000, 1000))
    i = 0
    for x in locationL:
        leftEdge = locationL[i]
        rightEdge = locationL[i] + area1[i]
        topEdge = locationT[i]
        bottEdge = locationT[i] + area2[i]
        blanket[leftEdge:rightEdge, topEdge:bottEdge] += 1
        i += 1
    return(blanket)

def countOverOne(array):
    i = 0
    j = 0
    sum = 0
    while i < 1000:
        j = 0
        while j < 1000:
            if 1 < array[i, j]:
                sum += 1
            j += 1
        i += 1
    return(sum)


locationL, locationT, area1, area2 = extractData(data)
array = fillArray(locationL, locationT, area1, area2)
ans = countOverOne(array)
print(ans)



## Note: This section is completely unnecessary, I just wanted to 
## practice making an object and giving it attributes.

# class rectangle():
#     def __init__(self, lEdge, tEdge, width, height):
#         self.location = [lEdge, tEdge]
#         self.area = width * height
# fabric = rectangle(1, 1, 2, 3)
# # print(fabric.location)
# # print(fabric.area)
