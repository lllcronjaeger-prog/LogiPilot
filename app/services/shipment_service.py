import pandas as pd
from app.database.database import connect

def get_week_dataframe(week:int)->pd.DataFrame:
    con=connect()
    df=pd.read_sql_query("SELECT * FROM shipments WHERE kalenderwoche=? ORDER BY entladedatum",con,params=(week,))
    con.close(); return df

def get_entrepreneurs(df):
    return sorted(df["Unternehmer"].dropna().unique()) if "Unternehmer" in df.columns else []

def filter_dataframe(df,entrepreneurs=None):
    if entrepreneurs and "Unternehmer" in df.columns:
        return df[df["Unternehmer"].isin(entrepreneurs)]
    return df
