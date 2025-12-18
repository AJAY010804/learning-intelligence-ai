def detect_risk(probability, score):
    if probability < 0.4 or score < 40:
        return "High Risk"
    elif probability < 0.6:
        return "Medium Risk"
    else:
        return "Low Risk"


def chapter_difficulty(time_spent, score):
    if time_spent > 90 and score < 50:
        return "Hard"
    elif time_spent > 60:
        return "Medium"
    else:
        return "Easy"


def generate_insights(time_spent, score, risk):
    insights = []

    if score < 40:
        insights.append("Low assessment score indicates learning difficulty")

    if time_spent > 90:
        insights.append("High time spent suggests content complexity")

    if risk == "High Risk":
        insights.append("Immediate mentor intervention recommended")

    return insights