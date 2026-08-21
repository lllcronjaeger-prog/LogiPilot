import pandas as pd
def load_week_dataframe(path,sheet,header,date_column,week):
 df=pd.read_excel(path,sheet_name=sheet,header=header); df[date_column]=pd.to_datetime(df[date_column],errors='coerce',dayfirst=True); return df[df[date_column].dt.isocalendar().week==week].copy()
