import sqlite3, importlib
from pathlib import Path
DB_PATH=Path(__file__).resolve().parents[2]/'data'/'logipilot.db'
MIGRATIONS=['001_initial','002_import_history','003_vehicle_alias','004_shipments']
def run_migrations():
    DB_PATH.parent.mkdir(exist_ok=True)
    con=sqlite3.connect(DB_PATH); cur=con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS schema_version(version TEXT PRIMARY KEY)')
    for m in MIGRATIONS:
        cur.execute('SELECT 1 FROM schema_version WHERE version=?',(m,))
        if cur.fetchone(): continue
        importlib.import_module(f'app.database.migrations.{m}').migrate(cur)
        cur.execute('INSERT INTO schema_version VALUES(?)',(m,)); con.commit()
    con.close()
