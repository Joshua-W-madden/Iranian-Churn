import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("Customer Churn.csv")

dataset = dataset.drop(["Age", "Customer Value"], axis=1) # removes redundant catagory
target = dataset["Churn"] #saves target values
dataset = dataset.drop("Churn",axis=1) # removes churn 
exclude_cols = ["Age Group","Status", "Tariff Plan", "Complains" ]

dataset["Tariff Plan"] = dataset["Tariff Plan"].replace(2, 0)
dataset["Status"] = dataset["Status"].replace(2, 0) #sets the binary values to 1,0 for tariff plan and statys
# Select only numeric columns to normalize
cols_to_normalize = dataset.columns.difference(exclude_cols)

# Apply Z-score normalization
dataset[cols_to_normalize] = (dataset[cols_to_normalize] - dataset[cols_to_normalize].mean()) / dataset[cols_to_normalize].std()


"""
creates 2 new csv
dataset.to_csv("cleanedNonC.csv", index=False) 
target.to_csv("cleanedChurn.csv", index=False)
"""
fig, axes = plt.subplots(4, 3, figsize=(15, 10))
axes = axes.flatten()
for i, col in enumerate(dataset.columns):
    if i == exclude_cols:
        non_counts = dataset[col].value_counts().sort_index()
        churn_counts = target.value_counts().sort_index()

        all_categories = sorted(set(non_counts.index) | set(churn_counts.index))

        non_counts = non_counts.reindex(all_categories, fill_value=0)
        churn_counts = churn_counts.reindex(all_categories, fill_value=0)
        
        x = range(len(non_counts))
        axes[i].bar(x, non_counts.values, label="Not churned")
        axes[i].bar(x, churn_counts.values, label="Churned")
        axes[i].set_xticks(x)      
    else: 
        axes[i].hist([dataset[col], target], label=["Not churned", "Churned"])
    axes[i].set_title(col)
    axes[i].legend()

fig.delaxes(axes[11])
plt.tight_layout()
plt.show()
