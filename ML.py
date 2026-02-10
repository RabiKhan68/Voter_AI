import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv("voters.csv")

# Map categorical values
data["Income"] = data["Income"].map({"Low": 0, "Medium": 1, "High": 2})
data["Education"] = data["Education"].map({"HighSchool": 0, "College": 1, "Graduate": 2})

# Optional: check missing values
print(data.isnull().sum())

X = data[["Age", "Income", "Education"]]
y = data["Party_Voted"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

print("Training accuracy:", model.score(X_train, y_train))
print("Test accuracy:", model.score(X_test, y_test))

joblib.dump(model, "model.pkl")
print("Model trained and saved as model.pkl")