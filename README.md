# Learning Intelligence AI Tool

## Overview

The **Learning Intelligence AI Tool** is a production-ready AI system designed to analyze learner behavior and generate predictive insights for mentors and administrators on an internship or training platform.

Unlike notebook-based experiments, this project delivers a **fully executable AI tool** exposed through a REST API, integrating machine learning into a real-world software pipeline.

---

## Key Capabilities

* ✅ Course completion prediction (ML-based)
* ⚠️ Early dropout risk detection
* 📚 Chapter difficulty identification
* 🧠 Human-readable insights for mentors
* 🌐 REST API interface using FastAPI
* 💾 Saved & loaded ML model
* 🧪 Unit-tested prediction logic

---

## AI System Architecture

The system is designed using a modular, production-style architecture:

1. **Input Layer**

   * JSON input via REST API

2. **Preprocessing Layer**

   * Input validation and consistency checks

3. **Feature Engineering**

   * Time spent on chapters
   * Assessment scores

4. **Model Inference**

   * Logistic Regression (binary classification)
   * Model trained offline and loaded during runtime

5. **Insight Generation**

   * Risk categorization
   * Chapter difficulty scoring
   * Actionable recommendations

6. **API Layer**

   * FastAPI-based inference service

---

## Project Directory Structure

```
learning-intelligence-ai/
│
├── app.py                  # FastAPI application entry point
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
│
├── data/
│   └── learner_data.csv    # Sample learner dataset
│
├── model/
│   └── completion_model.pkl  # Trained ML model
│
├── src/
│   ├── __init__.py
│   ├── preprocess.py       # Input validation & preprocessing
│   ├── features.py         # Feature handling (if extended)
│   ├── predict.py          # Model loading & prediction logic
│   ├── insights.py         # Risk, difficulty & insight generation
│   └── train_model.py      # Offline model training script
│
├── tests/
│   ├── __init__.py
│   └── test_basic.py       # Unit tests for prediction logic
│
└── sample_output.json      # Example API output
```

---

## Technology Stack

* Python 3
* FastAPI
* Scikit-learn
* Pandas
* NumPy
* Pytest

---

## Machine Learning Details

* **Model Type:** Logistic Regression
* **Problem Type:** Binary Classification
* **Target Variable:** Course completion (Complete / Dropout)

### Features Used

* Time spent on chapter
* Assessment score

The trained model is saved as a `.pkl` file and loaded during inference to ensure reproducibility.

---

## Input Format (API Request)

```json
{
  "student_id": 101,
  "course_id": "DS101",
  "chapter_id": 2,
  "time_spent": 120,
  "score": 35
}
```

---

## Output Format (API Response)

```json
{
  "student_id": 101,
  "course_id": "DS101",
  "prediction": "Likely to Drop Out",
  "completion_probability": 0.12,
  "risk_level": "High Risk",
  "chapter_difficulty": "Hard",
  "insights": [
    "Low assessment score indicates learning difficulty",
    "High time spent suggests content complexity",
    "Immediate mentor intervention recommended"
  ]
}
```

---

## How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/AJAY010804/learning-intelligence-ai.git
cd learning-intelligence-ai
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the Model

```bash
python src/train_model.py
```

### 4. Start the API Server

```bash
uvicorn app:app --reload
```

### 5. Test the Tool

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## Testing

Core prediction logic is validated using unit tests.

Run tests:

```bash
pytest
```

---

## AI Usage Disclosure

AI tools (including ChatGPT) were used to assist in project structuring and documentation refinement.
All machine learning logic, feature engineering, model training, system design, testing, and validation were implemented and verified independently.

---

## Ethical Considerations

* No personal or sensitive data is used
* Predictions are interpretable and transparent
* Outputs support human decision-making, not replace it

---

## Author

**Ajay Yemmewar**
