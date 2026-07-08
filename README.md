AI Trust Gateway

Enterprise AI governance platform for Azure OpenAI with prompt inspection, auditing, policy enforcement, and cost monitoring.
Invoke-RestMethod `
-Uri http://localhost:7071/api/ClassifyPrompt `
-Method POST `
-ContentType "application/json" `
-Body '{"prompt":"my aadhar is 123456789012","sanitize":false}'
