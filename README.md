
AI Trust Gateway

Enterprise AI governance platform for Azure OpenAI with prompt inspection, auditing, policy enforcement, and cost monitoring.

[Enterprise AI Governance Platform1.pdf](https://github.com/user-attachments/files/29811891/Enterprise.AI.Governance.Platform1.pdf)

[Enterprise AI Governance Platform1 (1).pptx](https://github.com/user-attachments/files/29812225/Enterprise.AI.Governance.Platform1.1.pptx)


Section 5: Detection Engine Implementation
File

functions/ai/mock_ai.py

Purpose

The MockAI class acts as the AI governance engine. It loads enterprise policies, regex patterns, and keywords, then analyzes every prompt before returning a governance decision.

class MockAI(AIClient):

    def __init__(self):

        current_dir = os.path.dirname(__file__)

        with open(keyword_file, "r") as file:
            self.keywords = json.load(file)

        with open(regex_file, "r") as file:
            self.regex_patterns = json.load(file)

        with open(policy_file, "r") as file:
            self.policy = json.load(file)
Explanation
Loads keyword dictionary.
Loads regex patterns.
Loads enterprise governance policy.
Keeps configuration external using JSON files.
Section 6: Keyword Detection
Code
for category, words in self.keywords.items():

    for word in words:

        if word.lower() in prompt.lower():

            keyword_hits += 1

            if category not in detected_categories:
                detected_categories.append(category)
Explanation

This module performs simple keyword-based detection.

Example:

Input

Password is admin123

Output

PASSWORD detected
Section 7: Regex Detection
Code
for category, pattern in self.regex_patterns.items():

    matches = re.findall(pattern, sanitized_prompt)

    if matches:

        regex_hits += len(matches)

        if category not in detected_categories:
            detected_categories.append(category)
Explanation

Regex provides structured pattern matching for PII such as:

Email
Aadhaar
PAN
Credit Card
Phone Number
Password

This method is more accurate than keyword detection.

Section 8: Prompt Sanitization
Code
sanitized_prompt = re.sub(

    pattern,

    lambda m: m.group(0).replace(
        m.group(1),
        f"[{category}]"
    ),

    sanitized_prompt
)
Explanation

Instead of blocking, the sensitive value is replaced while preserving the original sentence.

Example

Before

My PAN is ABCDE1234F

After

My PAN is [PAN]
Section 9: Risk Calculation
Code
highest_score = 0

for category in detected_categories:

    category_score = self.policy[category]["risk_score"]

    highest_score = max(highest_score, category_score)
Explanation

Every detected category has an associated risk score stored in policy.json.

The highest score determines the overall risk.

Section 10: Confidence Calculation
Code
confidence = min(

    100,

    regex_hits * 35 +

    keyword_hits * 15

)
Explanation

Confidence indicates how certain the detection engine is.

Current calculation:

Regex Match = 35%
Keyword Match = 15%

Maximum = 100%

Section 11: Policy Engine
Code
decision = (

    "SANITIZE"

    if sanitize

    else self.policy[highest_category]["action"]
)
Explanation

The Policy Engine decides whether to:

ALLOW
SANITIZE
BLOCK

based on enterprise rules.

Section 12: API Endpoint
File

function_app.py

Code
@app.route(
    route="ClassifyPrompt",
    auth_level=func.AuthLevel.ANONYMOUS
)
Explanation

Creates an HTTP endpoint that receives prompts from the dashboard.

Reading the Request
body = req.get_json()

prompt = body.get("prompt", "")

sanitize = body.get("sanitize", False)

Purpose:

Extracts the prompt and sanitization preference.

Calling the Governance Engine
result = client.classify(
    prompt,
    sanitize
)

Purpose:

Sends the prompt to the Detection and Policy Engine.

Returning the Response
return func.HttpResponse(

    json.dumps(result),

    mimetype="application/json",

    status_code=200
)

Purpose:

Returns the governance result to the frontend in JSON format.

Section 13: Example Response
{
  "risk": "HIGH",
  "risk_score": 95,
  "confidence": 70,
  "decision": "BLOCK",
  "contains_pii": true,
  "categories": [
    "AADHAAR"
  ],
  "reason": "Detected: AADHAAR",
  "sanitized_prompt": ""
}
Section 14: Enterprise Workflow
Dashboard
        │
        ▼
JavaScript Fetch API
        │
        ▼
Azure Function
        │
        ▼
MockAI.classify()
        │
 ┌──────────────┐
 │ Keyword Scan │
 └──────────────┘
        │
 ┌──────────────┐
 │ Regex Scan   │
 └──────────────┘
        │
 ┌──────────────┐
 │ Policy Engine│
 └──────────────┘
        │
        ▼
Decision
        │
        ▼
Dashboard Response
