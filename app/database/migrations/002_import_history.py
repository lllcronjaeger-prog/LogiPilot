def migrate(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS imports(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT,
            filename TEXT,
            week TEXT,
            imported_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)