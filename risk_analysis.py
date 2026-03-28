class RiskAnalyzer:
    def __init__(self):
        self.high_risk_keywords = ["termination", "penalty", "indemnify", "liability", "breach"]
        self.medium_risk_keywords = ["notice", "days", "delay", "limit"]

    def analyze_risks(self, clauses):
        risks = []
        for clause in clauses:
            text = clause['text'].lower()
            risk_type = "low"
            score = 0.1
            if any(keyword in text for keyword in self.high_risk_keywords):
                risk_type = "high"
                score = 0.9
            elif any(keyword in text for keyword in self.medium_risk_keywords):
                risk_type = "medium"
                score = 0.5
            risks.append({
                "clause": clause['text'],
                "text": clause['text'],
                "type": risk_type,
                "score": score
            })
        return risks