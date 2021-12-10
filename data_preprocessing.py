import numpy as np
import pandas as pd

df = pd.read_csv("stroke.csv")
# Determine if missing patterns exist
df.apply(lambda x: sum(x.isnull()), axis=0)
bmi_mean = np.mean(df["bmi"])
target = df["bmi"][1]
for index in range(0, len(df["bmi"])):
    if df["bmi"][index] == target:
        df["bmi"][index] = bmi_mean

print(df)
