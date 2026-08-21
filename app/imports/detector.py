
import pandas as pd

DATE_HINTS=["entladedatum","entladedatum von","liefertermin","entladung","abladetermin","ankunft"]

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

def _parse_dates(series):
    for fmt in ("%d.%m.%Y","%d.%m.%y","%Y-%m-%d","%d/%m/%Y"):
        parsed=pd.to_datetime(series, format=fmt, errors="coerce")
        if parsed.notna().sum()>=10:
            return parsed
    return pd.to_datetime(series, errors="coerce", dayfirst=True)

def available_weeks(path, det):
    for header in range(6):
        try:
            df=pd.read_excel(path, sheet_name=det.sheet, header=header)
        except Exception:
            continue
        for col in df.columns:
            name=str(col).strip().lower()
            if any(h in name for h in DATE_HINTS):
                s=_parse_dates(df[col])
                s=s[(s.dt.year>=2020)&(s.dt.year<=2035)]
                if not s.empty:
                    weeks=sorted({f"KW {d.isocalendar().week} ({d.year})" for d in s})
                    return weeks, header, col
    return [], None, None
