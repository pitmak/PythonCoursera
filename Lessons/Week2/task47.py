prev = int(input())
waitingForDown = False
prevLocalMax = None
currLocalMax = None
minDistance = 9999999999
i = 1
while True:
    n = int(input())
    if n == 0:
        break
    if n > prev:
        waitingForDown = True
    elif n == prev:
        waitingForDown = False
    elif waitingForDown:
        currLocalMax = i - 1
        if not (prevLocalMax is None):
            distance = currLocalMax - prevLocalMax
            if distance < minDistance:
                minDistance = distance
        prevLocalMax = currLocalMax
        waitingForDown = False
    prev = n
    i += 1
if minDistance != 9999999999:
    print(minDistance)
else:
    print(0)
