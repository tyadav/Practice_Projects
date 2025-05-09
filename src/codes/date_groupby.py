#Import library
import pandas as pd

df = pd.DataFrame({"date":["3-15-22", "3-16-22","3-22-22"],
                   "price": [2,3,4]})

df["date"] = pd.to_datetime(df["date"])
print(df)

df1 = df.groupby(pd.Grouper(key="date",freq="1W")).mean()
print(df1)
