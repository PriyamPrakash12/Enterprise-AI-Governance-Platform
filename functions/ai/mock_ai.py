from ai.ai_client import AIClient

class MockAI(AIClient):
    def classify(self, prompt):
        sensitive_word = ["aadhaar","pan","password","credit card","debit card"]
        
        for word in sensitive_word:
            if word.lower() in prompt.lower():
                return {
                    "risk": "HIGH",
                    "decision": "BLOCK",
                    "contains_pii": True,
                    "categories": [word.upper()]
                }
        return {
            "risk": "LOW",
            "decision": "ALLOW",
            "contains_pii": False,
            "categories": []
        }