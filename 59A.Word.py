

# 29/01/2026. Implementation, string problem. 800 Rated. 

s = list(map(str, input().strip()))

upperCase = 0 
lowerCase = 0

for i in s:
    if i.islower():
        lowerCase += 1
    if i.isupper():
        upperCase += 1

if upperCase > lowerCase:
    s = "".join(s).upper()
elif lowerCase >= upperCase:
    s = "".join(s).lower()

print(s)


