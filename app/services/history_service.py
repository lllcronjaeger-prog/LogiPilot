
import sqlite3
from pathlib import Path
DB=Path(__file__).resolve().parents[2]/"data"/"logipilot.db"

def save_import(source,filename,week):
    con=sqlite3.connect(DB)
    con.execute("INSERT INTO imports(source,filename,week) VALUES(?,?,?)",(source,filename,str(week)))
    con.commit(); con.close()

def list_imports():
    con=sqlite3.connect(DB)
    rows=con.execute("SELECT source,filename,week,imported_at FROM imports ORDER BY imported_at DESC").fetchall()
    con.close()
    return rows
