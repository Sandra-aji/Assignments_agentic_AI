class Action:
    """Store new/current state and report or alert when required."""

    def __init__(self, database):
        self.database = database

    def execute(self, records, decision_result):
        stored_count = 0
        changed_count = 0

        for record in records:
            result = self.database.upsert_record(record)

            if result["is_new"] or result["changed"]:
                stored_count += 1

            if result["changed"]:
                changed_count += 1

        action = decision_result["action"]

        if action == "ALERT":
            message = (
                f"HIGH-priority alert: {changed_count} "
                "significant change(s) detected."
            )

        elif action == "STORE_AND_REPORT":
            message = (
                f"Monitoring update: {stored_count} new or "
                "changed record(s) stored."
            )

        else:
            message = (
                "No significant change detected. "
                "Current state retained without duplicate history."
            )

        return {
            "action": action,
            "stored_count": stored_count,
            "changed_count": changed_count,
            "message": message
        }
