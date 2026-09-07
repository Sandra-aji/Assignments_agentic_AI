class Analysis:
    """
    Detect actual state changes by comparing current records
    with the latest state stored by SENTINEL-NEXUS.
    """

    def __init__(self, database):
        self.database = database

    def analyze(self, processed_data):
        changed_records = []
        new_records = []
        unchanged_records = []

        for record in processed_data["records"]:
            previous = self.database.get_current_record(
                record["record_key"]
            )

            if previous is None:
                new_records.append(record)
                continue

            if previous["data"] != record["data"]:
                changed_records.append({
                    "current": record,
                    "previous": previous["data"]
                })
            else:
                unchanged_records.append(record)

        important_change = bool(
            changed_records or new_records
        )

        return {
            "important_change": important_change,
            "changed_records": changed_records,
            "new_records": new_records,
            "unchanged_records": unchanged_records,
            "total_records": processed_data["record_count"]
        }
