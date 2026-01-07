
n,m = map(int, input().split())

flag = []
for i in range(n):
    row = input().strip()
    flag.append(row)

valid = True
for i in range(n):
    if flag[i] != flag[i][0]*m:
        valid = False
        break

if valid:
    for i in range(n-1):
        if flag[i][0] == flag[i+1][0]:
            valid = False
            break

print("YES" if valid else "NO")

