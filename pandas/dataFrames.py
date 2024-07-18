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
# print(df.isnull())
# print(df.isnull().sum())

# select specific columns

# age = df["Age"]
# # print(age)
# print(type(df["Age"])) #output --> <class 'pandas.core.series.Series'>

# abc = df[["Age","Gender"]]
# print(abc)
# print(type(df[["Age","Gender"]]))#output --> <class 'pandas.core.frame.DataFrame'>

# above_40 = df[df["Age"]>40]
# above_40_name =df.loc[df["Age"]>40,"Name"]
# print(above_40)
# print(above_40_name)
# print(above_40.shape)

# a= df[df["Age"].notna()]
# print(a)

# a=df.iloc[9:25, 2:5]
# b=df.iloc[9,:]
# print(a)
# df.iloc[1,0]="keshav"        changing data
# print(df.loc[1,:])
# print(b)