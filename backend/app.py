from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
from dotenv import load_dotenv
import os
import firebase_admin
from firebase_admin import credentials, firestore

# Load env
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

# response = client.models.generate_content(
#     model="gemini-2.5-flash", 
#     contents="Hello Gemini"
# )

# Firebase setup
cred = credentials.Certificate("serviceAccount.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Flask
app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return {"message": "Bazaar Eye Backend Running"}

@app.route("/price-advisor", methods=["POST"])
def price_advisor():
    data = request.json

    laptop = data.get("laptop")
    condition = data.get("condition")
    market = data.get("market", "Nehru Place Delhi")

    prompt = f"""
    You are an expert laptop resale market advisor for Indian street markets like {market}.
    Analyze the laptop details below and give output in structured bullet points.

    Laptop: {laptop}
    Condition: {condition}

    Provide:
    1) Realistic price range in INR
    2) Ideal price buyer should aim for
    3) Maximum safe price (do not overpay above this)
    4) Negotiation strategy in 3-4 lines in Indian street style tone
    5) Scam alerts or things to check (battery health, keyboard, heating, SSD health)
    6) Confidence score (Low/Medium/High)
    """

    response = model.generate_content(prompt)
    result = response.text

    # Save in Firebase
    doc = {
        "laptop": laptop,
        "condition": condition,
        "market": market,
        "response": result
    }

    db.collection("price_checks").add(doc)

    return jsonify({"analysis": result})


if __name__ == "__main__":
    app.run(debug=True)
