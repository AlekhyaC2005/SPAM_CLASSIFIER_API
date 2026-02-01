import streamlit as st
import requests

API_BASE_URL = "https://spam-classifier-api-uiiy.onrender.com"

st.set_page_config(page_title="Spam Classifier", layout="centered")

st.title("📩 SMS Spam Classifier")
st.write("Enter a message to detect spam and get an explanation.")

# ------------------------------
# User Input
# ------------------------------
user_text = st.text_area("Enter your message", height=120)

# ------------------------------
# Button
# ------------------------------
if st.button("Analyze Message"):
    if not user_text.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Analyzing..."):

            # ------------------------------
            # 1️⃣ Call Spam Prediction API
            # ------------------------------
            try:
                predict_response = requests.post(
                    f"{API_BASE_URL}/spam/predict",
                    json={"text": user_text},
                    timeout=10
                )

                predict_response.raise_for_status()
                predict_data = predict_response.json()

                prediction = predict_data["prediction"]

                st.subheader("🔍 Prediction Result")
                st.success(f"**{prediction}**")

            except Exception as e:
                st.error("Failed to get spam prediction.")
                st.stop()

            # ------------------------------
            # 2️⃣ Call Spam Explanation API
            # ------------------------------
            try:
                explain_response = requests.post(
                    f"{API_BASE_URL}/spam/explain",
                    json={
                        "text": user_text,
                        "prediction": prediction
                    },
                    timeout=15
                )

                explain_response.raise_for_status()
                explain_data = explain_response.json()

                explanation = explain_data["explanation"]

                st.subheader("🧠 Explanation")
                st.info(explanation)

            except Exception as e:
                st.error("Failed to get explanation.")
