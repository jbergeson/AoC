import datetime
import numpy as np

data = open("D4P1.txt").read().split("\n")
#data = open("PracData.txt").read().split("\n")

def organizeData(data):
    actions = {}
    for line in data:
        time = line[1:17]
        word = line.split(" ")
        if (word[2] == "Guard"):
            actions.update({time: word[3]})
        else: 
            actions.update({time:word[2]})
    chronological = sorted(actions.keys())
    orderedActions = {}
    for myKey in chronological:
        myValue = actions[myKey]
        orderedActions.update({myKey:myValue})
    return(orderedActions)

def sumTime(movement):
    time = list(movement.keys())
    moves = list(movement.values())
    guards = [[0], [0]]
    minutesAsleep = [[0] for i in range(61)]
    j = 0
    for action in moves:
        if (action[0] == "#"):
            if (action not in guards[0]):
                guards[0].append(action)
                guards[1].append(0)
                minutesAsleep[0].append(action)
                for index in range(1, 61):
                    minutesAsleep[index].append(0)
            location = guards[0].index(action)
        elif ("falls" in action):
            min1 = time[j]
            min2 = time[j + 1]
            min1 = int(min1[14:16])
            min2 = int(min2[14:16])
            for index in range(min1 + 1, min2 + 1): 
                minutesAsleep[index][location] += 1
            guards[1][location] += timeDifference(time[j], time[j + 1])
        j += 1
    return(guards, minutesAsleep)

def timeDifference(time1, time2):  
    datetime1 = datetime.datetime.strptime(time1, "%Y-%m-%d %H:%M")
    datetime2 = datetime.datetime.strptime(time2, "%Y-%m-%d %H:%M")
    minutes = datetime2 - datetime1
    minutes = str(minutes)
    minutes = minutes.strip("0")
    minutes = minutes.strip(":")
    minutes = int(minutes)
    return(minutes)                

def findGuard(guards):  
    location = guards[1].index(max(guards[1]))
    guard = guards[0][location]
    return(guard)

def findMin(minutesAsleep, guard): 
    column = minutesAsleep[0].index(guard)
    guardMins = []
    for i in range(1, 61):
        guardMins.append(minutesAsleep[i][column])
    maximum = max(guardMins)
    minute = guardMins.index(maximum)
    return(minute)

def partTwo(minutesAsleep):
    totalMax = 0
    for j in range(1,61):
        locMax = max(minutesAsleep[j])
        if (locMax > totalMax):
            totalMax = locMax
    for i in range(61):
        if (totalMax in minutesAsleep[i]):
            location = minutesAsleep[i].index(totalMax)
            break
    return(i, location)

movement = organizeData(data)
guards, minutesAsleep = sumTime(movement)
guard = findGuard(guards)
print("The guard with the most time asleep is %s" % guard)
minute = findMin(minutesAsleep, guard)
print("The minute he spends asleep the most is %d" % minute)
guard = guard.strip("#")
guard = int(guard)
ans = guard * minute
print("The answer using method 1 is: %d" % ans)
row, col = partTwo(minutesAsleep)
minute2 = row - 1
guard2 = minutesAsleep[0][col]
guard2 = guard2.strip("#")
guard2 = int(guard2)
ans2 = minute2 * guard2
print(minute2, guard2)
print("The answer using method 2 is: %d" %ans2)

