
# 29/12/2025. Need to understand the greedy algorithm one part again.

days, sumTime = map(int, input().split())

rg_Day = []

for day in range(days):
    minTime, maxTime = map(int, input().split())
    rg_Day.append((minTime,maxTime))

min_sum = sum(x for x, y in rg_Day)
max_sum = sum(y for x, y in rg_Day)

if not (min_sum <= sumTime <= max_sum):
    None

result = [x for x,y in rg_Day]
current_sum = min_sum

remaining_needed = sumTime - current_sum

for i in range(len(rg_Day)):    # Greedy distribution
    if remaining_needed <= 0 :
        break

    x_i, y_i = rg_Day[i]
    can_add = y_i - x_i

    to_add = min(remaining_needed, can_add)
    result[i] += to_add
    remaining_needed -= to_add

isEqual = False
sums = 0
for i in result:
    sums += i
    if sums == sumTime:
        isEqual = True

if isEqual:
    s_result = ""
    for i in result:
        s_result += str(i)
        s_result += " "

    print("YES")
    print(s_result)
else:
    print("NO")





