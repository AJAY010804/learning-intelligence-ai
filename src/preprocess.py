def preprocess_input(data):
    required_fields = ["student_id", "course_id", "chapter_id", "time_spent", "score"]

    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing field: {field}")

    return data