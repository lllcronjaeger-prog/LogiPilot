import pandas as pd
from app.database.database import connect
def load_week_dataframe(week:int):
    con=connect(); df=pd.read_sql_query("SELECT sendungsnummer AS Sendungsnummer, kennzeichen AS Kennzeichen, unternehmer AS Unternehmer, entladedatum AS Entladedatum FROM shipments WHERE kalenderwoche=?",con,params=(week,)); con.close(); return df
