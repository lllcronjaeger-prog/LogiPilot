from app.services.shipment_service import get_week_dataframe

class DispatcherService:
    def load(self, week:int):
        return get_week_dataframe(week)
