```json
{
    "tests/test_knowledge_agent.py": {
        "content": "
import logging
from typing import Dict, List
from langgraph import StateGraph
from lindy import Workflow
from giskard import Agent

def test_knowledge_agent(non_stationary_drift_index: int, stochastic_regime_switch: bool) -> Dict[str, List[float]]:
    """
    Test the knowledge agent with non-stationary drift index and stochastic regime switch.

    Args:
    - non_stationary_drift_index (int): The index of non-stationary drift.
    - stochastic_regime_switch (bool): Whether to use stochastic regime switch.

    Returns:
    - A dictionary with the test results.
    """
    try:
        logging.info('Starting test_knowledge_agent')
        # Create a StateGraph instance
        state_graph = StateGraph()
        # Create a Workflow instance
        workflow = Workflow()
        # Create an Agent instance
        agent = Agent()
        # Initialize the agent with the state graph and workflow
        agent.initialize(state_graph, workflow)
        # Test the agent with non-stationary drift index and stochastic regime switch
        test_results = agent.test(non_stationary_drift_index, stochastic_regime_switch)
        logging.info('Test results: %s', test_results)
        return test_results
    except Exception as e:
        logging.error('Error in test_knowledge_agent: %s', e)
        return {}

def test_state_graph(state_graph: StateGraph) -> bool:
    """
    Test the state graph.

    Args:
    - state_graph (StateGraph): The state graph to test.

    Returns:
    - True if the state graph is valid, False otherwise.
    """
    try:
        logging.info('Starting test_state_graph')
        # Test the state graph
        is_valid = state_graph.is_valid()
        logging.info('State graph is valid: %s', is_valid)
        return is_valid
    except Exception as e:
        logging.error('Error in test_state_graph: %s', e)
        return False

def test_workflow(workflow: Workflow) -> bool:
    """
    Test the workflow.

    Args:
    - workflow (Workflow): The workflow to test.

    Returns:
    - True if the workflow is valid, False otherwise.
    """
    try:
        logging.info('Starting test_workflow')
        # Test the workflow
        is_valid = workflow.is_valid()
        logging.info('Workflow is valid: %s', is_valid)
        return is_valid
    except Exception as e:
        logging.error('Error in test_workflow: %s', e)
        return False

if __name__ == '__main__':
    # Create a StateGraph instance
    state_graph = StateGraph()
    # Create a Workflow instance
    workflow = Workflow()
    # Create an Agent instance
    agent = Agent()
    # Initialize the agent with the state graph and workflow
    agent.initialize(state_graph, workflow)
    # Test the agent with non-stationary drift index and stochastic regime switch
    non_stationary_drift_index = 10
    stochastic_regime_switch = True
    test_results = test_knowledge_agent(non_stationary_drift_index, stochastic_regime_switch)
    print('Test results:', test_results)
    # Test the state graph
    is_valid = test_state_graph(state_graph)
    print('State graph is valid:', is_valid)
    # Test the workflow
    is_valid = test_workflow(workflow)
    print('Workflow is valid:', is_valid)
",
        "commit_message": "feat: implement specialized test_knowledge_agent logic"
    }
}
```