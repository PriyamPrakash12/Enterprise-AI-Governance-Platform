import azure.functions as func
import logging

app = func.FunctionApp()

@app.route(route="ClassifyPrompt", auth_level=func.AuthLevel.ANONYMOUS)
def classify_prompt(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Request received")

    return func.HttpResponse(
        "ClassifyPrompt API is working!",
        status_code=200
    )