from PySide6.QtWidgets import QWidget,QHBoxLayout,QTableView
from app.ui.filter_panel import FilterPanel
from app.ui.pandas_model import PandasModel
class WeekView(QWidget):
    def __init__(self,df): super().__init__(); l=QHBoxLayout(self); t=QTableView(); t.setModel(PandasModel(df)); l.addWidget(t,4); l.addWidget(FilterPanel(),1)
