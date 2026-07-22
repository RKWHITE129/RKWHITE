# while循环
rows = 1
while rows <= 9:

    columns = 1
    while columns <= rows:
        print(f"{columns} * {rows} = {rows * columns}\t", end='')
        columns += 1

    rows += 1
    print()

# for循环
for rows in range(1, 10):

    for columns in range(1, rows + 1):
        print(f"{columns} * {rows} = {columns * rows:<4}", end=" ")

    print()
