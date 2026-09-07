class Processing:
    """Convert monitoring records into a common structured format."""

    def process(self, records):
        processed_records = []

        for record in records:
            processed_records.append(record.to_dict())

        return {
            "record_count": len(processed_records),
            "records": processed_records
        }
