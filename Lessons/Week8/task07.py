import itertools

print(
    *itertools.accumulate(
        map(int, input().split()),
        lambda a, b: a + b
    )
)
