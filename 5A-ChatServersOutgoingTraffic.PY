
traffic = 0
online_count = 0
start = True
names = []
while True:
    line = input().strip()
    if not line:
        continue

    if line[0] == '+':
        online_count += 1
        names.append(line[1:])
        start = False
    elif line[0] == '-':
        online_count -= 1
        names.remove(line[1:])
    else:
        message = line.split(':', 1)[1]
        traffic += len(message) * online_count

    print(traffic)
