from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.preprocess import preprocess_input
from src.predict import predict_completion
from src.insights import detect_risk, chapter_difficulty, generate_insights

app = FastAPI(title="Learning Intelligence AI Tool")


class LearnerInput(BaseModel):
    student_id: int
    course_id: str
    chapter_id: int
    time_spent: int
    score: int


@app.post("/predict")
def predict(data: LearnerInput):
    try:
        input_data = preprocess_input(data.dict())

        prediction, probability = predict_completion(
            input_data["time_spent"], input_data["score"]
        )

        risk = detect_risk(probability, input_data["score"])
        difficulty = chapter_difficulty(
            input_data["time_spent"], input_data["score"]
        )

        insights = generate_insights(
            input_data["time_spent"], input_data["score"], risk
        )

        return {
            "student_id": input_data["student_id"],
            "course_id": input_data["course_id"],
            "prediction": prediction,
            "completion_probability": round(probability, 2),
            "risk_level": risk,
            "chapter_difficulty": difficulty,
            "insights": insights
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))