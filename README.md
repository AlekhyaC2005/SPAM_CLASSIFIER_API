**📩 Spam Classifier with Explanation (FastAPI + Streamlit + LLM)**
An end-to-end Spam Detection system that not only classifies messages as Spam / Not Spam, but also explains the reasoning behind the prediction using a Large Language Model.
________________________________________
**🚀 Live Demo**
🔗 Streamlit App
👉 https://spam-classifier-with-explanation.streamlit.app/](https://spamclassifierappapi.streamlit.app/

🔗 FastAPI Backend
👉 https://spam-classifier-api-uiiy.onrender.com
________________________________________
**🧠 Project Overview**
This project combines:
•	A traditional Machine Learning classifier for accurate spam detection
•	A Large Language Model (LLM) to provide human-friendly explanations and advice
Why this approach?
•	ML models are fast and reliable for classification
•	LLMs make predictions explainable and user-friendly
________________________________________
**🧪 Spam Classification Model**

📌 Model Used
Multinomial Naive Bayes
This model is trained on processed SMS/Email text using TF-IDF vectorization, making it highly effective for text classification tasks.
📊 Model Performance
Metric	Score
Accuracy	0.9822
Precision	0.99
Recall	0.8534
F1-Score	0.9167
✔ High precision ensures very few false spam alerts
✔ Strong recall ensures most spam messages are caught
________________________________________
**🤖 Large Language Model (LLM) for Explanation**

📌 Model Used
LLaMA-3.1-8B-Instant
The LLM is used after classification to:
•	Explain why a message is spam or not
•	Identify the type of spam (phishing, promotion, scam, etc.)
•	Provide one practical safety suggestion
🧠 Why LLaMA-3.1-8B-Instant?
•	Excellent reasoning and instruction following
•	Fast inference for real-time APIs
•	Generates clear, concise, and contextual explanations
•	Ideal for Explainable AI (XAI) use cases
________________________________________
**🔄 System Workflow**

1.	User enters a message
2.	Text is preprocessed (tokenization, stopwords removal, stemming)
3.	Multinomial Naive Bayes predicts → Spam / Not Spam
4.	Prediction + message are sent to LLaMA-3.1-8B-Instant
5.	User receives:
o	Classification result
o	Explanation
o	One safety recommendation
________________________________________
**🧩 API Endpoints**

1️⃣ Spam Prediction
POST /spam/predict
Request
{
  "text": "Congratulations! You have won a free prize"
}
Response
{
  "text": "Congratulations! You have won a free prize",
  "prediction": "Spam"
}
________________________________________
**2️⃣ Spam Explanation**

POST /spam/explain
Input
•	User message
•	Model prediction
Output
•	Type of spam
•	Reason for classification
•	One helpful advice
________________________________________
**🖥️ Streamlit App Features**

•	Clean UI for user input
•	Displays:
o	🔹 Spam / Not Spam prediction
o	🔹 LLM-generated explanation
•	Uses live FastAPI backend
•	Beginner-friendly and responsive
________________________________________
**🛠 Tech Stack**

•	Backend: FastAPI
•	Frontend: Streamlit
•	ML Model: Multinomial Naive Bayes
•	Vectorization: TF-IDF
•	LLM: LLaMA-3.1-8B-Instant
•	NLP: NLTK
•	Deployment:
o	API → Render
o	App → Streamlit Cloud
________________________________________
**📌 Key Highlights**

✔ High-accuracy spam detection
✔ Explainable AI output
✔ Real-time API + UI
✔ Production-ready architecture
✔ Clear separation of ML and LLM layers
________________________________________
**📬 Future Improvements**

•	Add confidence scores
•	Multi-language spam detection
•	User feedback loop
•	Model retraining pipeline
________________________________________
**👤 Author**

Alekhya Chatterjee
If you found this useful, feel free to ⭐ the repository!





