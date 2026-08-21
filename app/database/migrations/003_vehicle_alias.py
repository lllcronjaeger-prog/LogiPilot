def migrate(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vehicles(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            standard_kennzeichen TEXT UNIQUE,
            standort TEXT DEFAULT 'Leipzig',
            aktiv INTEGER DEFAULT 1
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vehicle_aliases(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vehicle_id INTEGER,
            alias TEXT UNIQUE,
            FOREIGN KEY(vehicle_id) REFERENCES vehicles(id)
        )
    """)