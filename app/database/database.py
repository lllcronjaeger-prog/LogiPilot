from pathlib import Path
import sqlite3

DB = Path(__file__).resolve().parents[2] / "data" / "logipilot.db"

def connect():
    DB.parent.mkdir(exist_ok=True)
    return sqlite3.connect(DB)

def init_db():
    con = connect()
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS imports(id INTEGER PRIMARY KEY AUTOINCREMENT, source TEXT, filename TEXT, week TEXT, imported_at TEXT DEFAULT CURRENT_TIMESTAMP)")
    con.commit()
    con.close()
