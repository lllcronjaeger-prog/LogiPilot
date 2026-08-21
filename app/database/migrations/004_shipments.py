def migrate(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS shipments(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            import_id INTEGER,
            standort TEXT DEFAULT 'Leipzig',
            sendungsnummer TEXT,
            kennzeichen TEXT,
            vehicle_id INTEGER,
            unternehmer TEXT,
            entladedatum TEXT,
            kalenderwoche INTEGER,
            erloes REAL,
            kosten REAL
        )
    """)