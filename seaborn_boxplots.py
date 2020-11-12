import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(123)  # set random seed for reproducibility

# we have three groups of individuals and we want to compare their weights

weights_group_1 = np.random.uniform(low=50, high=90, size=10)  # kg
weights_group_2 = np.random.uniform(low=50, high=90, size=10)  # kg
weights_group_3 = np.random.uniform(low=50, high=90, size=10)  # kg

# convert np.arrays to dictionaries
d_weights_1 = {"weights_1": weights_group_1}
d_weights_2 = {"weights_2": weights_group_2}
d_weights_3 = {"weights_3": weights_group_3}

# convert dictionaries to pandas Dataframe
df_weights_1 = pd.DataFrame(d_weights_1)
df_weights_2 = pd.DataFrame(d_weights_2)
df_weights_3 = pd.DataFrame(d_weights_3)

# concatenate Dataframes into one unique Dataframe
merged_df = pd.concat([df_weights_1, df_weights_2, df_weights_3], ignore_index=True, axis=1)
merged_df.columns = ["group_1", "group_2", "group_3"]  # assign names to columns

# create boxplots
_ = sns.boxplot(data=merged_df)
# set ylabel
plt.ylabel("[kg]", fontsize=12)
# set bold title
plt.title("Weight", weight="bold", fontsize=15)
# set y axis values
plt.yticks(np.arange(45, 95, 5))
# show horizontal gridlines
plt.grid(axis='y', linestyle='-')
plt.show()
