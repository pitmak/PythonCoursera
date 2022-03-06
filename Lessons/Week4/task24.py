def prnSqr():
    n = int(input())
    if n == 0:
        return ' '
    st = prnSqr()
    sqr = int(n ** 0.5)
    if sqr * sqr == n:
        st += str(n) + ' '
    return st


st = prnSqr()
if st == ' ':
    print(0)
else:
    print(st)
