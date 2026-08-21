def migrate(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vehicle_uid(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vehicle_uid TEXT UNIQUE NOT NULL,
            kennzeichen TEXT UNIQUE NOT NULL
        )
    """)
