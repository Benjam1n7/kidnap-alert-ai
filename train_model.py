import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
import pickle

df = pd.read_csv("data.csv")
encoder = LabelEncoder()
df["police_presence"] = encoder.fit_transform(df["police_presence"])
X = df[["incidents", "last_30_days", "police_presence"]]
y = [1 if i > 40 else 0 for i in df["incidents"]]
model = LogisticRegression()
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model.pkl")
