
from app.imports.pipeline import import_preview

def load_week(path,week):
    meta,df=import_preview(path)
    week_df=df[df[meta["date_column"]].dt.isocalendar().week==week].copy()
    return meta,week_df
