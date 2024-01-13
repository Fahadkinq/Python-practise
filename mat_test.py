import matplotlib.pyplot as plt
import pandas as pd

url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df=pd.read_csv(url , names=headers)

x=df["engine-size"]
y=df["price"]

plt.scatter(x,y)

plt.title("scatterplot of Engine Size VS  Price")
plt.xlabel("Engine Size")
plt.xlabel("price")

plt.grid(True)
plt.show()