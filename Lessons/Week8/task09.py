import itertools

# list(
#     map(
#         lambda x: print(*x, sep=''),
#         itertools.permutations(
#             range(1, int(input()) + 1)
#         )
#     )
# )

print(
    *map(
        lambda x: ''.join(x),
        itertools.permutations(
            map(
                str,
                range(1, int(input()) + 1)
            )
        )
    ),
    sep='\n'
)
