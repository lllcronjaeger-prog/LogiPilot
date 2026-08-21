import pandas as pd
from app.database.database import connect

def get_dashboard_stats(week:int)->dict:
    con=connect()
    df=pd.read_sql_query("SELECT * FROM shipments WHERE kalenderwoche=?", con, params=(week,))
    con.close()
    return {
        "week": week,
        "shipments": len(df),
        "entrepreneurs": df["Unternehmer"].nunique() if "Unternehmer" in df.columns else 0,
        "fleet": df["Kennzeichen"].nunique() if "Kennzeichen" in df.columns else 0,
    }
