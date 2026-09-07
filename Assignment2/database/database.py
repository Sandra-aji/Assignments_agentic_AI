import sqlite3
import os


class SentinelDatabase:
    """
    Handles SQLite database operations for
    SENTINEL-NEXUS.
    """

    def __init__(self, database_path="data/sentinel_clean.db"):
        self.database_path = database_path

        os.makedirs(
            os.path.dirname(database_path),
            exist_ok=True
        )

        self.create_table()

    def connect(self):
        """Create a database connection."""

        return sqlite3.connect(self.database_path)

    def create_table(self):
        """Create the monitoring records table."""

        connection = self.connect()

        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS monitoring_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT,
                source_type TEXT NOT NULL,
                source TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        connection.commit()
        connection.close()

    def insert_record(self, record):
        """Insert a monitoring record into the database."""

        connection = self.connect()

        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO monitoring_records
            (title, content, source_type, source)
            VALUES (?, ?, ?, ?)
        """, (
            record.title,
            record.content,
            record.source_type,
            record.source
        ))

        connection.commit()
        connection.close()

    def get_all_records(self):
        """Retrieve all stored monitoring records."""

        connection = self.connect()

        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, title, content,
                   source_type, source, created_at
            FROM monitoring_records
            ORDER BY id
        """)

        records = cursor.fetchall()

        connection.close()

        return records

    def search_records(self, keyword):
        """Search stored records by title or content."""

        connection = self.connect()

        cursor = connection.cursor()

        search_pattern = f"%{keyword}%"

        cursor.execute("""
            SELECT id, title, content,
                   source_type, source, created_at
            FROM monitoring_records
            WHERE title LIKE ?
               OR content LIKE ?
            ORDER BY id
        """, (
            search_pattern,
            search_pattern
        ))

        records = cursor.fetchall()

        connection.close()

        return records

    def update_record(self, record_id, title, content):
        """Update an existing monitoring record."""

        connection = self.connect()

        cursor = connection.cursor()

        cursor.execute("""
            UPDATE monitoring_records
            SET title = ?, content = ?
            WHERE id = ?
        """, (
            title,
            content,
            record_id
        ))

        connection.commit()

        updated_count = cursor.rowcount

        connection.close()

        return updated_count

    def delete_record(self, record_id):
        """Delete a monitoring record."""

        connection = self.connect()

        cursor = connection.cursor()

        cursor.execute("""
            DELETE FROM monitoring_records
            WHERE id = ?
        """, (record_id,))

        connection.commit()

        deleted_count = cursor.rowcount

        connection.close()

        return deleted_count