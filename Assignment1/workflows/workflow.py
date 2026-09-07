from workflows.sequential import sequential_workflow
from workflows.conditional import conditional_workflow
from workflows.iterative import iterative_workflow
from workflows.functional import functional_workflow
from workflows.pipeline import pipeline_workflow


class WorkflowManager:
    """
    Manages the different workflow strategies
    available in NEXORA-OPS.
    """

    def __init__(self, agent):
        self.agent = agent

    def run(self, workflow_type, data):
        """
        Execute the selected workflow.
        """

        workflows = {
            "sequential": sequential_workflow,
            "conditional": conditional_workflow,
            "iterative": iterative_workflow,
            "functional": functional_workflow,
            "pipeline": pipeline_workflow
        }

        workflow = workflows.get(workflow_type)

        if workflow is None:
            raise ValueError(
                f"Unknown workflow: {workflow_type}"
            )

        return workflow(self.agent, data)