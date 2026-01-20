from flask import Flask, request, jsonify
from flask_cors import CORS
from db import contracts
from analyzer import extract_clauses, detect_risk, negotiation_tips

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    contract_text = data["contract"]

    clauses = extract_clauses(contract_text)
    risks = detect_risk(contract_text)
    tips = negotiation_tips(contract_text)

    contracts.insert_one({
        "contract": contract_text,
        "clauses": clauses,
        "risks": risks,
        "tips": tips
    })

    return jsonify({
        "clauses": clauses,
        "risks": risks,
        "negotiation_tips": tips
    })


@app.route("/chat", methods=["POST"])
def chat():
    question = request.json["question"]
    return jsonify({
        "answer": f"AI Assistant response to: {question}"
    })


if __name__ == "__main__":
    app.run(debug=True)