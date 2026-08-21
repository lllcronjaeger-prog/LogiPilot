
import pandas as pd
from app.imports.detector import detect_workbook,find_date_column
from app.services.vehicle_service import normalize_plate

def import_preview(path):
    meta=detect_workbook(path)
    header,date_col=find_date_column(path,meta["sheet"])
    if date_col is None:
        raise ValueError("Keine Datumsspalte gefunden.")
    df=pd.read_excel(path,sheet_name=meta["sheet"],header=header)
    df[date_col]=pd.to_datetime(df[date_col],errors="coerce",dayfirst=True)
    if "Kennzeichen" in df.columns:
        df["Kennzeichen"]=df["Kennzeichen"].fillna("").map(normalize_plate)
    meta.update({"header":header,"date_column":date_col})
    return meta,df
