from models.record import MonitoringRecord


class DatabaseCollector:
    """
    Read a separate source database containing previously recorded
    software-project monitoring information.
    """

    def __init__(self, source_database):
        self.source_database = source_database

    def collect(self):
        rows = self.source_database.get_source_records()

        records = []

        for row in rows:
            records.append(
                MonitoringRecord(
                    record_key=row["record_key"],
                    title=row["title"],
                    content=row["content"],
                    source_type="Database",
                    source=row["source"],
                    data=row["data"]
                )
            )

        return records
