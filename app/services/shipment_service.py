import pandas as pd
from app.database.database import connect
from app.services.fleet_service import get_fleet_plates

def get_week_dataframe(week:int)->pd.DataFrame:
    con=connect()
    df=pd.read_sql_query(
        """SELECT sendungsnummer AS Sendungsnummer,
                  kennzeichen AS Kennzeichen,
                  unternehmer AS Unternehmer,
                  entladedatum AS Entladedatum,
                  kalenderwoche AS Kalenderwoche
           FROM shipments WHERE kalenderwoche=? ORDER BY entladedatum""",
        con,params=(week,))
    con.close()
    return df

def get_entrepreneurs(df:pd.DataFrame):
    return sorted(df["Unternehmer"].dropna().unique()) if "Unternehmer" in df.columns else []

def filter_dataframe(df:pd.DataFrame, entrepreneurs=None, fleet_only=False):
    out=df.copy()
    if entrepreneurs and "Unternehmer" in out.columns:
        out=out[out["Unternehmer"].isin(entrepreneurs)]
    if fleet_only and "Kennzeichen" in out.columns:
        fleet=get_fleet_plates()
        out=out[out["Kennzeichen"].str.upper().isin(fleet)]
    return out
