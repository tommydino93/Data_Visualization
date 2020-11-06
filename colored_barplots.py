import matplotlib.pyplot as plt

"""The data for this barplot was taken from the website OurWorldInData"""

# define input data
countries = ["Italy", "Mexico", "South_Africa", "Japan"]
life_expectancies = [83.5, 75.1, 64.1, 84.6]

# create barplot
plt.bar(countries, life_expectancies, color=['green', 'blue', 'yellow', 'purple'])
# set label for x axis
plt.xlabel("Countries", fontsize=12)
# set label for y axis
plt.ylabel("Years", fontsize=12)
# set title
plt.title("Life expectancy (data from 2019)", weight="bold", fontsize=15)

plt.show()
