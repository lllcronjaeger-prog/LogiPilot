from PySide6.QtWidgets import QWidget,QHBoxLayout,QTableView
from app.ui.filter_panel import FilterPanel
from app.ui.pandas_model import PandasModel

class WeekView(QWidget):
    def __init__(self,df):
        super().__init__()
        self.df=df.copy(); self.view=self.df.copy()
        l=QHBoxLayout(self)
        self.table=QTableView(); self.table.setSortingEnabled(True); l.addWidget(self.table,4)
        self.filters=FilterPanel(); l.addWidget(self.filters,1)
        if "Unternehmer" in self.df.columns:
            self.filters.set_entrepreneurs(self.df["Unternehmer"].dropna().unique())
        self.filters.filtersChanged.connect(self.apply_filters)
        self.apply_filters()
    def apply_filters(self):
        out=self.df
        sel=self.filters.selected()
        if sel and "Unternehmer" in out.columns:
            out=out[out["Unternehmer"].isin(sel)]
        self.view=out
        self.table.setModel(PandasModel(self.view))
        self.filters.set_status(len(self.view),len(self.df))
