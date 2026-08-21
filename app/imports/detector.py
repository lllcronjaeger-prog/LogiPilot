
import pandas as pd

class DetectionResult:
    def __init__(self, source, sheet, header):
        self.source=source
        self.sheet=sheet
        self.header=header

def detect(path):
    xl=pd.ExcelFile(path)
    names={s.lower():s for s in xl.sheet_names}
    if "speditionsbuch" in names:
        return DetectionResult("Speditionsbuch", names["speditionsbuch"], 0)
    if "disposition" in names:
        return DetectionResult("DispoTest", names["disposition"], 1)
    return DetectionResult("Unbekannt", xl.sheet_names[0], 0)

def available_weeks(path, det):
    date_names=["entladedatum","entladedatum von","liefertermin","entladung","abladetermin","ankunft"]
    for header in range(6):
        try:
            df=pd.read_excel(path, sheet_name=det.sheet, header=header)
        except Exception:
            continue
        for col in df.columns:
            name=str(col).strip().lower()
            if any(d in name for d in date_names):
                s=pd.to_datetime(df[col], errors="coerce", dayfirst=True)
                s=s[(s.dt.year>=2020)&(s.dt.year<=2035)]
                if not s.empty:
                    weeks=sorted({f"KW {d.isocalendar().week} ({d.year})" for d in s})
                    return weeks, header, col
        for col in df.columns:
            s=pd.to_datetime(df[col], errors="coerce", dayfirst=True)
            s=s[(s.dt.year>=2020)&(s.dt.year<=2035)]
            if len(s.dropna())>10:
                weeks=sorted({f"KW {d.isocalendar().week} ({d.year})" for d in s.dropna()})
                return weeks, header, col
    return [], None, None
