from pathlib import Path
import pandas as pd
from openpyxl import load_workbook
import shutil

SOURCE_DATE_COLUMN='Liefertermin'

def create_reports(source_file, kw):
    xl=pd.ExcelFile(source_file)
    sheet='Disposition' if 'Disposition' in xl.sheet_names else xl.sheet_names[0]
    df=pd.read_excel(source_file,sheet_name=sheet,header=1)
    d=pd.to_datetime(df[SOURCE_DATE_COLUMN],errors='coerce',dayfirst=True)
    week=df[d.dt.isocalendar().week==kw].copy()
    out=Path(source_file).parent/'Auswertungen'/f'KW{kw:02d}'
    out.mkdir(parents=True,exist_ok=True)
    week.to_excel(out/'01_Wochenübersicht.xlsx',index=False)
    if 'Fahrzeug' in week.columns:
        week.groupby('Fahrzeug').size().reset_index(name='Aufträge').to_excel(out/'02_Fuhrpark.xlsx',index=False)
    if 'Unternehmer' in week.columns:
        week.groupby('Unternehmer').size().reset_index(name='Aufträge').to_excel(out/'03_Unternehmer.xlsx',index=False)
    return out
