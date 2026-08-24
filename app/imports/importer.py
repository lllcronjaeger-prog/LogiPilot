from app.database.database import connect
import pandas as pd

COLUMN_MAP = {
    "Dossier":"Dossier",
    "Kundenauftragsnummer":"Kundenauftragsnummer",
    "Ladetermin":"Ladetermin",
    "Liefertermin":"Entladedatum",
    "Beladeadresse":"Absender",
    "Entladeadresse":"Empfänger",
    "Interne Hinweise":"Hinweise",
    "Fahrzeug":"Kennzeichen",
    "Unternehmer":"Unternehmer",
}

def import_dispotest(path):
    xl=pd.ExcelFile(path)
    sheet="Disposition" if "Disposition" in xl.sheet_names else xl.sheet_names[0]
    df=pd.read_excel(path,sheet_name=sheet,header=1)
    out=pd.DataFrame()
    # Reihenfolge der Spalten darf sich ändern -> nach Namen suchen
    for src_col,target in COLUMN_MAP.items():
        if src_col in df.columns:
            out[target]=df[src_col]
    s=pd.to_datetime(out["Entladedatum"],errors="coerce",dayfirst=True)
    out["Entladedatum"]=s.dt.strftime("%d.%m.%Y")
    out["Wochentag"]=s.dt.dayofweek
    out["kalenderwoche"]=s.dt.isocalendar().week.astype("Int64")
    out=out.dropna(how="all")
    con=connect()
    con.execute("""CREATE TABLE IF NOT EXISTS shipments(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Dossier TEXT,
        Kundenauftragsnummer TEXT UNIQUE,
        Kennzeichen TEXT,
        Unternehmer TEXT,
        Absender TEXT,
        Empfänger TEXT,
        Hinweise TEXT,
        Ladetermin TEXT,
        Entladedatum TEXT,
        Wochentag INTEGER,
        kalenderwoche INTEGER
    )""")
    if out["kalenderwoche"].notna().any():
        kw=int(out["kalenderwoche"].dropna().mode().iloc[0])
        con.execute("DELETE FROM shipments WHERE kalenderwoche=?",(kw,))
    out.to_sql("shipments",con,if_exists="append",index=False)
    con.commit(); con.close()
    return len(out)
