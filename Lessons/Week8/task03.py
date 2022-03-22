print(
    min(
        filter(
            lambda x: x % 2,
            map(
                int,
                open('input.txt', 'r', encoding='utf-8').read().split()
            )
        )
    )
)
