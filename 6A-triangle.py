
# # 18/12/2025 Below was my solutions

# lengths = [7,2,2,4]

# highest_side = max(lengths)
# lowest_side = min(lengths)

# greater_than_highest_side = 0
# for side in lengths:
#     if side > lowest_side and side < highest_side:
#         greater_than_highest_side += side

# if highest_side + lowest_side > greater_than_highest_side and greater_than_highest_side + lowest_side > highest_side and greater_than_highest_side + highest_side > lowest_side:
#     print("TRIANGLE")
# elif greater_than_highest_side == highest_side + lowest_side:
#     print("SEGMENT")
# else:
#     print("IMPOSSIBLE")


# Actual solutoins are the following
sticks = sorted(list(map(int, input().split())))

a,b,c,d = sticks

if (a+b>c) or (b+c>d):
    print("TRIANGLE")
elif (a+b == c) or (b+c == d):
    print("SEGMENT")
else:
    print("IMPOSSIBLE")

