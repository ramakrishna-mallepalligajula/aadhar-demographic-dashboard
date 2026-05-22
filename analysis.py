import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("aadhar_data.csv")

# First 5 rows
print(df.head())

# Dataset info
print(df.info())

# Missing values
print(df.isnull().sum())

# Shape
print("Rows and Columns:", df.shape)


# Total population in each age group

print("Children (0-5):", df["age_0_5"].sum())
print("Teenagers (5-17):", df["age_5_17"].sum())
print("Adults (18+):", df["age_18_greater"].sum())

# District wise adult population

district_population = df.groupby("district")["age_18_greater"].sum()
print(district_population.sort_values(ascending=False).head(10))

#total population

df["total_population"] = (
    df["age_0_5"] +
    df["age_5_17"] +
    df["age_18_greater"]
)
print(df.head())

#top populated by District 
top_districts = df.groupby("district")["total_population"].sum()
print(top_districts.sort_values(ascending=False).head(10))

#data visualization
df["date"] = pd.to_datetime(df["date"], dayfirst=True)
top_districts.sort_values(ascending=False).head(10).plot(kind="bar")
plt.title("Top 10 Districts by Population")
plt.xlabel("District")
plt.ylabel("Population")
plt.show()

# Top 10 populated districts

top_districts = (
    df.groupby("district")["total_population"]
    .sum()
    .sort_values(ascending=False)
)

print(top_districts.head(10))

#top pin codes

top_pincodes = (
    df.groupby("pincode")["total_population"]
    .sum()
    .sort_values(ascending=False)
)

print(top_pincodes.head(10))

#age distribution analysis

age_groups = {
    "0-5": df["age_0_5"].sum(),
    "5-17": df["age_5_17"].sum(),
    "18+": df["age_18_greater"].sum()
}

print(age_groups)

import matplotlib.pyplot as plt

plt.pie(
    age_groups.values(),
    labels=age_groups.keys(),
    autopct="%1.1f%%"
)

plt.title("Population Age Distribution")

plt.show()

# District with highest adult population

adult_population = (
    df.groupby("district")["age_18_greater"]
    .sum()
    .sort_values(ascending=False)
)

print("Highest adult population district:")
print(adult_population.head(1))

df.to_csv("processed_aadhar_data.csv", index=False)