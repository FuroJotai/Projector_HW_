import matplotlib.pyplot as plt
import pandas as pd

url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv'
df = pd.read_csv(url)

teams = df['Team']
passing_accuracy = df['Passing Accuracy'].str.replace('%', '').astype(float)
goals = df['Goals']
crosses = df['Crosses']

fig, axs = plt.subplots(1, 2, figsize = (18, 8))

axs[0].scatter(passing_accuracy, goals, color = 'blue', marker = 'o')
for i, team in enumerate(teams):
    axs[0].text(passing_accuracy[i], goals[i], team, fontsize = 9)
    axs[0].set_xlabel('Passing Accuracy (%)')
    axs[0].set_ylabel('Goals')
    axs[0].set_title('Relation between Passing Accuracy and Goals at Euro 2012')
    axs[0].grid(True)


axs[1].scatter(crosses, goals, color = 'green', marker = 'o')
for i, team in enumerate(teams):
    axs[1].text(crosses[i], goals[i], team, fontsize = 9)
    axs[1].set_xlabel('Crosses')
    axs[1].set_ylabel('Goals')
    axs[1].set_title('Relation between Crosses and Goals at Euro 2012')
    axs[1].grid(True)    



fig.text(0.5, 0.02, 'Spain won Euro2012 keeping balance between ball control and crosses', 
         ha = 'center', fontsize = 12, color = 'black')


plt.tight_layout(pad = 4.0)
plt.show()

