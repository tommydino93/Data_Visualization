import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(123)  # set random seed for reproducibility

weight_subject_1 = np.random.uniform(low=50, high=90, size=10)  # kg
weight_subject_2 = np.random.uniform(low=50, high=90, size=10)  # kg
weight_subject_3 = np.random.uniform(low=50, high=90, size=10)  # kg

# convert lists to dictionaries
d_weight_1 = {"weight_1": weight_subject_1}
d_weight_2 = {"weight_2": weight_subject_2}
d_weight_3 = {"weight_3": weight_subject_3}

# convert dictionaries to pandas Dataframe
df_weight_1 = pd.DataFrame(d_weight_1)
df_weight_2 = pd.DataFrame(d_weight_2)
df_weight_3 = pd.DataFrame(d_weight_3)

# concatenate Dataframes into one unique Dataframe
merged_df = pd.concat([df_weight_1, df_weight_2, df_weight_3], ignore_index=True, axis=1)
merged_df.columns = ["sub_1", "sub_2", "sub_3"]  # assign names to columns

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
