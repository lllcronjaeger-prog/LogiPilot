from PySide6.QtWidgets import QWidget,QHBoxLayout,QTableView
from app.ui.filter_panel import FilterPanel
from app.ui.pandas_model import PandasModel

class WeekView(QWidget):
    def __init__(self,df):
        super().__init__()
        self.df=df.copy(); self.current=self.df.copy()
        lay=QHBoxLayout(self)
        self.table=QTableView(); self.table.setSortingEnabled(True); lay.addWidget(self.table,4)
        self.panel=FilterPanel(); lay.addWidget(self.panel,1)
        if "Unternehmer" in self.df.columns:
            self.panel.set_entrepreneurs(self.df["Unternehmer"].dropna().unique())
        self.panel.filtersChanged.connect(self.apply_filters)
        self.apply_filters()
    def apply_filters(self):
        out=self.df
        sel=self.panel.selected()
        if sel and "Unternehmer" in out.columns:
            out=out[out["Unternehmer"].isin(sel)]
        self.current=out
        self.table.setModel(PandasModel(self.current))
        self.panel.set_status(len(self.current),len(self.df))
