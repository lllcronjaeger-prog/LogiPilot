import pandas as pd
from app.database.database import connect

def get_week_dataframe(week):
 c=connect();df=pd.read_sql_query('SELECT * FROM shipments WHERE kalenderwoche=?',c,params=(week,));c.close();return df
