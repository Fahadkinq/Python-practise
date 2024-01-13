import pandas as pd

url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df=pd.read_csv(url , names=headers)

print("Data of top 5 Values:")
print(df.head(5))

print("Data of bottom 5 Values:")
print(df.tail(5))

print("Statistical evaluation:")
print(df.describe(include="all"))

column_name= "make"

data_type= df[column_name].dtype

print(f"Data type of column '{column_name}' : {data_type}/n")

clean_data=df.dropna(subset=["normalized-losses"])
print(f"Data after Clereaning'{clean_data}':")

