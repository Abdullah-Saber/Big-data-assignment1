import pandas as pd
import matplotlib.pyplot as plt

# Load the processed dataset
df = pd.read_csv("res_dpre.csv")

# Count the number of movies in each rating category
rating_counts = df["rating_category"].value_counts()

# Create a bar chart
plt.figure(figsize=(8, 5))
rating_counts.plot(kind="bar", color=["red", "orange", "green"])

# Add labels and title
plt.xlabel("Rating Category")
plt.ylabel("Number of Movies")
plt.title("Distribution of Movies by Rating Category")

# Save the figure
plt.savefig("vis.png")

print("Visualization saved as vis.png")

# Proceed to the next step
exec(open("model.py").read())
