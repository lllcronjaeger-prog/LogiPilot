
import pandas as pd
from pathlib import Path

class DetectionResult:
    def __init__(self,source,sheet,header):
        self.source=source; self.sheet=sheet; self.header=header

def detect(path):
    xl=pd.ExcelFile(path)
    names={s.lower():s for s in xl.sheet_names}
    if 'speditionsbuch' in names:
        return DetectionResult('Speditionsbuch',names['speditionsbuch'],0)
    if 'disposition' in names:
        return DetectionResult('DispoTest',names['disposition'],1)
    return DetectionResult('Unbekannt',xl.sheet_names[0],0)

def available_weeks(path, det):
    import pandas as pd

    # Begriffe, nach denen wir gezielt suchen
    date_names = [
        "entladedatum",
        "liefertermin",
        "entladung",
        "abladetermin",
        "ankunft",
        "entlade-datum",
    ]

    # Kopfzeilen 0–5 testen
    for header in range(0, 6):
        try:
            df = pd.read_excel(path, sheet_name=det.sheet, header=header)
        except Exception:
            continue

        # 1. Bevorzugt nach passenden Spaltennamen suchen
        for col in df.columns:
            col_name = str(col).strip().lower()

            if any(name in col_name for name in date_names):
                s = pd.to_datetime(df[col], errors="coerce", dayfirst=True)

                # Nur realistische Daten akzeptieren
                s = s[(s.dt.year >= 2020) & (s.dt.year <= 2035)]

                if not s.empty:
                    weeks = sorted(
                        {f"KW {d.isocalendar().week} ({d.year})" for d in s}
                    )
                    return weeks, header, col

        # 2. Fallback: echte Datums-Spalten finden
        for col in df.columns:
            s = pd.to_datetime(df[col], errors="coerce", dayfirst=True)

            s = s[(s.dt.year >= 2020) & (s.dt.year <= 2035)]

            if len(s.dropna()) > 10:
                weeks = sorted(
                    {f"KW {d.isocalendar().week} ({d.year})" for d in s.dropna()}
                )
                return weeks, header, col

    return [], None, None