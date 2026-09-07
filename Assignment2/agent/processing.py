class Processing:
    """
    Processing component of SENTINEL-NEXUS.

    Converts collected records into a structured
    format for analysis and reasoning.
    """

    def process(self, records):
        """
        Process collected monitoring records.
        """

        processed_records = []

        for record in records:
            processed_records.append({
                "title": record.title,
                "content": record.content,
                "source_type": record.source_type,
                "source": record.source
            })

        return {
            "record_count": len(processed_records),
            "records": processed_records
        }