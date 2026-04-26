import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load dataset
df = pd.read_csv("IPL2025Bowlers.csv")

# Step 2: Clean column names
df.columns = df.columns.str.strip().str.title()

# Step 3: Identify columns
team_col = "Team"
runs_col = "Runs"

# Auto-detect numeric column if "Runs" not found
if runs_col not in df.columns:
    numeric_cols = df.select_dtypes(include=['int64','float64']).columns
    runs_col = numeric_cols[0]   # pick first numeric column

# Step 4: Group by Team and sort
team_runs = df.groupby(team_col)[runs_col].sum().reset_index()
team_runs = team_runs.sort_values(by=runs_col, ascending=False)


print("\nSorted Teams by Runs:")
print(team_runs.head(10))

# Step 5: Visualization (FutureWarning fix)
sns.set(style="whitegrid")
plt.figure(figsize=(10,6))
sns.barplot(
    x=runs_col,
    y=team_col,
    data=team_runs.head(10),
    hue=team_col,        # assign hue to team
    legend=False,        # hide redundant legend
    palette="viridis"
)
plt.title("Top 10 Teams by Runs - IPL 2025", fontsize=16)
plt.xlabel("Total Runs")
plt.ylabel("Team")
plt.show()

