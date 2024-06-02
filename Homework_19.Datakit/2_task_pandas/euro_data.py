import pandas as pd

url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv"

euro_data = pd.read_csv(url)


# 1. Find team with yellow and red cards
condition_cards = (euro_data['Red Cards'] & euro_data['Yellow Cards'] > 0)
team_with_cards = euro_data.loc[condition_cards, 'Team']
print(team_with_cards)


# 2. Quantity of Euro2012 participants

participants = euro_data['Team'].nunique()
print(str(participants) + " " + "teams participated in Euro 2012")


# 3. Teams that scored more than 6 goals

more_than_six_goals = (euro_data['Goals'] > 6)
teams_more_than_six_goals = euro_data.loc[more_than_six_goals, 'Team']

print(teams_more_than_six_goals)