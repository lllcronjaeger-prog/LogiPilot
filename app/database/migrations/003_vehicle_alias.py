def migrate(c):
 c.execute("CREATE TABLE IF NOT EXISTS vehicles(id INTEGER PRIMARY KEY AUTOINCREMENT,standard_kennzeichen TEXT UNIQUE,standort TEXT DEFAULT 'Leipzig',aktiv INTEGER DEFAULT 1)"); c.execute("CREATE TABLE IF NOT EXISTS vehicle_aliases(id INTEGER PRIMARY KEY AUTOINCREMENT,vehicle_id INTEGER,alias TEXT UNIQUE,FOREIGN KEY(vehicle_id) REFERENCES vehicles(id))")
