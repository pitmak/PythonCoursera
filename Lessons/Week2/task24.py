l1 = int(input())
w1 = int(input())
h1 = int(input())

l2 = int(input())
w2 = int(input())
h2 = int(input())

lc = int(input())
wc = int(input())
hc = int(input())

if (
        h1 <= hc and h2 <= hc and (
        l1 + l2 <= lc and w1 <= wc and w2 <= wc or
        l1 + w2 <= lc and w1 <= wc and l2 <= wc or
        w1 + l2 <= lc and l1 <= wc and w2 <= wc or
        w1 + w2 <= lc and l1 <= wc and l2 <= wc) or
        h1 <= hc and h2 <= hc and (
        l1 + l2 <= wc and w1 <= lc and w2 <= lc or
        l1 + w2 <= wc and w1 <= lc and l2 <= lc or
        w1 + l2 <= wc and l1 <= lc and w2 <= lc or
        w1 + w2 <= wc and l1 <= lc and l2 <= lc) or
        h1 + h2 <= hc and (
        l1 <= lc and w1 <= wc and l2 <= lc and w2 <= wc or
        w1 <= lc and l1 <= wc and l2 <= lc and w2 <= wc or
        l1 <= lc and w1 <= wc and w2 <= lc and l2 <= wc or
        w1 <= lc and l1 <= wc and w2 <= lc and l2 <= wc)
):
    print('YES')
else:
    print('NO')
