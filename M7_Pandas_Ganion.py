"""
Alicia Ganion
SDEV 220
M7_Pandas
"""

import pandas as pd

#DataFrame
df = pd.read_csv("orders.csv")
print(df)

#prints the first 5 rows
df.head()

#prints the last 5 rows
df.tail()

#prints general information about df
df.info()

#prints descriptive statistics
df.describe()

#list of columns
df.columns

#gives range
df.index

#all of the values in the column - index all values in country column
df["Country"]

#print length
len(df["Country"])

#print all unique values
set(df["Country"])

#prints country and product columns
df[["Country", "Product"]]

#index location - in this instance the first row (or 0)
df.iloc[0]

#converts to list and prints values
list(df.iloc[10])

df.iloc[10][0]

#gives row value of Country
df.iloc[10]["Country"]

df.iloc[10]["Shipped"]

df.head()

#all products in electronics category
df[df["Category"] == "Electronics"]

#gives both products = electronics and country = USA
df[(df["Category"] == "Electronics") & (df["Country"] == "USA")]

#gives all products = electronics OR country = USA
df[(df["Category"] == "Electronics") | (df["Country"] == "USA")]

#lists all quantity greater than 20
df[df["Quantity"] > 20]

#lists all quantity greater than 2
df[df["Quantity"] > 2]

#lists all quantity less than 2
df[df["Quantity"] < 2]

#lists all quantity less than or equal to 2
df[df["Quantity"] <= 2]


#lists all quantity not = 2
df[df["Quantity"] != 2]

#lists all customer names starting with A
df[df["CustomerName"].str.startswith("A")]

#lists all customer names ending with a
df[df["CustomerName"].str.endswith("a")]

#lists any country with USA, Sweden, Brazil
df[df["Country"].isin(["USA", "Sweden", "Brazil"])]

#lists any country NOT USA, Sweden, Brazil
df[~df["Country"].isin(["USA", "Sweden", "Brazil"])]

#changing product name to Time
df.loc[df["CustomerName"] == "Anna Ivanova", "Product"] = "Tim"

#looking at Anna
df.loc[df["CustomerName"] == "Anna Ivanova"]

#all countries named USA changed to United States
df.loc[df["Country"] == "USA", "Country"] = "United States"

#looking at United States
df.loc[df["Country"] == "United States"]

#all of countries changed to upper case
df["Country"] = df["Country"].str.upper()

#look at upper case countries
df["Country"]

#drop row at index 39
df = df.drop(39)

#drop na values
df.dropna()

#fill na values
df.fillna({"OrderID": 0}, inplace=True)

#rename columns
df.rename(columns={"OrderID": "Order ID"}, inplace=True)

#count of every single value that exists in country
df["Country"].value_counts()

#sum total price of all products grouped by country
df.groupby("Country")["Price"].sum()

#sort prices by descending values
df.sort_values("Price", ascending=False)

#save to new spreadsheet -- does NOT include index
df.to_csv("new_file.csv", index=False)
