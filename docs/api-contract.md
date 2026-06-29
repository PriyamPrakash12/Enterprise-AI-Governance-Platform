# ClassifyPrompt API

## Endpoint

POST /api/ClassifyPrompt

## Request

{
  "prompt": "My Aadhaar number is 1234"
}

## Response

{
  "risk": "HIGH",
  "contains_pii": true,
  "categories": ["AADHAAR"]
}