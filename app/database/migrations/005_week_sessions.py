def migrate(cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS week_sessions(id INTEGER PRIMARY KEY AUTOINCREMENT, year INTEGER, week INTEGER, created_at TEXT DEFAULT CURRENT_TIMESTAMP, status TEXT DEFAULT 'offen')")
