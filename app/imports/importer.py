from pathlib import Path
import sqlite3
import pandas as pd

DB = Path("logipilot.db")


def _first_matching_column(df, keywords):
    """Gibt die erste Spalte zurück, die eines der Suchwörter enthält."""
    for col in df.columns:
        name = str(col).strip().lower()
        if any(k in name for k in keywords):
            return col
    return None


def import_dispotest(path):
    """
    Importiert DispoTest (.xls/.xlsx) nach SQLite.
    Verwendet immer nur die erste passende Spalte, damit keine
    doppelten 'Entladedatum'-Spalten entstehen.
    """

    xl = pd.ExcelFile(path)
    sheet = "Disposition" if "Disposition" in xl.sheet_names else xl.sheet_names[0]
    df = pd.read_excel(path, sheet_name=sheet, header=1)

    kenn = _first_matching_column(df, ["kenn"])
    unter = _first_matching_column(df, ["unternehmer"])
    datum = _first_matching_column(df, ["liefertermin", "entlade"])

    out = pd.DataFrame()

    if kenn:
        out["Kennzeichen"] = df[kenn]

    if unter:
        out["Unternehmer"] = df[unter]

    if datum:
        s = pd.to_datetime(df[datum], errors="coerce", dayfirst=True)
        out["Entladedatum"] = s.dt.strftime("%d.%m.%Y")
        out["kalenderwoche"] = s.dt.isocalendar().week.astype("Int64")

    out = out.dropna(how="all")

    con = sqlite3.connect(DB)

    con.execute("""
        CREATE TABLE IF NOT EXISTS shipments(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Kennzeichen TEXT,
            Unternehmer TEXT,
            Entladedatum TEXT,
            kalenderwoche INTEGER
        )
    """)

    if "kalenderwoche" in out.columns and out["kalenderwoche"].notna().any():
        kw = int(out["kalenderwoche"].dropna().mode().iloc[0])
        con.execute("DELETE FROM shipments WHERE kalenderwoche=?", (kw,))

    out.to_sql("shipments", con, if_exists="append", index=False)

    con.commit()
    con.close()

    return len(out)