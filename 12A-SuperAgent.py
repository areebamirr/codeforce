
# 08/01/2026. Understood this problem by own and solved the problem by own.

keys = []
for _ in range(3):
    key = input()
    keys.append(key)

if str(keys[0])[::-1] == str(keys[2]) and str(keys[1][0]) == str(keys[1][2]):
    print("YES")
else:
    print("NO")

