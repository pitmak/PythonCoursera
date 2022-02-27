prev = int(input())
seq = 1
maxSeq = 1

while True:
    n = int(input())
    if n == 0:
        break
    if n == prev:
        seq += 1
        if seq > maxSeq:
            maxSeq = seq
    else:
        prev = n
        seq = 1

print(maxSeq)
