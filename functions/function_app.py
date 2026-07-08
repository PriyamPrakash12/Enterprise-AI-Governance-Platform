import azure.functions as func
import logging
import json

from ai.mock_ai import MockAI

app = func.FunctionApp()

client = MockAI()

@app.route(route="ClassifyPrompt", auth_level=func.AuthLevel.ANONYMOUS)
def classify_prompt(req: func.HttpRequest) -> func.HttpResponse:

    logging.info("========== REQUEST RECEIVED ==========")

    logging.info(req.get_body())

    try:
        body = req.get_json()

        logging.info(body)

        prompt = body.get("prompt", "")
        sanitize = body.get("sanitize", False)

        result = client.classify(prompt, sanitize)

        return func.HttpResponse(
            json.dumps(result),
            mimetype="application/json",
            status_code=200
        )

    except Exception as e:

        logging.exception(e)

        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            mimetype="application/json",
            status_code=400
        )