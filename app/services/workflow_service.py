from app.services.shipment_service import get_week_dataframe
from app.exports.export_pipeline import export_complete_week

class WorkflowService:
    def load_week(self, week:int):
        return get_week_dataframe(week)
    def export_week(self, week:int, kind:str, template_dir, output_dir):
        return export_complete_week(week, kind, template_dir, output_dir)
