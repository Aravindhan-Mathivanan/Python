for testcases in range(int(input())):
    n,m = map(int, input().split())
    black_shape = []

    for rows in range(n):
        cells = input()[:m]
        black_cell = ''

        for black in cells:
            if black == '#':
                black_cell += black
        black_shape.append(len(black_cell))

    print(max(black_shape))