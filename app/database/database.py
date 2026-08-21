
from pathlib import Path
import sqlite3
DB=Path(__file__).resolve().parents[2]/'data'/'logipilot.db'
def init_db():
    DB.parent.mkdir(exist_ok=True)
    con=sqlite3.connect(DB)
    con.execute("CREATE TABLE IF NOT EXISTS imports(id INTEGER PRIMARY KEY, filename TEXT, source TEXT)")
    con.commit(); con.close()
