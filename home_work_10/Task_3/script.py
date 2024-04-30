import random
import csv


players = ["Josh", "Luke", "Kate", "Mark", "Mary"]


with open('game_scores.csv', 'w', newline='') as csvfile:
    fieldnames = ['Player name', 'Score']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for player in players:
        for _ in range(100):
            writer.writerow({'Player name': player, 'Score': random.randint(0, 1000)})
