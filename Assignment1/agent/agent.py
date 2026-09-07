from agent.perception import Perception
from agent.reasoning import Reasoning
from agent.decision import Decision
from agent.action import Action


class NexoraAgent:
    """
    Main NEXORA-OPS intelligent agent.

    Coordinates the Agent Loop:
    Perception → Reasoning → Decision → Action
    """

    def __init__(self):
        self.perception = Perception()
        self.reasoning = Reasoning()
        self.decision = Decision()
        self.action = Action()

    def process_request(self, request):
        """
        Process a business request through the complete
        NEXORA-OPS agent loop.
        """

        print("\n" + "=" * 52)
        print("              NEXORA-OPS AGENT SYSTEM")
        print("=" * 52)

        # ------------------------------------------------
        # 1. PERCEPTION
        # ------------------------------------------------

        print("\n[1] PERCEPTION")
        print("Request received successfully.")

        perception_data = self.perception.perceive(
            request.description
        )
        
        request.category = perception_data["category"]
        
        print(
            f"Detected Category: "
            f"{perception_data['category']}"
        )

        print(
            f"Detected Urgency : "
            f"{perception_data['urgency']}"
        )

        # ------------------------------------------------
        # 2. REASONING
        # ------------------------------------------------

        print("\n[2] REASONING")

        reasoning_data = self.reasoning.reason(
            perception_data
        )

        request.priority = reasoning_data["priority"]
        
        print(
            f"Priority Assigned: "
            f"{reasoning_data['priority']}"
        )

        # ------------------------------------------------
        # 3. DECISION
        # ------------------------------------------------

        print("\n[3] DECISION")

        decision_data = self.decision.decide(
            reasoning_data
        )

        print(
            f"Department Selected: "
            f"{decision_data['department']}"
        )

        print(
            f"Action Selected    : "
            f"{decision_data['action']}"
        )

        # ------------------------------------------------
        # 4. ACTION
        # ------------------------------------------------

        print("\n[4] ACTION")

        request = self.action.execute(
            request,
            decision_data
        )

        print(
            f"Action: {request.action}"
        )

        print(
            f"Status: {request.status}"
        )

        return request