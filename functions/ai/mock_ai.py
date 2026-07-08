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

        policy_file = os.path.join(
            current_dir,
            "..",
            "..",
            "resources",
            "policy.json"
        )

        with open(keyword_file, "r") as file:
            self.keywords = json.load(file)

        with open(regex_file, "r") as file:
            self.regex_patterns = json.load(file)

        with open(policy_file, "r") as file:
            self.policy = json.load(file)

    def classify(self, prompt, sanitize=False):

        detected_categories = []
        sanitized_prompt = prompt

        keyword_hits = 0
        regex_hits = 0

        # ----------------------------------
        # Keyword Detection
        # ----------------------------------
        for category, words in self.keywords.items():

            for word in words:

                if word.lower() in prompt.lower():

                    keyword_hits += 1

                    if category not in detected_categories:
                        detected_categories.append(category)

        # ----------------------------------
        # Regex Detection + Sanitization
        # ----------------------------------
        for category, pattern in self.regex_patterns.items():

            matches = re.findall(pattern, sanitized_prompt)

            if matches:

                regex_hits += len(matches)

                if category not in detected_categories:
                    detected_categories.append(category)

                if sanitize:

                    if category == "PASSWORD":

                        sanitized_prompt = re.sub(
                            pattern,
                            lambda m: m.group(0).replace(
                                m.group(1),
                                "[PASSWORD]"
                            ),
                            sanitized_prompt
                        )

                    else:

                        sanitized_prompt = re.sub(
                            pattern,
                            lambda m: m.group(0).replace(
                                m.group(1),
                                f"[{category}]"
                            ),
                            sanitized_prompt
                        )

        # ----------------------------------
        # Risk Calculation using Policy Engine
        # ----------------------------------
        highest_score = 0
        risk = "LOW"
        decision = "ALLOW"

        for category in detected_categories:

            if category in self.policy:

                category_policy = self.policy[category]

                if category_policy["risk_score"] > highest_score:

                    highest_score = category_policy["risk_score"]
                    risk = category_policy["risk"]
                    decision = category_policy["action"]

        # ----------------------------------
        # Confidence Calculation
        # ----------------------------------
        confidence = min(
            100,
            regex_hits * 35 +
            keyword_hits * 15
        )

        # ----------------------------------
        # Final Response
        # ----------------------------------
        if detected_categories:

            if sanitize:
                decision = "SANITIZE"

            return {

                "risk": risk,

                "risk_score": highest_score,

                "confidence": confidence,

                "decision": decision,

                "contains_pii": True,

                "categories": detected_categories,

                "reason": f"Detected: {', '.join(detected_categories)}.",

                "sanitized_prompt":
                    sanitized_prompt if sanitize else ""

            }

        return {

            "risk": "LOW",

            "risk_score": 0,

            "confidence": 0,

            "decision": "ALLOW",

            "contains_pii": False,

            "categories": [],

            "reason": "No sensitive information detected.",

            "sanitized_prompt": ""

        }