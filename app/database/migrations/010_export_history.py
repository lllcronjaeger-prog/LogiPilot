def migrate(cursor):
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS export_history(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            year INTEGER,
            week INTEGER,
            export_type TEXT,
            file_name TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
