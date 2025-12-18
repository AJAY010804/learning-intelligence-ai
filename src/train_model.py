import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

# Load data
data = pd.read_csv("data/learner_data.csv")

# Features and target
X = data[['time_spent', 'score']]
y = data['completed']

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model
with open("model/completion_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved successfully")