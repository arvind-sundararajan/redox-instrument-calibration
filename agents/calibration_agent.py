```json
{
    "agents/calibration_agent.py": {
        "content": "
import logging
from typing import Dict, List
from langgraph import StateGraph
from lindy import Workflow
from giskard import MLModel

class CalibrationAgent:
    """
    Agent responsible for calibrating oxidation-reduction potential instruments.
    """
    
    def __init__(self, config: Dict[str, str]):
        """
        Initialize the calibration agent with a configuration dictionary.
        
        Args:
        config (Dict[str, str]): Configuration dictionary containing instrument settings.
        """
        self.config = config
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
    def non_stationary_drift_index(self, data: List[float]) -> float:
        """
        Calculate the non-stationary drift index for the given data.
        
        Args:
        data (List[float]): List of oxidation-reduction potential values.
        
        Returns:
        float: Non-stationary drift index.
        """
        try:
            # Calculate the non-stationary drift index using a stochastic regime switch model
            model = MLModel(self.config['model_path'])
            drift_index = model.predict(data)
            self.logger.info('Non-stationary drift index calculated: %f', drift_index)
            return drift_index
        except Exception as e:
            self.logger.error('Error calculating non-stationary drift index: %s', str(e))
            raise
        
    def stochastic_regime_switch(self, data: List[float]) -> List[float]:
        """
        Apply a stochastic regime switch to the given data.
        
        Args:
        data (List[float]): List of oxidation-reduction potential values.
        
        Returns:
        List[float]: List of values after applying the stochastic regime switch.
        """
        try:
            # Create a StateGraph to model the stochastic regime switch
            graph = StateGraph()
            graph.add_state('high_regime')
            graph.add_state('low_regime')
            graph.add_transition('high_regime', 'low_regime', 0.5)
            graph.add_transition('low_regime', 'high_regime', 0.3)
            # Apply the stochastic regime switch to the data
            switched_data = []
            for value in data:
                state = graph.get_current_state()
                if state == 'high_regime':
                    switched_data.append(value * 1.2)
                else:
                    switched_data.append(value * 0.8)
            self.logger.info('Stochastic regime switch applied')
            return switched_data
        except Exception as e:
            self.logger.error('Error applying stochastic regime switch: %s', str(e))
            raise
        
    def calibrate_instrument(self, data: List[float]) -> List[float]:
        """
        Calibrate the oxidation-reduction potential instrument using the given data.
        
        Args:
        data (List[float]): List of oxidation-reduction potential values.
        
        Returns:
        List[float]: List of calibrated values.
        """
        try:
            # Calculate the non-stationary drift index
            drift_index = self.non_stationary_drift_index(data)
            # Apply the stochastic regime switch
            switched_data = self.stochastic_regime_switch(data)
            # Create a workflow to calibrate the instrument
            workflow = Workflow(self.config['workflow_path'])
            calibrated_data = workflow.run(switched_data)
            self.logger.info('Instrument calibrated')
            return calibrated_data
        except Exception as e:
            self.logger.error('Error calibrating instrument: %s', str(e))
            raise
        
if __name__ == '__main__':
    # Create a simulation of the 'Rocket Science' problem
    config = {'model_path': 'model.pkl', 'workflow_path': 'workflow.json'}
    agent = CalibrationAgent(config)
    data = [1.2, 2.3, 3.1, 4.2, 5.1]
    calibrated_data = agent.calibrate_instrument(data)
    print('Calibrated data:', calibrated_data)
",
        "commit_message": "feat: implement specialized calibration_agent logic"
    }
}
```