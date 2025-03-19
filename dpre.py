import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load dataset
df = pd.read_csv("top_rated_movies(tmdb).csv")

# Data Cleaning: Drop rows with missing release_date
print(df.isna().sum())
df.dropna(subset=["release_date"], inplace=True)

# Check correlation before column reduction (only numeric columns)
print(df.select_dtypes(include=["number"]).corr())

# Data Reduction: Keep relevant columns based on correlation analysis
df = df[["title", "release_date", "popularity", "vote_average", "vote_count"]]

# Normalize popularity column
scaler = MinMaxScaler()
df["popularity_scaled"] = scaler.fit_transform(df[["popularity"]])

# Data Discretization: Categorize vote_average
bins = [0, 5, 7.5, 10]  # Ranges for Low, Medium, High
labels = ["Low", "Medium", "High"]
df["rating_category"] = pd.cut(
    df["vote_average"], bins=bins, labels=labels, include_lowest=True
)

# Save processed dataset
df.to_csv("res_dpre.csv", index=False)

# Proceed to the next step
exec(open("eda.py").read())
