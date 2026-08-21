import sqlite3
from pathlib import Path
import importlib

DB_PATH = Path(__file__).resolve().parents[2] / "data" / "logipilot.db"

MIGRATIONS = [
    "001_initial",
    "002_import_history",
    "003_vehicle_alias",
    "004_shipments",
]

def run_migrations():
    DB_PATH.parent.mkdir(exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS schema_version(
            version TEXT PRIMARY KEY
        )
    """)

    for migration in MIGRATIONS:
        cur.execute(
            "SELECT 1 FROM schema_version WHERE version=?",
            (migration,)
        )

        if cur.fetchone():
            continue

        module = importlib.import_module(
            f"app.database.migrations.{migration}"
        )

        module.migrate(cur)

        cur.execute(
            "INSERT INTO schema_version VALUES(?)",
            (migration,)
        )

        conn.commit()

    conn.close()