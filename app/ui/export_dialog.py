from pathlib import Path
from PySide6.QtWidgets import QFileDialog,QMessageBox
from app.exports.excel_export import export_week

def export_week_dialog(parent, week:int):
    folder=QFileDialog.getExistingDirectory(parent,"Ausgabeordner wählen")
    if not folder:
        return
    file=export_week(week, Path(folder))
    QMessageBox.information(parent,"Export abgeschlossen",f"Datei erstellt:\n{file}")
