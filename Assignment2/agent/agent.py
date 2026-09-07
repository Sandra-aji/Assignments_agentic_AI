from agent.perception import Perception
from agent.collection import Collection
from agent.processing import Processing
from agent.analysis import Analysis
from agent.reasoning import Reasoning
from agent.decision import Decision
from agent.action import Action

from utils.validators import (
    validate_monitoring_request,
    validate_records
)
from utils.logger import get_logger


class SentinelNexusAgent:
    """
    Main SENTINEL-NEXUS Agent.

    Perception → Collection → Processing
    → Analysis → Reasoning → Decision → Action
    """

    def __init__(
        self,
        api_collector,
        web_collector,
        database_collector,
        database
    ):
        self.perception = Perception()

        self.collection = Collection(
            api_collector,
            web_collector,
            database_collector
        )

        self.processing = Processing()
        self.analysis = Analysis(database)
        self.reasoning = Reasoning()
        self.decision = Decision()
        self.action = Action(database)

        self.logger = get_logger()

    def run(self, monitoring_request):
        self.logger.info(
            "Agent started: %s",
            monitoring_request
        )

        try:
            validate_monitoring_request(
                monitoring_request
            )

            perception_result = self.perception.perceive(
                monitoring_request
            )

            source_type = perception_result["source_type"]

            records = self.collection.collect(source_type)

            validate_records(records)

            processed_data = self.processing.process(records)

            analysis_result = self.analysis.analyze(
                processed_data
            )

            reasoning_result = self.reasoning.reason(
                analysis_result
            )

            decision_result = self.decision.decide(
                reasoning_result
            )

            action_result = self.action.execute(
                records,
                decision_result
            )

            self.logger.info(
                "Agent completed: source=%s records=%d "
                "priority=%s action=%s",
                source_type,
                len(records),
                decision_result["priority"],
                decision_result["action"]
            )

            return {
                "agent": "SENTINEL-NEXUS",
                "request": monitoring_request,
                "source_type": source_type,
                "records_processed": len(records),
                "important_change": reasoning_result[
                    "important_change"
                ],
                "priority": decision_result["priority"],
                "action": action_result["action"],
                "stored_count": action_result["stored_count"],
                "changed_count": action_result["changed_count"],
                "reasons": reasoning_result["reasons"],
                "message": action_result["message"],
                "status": "COMPLETED"
            }

        except Exception as error:
            self.logger.error(
                "Agent execution failed: %s",
                error
            )
            raise
