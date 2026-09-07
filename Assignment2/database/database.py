import json
import os
import sqlite3


class SentinelDatabase:
    """
    Agent storage database.

    Stores the latest state and a history of detected changes.
    """

    def __init__(self, database_path="data/sentinel_clean.db"):
        self.database_path = database_path
        os.makedirs(
            os.path.dirname(database_path),
            exist_ok=True
        )
        self.create_tables()

    def connect(self):
        return sqlite3.connect(self.database_path)

    def create_tables(self):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS monitoring_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                record_key TEXT NOT NULL UNIQUE,
                title TEXT NOT NULL,
                content TEXT,
                source_type TEXT NOT NULL,
                source TEXT NOT NULL,
                data_json TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS change_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                record_key TEXT NOT NULL,
                title TEXT NOT NULL,
                previous_data_json TEXT,
                current_data_json TEXT,
                source_type TEXT NOT NULL,
                detected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        connection.commit()
        connection.close()

    def get_current_record(self, record_key):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, record_key, title, content,
                   source_type, source, data_json,
                   created_at, updated_at
            FROM monitoring_records
            WHERE record_key = ?
        """, (record_key,))

        row = cursor.fetchone()
        connection.close()

        if not row:
            return None

        return {
            "id": row[0],
            "record_key": row[1],
            "title": row[2],
            "content": row[3],
            "source_type": row[4],
            "source": row[5],
            "data": json.loads(row[6] or "{}"),
            "created_at": row[7],
            "updated_at": row[8]
        }

    def upsert_record(self, record):
        previous = self.get_current_record(record.record_key)

        connection = self.connect()
        cursor = connection.cursor()

        data_json = json.dumps(record.data, sort_keys=True)

        if previous is None:
            cursor.execute("""
                INSERT INTO monitoring_records
                (record_key, title, content, source_type,
                 source, data_json)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                record.record_key,
                record.title,
                record.content,
                record.source_type,
                record.source,
                data_json
            ))
            changed = True

        else:
            cursor.execute("""
                UPDATE monitoring_records
                SET title = ?,
                    content = ?,
                    source_type = ?,
                    source = ?,
                    data_json = ?,
                    updated_at = CURRENT_TIMESTAMP
                WHERE record_key = ?
            """, (
                record.title,
                record.content,
                record.source_type,
                record.source,
                data_json,
                record.record_key
            ))
            changed = previous["data"] != record.data

        connection.commit()
        connection.close()

        if changed:
            self.insert_change_history(
                record,
                previous["data"] if previous else None
            )

        return {
            "is_new": previous is None,
            "changed": changed
        }

    def insert_change_history(self, record, previous_data):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO change_history
            (record_key, title, previous_data_json,
             current_data_json, source_type)
            VALUES (?, ?, ?, ?, ?)
        """, (
            record.record_key,
            record.title,
            json.dumps(previous_data, sort_keys=True)
            if previous_data is not None else None,
            json.dumps(record.data, sort_keys=True),
            record.source_type
        ))

        connection.commit()
        connection.close()

    def get_all_records(self):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, record_key, title, content,
                   source_type, source, data_json,
                   created_at, updated_at
            FROM monitoring_records
            ORDER BY id
        """)

        rows = cursor.fetchall()
        connection.close()
        return rows

    def search_records(self, keyword):
        connection = self.connect()
        cursor = connection.cursor()

        pattern = f"%{keyword}%"

        cursor.execute("""
            SELECT id, record_key, title, content,
                   source_type, source, data_json,
                   created_at, updated_at
            FROM monitoring_records
            WHERE title LIKE ?
               OR content LIKE ?
               OR record_key LIKE ?
            ORDER BY updated_at DESC
        """, (pattern, pattern, pattern))

        rows = cursor.fetchall()
        connection.close()
        return rows

    def update_record(self, record_id, title, content):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE monitoring_records
            SET title = ?, content = ?,
                updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (title, content, record_id))

        connection.commit()
        count = cursor.rowcount
        connection.close()
        return count

    def delete_record(self, record_id):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
            DELETE FROM monitoring_records
            WHERE id = ?
        """, (record_id,))

        connection.commit()
        count = cursor.rowcount
        connection.close()
        return count

    def get_change_history(self):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, record_key, title,
                   previous_data_json, current_data_json,
                   source_type, detected_at
            FROM change_history
            ORDER BY id
        """)

        rows = cursor.fetchall()
        connection.close()
        return rows
