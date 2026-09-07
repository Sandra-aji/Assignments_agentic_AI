class Reasoning:
    """
    Reasoning component of the NEXORA-OPS agent.

    It analyzes information obtained during perception
    and determines the appropriate priority.
    """

    def reason(self, perception_data):
        """
        Analyze perceived information and determine
        the priority of the request.
        """

        category = perception_data["category"]
        urgency = perception_data["urgency"]

        priority = self._assign_priority(category, urgency)

        return {
            "category": category,
            "urgency": urgency,
            "priority": priority
        }

    def _assign_priority(self, category, urgency):
        """Assign priority based on category and urgency."""

        if urgency == "High":
            return "HIGH"

        if urgency == "Medium":
            return "MEDIUM"

        # Certain categories can require attention
        # even when no explicit urgency is detected.
        if category == "Complaint":
            return "MEDIUM"

        return "LOW"