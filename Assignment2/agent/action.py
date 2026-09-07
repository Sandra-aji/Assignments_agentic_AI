class Action:
    """
    Action component of SENTINEL-NEXUS.

    Performs the action decided by the agent,
    such as storing records or generating an alert.
    """

    def __init__(self, database):
        self.database = database

    def execute(self, records, decision_result):
        """
        Execute the decided monitoring action.
        """

        action = decision_result["action"]

        stored_count = 0

        if action in ["STORE", "ALERT"]:

            for record in records:

                # Avoid duplicating records that
                # were already collected from the database.
                if record.source_type != "Database":
                    self.database.insert_record(record)
                    stored_count += 1

        if action == "ALERT":
            message = (
                f"ALERT: {len(records)} records contain "
                "important information."
            )

        else:
            message = (
                f"Monitoring completed. "
                f"{stored_count} records stored."
            )

        return {
            "action": action,
            "stored_count": stored_count,
            "message": message
        }