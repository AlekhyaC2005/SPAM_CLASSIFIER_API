from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Ensure required NLTK resources
import nltk
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")

router = APIRouter(prefix="/spam", tags=["Spam Detection"])

ps = PorterStemmer()

# ------------------------------
# Load model & vectorizer
# ------------------------------
try:
    tfidf = pickle.load(open("vectorizer.pkl", "rb"))
    model = pickle.load(open("model.pkl", "rb"))
except Exception as e:
    raise RuntimeError(f"Failed to load model files: {e}")


# ------------------------------
# Text preprocessing
# ------------------------------
def transform_text(text):

  # lower case
  text=text.lower()

  # word tokenize
  text=nltk.word_tokenize(text)

  # removing special characters
  y=[]
  for i in text:
    if i.isalnum():
      y.append(i)

  # removing stop words and special char
  text=y[:]
  y.clear()

  for i in text:
    if i not in stopwords.words("english") and i not in string.punctuation:
      y.append(i)

  # stemming
  text=y[:]
  y.clear()

  for i in text:
    y.append(ps.stem(i))

  return " ".join(y)



# ------------------------------
# Request Schema
# ------------------------------
class SpamRequest(BaseModel):
    text: str


# ------------------------------
# Route
# ------------------------------
@router.post("/predict")
def predict_spam(request: SpamRequest):
    try:
        transformed_text = transform_text(request.text)
        vector_input = tfidf.transform([transformed_text])
        prediction = model.predict(vector_input)[0]

        return {
            "text": request.text,
            "prediction": "Spam" if prediction == 1 else "Not Spam"
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Spam prediction failed: {str(e)}"
        )
