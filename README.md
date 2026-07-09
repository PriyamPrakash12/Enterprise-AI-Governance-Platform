
AI Trust Gateway

Enterprise AI governance platform for Azure OpenAI with prompt inspection, auditing, policy enforcement, and cost monitoring.

[Enterprise AI Governance Platform1.pdf](https://github.com/user-attachments/files/29811891/Enterprise.AI.Governance.Platform1.pdf)

[Enterprise AI Governance Platform1 (1).pptx](https://github.com/user-attachments/files/29812225/Enterprise.AI.Governance.Platform1.1.pptx)


Based on everything we've built over the past few weeks, below is a detailed technical documentation for your project.

---

# Enterprise AI Governance Platform

## Technical Project Documentation

**Version:** 1.0

**Technology Stack**

* Python 3.11
* Azure Functions
* HTML5
* CSS3
* JavaScript
* Bootstrap 5
* JSON
* Regex
* Azure CLI
* Azure AI Foundry (Planned)

---

# 1. Project Overview

## Introduction

The Enterprise AI Governance Platform is a cloud-based governance layer designed to inspect, analyze, and control AI prompts before they are processed by an AI model.

The purpose of the project is to reduce AI-related risks by detecting sensitive information such as Personally Identifiable Information (PII), applying enterprise governance policies, calculating risk, and deciding whether a prompt should be:

* Allowed
* Sanitized
* Blocked

Rather than allowing users to communicate directly with an LLM, every request passes through the governance layer first.

---

# Problem Statement

Large Language Models can unintentionally process confidential enterprise information.

Examples include:

* Aadhaar Number
* PAN Card
* Passwords
* Credit Card Numbers
* Email IDs
* Phone Numbers

If this information reaches an AI model without inspection, it may violate:

* Company Policies
* GDPR
* HIPAA
* PCI DSS
* Internal Security Standards

The project introduces a governance layer that enforces enterprise policies before forwarding prompts to AI.

---

# Objectives

The platform aims to:

* Detect sensitive information
* Identify PII
* Calculate risk
* Assign confidence score
* Apply governance policies
* Sanitize prompts
* Block unsafe requests
* Prepare for Azure OpenAI integration

---

# Current Architecture

```
               User

                 │

                 ▼

         Web Dashboard

                 │

                 ▼

        Azure Function API

                 │

        ---------------------

        Detection Engine

        ---------------------

                 │

        ---------------------

         Policy Engine

        ---------------------

                 │

      BLOCK / SANITIZE / ALLOW

                 │

        (MockAI Currently)

                 │

        Azure OpenAI (Future)
```

---

# 2. Project Folder Structure

```
Enterprise-AI-Governance-Platform

│

├── dashboard
│   ├── index.html
│   ├── style.css
│   └── script.js

│
├── functions
│   ├── function_app.py
│   │
│   └── ai
│       ├── ai_client.py
│       └── mock_ai.py

│
├── resources
│   ├── keywords.json
│   ├── regex_patterns.json
│   └── policy.json

│
├── requirements.txt

├── host.json

└── local.settings.json
```

---

# 3. Technologies Used

## Azure Functions

Purpose

Acts as the serverless backend.

Responsibilities

* Receives HTTP request
* Reads prompt
* Invokes governance engine
* Returns JSON response

Benefits

* Serverless
* Scalable
* Low cost
* Azure native

---

## HTML

Used for

Dashboard UI

Contains

* Prompt textbox
* Analyze button
* Sanitization switch
* Result display

---

## CSS

Provides

Professional governance dashboard

Features

* Dark console theme
* Risk colors
* Progress bars
* Decision badges

---

## JavaScript

Responsibilities

* Sends prompt
* Calls Azure Function
* Updates dashboard
* Displays progress bars

---

## Bootstrap

Used for

Responsive UI

---

## Regex

Used for

Pattern detection

Examples

Email

Phone

PAN

Aadhaar

Password

Credit Card

---

## JSON

Stores

Keywords

Regex patterns

Enterprise policies

---

# 4. Governance Layer

The governance layer sits between the user and the AI model.

Its responsibility is:

Inspect

↓

Detect

↓

Apply Policy

↓

Decide

↓

Forward

---

Instead of

```
User

↓

OpenAI
```

We have

```
User

↓

Governance Layer

↓

OpenAI
```

---

# 5. Detection Engine

Implemented inside

```
MockAI.classify()
```

Responsibilities

* Scan prompt
* Identify sensitive information
* Detect categories
* Calculate confidence

Detection methods

### Keyword Detection

Uses

```
keywords.json
```

Example

```
password

aadhaar

pan

credit card
```

---

### Regex Detection

Uses

```
regex_patterns.json
```

Example

```
Email

Phone

Credit Card

PAN

Password
```

Regex provides highly accurate detection.

---

# 6. Policy Engine

Implemented using

```
policy.json
```

Purpose

Convert detections into governance decisions.

Example

```
AADHAAR

↓

HIGH

↓

BLOCK
```

Example

```
EMAIL

↓

MEDIUM

↓

SANITIZE
```

Policy Example

```
EMAIL

Risk

MEDIUM

Action

SANITIZE
```

---

# 7. Risk Assessment

Risk levels

LOW

MEDIUM

HIGH

Current implementation

Each detected category has

Risk

Risk Score

Default Action

Example

Password

Risk Score

100

Decision

BLOCK

---

# 8. Confidence Score

Confidence represents

How certain the system is that PII exists.

Current calculation

Keyword detection contributes

15 points

Regex detection contributes

35 points

Maximum

100

---

# 9. Sanitization

Two modes

## Block Mode

Prompt

```
Password is admin123
```

Decision

BLOCK

---

## Sanitize Mode

Prompt

```
Password is admin123
```

Output

```
Password is [PASSWORD]
```

Current implementation

Regex replacement

Future

Azure OpenAI rewriting

---

# 10. MockAI

Purpose

Simulates Azure OpenAI.

Responsibilities

Detection

Policy evaluation

Sanitization

Risk calculation

MockAI allows complete development without consuming Azure AI credits.

---

# 11. Azure Function

Main entry point

```
ClassifyPrompt
```

Flow

Receive Request

↓

Read JSON

↓

Extract Prompt

↓

Extract Sanitize Option

↓

Call

```
MockAI.classify()
```

↓

Return JSON

---

# 12. Dashboard

The dashboard provides

Prompt input

↓

Policy selection

↓

Analysis

↓

Result visualization

Displays

Risk

Decision

Contains PII

Categories

Risk Score

Confidence

Reason

Sanitized Prompt

---

# 13. API Flow

Browser

↓

JavaScript

↓

Azure Function

↓

MockAI

↓

JSON Response

↓

Dashboard

---

# 14. Current Features

Completed

✔ Prompt analysis

✔ Regex detection

✔ Keyword detection

✔ Policy Engine

✔ Risk Score

✔ Confidence Score

✔ Block mode

✔ Sanitize mode

✔ Dashboard

✔ Azure Functions

✔ Local deployment

---

# 15. Future Scope

## Azure AI Foundry

Replace MockAI

↓

Azure OpenAI GPT-4.1

---

## Conversation Memory

Store

Conversation history

↓

Cosmos DB

---

## Authentication

Microsoft Entra ID

---

## Audit Logging

Store

User

Timestamp

Prompt

Decision

Risk

---

## Monitoring

Dashboard

Total Requests

Blocked Requests

Sanitized Requests

High Risk Requests

---

## RAG

Azure AI Search

Document Retrieval

Knowledge Base

---

## Multi-Model Support

GPT

Claude

Gemini

Llama

---

## Compliance

GDPR

HIPAA

PCI DSS

ISO 27001

---

# 16. Current Workflow

```
User

↓

Dashboard

↓

Azure Function

↓

Detection Engine

↓

Keyword Detection

↓

Regex Detection

↓

Policy Engine

↓

Risk Calculation

↓

Confidence Calculation

↓

Decision

↓

Allow

or

Sanitize

or

Block

↓

Return Response
```

---

# 17. Future Enterprise Workflow

```
User

↓

Dashboard

↓

Azure Function

↓

Authentication

↓

Detection Engine

↓

Policy Engine

↓

Audit Log

↓

Conversation Manager

↓

Azure OpenAI

↓

Response

↓

Cosmos DB
```

---

# 18. Project Outcome

The project successfully demonstrates the core concepts of an AI governance platform by:

* Detecting sensitive information before it reaches an AI model.
* Enforcing configurable enterprise policies through a dedicated policy engine.
* Calculating risk and confidence scores for each request.
* Supporting both blocking and sanitization workflows.
* Providing a user-friendly governance dashboard.
* Using Azure Functions as a scalable serverless backend.
* Establishing a modular architecture that can be extended with Azure AI Foundry, Azure Cosmos DB, Microsoft Entra ID, audit logging, monitoring, and Retrieval-Augmented Generation (RAG).

This prototype serves as a strong foundation for evolving into a full enterprise-grade AI governance platform capable of securely managing interactions with multiple AI models while meeting organizational security and compliance requirements.
