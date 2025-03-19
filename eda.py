import pandas as pd

# Load the processed dataset
df = pd.read_csv("res_dpre.csv")

# Insight 1: Average rating per year
average_rating_per_year = df.groupby(df["release_date"].str[:4])["vote_average"].mean()
average_rating_per_year.to_csv("eda-in-1.txt")

# Insight 2: Top 10 movies by popularity
top_10_popular = df.nlargest(10, "popularity")
top_10_popular[["title", "popularity"]].to_csv("eda-in-2.txt", index=False)

# Insight 3: Number of movies per rating category
rating_counts = df["rating_category"].value_counts()
rating_counts.to_csv("eda-in-3.txt")

print(
    "Exploratory Data Analysis completed and saved as eda-in-1.txt, eda-in-2.txt, eda-in-3.txt"
)

# Proceed to the next step
exec(open("vis.py").read())
