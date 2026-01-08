
# Date : 07/1/2026. Successfully solved by own

from fractions import Fraction

y, w = map(int, input().split())

maxs = y if y > w else w

events = 6
sample = 0
for i in range(maxs, events+1):
    sample += 1


if sample/events:
    if sample/events == 1:
        print("1/1")
    else:
        print(Fraction(sample, events))

elif sample == 0:
    print("0/1")


