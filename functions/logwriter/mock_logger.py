from datetime import datetime


def create_log(prompt, risk):

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "prompt": prompt,
        "risk": risk
    }