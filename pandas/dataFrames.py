import pandas as pd
# data ={
#     "name": [ "keshav", "paras", "lovnish"],
#     "age": [ 19, 18, 17 ],
#     "salary":[ 200000, 1000000, 300000 ]
# }

# creation of dataframe

# df = pd.DataFrame(data)
# print(df)


# we have to downlod openpyxl to open exel files in pandas


# d1=pd.read_csv("./pandas/sample.csv")
# print(d1)
# d2= pd.read_excel("./pandas/sample2.xlsx")
# print(d2)


# exploring data in pandas
df = pd.read_excel("./pandas/random1.xlsx")
# print(df)

# print(df.head(10))
# print(df.tail(10))
# in the both above function head(), tail() is i don't pass any value to it it take 5 as default value

 #get info about data
# print(df.info())

#get all matrix like max, min , median of int valuse only like in our case age and salary
# print(df.describe()) 

# get all null value in data
print(df.isnull())