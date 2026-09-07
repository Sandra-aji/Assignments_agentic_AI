class Analysis:
    """
    Analysis component of SENTINEL-NEXUS.

    Detects potentially important changes or events
    in processed monitoring data.
    """

    def analyze(self, processed_data):
        """
        Analyze processed records for important information.
        """

        records = processed_data["records"]

        important_records = []

        keywords = [
            "important",
            "warning",
            "alert",
            "failure",
            "error",
            "critical"
        ]

        for record in records:
            content = record["content"].lower()

            if any(keyword in content for keyword in keywords):
                important_records.append(record)

        return {
            "important_change": len(important_records) > 0,
            "important_records": important_records,
            "total_records": len(records)
        }