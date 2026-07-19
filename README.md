# Enterprise AI Governance Platform

An AI Governance Layer that intercepts prompts **before they reach a Large Language Model (LLM)** to detect sensitive information, evaluate security policies, sanitize confidential data, and provide real-time risk analysis.

> **Status:** Prototype (Local Version) | Azure AI Foundry Integration In Progress

---

## Overview

Enterprise users often unintentionally include confidential information such as Aadhaar numbers, PAN numbers, passwords, API keys, or other sensitive data while interacting with AI models.

This project introduces a **Governance Layer** between the user and the AI model.

Instead of sending prompts directly to an LLM, every request first passes through a security pipeline where it is analyzed and processed according to organizational policies.

---

## Features

- PII Detection
- Keyword Detection
- Policy Evaluation
- Prompt Sanitization
- Risk Classification
- Confidence Scoring
- Real-time Dashboard
- Modular AI Layer (MockAI)
- Serverless Backend using Azure Functions

---

## Architecture

```
User
   │
   ▼
Web Dashboard
   │
   ▼
Azure Function (HTTP Trigger)
   │
   ▼
Governance Layer
   ├── Detection Engine
   ├── Policy Engine
   ├── Risk Assessment
   ├── Sanitization
   ▼
MockAI
   │
   ▼
Response returned to Dashboard
```

Future architecture:

```
User
   │
Dashboard
   │
Azure Functions
   │
Governance Layer
   │
Azure AI Foundry / Azure OpenAI
   │
LLM Response
```

---

## Technology Stack

| Layer | Technology |
|--------|------------|
| Frontend | HTML5, CSS3, Bootstrap, JavaScript |
| Backend | Python |
| Serverless | Azure Functions |
| AI Layer | MockAI |
| Cloud | Microsoft Azure |
| Future Integration | Azure AI Foundry / Azure OpenAI |

---

## Project Structure

```
Enterprise-AI-Governance-Platform
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── ai/
│   └── mock_ai.py
│
├── FunctionApp/
│   └── function_app.py
│
├── policies/
│
├── local.settings.json
├── host.json
├── requirements.txt
│
├── Documentation/
│   └── Project Documentation.pdf
│
├── Presentation/
│   └── Project Presentation.pptx
│
└── README.md
```

---

## Workflow

1. User enters a prompt.
2. Frontend sends the prompt to Azure Functions.
3. Azure Function invokes the Governance Layer.
4. Detection Engine checks:
   - PII
   - Keywords
   - Sensitive Patterns
5. Policy Engine evaluates security rules.
6. Risk Score is generated.
7. Decision is taken:
   - Allow
   - Sanitize
   - Block
8. Response is displayed on the dashboard.

---

## Current Capabilities

✔ Detects sensitive information

✔ Identifies high-risk prompts

✔ Supports prompt sanitization

✔ Calculates confidence score

✔ Displays real-time analysis

✔ Modular backend for future AI integration

---

## Future Improvements

- Azure AI Foundry Integration
- Azure OpenAI Integration
- Conversation Memory
- Authentication
- Audit Logs
- Role-Based Access Control (RBAC)
- Policy Management Portal
- Multi-language Detection
- Prompt Injection Detection
- Content Safety APIs

---
## Documentation

Detailed project documentation is available in:

[Enterprise_AI_Governance_Platform_Technical_Documentation.docx](https://github.com/user-attachments/files/30166949/Enterprise_AI_Governance_Platform_Technical_Documentation.docx)

---

## Presentation

Project presentation is available in:

[Enterprise AI Governance.pdf](https://github.com/user-attachments/files/30167061/Enterprise.AI.Governance.pdf)

---

## How to Run

### Clone Repository

```bash
git clone https://github.com/yourusername/Enterprise-AI-Governance-Platform.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start Azure Functions

```bash
func start
```

### Open Frontend

Open

```
frontend/index.html
```

or use

```
Live Server
```

---

## Example Request

```json
{
    "prompt":"My Aadhaar number is 123456789012",
    "sanitize":true
}
```

Example Response

```json
{
    "risk":"HIGH",
    "decision":"SANITIZE",
    "contains_pii":true,
    "risk_score":95,
    "confidence":98,
    "sanitized_prompt":"My Aadhaar number is ************"
}
```

---

## Learning Outcomes

During this project, I learned:

- Azure Functions
- Serverless Architecture
- API Development
- Security-first AI Design
- Prompt Governance
- Policy-based Decision Making
- Modular Backend Design
- Frontend-Backend Integration

---
