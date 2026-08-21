from pathlib import Path

def refresh_excel_file(path):
    """Aktualisiert Pivot-Tabellen und Verbindungen über Excel (Windows)."""
    path = Path(path).resolve()
    try:
        import win32com.client
    except ImportError as e:
        raise RuntimeError(
            "pywin32 fehlt. Installiere es mit: pip install pywin32"
        ) from e

    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = False
    excel.DisplayAlerts = False

    wb = excel.Workbooks.Open(str(path))
    wb.RefreshAll()
    excel.CalculateUntilAsyncQueriesDone()
    wb.Save()
    wb.Close()
    excel.Quit()

    return path
