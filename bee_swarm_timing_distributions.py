import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Generate two distributions with different median values
dist1 = np.random.normal(loc=120, scale=10, size=300)
dist2 = np.random.normal(loc=140, scale=10, size=300)

# Draw the bee-swarm plots of the two distributions with the overlayed boxplots
sns.boxplot(data=[dist1, dist2], showfliers=False)
sns.swarmplot(data=[dist1, dist2], color=".25")

# Set the labels
plt.xticks([0, 1], ["Distribution_1", "Distribution_2"], fontsize=12)
# Set y-axis label
plt.ylabel("Seconds (s)", fontsize=12)
# Set the title
plt.title("Distribution of Timings", fontsize=16, fontweight='bold')

# Show the plot
plt.show()
