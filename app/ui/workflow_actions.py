from PySide6.QtWidgets import QMessageBox
from app.services.workflow_service import WorkflowService

service=WorkflowService()

def open_week(parent, week):
    return service.load_week(week)

def export_week(parent, week, kind, template_dir, output_dir):
    file=service.export_week(week, kind, template_dir, output_dir)
    QMessageBox.information(parent,"Export abgeschlossen",str(file))
    return file
