import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": [22, 25, 30, 28],
    "Score": [85, 90, 78, 95]
}

df = pd.DataFrame(data)

print(df)
print("\nAverage score:", df["Score"].mean())
