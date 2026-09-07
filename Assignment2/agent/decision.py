class Decision:
    """Determine priority and action from the reasoning result."""

    def decide(self, reasoning_result):
        if reasoning_result["high_priority"]:
            priority = "HIGH"
            action = "ALERT"

        elif reasoning_result["important_change"]:
            priority = "MEDIUM"
            action = "STORE_AND_REPORT"

        else:
            priority = "NORMAL"
            action = "NO_CHANGE"

        return {
            "priority": priority,
            "action": action
        }
