import csv


with open('game_scores.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  
    scores = {}
    for row in reader:
        scores[row[0]] = int(row[1])


max_scores = {}
for player, score in scores.items():
    if player not in max_scores or score > max_scores[player]:
        max_scores[player] = score

sorted_scores = sorted(max_scores.items(), key=lambda x: x[1], reverse=True)

with open('high_scores.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Player name', 'Highest score'])
    for player, score in sorted_scores:
        writer.writerow([player, score])

print("High scores have been saved to high_scores.csv")
