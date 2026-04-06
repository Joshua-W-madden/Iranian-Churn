import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("Customer Churn.csv")

churn = dataset[dataset["Churn"] == 1]
non_churn = dataset[dataset["Churn"] == 0]

fig, axes = plt.subplots(4,3, figsize=(15, 10))
axes = axes.flatten()  # turns the 3d array into 2d for faster processing

columns = [
    "Call  Failure",
    "Complains",
    "Subscription  Length",
    "Charge  Amount",
    "Seconds of Use",
    "Frequency of use",
    "Frequency of SMS",
    "Distinct Called Numbers",
    "Age Group",
    "Tariff Plan",
    "Status"
]

#debugging and new information 1 (check readme)
"""
for i, col in enumerate(columns):
    if i in (1, 7, 9):
        non_counts = non_churn[col].value_counts().sort_index()
        churn_counts = churn[col].value_counts().sort_index()

        all_categories = sorted(set(non_counts.index) | set(churn_counts.index))

        non_counts = non_counts.reindex(all_categories, fill_value=0)
        churn_counts = churn_counts.reindex(all_categories, fill_value=0)
        
        x = range(len(non_counts))
        print("x: ",x, " y: ", y)

"""
for i, col in enumerate(columns):
    if i in (1, 9, 7):
        non_counts = non_churn[col].value_counts().sort_index()
        churn_counts = churn[col].value_counts().sort_index()

        all_categories = sorted(set(non_counts.index) | set(churn_counts.index))

        non_counts = non_counts.reindex(all_categories, fill_value=0)
        churn_counts = churn_counts.reindex(all_categories, fill_value=0)
        if i == 7 :
            x = range(len(non_counts))
            axes[i].bar(x, non_counts.values, label="Not churned")
            axes[i].bar(x, churn_counts.values, label="Churned")
            axes[i].set_xticks(np.arange(min(x), max(x), 5))

        else:
            x = range(len(non_counts))
            axes[i].bar(x, non_counts.values, label="Not churned")
            axes[i].bar(x, churn_counts.values, label="Churned")
            axes[i].set_xticks(x)
    else: 
        axes[i].hist([non_churn[col], churn[col]], label=["Not churned", "Churned"])
    axes[i].set_title(col)
    axes[i].legend()

plt.tight_layout()
plt.show()


