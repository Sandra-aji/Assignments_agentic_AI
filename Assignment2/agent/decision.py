class Decision:
    """
    Decision component of SENTINEL-NEXUS.

    Determines the priority and action based on
    the reasoning result.
    """

    def decide(self, reasoning_result):
        """
        Make a decision based on detected changes.
        """

        if reasoning_result["important_change"]:
            priority = "HIGH"
            action = "ALERT"

        else:
            priority = "LOW"
            action = "STORE"

        return {
            "priority": priority,
            "action": action
        }