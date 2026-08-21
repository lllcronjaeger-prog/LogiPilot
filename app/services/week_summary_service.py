import pandas as pd
from app.database.database import connect

def create_summary(week:int):
    con=connect()
    try:
        df=pd.read_sql_query(
            "SELECT kennzeichen,unternehmer FROM shipments WHERE kalenderwoche=?",
            con,params=(week,)
        )
    finally:
        con.close()

    if df.empty:
        return []

    summary=(df.groupby(["kennzeichen","unternehmer"])
               .size()
               .reset_index(name="sendungen"))

    return [
        (r.kennzeichen,r.unternehmer,int(r.sendungen),"-")
        for r in summary.itertuples(index=False)
    ]
