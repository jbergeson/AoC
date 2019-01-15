import numpy as np 
data = open("D2P1.txt").read().split()


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
        twoCt += two
        threeCt += three
        i += 1
    return(twoCt, threeCt)
twoCt, threeCt = checksum(data)
print(twoCt)
print(threeCt)
print("The answer is ", twoCt * threeCt)