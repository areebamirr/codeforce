
n = int(input())

rounds = []
for _ in range(n):
    name, score = input().split()
    score = int(score)
    rounds.append((name, score))

final_scores = {}

for name, score in rounds:
    if name not in final_scores:
        final_scores[name] = 0
    final_scores[name] += score

max_score = max(final_scores.values())

candidates = []

for name, total in final_scores.values():
    if total == max_score:
        candidates.append(name)

current_scores = {}
winner = None

for name, score in rounds:
    if name not in current_scores:
        current_scores[name] = 0
    current_scores[name] += score

    if name in candidates and current_scores[name] >= max_score:
        winner = name
        break

print(winner)