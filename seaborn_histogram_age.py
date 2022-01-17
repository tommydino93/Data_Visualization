import random
import seaborn as sns
import matplotlib.pyplot as plt

# This script plots a histogtam of randomly generated ages with seaborn

random_ages = []  # create empty list

# generate 200 invented ages of people
for i in range(200):
  random_ages.append(random.randint(0,100))  # assume the age is between 0 and 100 years

# plot histogram of ages
ax = sns.histplot(random_ages)
# set xlabel
ax.set_xlabel("age", fontsize=12)
# set ylabel
ax.set_ylabel("count", fontsize=12)
# set bold title
ax.set_title("Age histogram", weight="bold", fontsize=15)
plt.show()
