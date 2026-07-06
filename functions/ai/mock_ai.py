from ai.ai_client import AIClient
import json
import os
import re


class MockAI(AIClient):

    def __init__(self):

        current_dir = os.path.dirname(__file__)

        keyword_file = os.path.join(
            current_dir,
            "..",
            "..",
            "resources",
            "keywords.json"
        )

        regex_file = os.path.join(
            current_dir,
            "..",
            "..",
            "resources",
            "regex_patterns.json"
        )

        with open(keyword_file, "r") as file:
            self.keywords = json.load(file)

        with open(regex_file, "r") as file:
            self.regex_patterns = json.load(file)

    def classify(self, prompt):

        detected_categories = []

        # Keyword detection
        for category, words in self.keywords.items():

            for word in words:

                if word.lower() in prompt.lower():

                    if category not in detected_categories:
                        detected_categories.append(category)

        # Regex detection
        for category, pattern in self.regex_patterns.items():

            if re.search(pattern, prompt):

                if category not in detected_categories:
                    detected_categories.append(category)

        # Final decision
        if detected_categories:

            return {
                "risk": "HIGH",
                "decision": "BLOCK",
                "contains_pii": True,
                "categories": detected_categories,
                "reason": f"Detected: {', '.join(detected_categories)}."
            }

        return {
            "risk": "LOW",
            "decision": "ALLOW",
            "contains_pii": False,
            "categories": [],
            "reason": "No sensitive information detected."
        }