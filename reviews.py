# add your code here
import pandas as pd

reviews = pd.read_csv("data\winemag-data-130k-v2.csv.zip")

country = reviews.country.value_counts()

avg_score = reviews.groupby("country").points.mean().round(decimals=1)

results = pd.DataFrame({'count': country, 'points': avg_score})

final_results = results.sort_values('count', ascending= 0)

final_results.to_csv("reviews-per-country.csv")



