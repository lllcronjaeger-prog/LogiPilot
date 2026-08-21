from pathlib import Path
from openpyxl import Workbook
from app.services.export_service import get_week_dataframe

def export_week(week:int, output_dir:Path):
    output_dir=Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    df=get_week_dataframe(week)

    wb=Workbook()
    ws=wb.active
    ws.title=f"KW{week}"

    if not df.empty:
        ws.append(list(df.columns))
        for row in df.itertuples(index=False):
            ws.append(list(row))

    file=output_dir/f"KW{week:02d}_Wochenübersicht.xlsx"
    wb.save(file)
    return file
