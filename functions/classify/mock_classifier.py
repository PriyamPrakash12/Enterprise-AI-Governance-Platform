def classify_prompt(prompt):

    sensitive_words = [
        "aadhaar",
        "pan",
        "password",
        "credit card"
    ]

    for word in sensitive_words:
        if word.lower() in prompt.lower():
            return {
                "risk": "HIGH",
                "contains_pii": True,
                "categories": [word.upper()]
            }

    return {
        "risk": "LOW",
        "contains_pii": False,
        "categories": []
    }