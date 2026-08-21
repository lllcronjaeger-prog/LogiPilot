from app.services.shipment_service import get_week_dataframe

def get_week_dataframe_for_export(week:int):
    return get_week_dataframe(week)
