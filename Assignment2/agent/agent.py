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

    Controls the complete Agent Loop:

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
        self.analysis = Analysis()
        self.reasoning = Reasoning()
        self.decision = Decision()
        self.action = Action(database)

        self.logger = get_logger()

    def run(self, monitoring_request):
        """
        Run the complete SENTINEL-NEXUS agent loop.
        """

        self.logger.info(
            "Agent started: %s",
            monitoring_request
        )

        try:
            # Validate request
            validate_monitoring_request(
                monitoring_request
            )

            self.logger.info(
                "Monitoring request validated"
            )

            # Step 1: Perception
            perception_result = self.perception.perceive(
                monitoring_request
            )

            source_type = perception_result["source_type"]

            self.logger.info(
                "Perception completed: %s",
                source_type
            )

            # Step 2: Collection
            records = self.collection.collect(
                source_type
            )

            self.logger.info(
                "Collection completed: %d records",
                len(records)
            )

            # Validate collected data
            validate_records(records)

            self.logger.info(
                "Collected data validated"
            )

            # Step 3: Processing
            processed_data = self.processing.process(
                records
            )

            self.logger.info(
                "Processing completed"
            )

            # Step 4: Analysis
            analysis_result = self.analysis.analyze(
                processed_data
            )

            self.logger.info(
                "Analysis completed: important_change=%s",
                analysis_result["important_change"]
            )

            # Step 5: Reasoning
            reasoning_result = self.reasoning.reason(
                analysis_result
            )

            self.logger.info(
                "Reasoning completed"
            )

            # Step 6: Decision
            decision_result = self.decision.decide(
                reasoning_result
            )

            self.logger.info(
                "Decision completed: priority=%s, action=%s",
                decision_result["priority"],
                decision_result["action"]
            )

            # Step 7: Action
            action_result = self.action.execute(
                records,
                decision_result
            )

            self.logger.info(
                "Action completed: %s",
                action_result["message"]
            )

            self.logger.info(
                "Agent completed successfully"
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
                "message": action_result["message"],
                "status": "COMPLETED"
            }

        except Exception as error:

            self.logger.error(
                "Agent execution failed: %s",
                error
            )

            raise