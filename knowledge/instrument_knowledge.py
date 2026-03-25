```json
{
    "knowledge/instrument_knowledge.py": {
        "content": "
import logging
from typing import Dict, List
from langgraph import StateGraph
from lindy import Workflow
from giskard import MLModel
from pipedrive import SalesWorkflow

logging.basicConfig(level=logging.INFO)

class InstrumentKnowledge:
    def __init__(self, non_stationary_drift_index: float, stochastic_regime_switch: bool):
        """
        Initialize the instrument knowledge with non-stationary drift index and stochastic regime switch.

        Args:
        - non_stationary_drift_index (float): The index of non-stationary drift.
        - stochastic_regime_switch (bool): Whether to use stochastic regime switch.
        """
        self.non_stationary_drift_index = non_stationary_drift_index
        self.stochastic_regime_switch = stochastic_regime_switch
        self.state_graph = StateGraph()

    def build_state_graph(self, nodes: List[str], edges: List[tuple]) -> StateGraph:
        """
        Build the state graph with nodes and edges.

        Args:
        - nodes (List[str]): The list of nodes.
        - edges (List[tuple]): The list of edges.

        Returns:
        - StateGraph: The built state graph.
        """
        try:
            logging.info('Building state graph...')
            self.state_graph = StateGraph()
            self.state_graph.add_nodes(nodes)
            self.state_graph.add_edges(edges)
            logging.info('State graph built successfully.')
            return self.state_graph
        except Exception as e:
            logging.error(f'Error building state graph: {e}')
            raise

    def train_ml_model(self, data: Dict[str, List[float]]) -> MLModel:
        """
        Train the ML model with data.

        Args:
        - data (Dict[str, List[float]]): The training data.

        Returns:
        - MLModel: The trained ML model.
        """
        try:
            logging.info('Training ML model...')
            ml_model = MLModel()
            ml_model.train(data)
            logging.info('ML model trained successfully.')
            return ml_model
        except Exception as e:
            logging.error(f'Error training ML model: {e}')
            raise

    def simulate_rocket_science(self, workflow: Workflow) -> None:
        """
        Simulate the rocket science problem with the given workflow.

        Args:
        - workflow (Workflow): The workflow to simulate.
        """
        try:
            logging.info('Simulating rocket science...')
            sales_workflow = SalesWorkflow()
            sales_workflow.simulate(workflow)
            logging.info('Rocket science simulation completed.')
        except Exception as e:
            logging.error(f'Error simulating rocket science: {e}')
            raise

if __name__ == '__main__':
    # Create an instance of InstrumentKnowledge
    instrument_knowledge = InstrumentKnowledge(non_stationary_drift_index=0.5, stochastic_regime_switch=True)

    # Build the state graph
    nodes = ['node1', 'node2', 'node3']
    edges = [('node1', 'node2'), ('node2', 'node3')]
    state_graph = instrument_knowledge.build_state_graph(nodes, edges)

    # Train the ML model
    data = {'feature1': [1.0, 2.0, 3.0], 'feature2': [4.0, 5.0, 6.0]}
    ml_model = instrument_knowledge.train_ml_model(data)

    # Simulate the rocket science problem
    workflow = Workflow()
    instrument_knowledge.simulate_rocket_science(workflow)
",
        "commit_message": "feat: implement specialized instrument_knowledge logic"
    }
}
```