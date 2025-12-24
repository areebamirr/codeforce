n, m = map(int, input().split())
rows = []
min_row = n
max_row = -1
min_col = m
max_col = -1

# Read all rows
for _ in range(n):
    row = input()
    rows.append(row)

# Find bounds of shaded squares
for i in range(n):
    for j in range(m):
        if rows[i][j] == '*':
            min_row = min(min_row, i)
            max_row = max(max_row, i)
            min_col = min(min_col, j)
            max_col = max(max_col, j)

# Output the minimal rectangle
for i in range(min_row, max_row + 1):  # Need +1 because range is exclusive
    for j in range(min_col, max_col + 1):
        print(rows[i][j], end='')
    print()  # New line after each row