import pickle
import numpy as np

# Load trained model
with open("model/completion_model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_completion(time_spent, score):
    X = np.array([[time_spent, score]])
    probability = model.predict_proba(X)[0][1]

    if probability >= 0.6:
        return "Likely to Complete", probability
    else:
        return "Likely to Drop Out", probability
    
    