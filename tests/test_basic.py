from src.predict import predict_completion

def test_prediction_output():
    prediction, prob = predict_completion(120, 30)
    assert prediction in ["Likely to Complete", "Likely to Drop Out"]
    assert 0 <= prob <= 1