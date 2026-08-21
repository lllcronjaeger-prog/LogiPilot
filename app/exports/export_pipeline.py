from pathlib import Path
from app.exports.template_filler import fill_template
from app.exports.pivot_refresh import refresh_excel_file

def export_complete_week(week:int, kind:str, template_dir:Path, output_dir:Path):
    file = fill_template(week, kind, template_dir, output_dir)
    try:
        refresh_excel_file(file)
    except Exception:
        # Export bleibt trotzdem gültig.
        pass
    return file
