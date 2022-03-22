import functools

print(
    functools.reduce(
        lambda a, b: a * b ** 5,
        map(int, input().split()),
        1
    )
)
