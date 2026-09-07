from models.record import MonitoringRecord


class DatabaseCollector:
    """
    Collect information from the SENTINEL-NEXUS
    SQLite database.
    """

    def __init__(self, database):
        self.database = database

    def collect(self):
        """
        Retrieve stored records from the database.
        """

        rows = self.database.get_all_records()

        records = []

        for row in rows:
            record = MonitoringRecord(
                title=row[1],
                content=row[2],
                source_type="Database",
                source=row[4]
            )

            records.append(record)

        return records