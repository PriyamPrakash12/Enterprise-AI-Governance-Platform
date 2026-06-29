from ai.mock_ai import MockAI

client = MockAI()

result = client.classify(
    "My Aadhaar number is 123456789"
)

print(result)