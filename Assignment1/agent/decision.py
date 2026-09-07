class Decision:
    """
    Decision component of the NEXORA-OPS agent.

    It determines the department, action, and escalation
    based on the reasoning results.
    """

    def decide(self, reasoning_data):
        """
        Make a decision using the results produced
        by the reasoning component.
        """

        category = reasoning_data["category"]
        priority = reasoning_data["priority"]

        department = self._select_department(category)
        action = self._select_action(priority)
        escalation = self._should_escalate(priority)

        return {
            "department": department,
            "action": action,
            "escalation": escalation
        }

    def _select_department(self, category):
        """Select the appropriate department."""

        department_map = {
            "Technical Support": "IT Support",
            "Service Request": "Operations",
            "Complaint": "Customer Service",
            "Payment Issue": "Finance",
            "Information Request": "Information Desk",
            "General Request": "General Support"
        }

        return department_map.get(category, "General Support")

    def _select_action(self, priority):
        """Determine the action based on priority."""

        if priority == "HIGH":
            return "Immediate Escalation"

        if priority == "MEDIUM":
            return "Create Support Request"

        return "Create Standard Request"

    def _should_escalate(self, priority):
        """Determine whether the request should be escalated."""

        return priority == "HIGH"