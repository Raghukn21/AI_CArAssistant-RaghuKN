def extract_clauses(text):
    clauses = {}

    if "interest" in text.lower():
        clauses["Interest Rate"] = "Interest clause detected"

    if "penalty" in text.lower():
        clauses["Penalty"] = "Penalty clause detected"

    if "repossession" in text.lower():
        clauses["Repossession"] = "Repossession clause detected"

    if "prepayment" in text.lower():
        clauses["Prepayment"] = "Prepayment charges detected"

    return clauses


def detect_risk(text):
    risks = []

    if "penalty" in text.lower():
        risks.append("High penalty risk")

    if "repossession" in text.lower():
        risks.append("Vehicle repossession risk")

    if not risks:
        risks.append("Low risk contract")

    return risks


def negotiation_tips(text):
    tips = []

    if "interest" in text.lower():
        tips.append("Request lower interest rate")

    if "penalty" in text.lower():
        tips.append("Negotiate penalty charges")

    if "prepayment" in text.lower():
        tips.append("Ask to reduce prepayment fee")

    return tips