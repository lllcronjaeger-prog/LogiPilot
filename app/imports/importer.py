from app.database.database import connect
import pandas as pd

COLUMN_MAP={
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

def _ensure_schema(con):
    con.execute("""CREATE TABLE IF NOT EXISTS shipments(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Dossier TEXT,
        Kundenauftragsnummer TEXT,
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
    cols={r[1] for r in con.execute("PRAGMA table_info(shipments)").fetchall()}
    wanted={"Dossier":"TEXT","Kundenauftragsnummer":"TEXT","Kennzeichen":"TEXT","Unternehmer":"TEXT",
            "Absender":"TEXT","Empfänger":"TEXT","Hinweise":"TEXT","Ladetermin":"TEXT",
            "Entladedatum":"TEXT","Wochentag":"INTEGER","kalenderwoche":"INTEGER"}
    for c,t in wanted.items():
        if c not in cols:
            con.execute(f"ALTER TABLE shipments ADD COLUMN {c} {t}")

def import_dispotest(path):
    xl=pd.ExcelFile(path)
    sheet="Disposition" if "Disposition" in xl.sheet_names else xl.sheet_names[0]
    df=pd.read_excel(path,sheet_name=sheet,header=1)
    out=pd.DataFrame()
    for s,t in COLUMN_MAP.items():
        if s in df.columns:
            out[t]=df[s]
    dt=pd.to_datetime(out["Entladedatum"],errors="coerce",dayfirst=True)
    out["Entladedatum"]=dt.dt.strftime("%d.%m.%Y")
    out["Wochentag"]=dt.dt.dayofweek
    out["kalenderwoche"]=dt.dt.isocalendar().week.astype("Int64")
    out=out.dropna(how="all")
    con=connect()
    _ensure_schema(con)
    if out["kalenderwoche"].notna().any():
        kw=int(out["kalenderwoche"].dropna().mode().iloc[0])
        con.execute("DELETE FROM shipments WHERE kalenderwoche=?",(kw,))
    out.to_sql("shipments",con,if_exists="append",index=False)
    con.commit(); con.close()
    return len(out)
