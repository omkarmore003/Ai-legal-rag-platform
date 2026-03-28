from document_ingestion import DocumentProcessor
from clause_analysis import ClauseAnalyzer
from knowledge_graph import KnowledgeGraphBuilder
from risk_analysis import RiskAnalyzer
from scenario_engine import ScenarioEngine
from rag_qa import RAGQASystem

class ContractAnalyzer:
    def __init__(self):
        self.doc_processor = DocumentProcessor()
        self.clause_analyzer = ClauseAnalyzer()
        self.graph_builder = KnowledgeGraphBuilder()
        self.risk_analyzer = RiskAnalyzer()
        self.scenario_engine = ScenarioEngine()
        self.rag_qa = None

    def analyze_contract(self, file_path):
        text = self.doc_processor.process(file_path)
        clauses = self.clause_analyzer.extract_clauses(text)
        graph = self.graph_builder.build_graph(clauses)
        risks = self.risk_analyzer.analyze_risks(clauses)
        self.graph_builder.add_risks(risks)
        scenarios = self.scenario_engine.simulate(clauses)
        self.graph_builder.add_scenarios(scenarios)
        self.rag_qa = RAGQASystem(clauses)
        return clauses, risks, scenarios