import numpy as py

data = open("D1P1.txt").read().split()
## Note: How does it know where to split?  We didn't give split() any 
## input...
data = [int(s) for s in data]
## Note: How can we do this?  We defined s after we used it...

n = len(data)
i = 0
x = 0
seen = set()
## Note: Why use a set instead of a list?  "data" was originally a 
## a list...

while True:
    if x in seen:
        print("First repeat is %d, and i is %d" % (x, i))
        break
        ## Note: Can you insert a break statement anywhere?  Even in 
        ## a while loop?
    seen.add(x)
    x += data[i]
    i += 1
    i = i % n
