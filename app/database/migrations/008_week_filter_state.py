def migrate(cursor):
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS week_filter_state(
            year INTEGER NOT NULL,
            week INTEGER NOT NULL,
            fleet_only INTEGER DEFAULT 0,
            PRIMARY KEY(year,week)
        )
        """
    )
