class Action:
    """
    Action component of the NEXORA-OPS agent.

    It executes the decision made by the agent and
    updates the state of the business request.
    """

    def execute(self, request, decision_data):
        """
        Execute the selected action and update
        the request state.
        """

        request.department = decision_data["department"]
        request.action = decision_data["action"]
        request.escalated = decision_data["escalation"]

        if request.escalated:
            request.update_state("Escalated")
        else:
            request.update_state("Processing")

        return request