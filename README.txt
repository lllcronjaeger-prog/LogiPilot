PR018 Excel Reports

Datei nach app/services/excel_reports.py kopieren.

Test:
from app.services.excel_reports import create_reports
create_reports(r"DispoTest.xls")

Erzeugt:
Auswertungen/JAHR_KWXX/
01_Wochenübersicht.xlsx
02_Fuhrpark.xlsx
03_Unternehmer.xlsx
04_Tagesübersicht.xlsx
05_Kennzahlen.xlsx
