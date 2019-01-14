import numpy as np
#data = np.loadtxt("D1P1.txt")
data = [1, 2, 3, 4, -4]
myLength = len(data)
zeroBase = myLength - 1
#print("Length is %d" % zeroBase)
ans = sum(data)
#print(ans)
newFreq = np.cumsum(data)
print(newFreq)
def main():
    a = 0
    b = 1
    var = False
    while (var == False):
        print("I ran")
        while (b <= zeroBase and newFreq[a] != newFreq[b]):
            print(a, b)
            print(newFreq[a], newFreq[b])
            b += 1
            if (a == b):
                b += 1
        if (a == zeroBase):
            var = True
        elif b <=(zeroBase):
            var = True
            print("a is %d and b is %d" % (a, b))
            print("Freq at a: %d, freq at b: %d" % (newFreq[a], newFreq[b]))
        a += 1       
        b = 0
    return(a, b)
main()