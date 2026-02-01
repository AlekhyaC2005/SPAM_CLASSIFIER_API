from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from models.explanation_model import chat_model
import json

router=APIRouter(prefix="/spam", tags=["Spam Explanation"])

# ------------------------------
# Request Schema
# ------------------------------
class SpamExplainRequest(BaseModel):
    text: str
    prediction: str  # "Spam" or "Not Spam"


# ------------------------------
# Route
# ------------------------------
@router.post("/explain")
def explain_spam(request: SpamExplainRequest):
    try:
        SYSTEM_PROMPT = """
You are a cybersecurity assistant.

Your task:
- If the message is spam, identify the type of spam (e.g. phishing, promotional, scam, lottery, financial fraud).
- Briefly explain why it is considered that type.
- Give exactly ONE clear, practical advice.

Rules:
- Keep the response concise (2–3 sentences max).
- Do NOT repeat the message text.
- If the message is NOT spam, explain briefly why it seems safe and give one safety tip.
"""

        user_message = f"""
Message: "{request.text}"
Prediction: {request.prediction}
"""

        response = chat_model.invoke([
            ("system", SYSTEM_PROMPT),
            ("human", user_message)
        ])

        return {
            "prediction": request.prediction,
            "explanation": response.content.strip()
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Spam explanation failed: {str(e)}"
        )