import pandas as pd
import numpy as np

# Creating a DataFrame
data = {
    "name": ["keshav", "paras", "lovnish"],
    "age": [19, 18, 17],
    "salary": [200000, 1000000, 300000]
}

df = pd.DataFrame(data)
print(df)

# Reading data from files (requires openpyxl for Excel files)
d1 = pd.read_csv("./pandas/sample.csv")
print(d1)
d2 = pd.read_excel("./pandas/sample2.xlsx")
print(d2)

# Exploring data in pandas
df = pd.read_excel("./pandas/random1.xlsx")
print(df.head(10))  # First 10 rows
print(df.tail(10))  # Last 10 rows

# Getting information about data
print(df.info())

# Getting statistics of numerical columns
print(df.describe())

# Checking for null values
print(df.isnull())
print(df.isnull().sum())

# Selecting specific columns and modifying data
df.loc[(df["Age"]) >= 40, "Experience"] = "senior"
df.loc[(df["Age"]) < 40, "Experience"] = "junior"
print(df.head(20))

# Adding a calculated column
df["Bonus"] = (df["Salary"] / 100) * 20
print(df.head(20))

# Working with Series and DataFrames
age = df["Age"]
print(type(df["Age"]))  # <class 'pandas.core.series.Series'>

abc = df[["Age", "Gender"]]
print(type(df[["Age", "Gender"]]))  # <class 'pandas.core.frame.DataFrame'>

# Filtering data
above_40 = df[df["Age"] > 40]
above_40_name = df.loc[df["Age"] > 40, "Name"]
print(above_40)
print(above_40_name)
print(above_40.shape)

# Handling missing data
a = df[df["Age"].notna()]
print(a)

# Slicing data with iloc
a = df.iloc[9:25, 2:5]
b = df.iloc[9, :]
print(a)
print(b)

# Changing data
df.iloc[1, 0] = "keshav"
print(df.loc[1, :])

# Using map for data transformation
data = {"month": ["january", "february", "march", "april"]}
a = pd.DataFrame(data)

def extract(value):
    return value[0:3]

a["Short_name"] = a["month"].map(extract)
print(a)

# Dealing with duplicate data
df = pd.read_excel("./pandas/random1.xlsx")
print(df.duplicated())
print(df["Age"].duplicated())
print(df["Age"].duplicated().sum())
print(df.drop_duplicates("Job Title"))

# Working with missing data
df = pd.read_excel("./pandas/random1.xlsx")
print(df.isnull().sum())
print(df.replace(np.nan, "hi"))

meanSalary = df["Salary"].mean()
df["Salary"] = df["Salary"].replace(np.nan, meanSalary)
print(df)

# Group by operations
df = pd.read_excel("./pandas/random1.xlsx")
print(df.head())

gf = df.groupby(["Job Title", "Gender"]).agg({"Name": "count"})
gp1 = df.groupby("Job Title").agg({"Salary": "max"})
print(gf)
print(gp1)

# Merge, join, and concatenate in pandas
data1 = {
    "Emp Id": ["E01", "E02", "E03", "E04", "E05"],
    "Names": ["keshav", "paras", "love", "ansh", "aryan"],
    "Age": [17, 17, 18, 7, 11]
}
data2 = {
    "Emp Id": ["E01", "E02", "E03", "E04", "E05"],
    "Salary": [1000000, 100000, 1000000, 23450, 23242]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print(pd.merge(df1, df2, on="Emp Id"))

data1 = {
    "Emp Id": ["E01", "E07", "E03", "E04", "E09"],
    "Names": ["keshav", "paras", "love", "ansh", "aryan"],
    "Age": [17, 17, 18, 7, 11]
}
data2 = {
    "Emp Id": ["E01", "E02", "E03", "E08", "E05"],
    "Salary": [1000000, 100000, 1000000, 23450, 23242]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print(pd.merge(df1, df2, on="Emp Id", how="outer"))
print(pd.merge(df1, df2, on="Emp Id", how="inner"))
print(pd.merge(df1, df2, on="Emp Id", how="right"))
print(pd.merge(df1, df2, on="Emp Id", how="left"))

# Comparing DataFrames
data = {
    "Thing": ["pen", "laptop", "charger"],
    "price": [100, 100000, 10000],
    "quantity": [10, 1, 3]
}

df1 = pd.DataFrame(data)
df2 = df1.copy()
df2.loc[0, "price"] = 200
df2.loc[1, "price"] = 1200000
df2.loc[2, "price"] = 120000
df2.loc[0, "quantity"] = 15
df2.loc[2, "quantity"] = 2

print(df1.compare(df2))
print(df1.compare(df2, align_axis=0))
print(df1.compare(df2, keep_equal=True))
print(df1.compare(df2, keep_shape=True))

# Pivoting and melting in pandas
df = pd.DataFrame(
    data={
        "Province": ["ON", "QC", "BC", "AL", "AL", "MN", "ON"],
        "City": [
            "Toronto", "Montreal", "Vancouver", "Calgary", "Edmonton", "Winnipeg", "Windsor"
        ],
        "Sales": [13, 6, 16, 8, 4, 3, 1]
    }
)

table = pd.pivot_table(
    df,
    values=["Sales"],
    index=["Province"],
    columns=["City"],
    aggfunc="sum",
    margins=True,
)
print(table)
print(table.stack("City", future_stack=True))

print(df.melt(id_vars="City", value_vars="Sales"))
