import json
import os
import sqlite3


class SourceMonitoringDatabase:
    """
    Simulated external source database.

    This represents a separate database that another system
    could maintain and that SENTINEL-NEXUS can monitor.
    """

    def __init__(self, database_path="data/source_monitoring.db"):
        self.database_path = database_path
        os.makedirs(
            os.path.dirname(database_path),
            exist_ok=True
        )
        self.create_table()
        self.seed_if_empty()

    def connect(self):
        return sqlite3.connect(self.database_path)

    def create_table(self):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS service_status (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                record_key TEXT NOT NULL UNIQUE,
                title TEXT NOT NULL,
                content TEXT,
                source TEXT NOT NULL,
                data_json TEXT NOT NULL
            )
        """)

        connection.commit()
        connection.close()

    def seed_if_empty(self):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM service_status")
        count = cursor.fetchone()[0]

        if count == 0:
            data = {
                "repository": "python/cpython",
                "status": "operational",
                "open_issues": 0,
                "last_checked": "initial-source-snapshot"
            }

            cursor.execute("""
                INSERT INTO service_status
                (record_key, title, content, source, data_json)
                VALUES (?, ?, ?, ?, ?)
            """, (
                "source:python/cpython",
                "Python Project Source Snapshot",
                "Source database snapshot for the Python project.",
                "source_monitoring.db",
                json.dumps(data)
            ))

        connection.commit()
        connection.close()

    def get_source_records(self):
        connection = self.connect()
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        cursor.execute("""
            SELECT record_key, title, content,
                   source, data_json
            FROM service_status
            ORDER BY id
        """)

        rows = cursor.fetchall()
        connection.close()

        return [
            {
                "record_key": row["record_key"],
                "title": row["title"],
                "content": row["content"],
                "source": row["source"],
                "data": json.loads(row["data_json"])
            }
            for row in rows
        ]
