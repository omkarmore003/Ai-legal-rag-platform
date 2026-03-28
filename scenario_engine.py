class ScenarioEngine:
    def __init__(self):
        self.scenarios = [
            {
                "scenario": "Employee breaches confidentiality",
                "consequence": "Employer may seek damages or injunctive relief."
            },
            {
                "scenario": "Termination without notice",
                "consequence": "Party may be liable for wrongful termination claims."
            },
            {
                "scenario": "Late salary payment",
                "consequence": "Employer may face penalties or employee claims."
            }
        ]

    def simulate(self, text):
        return self.scenarios