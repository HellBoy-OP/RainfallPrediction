import pickle

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# read the dataset
data = pd.read_csv("rainfall.csv")

# get the columns with missing values
numeric_cols = data.select_dtypes(include=[np.number]).columns
means = data[numeric_cols].mean()

# fill the missing values with the mean of the column
data[numeric_cols] = data[numeric_cols].fillna(means)

# group the data by SUBDIVISION
group = data.groupby("SUBDIVISION")[
    ["YEAR", "JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
]

# subdivisions = data["SUBDIVISION"].unique().tolist()

# get the data for GANGETIC WEST BENGAL
data = group.get_group(("GANGETIC WEST BENGAL"))

# melt the data
df = data.melt(["YEAR"]).reset_index()

# rename the columns
df = df[["YEAR", "variable", "value"]].reset_index().sort_values(by=["YEAR", "index"])

df.columns = ["Index", "Year", "Month", "Avg_Rainfall"]
Month_map = {
    "JAN": 1,
    "FEB": 2,
    "MAR": 3,
    "APR": 4,
    "MAY": 5,
    "JUN": 6,
    "JUL": 7,
    "AUG": 8,
    "SEP": 9,
    "OCT": 10,
    "NOV": 11,
    "DEC": 12,
}
df["Month"] = df["Month"].map(Month_map)

df.drop(columns="Index", inplace=True)

X = np.asanyarray(df[["Year", "Month"]]).astype("int")
y = np.asanyarray(df["Avg_Rainfall"]).astype("int")

# split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=10
)

# create the model
random_forest_model = RandomForestRegressor(
    max_depth=100,
    max_features="sqrt",
    min_samples_leaf=4,
    min_samples_split=10,
    n_estimators=800,
)
random_forest_model.fit(X_train, y_train)

# save the model
file = open("model.pkl", "wb")
pickle.dump(random_forest_model, file)
file.close()
