from fastapi import FastAPI
from routers.explanation import router as spam_router
from routers.prediction import router as spam_explain_router

app = FastAPI(title="Spam Detection API")

app.include_router(spam_router)
app.include_router(spam_explain_router)
