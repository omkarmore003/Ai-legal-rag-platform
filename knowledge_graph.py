import networkx as nx
import spacy

class KnowledgeGraphBuilder:
    def __init__(self):
        self.graph = nx.DiGraph()
        self.nlp = spacy.load("en_core_web_sm")

    def build_graph(self, clauses):
        for clause in clauses:
            clause_text = clause["text"]
            clause_type = clause["type"]
            self.graph.add_node(clause_text, type=clause_type)
            doc = self.nlp(clause_text)
            for ent in doc.ents:
                self.graph.add_node(ent.text, type=ent.label_)
                self.graph.add_edge(clause_text, ent.text, relation="mentions")
        return self.graph

    def add_risks(self, risks):
        for risk in risks:
            risk_node = f"RISK: {risk['type']}"
            self.graph.add_node(risk_node, type="risk", score=risk["score"])
            self.graph.add_edge(risk["text"], risk_node, relation="has_risk")

    def add_scenarios(self, scenarios):
        for scenario in scenarios:
            scenario_node = f"SCENARIO: {scenario['scenario']}"
            self.graph.add_node(scenario_node, type="scenario")
            self.graph.add_edge(scenario_node, scenario["consequence"], relation="leads_to")

    def get_graph(self):
        return self.graph