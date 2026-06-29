print("TEST STARTED")

from classify.mock_classifier import classify_prompt
from logwriter.mock_logger import create_log

prompt = "aadhar"

result = classify_prompt(prompt)

print("Classification Result:")
print(result)

log = create_log(prompt, result["risk"])

print("\nLog Entry:")
print(log)